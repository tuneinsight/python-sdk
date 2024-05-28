from enum import Enum
from typing import Dict, List, Callable
from warnings import warn
import pandas as pd

from tuneinsight.utils.code import get_code
from tuneinsight.api.sdk.types import UNSET
from tuneinsight.api.sdk import models
from tuneinsight.computations.dataset_schema import DatasetSchema
from tuneinsight.api.sdk.models import PreprocessingOperationType as op_type


class Operation(Enum):
    ONE_HOT = op_type.ONEHOTENCODING
    PHONETIC = op_type.PHONETICENCODING
    SELECT = op_type.SELECT
    DROP = op_type.DROP
    FILTER = op_type.FILTER
    COUNTS = op_type.COUNTS
    SURVIVAL = op_type.SURVIVAL
    TRANSPOSE = op_type.TRANSPOSE
    RENAME = op_type.RENAME

    def to_preproc_operation_type(self) -> op_type:
        return op_type(self.value)


class PreprocessingBuilder:
    """
    Pre-processing chain builder. This class is used to build a sequence of preprocessing operations
    that are applied sequentially on the local dataset before running the computations.

    """

    chain: List[models.PreprocessingOperation]
    compound_chain: Dict[str, models.PreprocessingChain]
    output_selection: models.Select
    output_selection_set: bool
    schema: DatasetSchema

    def __init__(self):
        self.reset()

    def new_schema(self) -> DatasetSchema:
        self.schema = DatasetSchema()
        return self.schema

    def new_chain(self, chain: List[models.PreprocessingOperation]):
        """Sets the global pre-processing chain

        Args:
            chain (List[models.PreprocessingOperation]): list of pre-processing operations constituting the chain

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        self.chain = chain
        return self

    def new_compound_chain(self, chain: Dict[str, models.PreprocessingChain]):
        """Sets the compound pre-processing chain

        Args:
            chain (Dict[str, models.PreprocessingChain]): dictionary mapping each node to its individual preprocessing chain

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        self.compound_chain = chain
        return self

    def one_hot_encoding(
        self,
        target_column: str,
        prefix: str,
        specified_types: List[str],
        nodes: List[str] = None,
    ):
        """Add a one hot encoding operation to the preprocessing chain. This operation encodes a target column into one hot encoding and extends the table with the resulting columns.


        Args:
            target_column (str): the name of the column on which to perform the one-hot-encoding
            prefix (str): the prefix of the output column name containing the one-hot encoded values
            specified_types (List[str]): a list of categorical values to create one-hot encoding columns for (even if they are not in the target column)
            nodes (List[str], optional): list of the name of nodes to apply the operation on, applied to all if None. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        self.append_to_chain(
            models.OneHotEncoding(
                type=models.PreprocessingOperationType.ONEHOTENCODING,
                input_col=target_column,
                prefix=prefix,
                specified_types=specified_types,
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
        """Add a select operation to the preprocessing chain. The operation selects specified columns from data.

        Args:
            columns (List[str]): list of column names to be selected
            create_if_missing (bool, optional): whether to create the columns if they do not exist. Defaults to False.
            dummy_value (str, optional): what to fill the created columns with. Defaults to "".
            nodes (List[str], optional): list of the name of nodes to apply the operation on, applied to all if None. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        self.append_to_chain(
            models.Select(
                type=models.PreprocessingOperationType.SELECT,
                cols=columns,
                create_if_missing=create_if_missing,
                dummy_value=dummy_value,
            ),
            nodes,
        )
        return self

    def set_columns(
        self, columns: List[str], create_if_missing: bool = False, dummy_value: str = ""
    ):
        """
        set_columns sets the selected columns after all other preprocessing blocks are applied

        Args:
            columns (List[str]): list of column names to be selected
            create_if_missing (bool, optional): whether to create the columns if they do not exist. Defaults to False.
            dummy_value (str, optional): what to fill the created columns with. Defaults to "".
        """
        self.output_selection.cols = columns
        self.output_selection.create_if_missing = create_if_missing
        self.output_selection.dummy_value = dummy_value
        self.output_selection_set = True

    def filter(
        self,
        target_column: str,
        comparator: models.ComparisonType,
        value: str,
        numerical: bool = False,
        nodes: List[str] = None,
    ):
        """Add a filter operation to the preprocessing chain. The operation filters rows from the data under a given condition.

        Args:
            target_column (str): name of column to filter on
            comparator (models.ComparisonType): type of comparison
            value (str): value with which to compare
            numerical (bool, optional): whether the comparison is on numerical values. Defaults to False.
            nodes (List[str], optional): list of the name of nodes to apply the operation on, applied to all if None. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        self.append_to_chain(
            models.Filter(
                type=models.PreprocessingOperationType.FILTER,
                col_name=target_column,
                comparator=comparator,
                value=str(value),
                numerical=numerical,
            ),
            nodes,
        )
        return self

    def isin(self, target_column: str, values: List[str], nodes: List[str] = None):
        """
        Adds a filter operation to the preprocessing chain that filters any rows whose 'target_column' attribute is not present in the list of provided 'values'.

        Args:
            target_column (str): the column to check the membership with.
            values (List[str]): the list of accepted values.
            nodes (List[str], optional): list of the name of nodes to apply the operation on, applied to all if None. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        self.append_to_chain(
            models.Filter(
                type=models.PreprocessingOperationType.FILTER,
                col_name=target_column,
                comparator=models.ComparisonType.ISIN,
                values=values,
                value="",
            ),
            nodes,
        )
        return self

    def counts(self, output_column_name: str, nodes: List[str] = None):
        """Add a counts operation to the preprocessing chain. The operation concatenates a new column filled with ones.

        Args:
            output_column_name (str): name of the column to store the counts. If not specified, the name 'count' will be used.
            nodes (List[str], optional): list of the name of nodes to apply the operation on, applied to all if None. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        self.append_to_chain(
            models.Counts(
                type=models.PreprocessingOperationType.COUNTS,
                output_col=output_column_name,
            ),
            nodes,
        )
        return self

    def transpose(self, copy: bool = False, nodes: List[str] = None):
        """Add a transpose operation to the preprocessing chain. The operation transposes the index and columns of the data.


        Args:
            copy (bool, optional): Whether to copy the data after transposing. Defaults to False.
            nodes (List[str], optional): list of the name of nodes to apply the operation on, applied to all if None. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        self.append_to_chain(
            models.Transpose(
                type=models.PreprocessingOperationType.TRANSPOSE, copy=copy
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
        """Add a set index operation to the preprocessing chain. The operation sets the DataFrame index using existing columns.

        Args:
            columns (List[str]): list of column names to set as index
            drop (bool, optional): Delete columns to be used as the new index. Defaults to True.
            append (bool, optional): Whether to append columns to existing index. Defaults to False.
            nodes (List[str], optional): list of the name of nodes to apply the operation on, applied to all if None. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        self.append_to_chain(
            models.SetIndex(
                type=models.PreprocessingOperationType.SETINDEX,
                cols=columns,
                drop=drop,
                append=append,
            ),
            nodes,
        )
        return self

    def reset_index(
        self, drop: bool = False, level: List[str] = None, nodes: List[str] = None
    ):
        """Add a reset index operation to the preprocessing chain. The operation resets the DataFrame index (or a level of it).

        Args:
            drop (bool, optional):  Whether to insert index into dataframe columns. This resets the index to the default integer index. Defaults to False.
            level (List[str], optional): list of column names to remove from index. Defaults to None.
            nodes (List[str], optional): list of the name of nodes to apply the operation on, applied to all if None. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        self.append_to_chain(
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
        copy: bool = True,
        errors: bool = True,
        nodes: List[str] = None,
    ):
        """Add a rename operation to the preprocessing chain. The operation alters axis labels.

        Args:
            mapper (dict): Dict of name transformations to apply.
            axis (models.RenameAxis, optional): Axis to apply renaming to. Defaults to models.RenameAxis.COLUMNS.
            copy (bool, optional): Whether to copy underlying data. Defaults to True.
            errors (bool, optional): If True raise a KeyError when a dict-like mapper, index, or columns contains labels that are not present in the Index being transformed. If False existing keys will be renamed and extra keys will be ignored. Defaults to True.
            nodes (List[str], optional): list of the name of nodes to apply the operation on, applied to all if None. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        mapper = models.RenameMapper.from_dict(mapper)
        self.append_to_chain(
            models.Rename(
                type=models.PreprocessingOperationType.RENAME,
                mapper=mapper,
                axis=axis,
                copy=copy,
                errors=errors,
            ),
            nodes,
        )
        return self

    def astype(
        self,
        type_map: dict,
        copy: bool = True,
        errors: bool = True,
        nodes: List[str] = None,
    ):
        """Add an as type operation to the preprocessing chain. The operation casts column types.

        Args:
            type_map (dict):  Dict which maps column names to the data types they should be cast to.
            copy (bool, optional): Whether to return a copy of the data. Defaults to True.
            errors (bool, optional): If True raise a KeyError if a column in the type_map does not exist in the data. If False existing columns will be cast and extra columns will be ignored. Defaults to True.
            nodes (List[str], optional): list of the name of nodes to apply the operation on, applied to all if None. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        type_map = models.AsTypeTypeMap.from_dict(type_map)
        self.append_to_chain(
            models.AsType(
                type=models.PreprocessingOperationType.ASTYPE,
                type_map=type_map,
                copy=copy,
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
        """Add an extract operation to the preprocessing chain. The operation extracts field values from dict-like columns.


        Args:
            field (str): name of the field to extract
            columns (List[str]): list of column names from which to extract the field values.
            names (List[str]): names of the resulting columns containing the extracted values.
            nodes (List[str], optional): list of the name of nodes to apply the operation on, applied to all if None. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        assert isinstance(columns, list)
        self.append_to_chain(
            models.ExtractDictField(
                type=models.PreprocessingOperationType.EXTRACTDICTFIELD,
                field=field,
                cols=columns,
                names=names,
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
        """Add an apply regex operation to the preprocessing chain. The operation applies a regular expression to columns.

        Args:
            regex (str): regular expression to apply.
            columns (List[str]):  list of column names to apply the regular expression to.
            regex_type (models.ApplyRegExRegexType, optional): defines what we want to retrieve from the regex (see ApplyRegExRegexType). Defaults to models.ApplyRegExRegexType.MATCH.
            names (List[str]): names of resulting columns. If None, this operation is in place.
            nodes (List[str], optional): list of the name of nodes to apply the operation on, applied to all if None. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        assert isinstance(columns, list)
        self.append_to_chain(
            models.ApplyRegEx(
                type=models.PreprocessingOperationType.APPLYREGEX,
                regex=regex,
                cols=columns,
                regex_type=regex_type,
                names=names,
            ),
            nodes,
        )
        return self

    def quantiles(
        self, input_: str, min_v: float, max_v: float, nodes: List[str] = None
    ):
        """
        quantiles computes the local quantiles (min,q1,median,q3,max) of the input column,
        and then applies the following transformation to each quantile:
        - normalization using the given `min_v` and `max_v` values.
        - scaling by the dataset size.
        The output contains a single row with each transformed quantiles and as the last column the dataset size.
        This operation is intended to be used whenever collective quantiles are approximated through a weighted aggregation.
        Due to the output format, it is discouraged to run any other operation after running this one.
        After running a collective aggregation on the preprocessed values, the original values can be retrieved by performing the inverse transformation
        as a client-side post-processing operation.

        Args:
            input_ (str): the column from which to compute the quantiles
            min_v (float): the minimum expected value a sample can take
            max_v (float): the maximum expected value a sample can take
            nodes (List[str], optional): the nodes to apply this operation to. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        self.append_to_chain(
            models.Quantiles(
                type=models.PreprocessingOperationType.QUANTILES,
                input_=input_,
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
        time_diff computes the time difference between two datetime columns (must be parsable dates/times)

        Args:
            start (str): the column indicating the start of the measurement
            end (str): the column indicating the end of the measurement
            output (str): the output column name
            unit (models.TimeUnit, optional): the time unit to use. Defaults to models.TimeUnit.WEEKS.
            unit_value (int, optional): the value to use as interval for the time unit, defaults to 4.
            filter_na (bool, optional): whether to filter NaN values in both columns beforehand. Defaults to True.
            nodes (List[str], optional): the list of nodes to apply this preprocessing operation to. Defaults to None.

        Returns:
            _type_: _description_
        """
        duration = models.Duration(unit=unit, value=unit_value)
        self.append_to_chain(
            models.TimeDiff(
                type=models.PreprocessingOperationType.TIMEDIFF,
                start=start,
                end=end,
                output=output,
                interval=duration,
                filter_na=filter_na,
            ),
            nodes,
        )
        return self

    def dropna(self, subset: List[str] = None, nodes: List[str] = None):
        """
        dropna Drops all rows that contain NaN values, calls the standard pandas function, it also converts strings with the value 'NaN' to actual NaN values

        Args:
            nodes (List[str], optional): the list of nodes to apply this preprocessing operation to. Defaults to None.
        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        if subset is None:
            subset = UNSET
        self.append_to_chain(
            models.Dropna(type=models.PreprocessingOperationType.DROPNA, subset=subset),
            nodes,
        )
        return self

    def apply_mapping(
        self,
        input_: str,
        output: str,
        mapping: Dict[str, str],
        default: str = "",
        nodes: List[str] = None,
    ):
        """
        apply_mapping creates a new column based on another column, given a mapping defined by the user

        Args:
            input_ (str): the source column
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

        self.append_to_chain(
            models.ApplyMapping(
                type=models.PreprocessingOperationType.APPLYMAPPING,
                input_=input_,
                output=output,
                mapping=sm,
                default=str(default),
            ),
            nodes=nodes,
        )
        return self

    def cut(
        self,
        input_: str,
        output: str,
        cuts: List[float],
        labels: List[str] = None,
        nodes: List[str] = None,
    ):
        """
        cut transforms a numeric variable into categories according to a list of cuts and labels defined by the user

        Args:
            input_ (str): name of the input column
            output (str): name of the output column
            cuts (List[float]): the list of cuts (must be numerical)
            labels (List[str], optional): list of associated labels/categories must be equal to `len(cuts) - 1`
            nodes (List[str], optional): If specified, applies the preprocessing operation only for the given nodes. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """

        if len(labels) != len(cuts) - 1:
            raise ValueError(
                f"wrong number of labels, expected {len(cuts) - 1}, got {len(labels)}"
            )
        # Make sure the values passed are in appropriate format
        for i, _ in enumerate(cuts):
            cuts[i] = float(cuts[i])
        for i, _ in enumerate(labels):
            labels[i] = str(labels[i])
        self.append_to_chain(
            models.Cut(
                type=models.PreprocessingOperationType.CUT,
                input_=input_,
                output=output,
                cuts=cuts,
                labels=labels,
            ),
            nodes=nodes,
        )
        return self

    def deviation_squares(
        self,
        input_: str,
        output_: str,
        mean: float,
        count: int = 0,
        nodes: List[str] = None,
    ):
        """
        deviation_squares creates a new column where each value is equal to (df[input] - mean)^2- / (count - 1)
        if count is < 1 then the denominator is equal to 1 (computes the squared deviation)
        should be used when computing the variance of a variable once the global mean and count are known

        Args:
            input_ (str): the input column
            output_ (str): the output column
            mean (float): the previously computed global mean
            count (int, optional): the previously computed global count. Defaults to 0.
            nodes (List[str], optional): the nodes to assign the preprocessing operation to. Defaults to None.
        """
        mean = float(mean)
        count = int(count)
        self.append_to_chain(
            models.DeviationSquares(
                models.PreprocessingOperationType.DEVIATIONSQUARES,
                count=count,
                input_=input_,
                output=output_,
                mean=mean,
            ),
            nodes=nodes,
        )

    def add_columns(
        self,
        input_cols: List[str],
        output: str,
        sep: str = "",
        numerical: bool = False,
        nodes: List[str] = None,
    ):
        """
        add_columns adds the specified columns together, if the columns are not numerical a separator can be additionally specified

        Args:
            input_cols (str): the columns to add together
            output (str): name of the output column
            sep (str, optional): separator when the columns are strings. Defaults to "".
            numerical (bool, optional): whether or not to add numerically. Defaults to False.
            nodes (List[str], optional): the nodes for which the preprocessing applies to. Defaults to None.
        """
        self.append_to_chain(
            models.AddColumns(
                type=models.PreprocessingOperationType.ADDCOLUMNS,
                input_columns=input_cols,
                output=output,
                sep=sep,
                numerical=numerical,
            ),
            nodes,
        )

    def custom(
        self,
        function: Callable[[pd.DataFrame], pd.DataFrame],
        name: str = "",
        description: str = "",
        nodes: List[str] = None,
    ):
        """
        custom adds a custom python preprocessing block to the chain.
        **WARNING**: This preprocessing operation can be dangerous as it enables the users to run code on other organization's machine.
        Workflows containing such preprocessing blocks should always be carefully reviewed by the responsible data controllers from each
        participating organization before approving the project.

        Args:
            function (Callable[[pd.DataFrame], pd.DataFrame]): the preprocessing operation, must be a python function which takes as input a dataframe and returns a new dataframe
            name (str, optional): common name given to the operation, for indicative purposes. Defaults to "".
            description (str, optional): description given to the operation for indicative purposes. Defaults to "".
            nodes (List[str], optional): the nodes for which the preprocessing block will apply to. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        self.append_to_chain(
            models.Custom(
                type=models.PreprocessingOperationType.CUSTOM,
                name=name,
                description=description,
                function=get_code(function),
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
        """Add the necessary preprocessing operations for a Genome-Wide Association Study.

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
        """Add the necessary preprocessing operations for a survival analysis.

        Args:
            params (computations.SurvivalParameters): parameters of the survival analysis.
            nodes (List[str], optional): list of the name of nodes to apply the operations on, applied to all if None. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        self.append_to_chain(params.get_preprocessing_op(), nodes)
        return self

    def append_to_chain(
        self, op: models.PreprocessingOperation, nodes: List[str] = None
    ):
        """Append a preprocessing operation to the global or compound chain.

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

    def check_validity(self):
        """
        Check the validity of the preprocessing chains.
        """
        if self.check_chain(self.chain) is True:
            warn(
                "Preprocessing chain contains one hot encoding without a subsequent select. This could lead to an error if nodes have different categorical values. \n Chain: "
                + str(self.chain),
                stacklevel=2,
            )

        for node, node_chain in self.compound_chain.items():
            if self.check_chain(node_chain.chain) is True:
                warn(
                    "Preprocessing chain for node "
                    + node
                    + " contains one hot encoding without a subsequent select. This could lead to an error if nodes have different categorical values. \n Chain: "
                    + str(node_chain),
                    stacklevel=2,
                )

    @staticmethod
    def check_chain(chain: models.PreprocessingChain) -> bool:
        """
        Check that a preprocessing chain contains a select after one hot encoding.
        """
        one_hot_without_select = False
        for ppo in chain:
            if ppo.type == models.PreprocessingOperationType.ONEHOTENCODING:
                one_hot_without_select = True
            if ppo.type == models.PreprocessingOperationType.SELECT:
                one_hot_without_select = False

        return one_hot_without_select

    def get_params(self) -> models.ComputationPreprocessingParameters:
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

    def reset(self):
        """
        Resets the preprocessing builder to the initial state.
        """
        self.chain = []
        self.compound_chain = {}
        self.output_selection = models.Select(
            type=models.PreprocessingOperationType.SELECT, cols=[]
        )
        self.output_selection_set = False
        self.schema = None
