from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.select import Select


T = TypeVar("T", bound="DataSourceQuery")


@attr.s(auto_attribs=True)
class DataSourceQuery:
    """schema used for the query

    Attributes:
        api_json_path (Union[Unset, str]): JSONPath used for API data sources (if given, will be used to parse the API
            response)
        api_path_query (Union[Unset, str]): Query path for the API data source URL (e.g.
            https://example.com+{apiPathQuery})
        api_request_body (Union[Unset, str]): request body used for API data sources (if given, the request will use
            POST with this request body)
        database_query (Union[Unset, str]): query used to retrieve data from a database data source (typically in SQL
            format)
        database_query_builder (Union[Unset, str]): builder's version of the query (e.g. builder's JSON for the SPARQL
            Query)
        select (Union[Unset, Select]):
    """

    api_json_path: Union[Unset, str] = UNSET
    api_path_query: Union[Unset, str] = UNSET
    api_request_body: Union[Unset, str] = UNSET
    database_query: Union[Unset, str] = UNSET
    database_query_builder: Union[Unset, str] = UNSET
    select: Union[Unset, "Select"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        api_json_path = self.api_json_path
        api_path_query = self.api_path_query
        api_request_body = self.api_request_body
        database_query = self.database_query
        database_query_builder = self.database_query_builder
        select: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.select, Unset):
            select = self.select.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_json_path is not UNSET:
            field_dict["apiJsonPath"] = api_json_path
        if api_path_query is not UNSET:
            field_dict["apiPathQuery"] = api_path_query
        if api_request_body is not UNSET:
            field_dict["apiRequestBody"] = api_request_body
        if database_query is not UNSET:
            field_dict["databaseQuery"] = database_query
        if database_query_builder is not UNSET:
            field_dict["databaseQueryBuilder"] = database_query_builder
        if select is not UNSET:
            field_dict["select"] = select

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.select import Select

        d = src_dict.copy()
        api_json_path = d.pop("apiJsonPath", UNSET)

        api_path_query = d.pop("apiPathQuery", UNSET)

        api_request_body = d.pop("apiRequestBody", UNSET)

        database_query = d.pop("databaseQuery", UNSET)

        database_query_builder = d.pop("databaseQueryBuilder", UNSET)

        _select = d.pop("select", UNSET)
        select: Union[Unset, Select]
        if isinstance(_select, Unset):
            select = UNSET
        else:
            select = Select.from_dict(_select)

        data_source_query = cls(
            api_json_path=api_json_path,
            api_path_query=api_path_query,
            api_request_body=api_request_body,
            database_query=database_query,
            database_query_builder=database_query_builder,
            select=select,
        )

        data_source_query.additional_properties = d
        return data_source_query

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
