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
        df = self.column.remotedf
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

    def apply(self):
        df = self.column.remotedf
        df.builder.filter(
            self.column.name, self.comparator, str(self.value), self.numerical
        )


# Main class:


class RemoteDataFrame:
    """DataFrame-like interface for remote post-processing operations."""

    def __init__(self, builder: PreprocessingBuilder):
        self.builder = builder

    # Magic methods to mimic Pandas objects.
    def __getitem__(self, column):  # self[column]
        # If the argument of the selection is a _FilterOperation, apply the filter and return self.
        if isinstance(column, _FilterOperation):
            column.apply()
            return self
        # Otherwise, this is a selection operation for a single column.
        assert isinstance(column, str), "Can only select one column."
        return _SelectedColumn(self, column)

    def __setitem__(self, column, value):  # self[column] = value
        assert isinstance(column, str), "Can only set columns."
        # Setting a column = creating a column using a different operation depending on the operand.
        # Special case: value 1 (create a column of counts).
        if value == 1:
            self.builder.counts(output_column_name=column)
        # Pending operations are operations that concern one or more columns, and whose output must
        # be stored in a newly-created column.
        elif isinstance(value, _PendingOperation):
            value.commit(column)
        else:
            raise ValueError(f"Invalid type for value {value} in assignment.")

    # Re-implementing Pandas methods.
    def dropna(self, subset: List[str] = None, inplace=True):
        assert inplace is True, "dropna must be done inplace."
        self.builder.dropna(subset)
        return self

    def rename(
        self, mapper: dict, axis="columns", copy=True, errors="raise", inplace=True
    ):
        assert inplace is True, "rename must be done inplace."
        # Convert Pandas inputs into inputs compatible with the API.
        axis = {"columns": models.RenameAxis.COLUMNS, "index": models.RenameAxis.INDEX}[
            axis
        ]
        errors = {"raise": True, "ignore": False}[errors]
        self.builder.rename(mapper, axis=axis, copy=copy, errors=errors)
        return self

    def set_index(
        self,
        keys: Union[str, List[str]],
        drop: bool = True,
        append: bool = False,
        inplace=True,
    ):
        assert inplace is True, "set_index must be done inplace."
        if isinstance(keys, str):
            keys = [keys]
        assert isinstance(keys, list) and all(
            isinstance(k, str) for k in keys
        ), "keys must be a list of column names, or a single column name."
        self.builder.set_index(columns=keys, drop=drop, append=append)
        return self

    def reset_index(self, drop: bool = False, level: List[str] = None, inplace=True):
        assert inplace is True, "reset_index must be done inplace."
        self.builder.reset_index(drop=drop, level=level)
        return self

    def transpose(self, copy=False):
        self.builder.transpose(copy)
        return self

    def astype(self, dtype, copy=True, errors="raise"):
        assert isinstance(dtype, dict), "Must provide types as a dictionary."
        converted = {str: "str", int: "int", float: "float"}
        dtype = {k: converted.get(v, v) for k, v in dtype.items()}
        errors = {"raise": True, "ignore": False}[errors]
        self.builder.astype(dtype, copy, errors)
        return self


# We also wrap Pandas operations with our interface. The goal is to be able to use these
# variables with either Pandas Dataframes or RemoteDataFrames.


def get_dummies(
    df: Union[pd.DataFrame, RemoteDataFrame],
    target_column: str,
    prefix: str,
    specified_types: List[str],
):
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
):
    """Discretize a continuous column into bins. Similar to pd.cut.

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
    """Select a set of columns. Equivalent to df = df[columns], with additional functionalities."""
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


def custom(name: str = "", description: str = ""):
    """Decorator for custom operations with signature pd.DataFrame -> pd.DataFrame.

    Wraps a function from DataFrame to DataFrame to transparently handle RemoteDataFrames.
    If the input is a RemoteDataFrame, the function call to func is added to the
    preprocessing chain as a custom operation.

    Args:
        - name: the name of the function, for documentation purposes.
        - description: the description of the function, for documentation purposes.

    """

    def decorator(func):
        def wrappedfunc(df):
            if isinstance(df, pd.DataFrame):
                return func(df)
            if isinstance(df, RemoteDataFrame):
                df.builder.custom(function=func, name=name, description=description)
                return df
            raise ValueError(f"Invalid type for custom function: {type(df)}.")

        return wrappedfunc

    return decorator
