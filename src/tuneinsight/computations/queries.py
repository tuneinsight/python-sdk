"""Class used to define the data source query for each participant in the project."""

from typing import Callable, Dict, List, Union
from tuneinsight.computations.tiql import Builder
from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import is_unset
from tuneinsight.api.sdk.models.computation_data_source_parameters import (
    ComputationDataSourceParameters,
)
from tuneinsight.api.sdk.models.data_source_query import DataSourceQuery


class QueryBuilder:
    """
    Data source retrieval parameters for all participants.

    This class defines both the global or compound (per-participant) query that will be executed
    at the data sources of each participant to retrieve the data before the computations.
    It provides high-level methods to define API and database queries.

    This builder is typically attached to a computation directly (through the `.preprocessing`
    attribute of `Computation` objects), or in the project's local data selection.
    """

    global_query: DataSourceQuery
    compound_query: Dict[str, DataSourceQuery]
    query_set: bool

    def __init__(self, update_function: Callable = None):
        """
        Args:
            update_function (Callable, optional): if provided, this function is called whenever
                this preprocessing chain is changed. This can be used to automatically update
                the computation definition whenever the preprocessing is updated.
        """
        self.global_query = DataSourceQuery()
        self.compound_query = {}
        self.query_set = False
        self.update_function = update_function

    def _set_query(self, query_type: str, query: str, nodes: List[str] = None):
        if nodes is None:
            setattr(self.global_query, query_type, query)
        else:
            for node in nodes:
                if node not in self.compound_query:
                    self.compound_query[node] = DataSourceQuery()
                setattr(self.compound_query[node], query_type, query)
        self.query_set = True
        if self.update_function is not None:
            self.update_function()

    def _set_query_from_dict(self, query_type: str, query_dict: Dict[str, str]):
        for node in query_dict:
            query = query_dict[node]
            self._set_query(query_type, query, [node])

    def set_database_query(self, query: str, nodes: List[str] = None):
        """
        Sets the query to retrieve the input dataset from a database.

        Args
            query (str): the query to perform on the database.
            nodes (list, default None): the list of nodes to which this applies. By default, all nodes.
        """
        self._set_query("database_query", query, nodes)

    def set_database_query_from_dict(self, query_dict: Dict[str, str]):
        """
        Sets the query to retrieve the input dataset from a database for each node.

        Args
            query_dict (dict:str->str): a dictionary mapping the node name to the database query for that node.
        """
        self._set_query_from_dict("database_query", query_dict)

    def set_api_request_body(self, request_body: str, nodes: List[str] = None):
        """
        Sets the body of the request for an API datasource.

        Args
            request_body (str): the body of the request.
            nodes (list, default None): the list of nodes to which this applies. By default, all nodes.
        """
        self._set_query("api_request_body", request_body, nodes)

    def set_api_request_body_from_dict(self, query_dict: Dict[str, str]):
        """
        Sets the body of the request for an API datasource for each node.

        Args
            query_dict (dict:str->str): a dictionary mapping the node name to the request body for that node.
        """
        self._set_query_from_dict("api_request_body", query_dict)

    def set_api_path_query(self, query: str, nodes: List[str] = None):
        """
        Sets the query path of the request for an API datasource.

        Args
            query (str): the query path of the request.
            nodes (list, default None): the list of nodes to which this applies. By default, all nodes.
        """
        self._set_query("api_path_query", query, nodes)

    def set_api_path_query_from_dict(self, query_dict: Dict[str, str]):
        """
        Sets the query path of the request for an API datasource for each node.

        Args
            query_dict (dict:str->str): a dictionary mapping the node name to the query path for that node.
        """
        self._set_query_from_dict("api_path_query", query_dict)

    def set_api_json_path(self, json_path: str, nodes: List[str] = None):
        """
        Sets the JSON-path of the request for an API datasource.

        Args
            json_path (str): the JSON-path of the request.
            nodes (list, default None): the list of nodes to which this applies. By default, all nodes.
        """
        self._set_query("api_json_path", json_path, nodes)

    def set_api_json_path_from_dict(self, query_dict: Dict[str, str]):
        """
        Sets the JSON-path of the request for an API datasource for each node.

        Args
            query_dict (dict:str->str): a dictionary mapping the node name to the JSON-path for that node.
        """
        self._set_query_from_dict("api_json_path", query_dict)

    def set_cross_standard_query(
        self,
        query: Union[models.CrossStandardQuery, Builder],
        nodes: List[str] = None,
    ):
        """
        Sets the cross-standard feasibility query (tiql).

        If this is set and the datasource supports this format (i.e., this query can be translated to a
        query in the destination language), this overrides the other queries.

        Args:
            query (models.CrossStandardQuery): the query to set.
            nodes (list, default None): the list of nodes to which this applies. By default, all nodes.
        """
        if isinstance(query, Builder):
            query = query.get_model()
        self._set_query("cross_standard_query", query, nodes)

    def get_model(self) -> models.ComputationDataSourceParameters:
        """Returns the API model for this object."""
        params = ComputationDataSourceParameters()
        if self.query_set:
            params.data_source_query = self.global_query
            if self.compound_query:
                params.compound_query = models.DataSourceCompoundQuery()
                params.compound_query.additional_properties = self.compound_query
        return params

    def set_model(self, model: models.ComputationDataSourceParameters):
        """Initializes this object given an API model."""
        self.query_set = False
        if is_unset(model):
            return
        if isinstance(model.data_source_query, DataSourceQuery):
            self.global_query = model.data_source_query
            self.query_set = True
        if isinstance(model.compound_query, models.DataSourceCompoundQuery):
            self.compound_query = model.compound_query.additional_properties
            self.query_set = True
        # Do not call update_function here (as this function is called when updating from the API).
