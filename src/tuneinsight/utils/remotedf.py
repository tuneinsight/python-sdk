"""Utilities to define preprocessing operations using only Pandas operations.

This module defines the RemoteDataFrame class, which provides a Pandas-like interface
to the preprocessing operations supported by the API. The goal is to enable users to
seamlessly swap between local DataFrame objects and the RemoteDataFrame without
changing the code. This enables them to test the code locally and immediately use it remotely.

This module defines the following classes and functions:
 - RemoteDataFrame, a pandas.DataFrame analogue connected to a Tune Insight instance. It
    supports many operations available on a pd.DataFrame (see documentation).
 - get_dummies, an analogue to pd.get_dummies that works on a RemoteDataFrame as well.
 - cut, an analogue to pd.cut that works on a RemoteDataFrame as well.
 - select, a utility to select a subset of columns on a DataFrame or RemoteDataFrame.
 - custom, a decorator to write functions that operate over pandas.DataFrames locally or remotely.

"""

from typing import Union, List

import re
import black
import numpy as np
import pandas as pd

from tuneinsight.api.sdk import models
from tuneinsight.computations.preprocessing import PreprocessingBuilder


# Internal classes that serve as holders for pending operations.


class _SelectedColumn:
    """The output of a selection operation (df[column_name])."""

    def __init__(self, remotedf, name: str):
        self.remotedf = remotedf
        self.name = name

    def __add__(self, other_column):
        assert isinstance(other_column, _SelectedColumn)
        return _SumOfColumns(self, other_column)

    def __mul__(self, value):
        if isinstance(value, (int, float)):
            return _ScaleOperation(self, value)
        if isinstance(value, _SelectedColumn):
            return _MultiplyColumnsOperations(self, value)
        raise ValueError(f"multiplication with {type(value)} not supported")

    def __rmul__(self, value):
        return self.__mul__(value)

    # Some operations only apply to one column at a time.
    # The actual operation is not applied until the variable is set.
    def replace(self, to_replace: dict, inplace=False, default=""):
        assert inplace is False, "replace cannot be done in place."
        return _ApplyMappingOperation(self, to_replace, default)

    # All the following magic operations enable the filter operations (for comparisons).
    def __eq__(self, value):
        return _FilterOperation(self, models.ComparisonType.EQUAL, value, False)

    def __ne__(self, value):
        return _FilterOperation(self, models.ComparisonType.NEQUAL, value, False)

    def __lt__(self, value):
        return _FilterOperation(self, models.ComparisonType.LESS, value, True)

    def __le__(self, value):
        return _FilterOperation(self, models.ComparisonType.LESSEQ, value, True)

    def __gt__(self, value):
        return _FilterOperation(self, models.ComparisonType.GREATER, value, True)

    def __ge__(self, value):
        return _FilterOperation(self, models.ComparisonType.GREATEREQ, value, True)


class _PendingOperation:
    """
    Operations that have been initiated but still need to be added to the chain.

    _PendingOperations are typically created when operations are performed on a
    _SelectedColumn object (e.g., a sum of two variables). These operations still
    need a "destination" (the name of the column created for their output) before
    they can be committed to the chain. This occurs when the user assigns an item
    to the value, e.g., remotedf["new_column"] = p: _PendingOperation.

    """

    def commit(self, output_name: str):
        raise NotImplementedError()


class _SumOfColumns(_PendingOperation):
    """The output of the sum of one or more selected columns."""

    def __init__(self, operand1, operand2, sep="", numerical=True):
        self.columns = [operand1, operand2]
        assert operand1.remotedf == operand2.remotedf, "Must have the same dataset."
        # These variables are typically unaffected in the usual syntax, but can be
        # modified manually if the user wants to.
        self.numerical = numerical
        self.sep = sep

    def commit(self, output_name: str):
        df = self.columns[0].remotedf
        df.builder.add_columns(
            input_cols=[c.name for c in self.columns],
            output=output_name,
            sep=self.sep,
            numerical=self.numerical,
        )


class _ApplyMappingOperation(_PendingOperation):
    """A pending apply_mapping operation on a column."""

    def __init__(self, column: _SelectedColumn, to_replace: dict, default: str = ""):
        self.column = column
        self.to_replace = to_replace
        self.default = default

    def commit(self, output_name: str):
        df: RemoteDataFrame = self.column.remotedf
        df.builder.apply_mapping(
            self.column.name, output_name, self.to_replace, self.default
        )


