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
        database_query (Union[Unset, str]): query used to retrieve data from a database data source (typically in SQL
            format)
        select (Union[Unset, Select]):
        api_json_path (Union[Unset, str]): JSONPath used for API data sources (if given, will be used to parse the API
            response)
        api_path_query (Union[Unset, str]): Query path for the API data source URL (e.g.
            https://example.com+{apiPathQuery})
        api_request_body (Union[Unset, str]): request body used for API data sources (if given, the request will use
            POST with this request body)
    """

    database_query: Union[Unset, str] = UNSET
    select: Union[Unset, "Select"] = UNSET
    api_json_path: Union[Unset, str] = UNSET
    api_path_query: Union[Unset, str] = UNSET
    api_request_body: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        database_query = self.database_query
        select: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.select, Unset):
            select = self.select.to_dict()

        api_json_path = self.api_json_path
        api_path_query = self.api_path_query
        api_request_body = self.api_request_body

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if database_query is not UNSET:
            field_dict["databaseQuery"] = database_query
        if select is not UNSET:
            field_dict["select"] = select
        if api_json_path is not UNSET:
            field_dict["apiJsonPath"] = api_json_path
        if api_path_query is not UNSET:
            field_dict["apiPathQuery"] = api_path_query
        if api_request_body is not UNSET:
            field_dict["apiRequestBody"] = api_request_body

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.select import Select

        d = src_dict.copy()
        database_query = d.pop("databaseQuery", UNSET)

        _select = d.pop("select", UNSET)
        select: Union[Unset, Select]
        if isinstance(_select, Unset):
            select = UNSET
        else:
            select = Select.from_dict(_select)

        api_json_path = d.pop("apiJsonPath", UNSET)

        api_path_query = d.pop("apiPathQuery", UNSET)

        api_request_body = d.pop("apiRequestBody", UNSET)

        data_source_query = cls(
            database_query=database_query,
            select=select,
            api_json_path=api_json_path,
            api_path_query=api_path_query,
            api_request_body=api_request_body,
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
