from typing import Dict,List
from warnings import warn
from tuneinsight.api.sdk import models
from tuneinsight.computations.survival import SurvivalParameters


class PreprocessingBuilder:
    """
    Pre-processing chain builder
    """

    chain: List[models.PreprocessingOperation]
    compound_chain: Dict[str, models.PreprocessingChain]

    def __init__(self):
        self.chain = []
        self.compound_chain = {}


    def new_chain(self, chain: List[models.PreprocessingOperation]):
        """ Sets the global pre-processing chain

        Args:
            chain (List[models.PreprocessingOperation]): list of pre-processing operations constituting the chain

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        self.chain = chain
        return self

    def new_compound_chain(self, chain: Dict[str, models.PreprocessingChain]):
        """ Sets the compound pre-processing chain

        Args:
            chain (Dict[str, models.PreprocessingChain]): dictionary mapping each node to its individual preprocessing chain

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        self.compound_chain = chain
        return self

    def one_hot_encoding(self, target_column: str, prefix: str, specified_types: List[str], nodes: List[str] = None):
        """ Add a one hot encoding operation to the preprocessing chain. This operation encodes a target column into one hot encoding and extends the table with the resulting columns.


        Args:
            target_column (str): the name of the column on which to perform the one-hot-encoding
            prefix (str): the prefix of the output column name containing the one-hot encoded values
            specified_types (List[str]): a list of categorical values to create one-hot encoding columns for (even if they are not in the target column)
            nodes (List[str], optional): list of the name of nodes to apply the operation on, applied to all if None. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        self.append_to_chain(models.OneHotEncoding(type=models.PreprocessingOperationType.ONEHOTENCODING, input_col = target_column, prefix = prefix, specified_types = specified_types), nodes)
        return self

    def select(self, columns: List[str], create_if_missing:bool = False, dummy_value:str = "", nodes: List[str] = None):
        """ Add a select operation to the preprocessing chain. The operation selects specified columns from data.

        Args:
            columns (List[str]): list of column names to be selected
            create_if_missing (bool, optional): whether to create the columns if they do not exist. Defaults to False.
            dummy_value (str, optional): what to fill the created columns with. Defaults to "".
            nodes (List[str], optional): list of the name of nodes to apply the operation on, applied to all if None. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        self.append_to_chain(models.Select(type=models.PreprocessingOperationType.SELECT, cols=columns, create_if_missing=create_if_missing, dummy_value=dummy_value), nodes)
        return self

    def filter(self, target_column: str, comparator:models.ComparisonType, value:str, numerical:bool = False, nodes: List[str] = None):
        """ Add a filter operation to the preprocessing chain. The operation filters rows from the data under a given condition.

        Args:
            target_column (str): name of column to filter on
            comparator (models.ComparisonType): type of comparison
            value (str): value with which to compare
            numerical (bool, optional): whether the comparison is on numerical values. Defaults to False.
            nodes (List[str], optional): list of the name of nodes to apply the operation on, applied to all if None. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        self.append_to_chain(models.Filter(type=models.PreprocessingOperationType.FILTER, col_name=target_column, comparator=comparator, value=value, numerical=numerical), nodes)
        return self

    def counts(self, output_column_name: str, nodes: List[str] = None):
        """ Add a counts operation to the preprocessing chain. The operation concatenates a new column filled with ones.

        Args:
            output_column_name (str): name of the column to store the counts. If not specified, the name 'count' will be used.
            nodes (List[str], optional): list of the name of nodes to apply the operation on, applied to all if None. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        self.append_to_chain(models.Counts(type=models.PreprocessingOperationType.COUNTS, output_col=output_column_name), nodes)
        return self

    def transpose(self, copy: bool = False, nodes: List[str] = None):
        """ Add a transpose operation to the preprocessing chain. The operation transposes the index and columns of the data.


        Args:
            copy (bool, optional): Whether to copy the data after transposing. Defaults to False.
            nodes (List[str], optional): list of the name of nodes to apply the operation on, applied to all if None. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        self.append_to_chain(models.Transpose(type=models.PreprocessingOperationType.TRANSPOSE, copy=copy), nodes)
        return self

    def set_index(self, columns: List[str], drop: bool = True, append: bool = False, nodes: List[str] = None):
        """ Add a set index operation to the preprocessing chain. The operation sets the DataFrame index using existing columns.

        Args:
            columns (List[str]): list of column names to set as index
            drop (bool, optional): Delete columns to be used as the new index. Defaults to True.
            append (bool, optional): Whether to append columns to existing index. Defaults to False.
            nodes (List[str], optional): list of the name of nodes to apply the operation on, applied to all if None. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        self.append_to_chain(models.SetIndex(type=models.PreprocessingOperationType.SETINDEX, cols=columns, drop=drop, append=append), nodes)
        return self

    def reset_index(self, drop: bool = False, level: List[str] = None, nodes: List[str] = None):
        """ Add a reset index operation to the preprocessing chain. The operation resets the DataFrame index (or a level of it).

        Args:
            drop (bool, optional):  Whether to insert index into dataframe columns. This resets the index to the default integer index. Defaults to False.
            level (List[str], optional): list of column names to remove from index. Defaults to None.
            nodes (List[str], optional): list of the name of nodes to apply the operation on, applied to all if None. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        self.append_to_chain(models.ResetIndex(type=models.PreprocessingOperationType.RESETINDEX, drop=drop, level=level), nodes)
        return self

    def rename(self, mapper: dict, axis: models.RenameAxis = models.RenameAxis.COLUMNS, copy: bool = True, errors: bool = True, nodes: List[str] = None):
        """ Add a rename operation to the preprocessing chain. The operation alters axis labels.

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
        self.append_to_chain(models.Rename(type=models.PreprocessingOperationType.RENAME, mapper=mapper, axis=axis, copy=copy, errors=errors), nodes)
        return self

    def astype(self, type_map: dict, copy: bool = True, errors: bool = True, nodes: List[str] = None):
        """ Add an as type operation to the preprocessing chain. The operation casts column types.

        Args:
            type_map (dict):  Dict which maps column names to the data types they should be cast to.
            copy (bool, optional): Whether to return a copy of the data. Defaults to True.
            errors (bool, optional): If True raise a KeyError if a column in the type_map does not exist in the data. If False existing columns will be cast and extra columns will be ignored. Defaults to True.
            nodes (List[str], optional): list of the name of nodes to apply the operation on, applied to all if None. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        type_map = models.AsTypeTypeMap.from_dict(type_map)
        self.append_to_chain(models.AsType(type=models.PreprocessingOperationType.ASTYPE, type_map=type_map, copy=copy, errors=errors), nodes)
        return self

    def extract(self, field:str, columns:List[str], names: List[str] = None, nodes: List[str] = None):
        """ Add an extract operation to the preprocessing chain. The operation extracts field values from dict-like columns.


        Args:
            field (str): name of the field to extract
            columns (List[str]): list of column names from which to extract the field values.
            names (List[str]): names of the resulting columns containing the extracted values.
            nodes (List[str], optional): list of the name of nodes to apply the operation on, applied to all if None. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        assert isinstance(columns,list)
        self.append_to_chain(models.ExtractDictField(type=models.PreprocessingOperationType.EXTRACTDICTFIELD, field=field, cols=columns, names=names), nodes)
        return self

    def apply_regex(self, regex:str, columns:List[str], names: List[str] = None, regex_type: models.ApplyRegExRegexType = models.ApplyRegExRegexType.MATCH, nodes: List[str] = None):
        """ Add an apply regex operation to the preprocessing chain. The operation applies a regular expression to columns.

        Args:
            regex (str): regular expression to apply.
            columns (List[str]):  list of column names to apply the regular expression to.
            regex_type (models.ApplyRegExRegexType, optional): defines what we want to retrieve from the regex (see ApplyRegExRegexType). Defaults to models.ApplyRegExRegexType.MATCH.
            names (List[str]): names of resulting columns.
            nodes (List[str], optional): list of the name of nodes to apply the operation on, applied to all if None. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        assert isinstance(columns,list)
        self.append_to_chain(models.ApplyRegEx(type=models.PreprocessingOperationType.APPLYREGEX, regex=regex, cols=columns, regex_type=regex_type, names=names), nodes)
        return self

    def gwas_preprocessing(self, genomic_nodes: List[str], clinical_nodes: List[str], sample_cols: List[str]):
        """ Add the necessary preprocessing operations for a Genome-Wide Association Study.

        Args:
            genomic_nodes (List[str]): list of names of the nodes containing genomic data.
            clinical_nodes (List[str]): list of names of the nodes containing clinical data.
            sample_cols (List[str]): list of column names containing sample data within the genomic data.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        self.set_index(columns=['LOCUS'], nodes=genomic_nodes)
        self.select(columns=sample_cols, nodes=genomic_nodes)
        self.extract(field='GT_type', columns=sample_cols, nodes=genomic_nodes)
        self.transpose(nodes=genomic_nodes)
        self.reset_index(nodes=genomic_nodes)
        self.rename(mapper={'index': 'ID'}, axis=models.RenameAxis.COLUMNS, nodes=genomic_nodes)
        self.rename(mapper={'Sample': 'ID'}, axis=models.RenameAxis.COLUMNS, nodes=clinical_nodes)
        return self

    def create_survival_columns(self, params: SurvivalParameters, nodes: List[str] = None):
        """ Add the necessary preprocessing operations for a survival analysis.

        Args:
            params (SurvivalParameters): parameters of the survival analysis.
            nodes (List[str], optional): list of the name of nodes to apply the operations on, applied to all if None. Defaults to None.

        Returns:
            self (PreprocessingBuilder): the updated PreprocessingBuilder
        """
        self.append_to_chain(params.get_preprocessing_op(),nodes)
        return self

    def append_to_chain(self, op: models.PreprocessingOperation, nodes: List[str] = None):
        """ Append a preprocessing operation to the global or compound chain.

        Args:
            op (models.PreprocessingOperation): the preprocessing operation to append
            nodes (List[str], optional): list of the name of nodes to apply the operation on, applied to all if None. Defaults to None.
        """
        if nodes is None:
            self.chain.append(op)
        else:
            assert isinstance(nodes,list)
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
            warn("Preprocessing chain contains one hot encoding without a subsequent select. This could lead to an error if nodes have different categorical values. \n Chain: " + str(self.chain), stacklevel=2)

        for node, node_chain in self.compound_chain.items():
            if self.check_chain(node_chain.chain) is True:
                warn("Preprocessing chain for node " + node + " contains one hot encoding without a subsequent select. This could lead to an error if nodes have different categorical values. \n Chain: " + str(node_chain), stacklevel=2)


    def check_chain(self, chain: models.PreprocessingChain) -> bool:
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