class _CutOperation(_PendingOperation):
    """A pending cut operation on a column."""

    def __init__(self, column: _SelectedColumn, bins: List[float], labels: List[str]):
        self.column = column
        self.bins = bins
        self.labels = labels

    def commit(self, output_name: str):
        df = self.column.remotedf
        df.builder.cut(self.column.name, output_name, self.bins, self.labels)


class _ScaleOperation(_PendingOperation):
    """A pending scaling operation on a column."""

    def __init__(self, column: _SelectedColumn, scale: float) -> None:
        self.column = column
        self.scale = scale

    def commit(self, output_name: str):
        df = self.column.remotedf
        df.builder.scale([self.column.name], self.scale, [output_name])


class _MultiplyColumnsOperations(_PendingOperation):
    """A pending operation multiplying columns together."""

    def __init__(self, column: _SelectedColumn, other: _SelectedColumn):
        self.df = column.remotedf
        if other.remotedf != self.df:
            raise ValueError("all operations must apply to the same RemoteDataFrame")
        self.columns = [column.name, other.name]

    def commit(self, output_name: str):
        self.df.builder.multiply_columns(self.columns, output_name)


class _FilterOperation:
    """A filter operation on a column.

    This one is different from other pending operations in that it will be used
    as the "output_column" operand: df[f: _FilterOperation] outputs df with
    the filter operation applied.

    """

    def __init__(
        self,
        column: _SelectedColumn,
        comparator: models.ComparisonType,
        value: str,
        numerical: bool = False,
    ):
        self.column = column
        self.comparator = comparator
        self.value = value
        self.numerical = numerical

    def apply(self, output_column=None):
        df = self.column.remotedf
        df.builder.filter(
            self.column.name,
            self.comparator,
            str(self.value),
            self.numerical,
            output_column=output_column,
        )


# Main class:


