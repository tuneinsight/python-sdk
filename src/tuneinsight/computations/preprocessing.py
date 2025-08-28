from enum import Enum
from typing import Dict, List, Callable, Union
from warnings import warn
import pandas as pd

from tuneinsight.api.sdk import Client, models
from tuneinsight.api.sdk.types import UNSET
from tuneinsight.api.sdk.types import is_set, is_unset
from tuneinsight.api.sdk.models import ComparisonType as ct
from tuneinsight.api.sdk.api.api_computations import get_preprocessing_dry_run

from tuneinsight.client.validation import validate_response
from tuneinsight.computations.dataset_schema import DatasetSchema
from tuneinsight.utils.code import get_code


# pylint: disable=too-many-lines


class Comparator(Enum):
    EQUAL = ct.EQUAL
    GREATER = ct.GREATER
    GREATEREQ = ct.GREATEREQ
    LESS = ct.LESS
    LESSEQ = ct.LESSEQ
    NEQUAL = ct.NEQUAL

    # Mapping from user-friendly symbols to Comparator models.
    @staticmethod
    def parse(string) -> "Comparator":
        """Parses a string to a comparator."""
        symbol_map = {
            "==": Comparator.EQUAL,
            ">": Comparator.GREATER,
            ">=": Comparator.GREATEREQ,
            "<": Comparator.LESS,
            "<=": Comparator.LESSEQ,
            "!=": Comparator.NEQUAL,
        }
        # If the input string is not found, return it as is.
        return symbol_map.get(string, string)


