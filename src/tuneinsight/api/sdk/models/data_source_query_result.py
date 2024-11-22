from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_source_query_preview import DataSourceQueryPreview
    from ..models.query import Query


T = TypeVar("T", bound="DataSourceQueryResult")


@attr.s(auto_attribs=True)
class DataSourceQueryResult:
    """payload returned when querying a data source. Contains the query results along with the query's status.

    Attributes:
        query (Union[Unset, Query]): Data source query
        results (Union[Unset, DataSourceQueryPreview]): preview of a datasource query
    """

    query: Union[Unset, "Query"] = UNSET
    results: Union[Unset, "DataSourceQueryPreview"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        query: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.query, Unset):
            query = self.query.to_dict()

        results: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.results, Unset):
            results = self.results.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if query is not UNSET:
            field_dict["query"] = query
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_source_query_preview import DataSourceQueryPreview
        from ..models.query import Query

        d = src_dict.copy()
        _query = d.pop("query", UNSET)
        query: Union[Unset, Query]
        if isinstance(_query, Unset):
            query = UNSET
        else:
            query = Query.from_dict(_query)

        _results = d.pop("results", UNSET)
        results: Union[Unset, DataSourceQueryPreview]
        if isinstance(_results, Unset):
            results = UNSET
        else:
            results = DataSourceQueryPreview.from_dict(_results)

        data_source_query_result = cls(
            query=query,
            results=results,
        )

        data_source_query_result.additional_properties = d
        return data_source_query_result

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