class RemoteDataFrame:
    """
    DataFrame-like interface for remote post-processing operations.

    This class mimics the interface of a `pandas.DataFrame`, so that it can be used
    interchangeably with a DataFrame. When operations are performed on this object,
    it instead adds the relevant information to the preprocessing chain. Code written
    for a `pandas.DataFrame` can then be applied on the `RemoteDataFrame` to create
    the preprocessing chain that would lead to the same result.

    Only a subset of operations are allowed on this object:
        - Selecting a subset of columns, `df = df[columns]`.
        - Adding columns together `df["new_column"] = df["a"] + df["b"]`.
        - Filtering `df = df[df["a"] <= 10]`.
        -  `drop`,`dropna`, `rename`, `set_index`, `reset_index`, `astype` (all with `inplace=True`), `transpose`.

    Some functions in this module mimic Pandas functions with the same name, that can
    be applied seamlessly on DataFrames and RemoteDataFrames:
        - `get_dummies`, for one-hot encoding,
        - `cut`, for binning numerical columns.

    Finally, this module also defines the `select` operation to select a subset of
    columns, and the `custom` decorator to run a custom preprocessing function.

    """

    def __init__(self, builder: PreprocessingBuilder):
        self.builder = builder

    # Magic methods to mimic Pandas objects.
    def __getitem__(self, column):  # self[column]
        # If the argument of the selection is a _FilterOperation, apply the filter and return self --> this is df[df == 1].
        if isinstance(column, _FilterOperation):
            column.apply()
            return self
        # Otherwise, this is a selection operation for a single column.
        assert isinstance(column, str), "Can only select one column."
        return _SelectedColumn(self, column)

    def __setitem__(self, column, value):  # self[column] = value
        assert isinstance(column, str), "Can only set columns."
        # Setting a column = creating a column using a different operation depending on the operand.
        # A fixed value: create a new column with that value.
        if isinstance(value, (int, float, str, bool)):
            self.builder.new_column(name=column, value=value)
        # Pending operations are operations that concern one or more columns, and whose output must
        # be stored in a newly-created column.
        elif isinstance(value, _PendingOperation):
            value.commit(column)
        # Pending filter operation: df[column] = df[filter].
        elif isinstance(value, _FilterOperation):
            #  This will create a new column with the filtered values.
            value.apply(output_column=column)
        else:
            raise ValueError(f"Invalid type for value {value} in assignment.")

    # Re-implementing Pandas methods.
    def drop(self, columns: List[str], inplace: bool = True):
        assert inplace is True, "drop must be done inplace"
        self.builder.drop(columns)
        return self

    def dropna(self, inplace: bool = True):
        """This operation drops all rows that contain NaN values, using the standard pandas function."""
        assert inplace is True, "dropna must be done inplace."
        self.builder.dropna()
        return self

    def rename(self, mapper: dict, axis="columns", errors="raise", inplace=True):
        """This operation alters the axis labels. By default, this operation renames the columns of a dataset."""
        assert inplace is True, "rename must be done inplace."
        # Convert Pandas inputs into inputs compatible with the API.
        axis = {"columns": models.RenameAxis.COLUMNS, "index": models.RenameAxis.INDEX}[
            axis
        ]
        errors = {"raise": True, "ignore": False}[errors]
        self.builder.rename(mapper, axis=axis, errors=errors)
        return self

    def set_index(
        self,
        keys: Union[str, List[str]],
        drop: bool = True,
        append: bool = False,
        inplace=True,
    ):
        """Sets the DataFrame index to one or more existing columns in the data."""
        assert inplace is True, "set_index must be done inplace."
        if isinstance(keys, str):
            keys = [keys]
        assert isinstance(keys, list) and all(
            isinstance(k, str) for k in keys
        ), "keys must be a list of column names, or a single column name."
        self.builder.set_index(columns=keys, drop=drop, append=append)
        return self

    def reset_index(self, drop: bool = False, level: List[str] = None, inplace=True):
        """Resets the DataFrame index (or a level of it if the index has several columns)."""
        assert inplace is True, "reset_index must be done inplace."
        self.builder.reset_index(drop=drop, level=level)
        return self

    def transpose(self):
        """Transposes the index and columns of the data (see `pandas.DataFrame.transpose`)."""
        self.builder.transpose()
        return self

    def astype(self, dtype, errors="raise"):
        "Casts column types, converting the data in one or more columns to specific type(s)."
        assert isinstance(dtype, dict), "Must provide types as a dictionary."
        converted = {str: "str", int: "int", float: "float"}
        dtype = {k: converted.get(v, v) for k, v in dtype.items()}
        errors = {"raise": True, "ignore": False}[errors]
        self.builder.astype(dtype, errors)
        return self


# We also wrap Pandas operations with our interface. The goal is to be able to use these
# variables with either Pandas Dataframes or RemoteDataFrames.


def get_dummies(
    df: Union[pd.DataFrame, RemoteDataFrame],
    target_column: str,
    prefix: str,
    specified_types: List[str],
) -> Union[pd.DataFrame, RemoteDataFrame]:
    """Create dummies (one-hot encoding) for a given column and collection of values."""
    if isinstance(df, RemoteDataFrame):
        df.builder.one_hot_encoding(target_column, prefix, specified_types)
        return df
    if isinstance(df, pd.DataFrame):
        # Instead of using pd.get_dummies, manually create the columns for each specified value.
        prefix_sep = ""
        if prefix != "":
            prefix_sep = "_"
        for value in specified_types:
            df[f"{prefix}{prefix_sep}{value}"] = df[target_column] == value
        return df
    # If neither a Remote or Pandas DataFrame.
    raise ValueError(f"Invalid type for get_dummies: {type(df)}.")


def cut(
    df: Union[pd.DataFrame, pd.Series, _SelectedColumn, RemoteDataFrame],
    bins=List[float],
    labels: List[str] = None,
    column: str = None,
) -> Union[pd.DataFrame, RemoteDataFrame]:
    """
    Discretizes a continuous column into bins. Similar to pd.cut.

    Args:
        df: the [Remote]DataFrame to cut. This should be either a column of the data, or the column argument should be specified.
        bins: edges of the bins for the discretization. There will be len(bins)-1 bins.
        labels (optional): how to label each bin in the output.
        column (optional): the column to cut.

    """
    assert np.iterable(bins), "Only iterable `bins` are supported."
    if column is not None:
        df = df[column]
    if isinstance(df, pd.Series):
        return pd.cut(df, bins, labels=labels)
    if isinstance(df, _SelectedColumn):
        return _CutOperation(df, bins, labels)
    if isinstance(df, RemoteDataFrame):
        raise ValueError("Cannot cut a whole dataset: select a column.")
    raise ValueError(f"Invalid type for cut: {type(df)}.")


