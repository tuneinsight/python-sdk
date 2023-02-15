from typing import Dict,List
from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.models.computation_data_source_parameters import ComputationDataSourceParameters



class QueryBuilder:


    global_query: str
    compound_query: Dict[str,str]
    query_set: bool
    datasource_id: str

    def __init__(self):
        self.global_query = ""
        self.compound_query = {}
        self.query_set = False
        self.datasource_id = ""

    def set_query(self,query: str,nodes: List[str] = None):
        if nodes is None:
            self.global_query = query
        else:
            for node in nodes:
                self.compound_query[node] = query
        self.query_set = True

    def get_parameters(self) -> models.ComputationDataSourceParameters:
        params = ComputationDataSourceParameters()
        params.data_source_query = self.global_query
        params.compound_query = models.DataSourceCompoundQuery()
        params.compound_query.additional_properties = self.compound_query
        if len(self.compound_query) == 0:
            params.compound_disabled = True
        return params