class PreprocessingBuilder:
    """
    Pre-processing chain builder. This class is used to build a sequence of preprocessing operations
    that are applied sequentially on the local dataset before running computations.

    The preprocessing builder creates a global chain (default) of operations applied to all nodes,
    and a compound chain for each node, which specifies operations to apply to a single node.

    Each preprocessing operation takes a `nodes` argument specifying on which nodes the operation
    applies (by default, `None`, meaning all nodes), and returns this object, so that they can
    be chained within one Python statement.

    ⚠️ Do not instantiate this object directly: this chain is typically attached to a computation
    directly (through the `.preprocessing` attribute of `Computation` objects), or in the project's
    local data selection. Use these instead.

    """

    chain: List[models.PreprocessingOperation]
    compound_chain: Dict[str, models.PreprocessingChain]
    output_selection: models.Select
    output_selection_set: bool
    schema: DatasetSchema

    def __init__(self, update_function: Callable = None):
        """
        Creates an empty preprocessing builder.

        Args:
            update_function (Callable, optional): if provided, this function is called whenever
                this preprocessing chain is changed. This can be used to automatically update
                the computation definition whenever the preprocessing is updated.
        """
        self.update_function = update_function
        if update_function is None:
            warn(
                "Initialized PreprocessingBuilder without an update function: "
                "changes you make on this object may not appear in the project."
            )
        self.reset(patch=False)

    def new_schema(self) -> DatasetSchema:
        """Creates and attaches a new dataset schema imposing constraints on data structure."""
        self.schema = DatasetSchema()
        return self.schema

    def new_chain(self, chain: List[models.PreprocessingOperation]):
        """
        Sets the global pre-processing chain to a value.

        Args:
            chain (List[models.PreprocessingOperation]): list of pre-processing operations constituting the chain

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        self.chain = chain
        return self

    def new_compound_chain(self, chain: Dict[str, models.PreprocessingChain]):
        """
        Sets the compound pre-processing chain to a value.

        Args:
            chain (Dict[str, models.PreprocessingChain]): dictionary mapping each node to its
                individual preprocessing chain.
        """
        self.compound_chain = chain
        return self

    def one_hot_encoding(
        self,
        input_column: str,
        prefix: str = None,
        specified_types: List[str] = None,
        strict: bool = None,
        nodes: List[str] = None,
    ):
        """
        Adds a one-hot encoding operation to the preprocessing chain.

        One-hot encoding encodes a categorical column into boolean columns, one for each possible value.
        The boolean columns are appended to the table. The list of possible values must be specified
        beforehand (`specified_types`) to ensure that all nodes have the same data structure.

        Args:
            target_column (str, optional): the name of the column on which to perform the one-hot-encoding.
            prefix (str, optional): the prefix of the output column name containing the one-hot encoded values.
            specified_types (List[str], optional): a list of categorical values to create one-hot encoding columns
                for (even if they are not in the target column).
            strict (bool, optional): if set to True, columns are created *only* for the specified types. Values
                outside of these types are ignored. This is required for differential privacy. This also requires
                that specified_types is provided.
            nodes (List[str], optional): list of the name of nodes to apply the operation on, applied
                to all if None. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        if strict is True and specified_types is None:
            raise ValueError("specified_types must be provided in strict mode.")
        self._append_to_chain(
            models.OneHotEncoding(
                type=models.PreprocessingOperationType.ONEHOTENCODING,
                input_column=input_column,
                prefix=prefix,
                specified_types=specified_types,
                strict=strict,
            ),
            nodes,
        )
        return self

    def select(
        self,
        columns: List[str],
        create_if_missing: bool = False,
        dummy_value: str = "",
        nodes: List[str] = None,
    ):
        """
        Adds a select operation to the preprocessing chain.

        This operation selects a set of specified columns from data. All other columns are dropped.

        Args:
            columns (List[str]): list of column names to be selected
            create_if_missing (bool, optional): whether to create the columns if they do not exist. Defaults to False.
            dummy_value (str, optional): what to fill the created columns with. Defaults to "".
            nodes (List[str], optional): list of the name of nodes to apply the operation on, applied to all if None. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        self._append_to_chain(
            models.Select(
                type=models.PreprocessingOperationType.SELECT,
                columns=columns,
                create_if_missing=create_if_missing,
                dummy_value=dummy_value,
            ),
            nodes,
        )
        return self

    def drop(self, columns: List[str], nodes: List[str] = None):
        """
        Adds a drop operation to the preprocessing chain, dropping a set of columns.

        Args:
            columns (List[str]): the columns to drop from the data.
            nodes (List[str], optional): list of the name of nodes to apply the operation on, applied to all if None. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        self._append_to_chain(
            models.Drop(type=models.PreprocessingOperationType.DROP, columns=columns),
            nodes,
        )
        return self

    def set_columns(
        self, columns: List[str], create_if_missing: bool = False, dummy_value: str = ""
    ):
        """
        Sets the selected columns after all other preprocessing blocks are applied.

        This is similar to `.select`, except it always occurs after all other preprocessing
        operations have been applied. This is always a global operation.

        Args:
            columns (List[str]): list of column names to be selected
            create_if_missing (bool, optional): whether to create the columns if they do not exist. Defaults to False.
            dummy_value (str, optional): what to fill the created columns with. Defaults to "".
        """
        self.output_selection.columns = columns
        self.output_selection.create_if_missing = create_if_missing
        self.output_selection.dummy_value = dummy_value
        self.output_selection_set = True

    def filter(
        self,
        target_column: str,
        comparator: Union[str, Comparator, models.ComparisonType],
        value: str,
        numerical: bool = False,
        output_column: str = None,
        nodes: List[str] = None,
    ):
        """
        Adds a filter operation to the preprocessing chain.

        This operation filters rows from the data under a given condition. All records that do not
        match this condition are dropped.

        Args:
            target_column (str): name of column to filter on.
            comparator (str or Comparator): type of comparison. Either use the Comparator enum,
                or a user-friendly string ("==", ">", ">=", "<", "<=", or "!=").
            value (str): value with which to compare.
            numerical (bool, optional): whether the comparison is on numerical values. Defaults to False.
            output_column (str, optional): if specified, the dataset is *not* filtered. Instead, the boolean values
                of the filter are saved in a new column with the given name, taking values 0 or 1.
            nodes (List[str], optional): list of the name of nodes to apply the operation on, applied to all if None. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        if isinstance(comparator, str):
            comparator = Comparator.parse(comparator)
        self._append_to_chain(
            models.Filter(
                type=models.PreprocessingOperationType.FILTER,
                column=target_column,
                comparator=comparator,
                value=str(value),
                numerical=numerical,
                output_column=output_column,
            ),
            nodes,
        )
        return self

    def isin(self, target_column: str, values: List[str], nodes: List[str] = None):
        """
        Adds a "is in" filter operation to the preprocessing chain.

        This operation filters any rows whose 'target_column' attribute is not present in the list of provided 'values'.

        Args:
            target_column (str): the column to check the membership with.
            values (List[str]): the list of accepted values.
            nodes (List[str], optional): list of the name of nodes to apply the operation on, applied to all if None. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        self._append_to_chain(
            models.Filter(
                type=models.PreprocessingOperationType.FILTER,
                column=target_column,
                comparator=models.ComparisonType.ISIN,
                values=values,
                value="",
            ),
            nodes,
        )
        return self

    def counts(self, output_column_name: str = "count", nodes: List[str] = None):
        """
        Adds a counts operation to the preprocessing chain.

        This operation appends a new column filled with ones (called `output_column_name`) to the dataset.
        When using Aggregation operations, summing this column gives a number of columns.

        Args:
            output_column_name (str): name of the column to store the counts. If not specified, the name 'count' will be used.
            nodes (List[str], optional): list of the name of nodes to apply the operation on, applied to all if None. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        return self.new_column(name=output_column_name, value=1, nodes=nodes)

    def transpose(self, nodes: List[str] = None):
        """
        Adds a transpose operation to the preprocessing chain.

        This operation transposes the index and columns of the data (see `pandas.DataFrame.transpose`).

        Args:
            nodes (List[str], optional): list of the name of nodes to apply the operation on, applied to all if None. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        self._append_to_chain(
            models.Transpose(
                type=models.PreprocessingOperationType.TRANSPOSE,
            ),
            nodes,
        )
        return self

    def set_index(
        self,
        columns: List[str],
        drop: bool = True,
        append: bool = False,
        nodes: List[str] = None,
    ):
        """
        Adds a set_index operation to the preprocessing chain.

        This operation sets the DataFrame index to one or more existing columns in the data.

        Args:
            columns (List[str]): list of column names to set as index
            drop (bool, optional): Delete columns to be used as the new index. Defaults to True.
            append (bool, optional): Whether to append columns to existing index. Defaults to False.
            nodes (List[str], optional): list of the name of nodes to apply the operation on, applied to all if None. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        self._append_to_chain(
            models.SetIndex(
                type=models.PreprocessingOperationType.SETINDEX,
                columns=columns,
                drop=drop,
                append=append,
            ),
            nodes,
        )
        return self

    def reset_index(
        self, drop: bool = False, level: List[str] = None, nodes: List[str] = None
    ):
        """
        Add a reset_index operation to the preprocessing chain.

        This operation resets the DataFrame index (or a level of it if the index has several columns).
        See `pandas.DataFrame.reset_index` for details.

        Args:
            drop (bool, optional):  Whether to insert index into dataframe columns. This resets the index
                to the default integer index. Defaults to False.
            level (List[str], optional): list of column names to remove from index. Defaults to None.
            nodes (List[str], optional): list of the name of nodes to apply the operation on, applied to all if None. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        self._append_to_chain(
            models.ResetIndex(
                type=models.PreprocessingOperationType.RESETINDEX,
                drop=drop,
                level=level,
            ),
            nodes,
        )
        return self

    def rename(
        self,
        mapper: dict,
        axis: models.RenameAxis = models.RenameAxis.COLUMNS,
        errors: bool = True,
        nodes: List[str] = None,
    ):
        """
        Adds a rename operation to the preprocessing chain.

        This operation alters the axis labels. By default, this operation renames the columns of a dataset.

        Args:
            mapper (dict): Dict of name transformations to apply.
            axis (models.RenameAxis, optional): Axis to apply renaming to. Defaults to models.RenameAxis.COLUMNS.
            errors (bool, optional): If True raise a KeyError when a dict-like mapper, index, or columns contains
                labels that are not present in the Index being transformed. If False existing keys will be renamed
                and extra keys will be ignored. Defaults to True.
            nodes (List[str], optional): list of the name of nodes to apply the operation on, applied to all if None. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        mapper = models.RenameMapper.from_dict(mapper)
        self._append_to_chain(
            models.Rename(
                type=models.PreprocessingOperationType.RENAME,
                mapper=mapper,
                axis=axis,
                errors=errors,
            ),
            nodes,
        )
        return self

    def astype(
        self,
        type_map: dict,
        errors: bool = True,
        nodes: List[str] = None,
    ):
        """
        Adds an as_type operation to the preprocessing chain.

        The operation casts column types, converting the data in one or more columns to specific type(s).

        Args:
            type_map (dict):  Dict which maps column names to the data types (str) they should be cast to.
            errors (bool, optional): If True raise a KeyError if a column in the type_map does not exist in the data.
                If False existing columns will be cast and extra columns will be ignored. Defaults to True.
            nodes (List[str], optional): list of the name of nodes to apply the operation on, applied to all if None. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        type_map = models.AsTypeTypeMap.from_dict(type_map)
        self._append_to_chain(
            models.AsType(
                type=models.PreprocessingOperationType.ASTYPE,
                type_map=type_map,
                errors=errors,
            ),
            nodes,
        )
        return self

    def extract(
        self,
        field: str,
        columns: List[str],
        names: List[str] = None,
        nodes: List[str] = None,
    ):
        """
        Adds an extract operation to the preprocessing chain.

        This operation extracts field values from columns that contain dict-like data.
        For instance, extract(field="a") on data=["{'a': 1}"] would return [1].

        Args:
            field (str): name of the field to extract
            columns (List[str]): list of column names from which to extract the field values.
            names (List[str]): names of the resulting columns containing the extracted values.
            nodes (List[str], optional): list of the name of nodes to apply the operation on, applied to all if None. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        assert isinstance(columns, list)
        self._append_to_chain(
            models.ExtractDictField(
                type=models.PreprocessingOperationType.EXTRACTDICTFIELD,
                field=field,
                input_columns=columns,
                output_columns=names,
            ),
            nodes,
        )
        return self

    def apply_regex(
        self,
        regex: str,
        columns: List[str],
        names: List[str] = None,
        regex_type: models.ApplyRegExRegexType = models.ApplyRegExRegexType.MATCH,
        nodes: List[str] = None,
    ):
        """
        Adds an apply_regex operation to the preprocessing chain.

        The operation applies a regular expression to one or more columns. This creates new
        columns (or changes values in-place) containing either a matching value (for regex_type=MATCH),
        an integer (the position of a match, for regex_type=POSITION), or the list of all matches
        (for regex_type=FINDALL).

        Args:
            regex (str): regular expression to apply.
            columns (List[str]):  list of column names to apply the regular expression to.
            regex_type (models.ApplyRegExRegexType, optional): defines what we want to retrieve from the regex
                (see ApplyRegExRegexType). Defaults to models.ApplyRegExRegexType.MATCH.
            names (List[str]): names of resulting columns. If None, this operation is in place.
            nodes (List[str], optional): list of the name of nodes to apply the operation on, applied to all if None. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        assert isinstance(columns, list)
        self._append_to_chain(
            models.ApplyRegEx(
                type=models.PreprocessingOperationType.APPLYREGEX,
                regex=regex,
                input_columns=columns,
                regex_type=regex_type,
                output_columns=names,
            ),
            nodes,
        )
        return self

    def quantiles(
        self, input_column: str, min_v: float, max_v: float, nodes: List[str] = None
    ):
        """
        Adds a quantiles operation to the preprocessing chain.

        This computes the normalized local quantiles (min,q1,median,q3,max) of the input column.
        It operates in three steps:
         1. the quantiles are computed exactly on the data.
         2. the quantiles are normalized using the given `min_v` and `max_v` values.
         3. the results are by the dataset size.

        The output of this operation transforms the dataset to a single row with each transformed
        quantile, and the dataset size as last column. This operation should only be used in the
        context of an aggregation, in order to approximate the collective quantiles.
        Due to the output format, it is discouraged to run any other operation after running this one.
        After running a collective aggregation on the preprocessed values, the original values can be
        retrieved by performing the inverse transformation as a client-side post-processing operation.

        Args:
            input_column (str): the column from which to compute the quantiles
            min_v (float): the minimum expected value a sample can take
            max_v (float): the maximum expected value a sample can take
            nodes (List[str], optional): the nodes to apply this operation to. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        self._append_to_chain(
            models.Quantiles(
                type=models.PreprocessingOperationType.QUANTILES,
                input_column=input_column,
                min_=min_v,
                max_=max_v,
            ),
            nodes=nodes,
        )
        return self

    def time_diff(
        self,
        start: str,
        end: str,
        output: str,
        unit: models.TimeUnit = models.TimeUnit.MONTHS,
        unit_value=1,
        filter_na: bool = True,
        nodes: List[str] = None,
    ):
        """
        Adds a time_diff operation to the preprocessing chain.

        This operation computes the time difference between two datetime columns.
        The columns must be parsable dates/times. A new column is created.

        Args:
            start (str): the column indicating the first column (start of a measurement).
            end (str): the column indicating the second column (end of the measurement).
            output (str): the output column name.
            unit (models.TimeUnit, optional): the time unit to use. Defaults to models.TimeUnit.WEEKS.
            unit_value (int, optional): the value to use as interval for the time unit, defaults to 4.
            filter_na (bool, optional): whether to filter NaN values in both columns beforehand. Defaults to True.
            nodes (List[str], optional): the list of nodes to apply this preprocessing operation to. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        self._append_to_chain(
            models.TimeDiff(
                type=models.PreprocessingOperationType.TIMEDIFF,
                start_column=start,
                end_column=end,
                output_column=output,
                interval=models.Duration(unit=unit, value=unit_value),
                filter_na=filter_na,
            ),
            nodes,
        )
        return self

    def dropna(self, subset: List[str] = None, nodes: List[str] = None):
        """
        Adds a drop-n/a operation to the preprocessing chain.

        This operation drops all rows that contain NaN values, using the standard pandas function.
        Note: it treats the strings 'NaN' has an actual NaN values (in addition to "").

        Args:
            nodes (List[str], optional): the list of nodes to apply this preprocessing operation to. Defaults to None.
        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        if subset is None:
            subset = UNSET
        self._append_to_chain(
            models.Dropna(type=models.PreprocessingOperationType.DROPNA, subset=subset),
            nodes,
        )
        return self

    def apply_mapping(
        self,
        input_column: str,
        output: str,
        mapping: Dict[str, str],
        default: str = "",
        nodes: List[str] = None,
    ):
        """
        Adds an apply_mapping operation to the preprocessing chain.

        This operation creates a new column based on another column, given a mapping defined by the user.

        Args:
            input_column (str): the source column
            output (str): the newly derived column name
            mapping (Dict[str,str]): the mapping of values
            default (str, optional): default value to use when the value does not match any value from the mapping. Defaults to "".
            nodes (List[str], optional): the list of nodes to apply this preprocessing operation to. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        sm = models.StringMapping.from_dict(mapping)
        # Convert all keys and values to strings
        for key, value in sm.additional_properties.items():
            sm.additional_properties[key] = str(value)

        self._append_to_chain(
            models.ApplyMapping(
                type=models.PreprocessingOperationType.APPLYMAPPING,
                input_column=input_column,
                output_column=output,
                mapping=sm,
                default=str(default),
            ),
            nodes=nodes,
        )
        return self

    def cut(
        self,
        input_column: str,
        output: str,
        cuts: List[float],
        labels: List[str] = None,
        nodes: List[str] = None,
    ):
        """
        Adds a cut operation to the preprocessing chain.

        This operation "bins" a numerical variable: it transforms each value into a category (bin),
        according to a list of cuts and labels defined by the user. For instance, the cuts [a, b]
        would create three categories: (, a), [a, b), [b, ).

        Args:
            input_column (str): name of the input column
            output (str): name of the output column
            cuts (List[float]): the list of cuts (must be numerical)
            labels (List[str], optional): list of associated labels/categories must be equal to `len(cuts) - 1`
            nodes (List[str], optional): If specified, applies the preprocessing operation only for the given nodes. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """

        if len(labels) != len(cuts) - 1:
            raise ValueError(
                f"Number of labels ({len(labels)}) does not match number of cuts + 1 ({len(cuts) - 1} + 1)."
            )
        # Make sure the values passed are in appropriate format
        for i, _ in enumerate(cuts):
            cuts[i] = float(cuts[i])
        for i, _ in enumerate(labels):
            labels[i] = str(labels[i])
        self._append_to_chain(
            models.Cut(
                type=models.PreprocessingOperationType.CUT,
                input_column=input_column,
                output_column=output,
                cuts=cuts,
                labels=labels,
            ),
            nodes=nodes,
        )
        return self

    def deviation_squares(
        self,
        input_column: str,
        output_column: str,
        mean: float,
        count: int = 0,
        nodes: List[str] = None,
    ):
        """
        Adds a deviation_squares operation to the preprocessing chain.

        This operation creates a new column where each value is equal to (df[input_column] - mean)^2 / (count - 1),
        where mean and count are fixed input variables. If count is < 1 then the denominator is set to 1.
        This should be used when computing the variance of a variable once the global mean and count are known.

        Args:
            input_column (str): the input column
            output_column (str): the output column
            mean (float): the previously computed global mean
            count (int, optional): the previously computed global count. Defaults to 0.
            nodes (List[str], optional): the nodes to assign the preprocessing operation to. Defaults to None.
        """
        mean = float(mean)
        count = int(count)
        self._append_to_chain(
            models.DeviationSquares(
                models.PreprocessingOperationType.DEVIATIONSQUARES,
                count=count,
                input_column=input_column,
                output_column=output_column,
                mean=mean,
            ),
            nodes=nodes,
        )
        return self

    def add_columns(
        self,
        input_cols: List[str],
        output: str,
        sep: str = "",
        numerical: bool = False,
        nodes: List[str] = None,
    ):
        """
        Adds an add_columns operation to the preprocessing chain.

        This operation adds together the specified columns, creating a new output column.
        By default, this operation is not numerical, and concatenates strings (with an
        optional separator). If numerical is True, arithmetic sum is used instead.

        Args:
            input_cols (str): the columns to add together
            output (str): name of the output column
            sep (str, optional): separator when the columns are strings. Defaults to "".
            numerical (bool, optional): whether or not to add numerically. Defaults to False.
            nodes (List[str], optional): the nodes for which the preprocessing applies to. Defaults to None.
        """
        self._append_to_chain(
            models.AddColumns(
                type=models.PreprocessingOperationType.ADDCOLUMNS,
                input_columns=input_cols,
                output_column=output,
                sep=sep,
                numerical=numerical,
            ),
            nodes,
        )
        return self

    def scale(
        self,
        input_columns: List[str],
        scale: float,
        output_columns: List[str] = None,
        nodes: List[str] = None,
    ):
        """
        Adds a scale operation to the preprocessing chain. This operation scales one or more columns by a constant.

        Args:
            input_columns (List[str]): the names of one or more columns to scale.
            scale (float): the constant factor by which to scale the columns.
            output_columns (List[str], optional): if specified, names of columns to save the results to. If not specified
              (by default), the input columns are overwritten in place.
            nodes (List[str], optional): the nodes for which the preprocessing applies to. Defaults to None.
        """
        self._append_to_chain(
            models.Scale(
                type=models.PreprocessingOperationType.SCALE,
                scale=scale,
                input_columns=input_columns,
                output_columns=output_columns,
            ),
            nodes,
        )
        return self

    def multiply_columns(
        self, input_columns: List[str], output_column: str, nodes: List[str] = None
    ):
        """
        Adds a multiply_columns operation to the preprocessing chain.

        This operation multiplies together the values in specified columns, and saves the result
        in the output column. It requires all input columns to contain numerical values.

        Args:
            input_columns (List[str]): the names of the columns to multiply together.
            output_column (str): the name of the output column.
            nodes (List[str], optional): the nodes for which the preprocessing applies to. Defaults to None.
        """
        self._append_to_chain(
            models.MultiplyColumns(
                type=models.PreprocessingOperationType.MULTIPLYCOLUMNS,
                input_columns=input_columns,
                output_column=output_column,
            ),
            nodes,
        )
        return self

    def new_column(
        self,
        name: str,
        value: str = None,
        loc: float = None,
        scale: float = None,
        nodes: List[str] = None,
    ):
        """
        Adds a new_column operation to the preprocessing chain.

        If `value` is specified, all the values in the new column will have this value.
        Otherwise, if `loc` and/or `scale` are defined, the values will be sampled from
        a normal distribution with mean `loc` (or 0) and standard deviation `scale` (or 1).
        If neither are specified, the new column will contain the value "1" (for counts).

        Args:
            name (str): the name of the new column to create.
            value (str, optional): If specified, the new column will have this value. Defaults to None.
            loc (float, optional): If specified, the mean of the random values sampled for this column.
                Defaults to None.
            scale (float, optional): If specified, the standard deviation of the random values sampled
                for this column. Defaults to None.
            nodes (List[str], optional): the nodes for which the preprocessing applies to. Defaults to None.
        """
        random = UNSET
        if loc is not None or scale is not None:
            random = models.NewColumnRandom(loc=loc, scale=scale)
        self._append_to_chain(
            models.NewColumn(
                type=models.PreprocessingOperationType.NEWCOLUMN,
                name=name,
                value=str(value),
                random=random,
            ),
            nodes,
        )
        return self

    def custom(
        self,
        function: Callable[[pd.DataFrame], pd.DataFrame],
        name: str = "",
        description: str = "",
        output_columns: List[str] = None,
        compatible_with_dp: bool = False,
        nodes: List[str] = None,
    ):
        """
        Adds a custom python preprocessing block to the chain.

        This operation runs a specified Python function on each input dataset, and uses the output of that
        function as processed dataset. In principle, arbitrary functions can be used here, although `import`
        statements are forbidden, and only the `np` and `pd` modules are available. This can be used to define
        complex preprocessing operations.

        🔥 This preprocessing operation can be dangerous as it enables the users to run code on other organization's
        machine. Workflows containing such preprocessing blocks should always be carefully reviewed by the responsible
        data controllers from each participating organization before approving the project. This operation can be
        disabled at the instance level, and may not be avaulable in oyur project.

        Args:
            function (Callable[[pd.DataFrame], pd.DataFrame]): the preprocessing operation, must be a python function
                which takes as input a dataframe and returns a new dataframe.
            name (str, optional): common name given to the operation, for indicative purposes. Defaults to "".
            description (str, optional): description given to the operation for indicative purposes. Defaults to "".
            compatible_with_dp (bool, optional): whether this operation is compatible with differential privacy. For this,
                it must (1) be a stable transformation (at most one output record per input record) and (2) have a statically
                determined set of output columns (i.e., not dependent on the input data). Contact Tune Insight if you
                have questions about this. 🔥 Only set to true if you know what you are doing.
            output_columns (List[str], optional): the  list of columns added to the output dataset. This is only
                required for dry runs and differential privacy. If provided, conformity is checked and an error is
                returned if the columns mismatch.
            nodes (List[str], optional): the nodes for which the preprocessing block will apply to. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        self._append_to_chain(
            models.Custom(
                type=models.PreprocessingOperationType.CUSTOM,
                name=name,
                description=description,
                function=get_code(function),
                output_columns=output_columns,
                compatible_with_differential_privacy=compatible_with_dp,
            ),
            nodes,
        )
        return self

    def gwas_preprocessing(
        self,
        genomic_nodes: List[str],
        clinical_nodes: List[str],
        sample_cols: List[str],
    ):
        """
        Adds the preprocessing operations required for a Genome-Wide Association Study.

        Args:
            genomic_nodes (List[str]): list of names of the nodes containing genomic data.
            clinical_nodes (List[str]): list of names of the nodes containing clinical data.
            sample_cols (List[str]): list of column names containing sample data within the genomic data.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        self.set_index(columns=["LOCUS"], nodes=genomic_nodes)
        self.select(columns=sample_cols, nodes=genomic_nodes)
        self.extract(field="GT_type", columns=sample_cols, nodes=genomic_nodes)
        self.transpose(nodes=genomic_nodes)
        self.reset_index(nodes=genomic_nodes)
        self.rename(
            mapper={"index": "ID"}, axis=models.RenameAxis.COLUMNS, nodes=genomic_nodes
        )
        self.rename(
            mapper={"Sample": "ID"},
            axis=models.RenameAxis.COLUMNS,
            nodes=clinical_nodes,
        )
        return self

    def create_survival_columns(
        self, params: "SurvivalParameters", nodes: List[str] = None
    ):
        """
        Adds the preprocessing operations required for a survival analysis.

        Args:
            params (computations.SurvivalParameters): parameters of the survival analysis.
            nodes (List[str], optional): list of the name of nodes to apply the operations on, applied to all if None. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        self._append_to_chain(params.get_preprocessing_op(), nodes)
        return self

    def dry_run(self, client: Client, starting_columns: List[str]) -> List[str]:
        if not isinstance(client, Client):
            client = client.client
        resp = get_preprocessing_dry_run.sync_detailed(
            client=client,
            json_body=get_preprocessing_dry_run.GetPreprocessingDryRunJsonBody(
                chain=models.PreprocessingChain(chain=self.chain),
                columns=starting_columns,
            ),
        )
        validate_response(resp)
        return resp.parsed

    def _append_to_chain(
        self, op: models.PreprocessingOperation, nodes: List[str] = None
    ):
        """
        Appends a preprocessing operation to the global or compound chain.

        Args:
            op (models.PreprocessingOperation): the preprocessing operation to append
            nodes (List[str], optional): list of the name of nodes to apply the operation on, applied to all if None. Defaults to None.
        """
        if nodes is None:
            self.chain.append(op)
        else:
            assert isinstance(nodes, list)
            for node in nodes:
                if node not in self.compound_chain.keys():
                    self.compound_chain.update({node: models.PreprocessingChain([op])})
                else:
                    node_chain = self.compound_chain.get(node)
                    node_chain.chain.append(op)
                    self.compound_chain[node] = node_chain
        if self.update_function is not None:
            self.update_function()

    def check_validity(self):
        """Checks that the preprocessing chains are valid."""
        if self._check_chain(self.chain) is True:
            warn(
                "Preprocessing chain contains one hot encoding without a subsequent select. This could lead to an error if nodes have different categorical values. \n Chain: "
                + str(self.chain),
                stacklevel=2,
            )

        for node, node_chain in self.compound_chain.items():
            if self._check_chain(node_chain.chain) is True:
                warn(
                    "Preprocessing chain for node "
                    + node
                    + " contains one hot encoding without a subsequent select. This could lead to an error if nodes have different categorical values. \n Chain: "
                    + str(node_chain),
                    stacklevel=2,
                )

    @staticmethod
    def _check_chain(chain: models.PreprocessingChain) -> bool:
        """
        Checks that a preprocessing chain contains a select after one hot encoding without specified types.
        """
        one_hot_without_select = False
        for ppo in chain:
            if ppo.type == models.PreprocessingOperationType.ONEHOTENCODING:
                if is_unset(ppo.specified_types):
                    one_hot_without_select = True
            if ppo.type == models.PreprocessingOperationType.SELECT:
                one_hot_without_select = False

        return one_hot_without_select

    def get_model(self) -> models.ComputationPreprocessingParameters:
        """Returns these parameters as an API model."""
        res = models.ComputationPreprocessingParameters()
        self.check_validity()
        if self.chain != []:
            res.global_preprocessing = models.PreprocessingChain(self.chain)
        if self.compound_chain != {}:
            compound_params = (
                models.ComputationPreprocessingParametersCompoundPreprocessing()
            )
            compound_params.additional_properties = self.compound_chain
            res.compound_preprocessing = compound_params
        if self.output_selection_set:
            res.select = self.output_selection

        if self.schema is not None:
            res.dataset_schema = self.schema.model
        return res

    def reset(self, patch: bool = True):
        """
        Resets the preprocessing builder to the initial state.

        Args:
            patch (bool, optional): whether to update the project when resetting.
        """
        self.chain = []
        self.compound_chain = {}
        self.output_selection = models.Select(
            type=models.PreprocessingOperationType.SELECT, columns=[]
        )
        self.output_selection_set = False
        self.schema = None
        if patch and self.update_function is not None:
            self.update_function()

    @classmethod
    def from_model(cls, model: models.ComputationPreprocessingParameters):
        """Initializes a PreprocessingBuilder from an API model."""
        p = cls()
        if is_unset(model):
            return p
        if is_set(model.global_preprocessing):
            p.new_chain(model.global_preprocessing.chain)
        if is_set(model.compound_preprocessing):
            p.new_compound_chain(model.compound_preprocessing.additional_properties)
        if is_set(model.select):
            p.output_selection = model.select
            p.output_selection_set = True
        if is_set(model.dataset_schema):
            p.schema = model.dataset_schema
        return p