def select(
    df: Union[pd.DataFrame, RemoteDataFrame],
    columns: List[str],
    create_if_missing: bool = False,
    dummy_value: str = "",
):
    """Selects a set of columns. Equivalent to df = df[columns], with additional functionalities."""
    if isinstance(df, pd.DataFrame):
        if create_if_missing:
            for col in columns:
                if col not in df.columns:
                    df[col] = dummy_value
        return df[columns]
    if isinstance(df, RemoteDataFrame):
        df.builder.select(columns)
        return df
    raise ValueError(f"Invalid type for select: {type(df)}")


def custom(
    name: str = "",
    description: str = "",
    compatible_with_dp=False,
    output_columns: List[str] = None,
):
    """
    Decorator for custom operations with signature pd.DataFrame -> pd.DataFrame.

    Wraps a function from DataFrame to DataFrame to transparently handle RemoteDataFrames.
    If the input is a RemoteDataFrame, the function call to func is added to the
    preprocessing chain as a custom operation.

    Args:
        name (str, optional): the name of the function, for documentation purposes.
        description (str, optional): the description of the function, for documentation purposes.
        compatible_with_dp (bool, optional): whether this operation is compatible with differential
            privacy. Only set this to True if you know what you are doing.
        output_columns (List[str], optional): the exact list of columns of the output data. This
            is enforced if provided, and is only required for differential privacy and dry runs.

    """

    def decorator(func):
        def wrappedfunc(df):
            if isinstance(df, pd.DataFrame):
                return func(df)
            if isinstance(df, RemoteDataFrame):
                df.builder.custom(
                    function=func,
                    name=name,
                    description=description,
                    output_columns=output_columns,
                    compatible_with_dp=compatible_with_dp,
                )
                return df
            raise ValueError(f"Invalid type for custom function: {type(df)}.")

        return wrappedfunc

    return decorator


def _render_arguments(operation, arguments: List[str], include_df=False):
    """Small helper to render a function of the type df = f(df, optional, arguments)."""
    op = operation.to_dict()
    rendered_args = []
    if include_df:
        rendered_args.append("df")
    for argument in arguments:
        # Convert to camel case to access the model variables.
        arg_words = argument.split("_")
        cc_arg = "".join([arg_words[0]] + [word.capitalize() for word in arg_words[1:]])
        if op.get(cc_arg) is not None:
            rendered_args.append(f"{argument}={repr(op[cc_arg])}")
    return ", ".join(rendered_args)


