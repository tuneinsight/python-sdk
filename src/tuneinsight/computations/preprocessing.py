from typing import Dict,List
from warnings import warn
from tuneinsight.api.sdk import models
from tuneinsight.computations.survival import SurvivalParameters


class PreprocessingBuilder:

    chain: List[models.PreprocessingOperation]
    compound_chain: Dict[str, models.PreprocessingChain]

    def __init__(self):
        self.chain = []
        self.compound_chain = {}


    def new_chain(self, chain: List[models.PreprocessingOperation]):
        self.chain = chain
        return self

    def new_compound_chain(self, chain: Dict[str, models.PreprocessingChain]):
        self.compound_chain = chain
        return self

    def one_hot_encoding(self, target_column: str, prefix: str, specified_types: List[str], nodes: List[str] = None):
        self.append_to_chain(models.OneHotEncoding(type=models.PreprocessingOperationType.ONEHOTENCODING, input_col = target_column, prefix = prefix, specified_types = specified_types), nodes)
        return self

    def select(self, columns: List[str], create_if_missing:bool = False, dummy_value:str = "", nodes: List[str] = None):
        self.append_to_chain(models.Select(type=models.PreprocessingOperationType.SELECT, cols=columns, create_if_missing=create_if_missing, dummy_value=dummy_value), nodes)
        return self

    def filter(self, target_column: str, comparator:models.ComparisonType, value:str, numerical:bool = False, nodes: List[str] = None):
        self.append_to_chain(models.Filter(type=models.PreprocessingOperationType.FILTER, col_name=target_column, comparator=comparator, value=value, numerical=numerical), nodes)
        return self

    def counts(self, output_column_name: str, nodes: List[str] = None):
        self.append_to_chain(models.Counts(type=models.PreprocessingOperationType.COUNTS, output_col=output_column_name), nodes)
        return self

    def transpose(self, copy: bool = False, nodes: List[str] = None):
        self.append_to_chain(models.Transpose(type=models.PreprocessingOperationType.TRANSPOSE, copy=copy), nodes)
        return self

    def set_index(self, columns: List[str], drop: bool = True, append: bool = False, nodes: List[str] = None):
        self.append_to_chain(models.SetIndex(type=models.PreprocessingOperationType.SETINDEX, cols=columns, drop=drop, append=append), nodes)
        return self

    def reset_index(self, drop: bool = False, level: List[str] = None, nodes: List[str] = None):
        self.append_to_chain(models.ResetIndex(type=models.PreprocessingOperationType.RESETINDEX, drop=drop, level=level), nodes)
        return self

    def rename(self, mapper: dict, axis: models.RenameAxis = models.RenameAxis.COLUMNS, copy: bool = True, errors: bool = True, nodes: List[str] = None):
        mapper = models.RenameMapper.from_dict(mapper)
        self.append_to_chain(models.Rename(type=models.PreprocessingOperationType.RENAME, mapper=mapper, axis=axis, copy=copy, errors=errors), nodes)
        return self

    def astype(self, type_map: dict, copy: bool = True, errors: bool = True, nodes: List[str] = None):
        type_map = models.AsTypeTypeMap.from_dict(type_map)
        self.append_to_chain(models.AsType(type=models.PreprocessingOperationType.ASTYPE, type_map=type_map, copy=copy, errors=errors), nodes)
        return self

    def extract(self, field:str, columns:List[str], names = List[str], nodes: List[str] = None):
        assert isinstance(columns,list)
        self.append_to_chain(models.ExtractDictField(type=models.PreprocessingOperationType.EXTRACTDICTFIELD, field=field, cols=columns, names=names), nodes)
        return self

    def apply_regex(self, regex:str, columns:List[str], regex_type: models.ApplyRegExRegexType = models.ApplyRegExRegexType.MATCH, names = List[str], nodes: List[str] = None):
        assert isinstance(columns,list)
        self.append_to_chain(models.ApplyRegEx(type=models.PreprocessingOperationType.APPLYREGEX, regex=regex, cols=columns, regex_type=regex_type, names=names), nodes)
        return self

    def gwas_preprocessing(self, genomic_nodes: List[str], clinical_nodes: List[str], sample_cols: List[str]):
        self.set_index(columns=['LOCUS'], nodes=genomic_nodes)
        self.select(columns=sample_cols, nodes=genomic_nodes)
        self.extract(field='GT_type', columns=sample_cols, nodes=genomic_nodes)
        self.transpose(nodes=genomic_nodes)
        self.reset_index(nodes=genomic_nodes)
        self.rename(mapper={'index': 'ID'}, axis=models.RenameAxis.COLUMNS, nodes=genomic_nodes)
        self.rename(mapper={'Sample': 'ID'}, axis=models.RenameAxis.COLUMNS, nodes=clinical_nodes)
        return self

    def create_survival_columns(self, params: SurvivalParameters, nodes: List[str] = None):
        self.append_to_chain(params.get_preprocessing_op(),nodes)
        return self

    def append_to_chain(self, op: models.PreprocessingOperation, nodes: List[str] = None):
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
