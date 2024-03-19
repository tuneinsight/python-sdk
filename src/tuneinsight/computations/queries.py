"""Class used to define the data source query for each participant in the project."""

from typing import Dict, List
from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.models.computation_data_source_parameters import (
    ComputationDataSourceParameters,
)
from tuneinsight.api.sdk.models.data_source_query import DataSourceQuery


class QueryBuilder:
    """
    Data Source retrieval parameters that define both the global or compound (per-participant)
    query that will be executed at the data sources of each participant to retrieve the data
    before the computations.
    """

    global_query: DataSourceQuery
    compound_query: Dict[str, DataSourceQuery]
    query_set: bool
    datasource_id: str

    def __init__(self):
        self.global_query = DataSourceQuery()
        self.compound_query = {}
        self.query_set = False
        self.datasource_id = ""

    def _set_query(self, query_type: str, query: str, nodes: List[str] = None):
        if nodes is None:
            setattr(self.global_query, query_type, query)
        else:
            for node in nodes:
                if node not in self.compound_query:
                    self.compound_query[node] = DataSourceQuery()
                setattr(self.compound_query[node], query_type, query)
        self.query_set = True

    def _set_query_from_dict(self, query_type: str, query_dict: Dict[str, str]):
        for node in query_dict:
            query = query_dict[node]
            self._set_query(query_type, query, [node])

    def set_database_query(self, query: str, nodes: List[str] = None):
        self._set_query("database_query", query, nodes)

    def set_database_query_from_dict(self, query_dict: Dict[str, str]):
        self._set_query_from_dict("database_query", query_dict)

    def set_api_request_body(self, request_body: str, nodes: List[str] = None):
        self._set_query("api_request_body", request_body, nodes)

    def set_api_request_body_from_dict(self, query_dict: Dict[str, str]):
        self._set_query_from_dict("api_request_body", query_dict)

    def set_api_path_query(self, query: str, nodes: List[str] = None):
        self._set_query("api_path_query", query, nodes)

    def set_api_path_query_from_dict(self, query_dict: Dict[str, str]):
        self._set_query_from_dict("api_path_query", query_dict)

    def set_api_json_path(self, json_path: str, nodes: List[str] = None):
        self._set_query("api_json_path", json_path, nodes)

    def set_api_json_path_from_dict(self, query_dict: Dict[str, str]):
        self._set_query_from_dict("api_json_path", query_dict)

    def get_parameters(self) -> models.ComputationDataSourceParameters:
        params = ComputationDataSourceParameters()
        if self.query_set:
            params.data_source_query = self.global_query
            params.compound_query = models.DataSourceCompoundQuery()
            params.compound_query.additional_properties = self.compound_query
        if len(self.compound_query) == 0:
            params.compound_disabled = True
        return params

    def set_parameters(self, params: models.ComputationDataSourceParameters):
        self.query_set = False
        if isinstance(params.data_source_query, DataSourceQuery):
            self.global_query = params.data_source_query
            self.query_set = True
        if isinstance(params.compound_query, models.DataSourceCompoundQuery):
            self.compound_query = params.compound_query.additional_properties
            self.query_set = True