# pylint: disable=too-many-branches,too-many-statements
def chain_to_code(chain: models.PreprocessingChain) -> str:
    """Returns the Python code equivalent to a given preprocessing chain using the RemoteDataFrame abstraction."""
    blocks = []
    imports_needed = set(["RemoteDataFrame"])
    function_definitions = []
    for op in chain.chain:
        # switch-case is Py 3.10 syntax and the SDK needs to support 3.9.
        if op.type == models.PreprocessingOperationType.ONEHOTENCODING:
            imports_needed.add("get_dummies")
            block = f"df = get_dummies({_render_arguments(op, ['input_column', 'prefix', 'specified_types'], include_df=True)})"
            block = block.replace(
                "input_column", "target_column"
            )  # Post-process (mismatch between API and pandas names).
            blocks.append(block)
        elif op.type == models.PreprocessingOperationType.SELECT:
            imports_needed.add("select")
            blocks.append(
                f"df = select({_render_arguments(op, ['columns', 'create_if_missing', 'dummy_value'], include_df=True)})"
            )
        elif op.type == models.PreprocessingOperationType.DROP:
            blocks.append(f"df = df.drop(columns={op.columns})")
        elif op.type == models.PreprocessingOperationType.FILTER:
            comp = {
                models.ComparisonType.EQUAL: "==",
                models.ComparisonType.GREATER: ">",
                models.ComparisonType.GREATEREQ: ">=",
                models.ComparisonType.LESS: "<",
                models.ComparisonType.LESSEQ: "==",
                models.ComparisonType.NEQUAL: "!=",
            }.get(op.comparator)
            if comp is not None:
                blocks.append(f'df = df[df["{op.column}"] {comp} {repr(op.value)}]')
            else:
                blocks.append(
                    f"# Filter operation not available for RemoteDataFrame and comparator {op.comparator}"
                )
        elif op.type == models.PreprocessingOperationType.TRANSPOSE:
            blocks.append("df = df.transpose()")
        elif op.type == models.PreprocessingOperationType.SETINDEX:
            blocks.append(
                f"df = df.set_index({_render_arguments(op, ['keys', 'drop', 'append'])})"
            )
        elif op.type == models.PreprocessingOperationType.ASTYPE:
            blocks.append(
                f"df = df.astype({repr(op.type_map.to_dict())}, {_render_arguments(op, ['errors'])})"
            )
        elif op.type == models.PreprocessingOperationType.RESETINDEX:
            blocks.append(
                f"df = df.reset_index({_render_arguments(op, ['drop', 'level'])})"
            )
        elif op.type == models.PreprocessingOperationType.RENAME:
            blocks.append(
                f"df = df.rename({_render_arguments(op, ['mapper', 'axis', 'errors'])}, inplace=True)"
            )
        elif op.type == models.PreprocessingOperationType.DROPNA:
            blocks.append("df = df.dropna(inplace=True)")
        elif op.type == models.PreprocessingOperationType.APPLYMAPPING:
            blocks.append(
                f'df["{op.output_column}"] = df["{op.input_column}"].replace(to_replace={op.mapping.to_dict()}, default={repr(op.default)})'
            )
        elif op.type == models.PreprocessingOperationType.CUT:
            imports_needed.add("cut")
            blocks.append(
                f"df['{op.output_column}'] = cut(df['{op.input_column}'], {_render_arguments(op, ['cuts', 'labels'])})".replace(
                    "cuts=", "bins="
                )
            )
        elif op.type == models.PreprocessingOperationType.ADDCOLUMNS:
            blocks.append(
                f"df['{op.output_column}'] = "
                + " + ".join(f"df['{col}']" for col in op.input_columns)
            )
        elif op.type == models.PreprocessingOperationType.SCALE:
            for ic, oc in zip(op.input_columns, op.output_columns):
                blocks.append(f"df[{repr(oc)}] = {op.scale} * df[{repr(ic)}]")
        elif op.type == models.PreprocessingOperationType.MULTIPLYCOLUMNS:
            blocks.append(
                f"df['{op.output_column}'] = "
                + " * ".join(f"df['{col}']" for col in op.input_columns)
            )
        elif op.type == models.PreprocessingOperationType.NEWCOLUMN:
            blocks.append(f"df['{op.name}'] = {repr(op.value)}")
        elif op.type == models.PreprocessingOperationType.CUSTOM:
            imports_needed.add("custom")
            # First, add the function definition.
            function_definitions.append(
                f"@custom({_render_arguments(op, ['name', 'description'])})\n{op.function}".strip()
            )
            # Then, add the function call to code blocks.
            function_name = re.findall("def ([\\w]+)\\(", op.function)[0]
            blocks.append(f"df = {function_name}(df)")
        else:
            blocks.append(
                f"# Operation of type {op.type} not available with RemoteDataFrame."
            )
    # Add the initial blocks.
    preamble = (
        [
            f"from tuneinsight.utils.remotedf import {', '.join(sorted(list(imports_needed)))}",
            "",
        ]
        + function_definitions
        + [
            "",
            "df = RemoteDataFrame(...)  # TODO: fill in the gaps.",
        ]
    )
    full_code = "\n".join(preamble + blocks)
    # Various post-processing for common "mistakes".
    full_code = full_code.replace("errors=True", "errors='raise'")
    full_code = full_code.replace("errors=False", "errors='ignore'")
    # Apply `black` to nicely format the code. Note: this is an unofficial use of the library.
    full_code = black.format_file_contents(full_code, fast=False, mode=black.FileMode())
    return full_code
