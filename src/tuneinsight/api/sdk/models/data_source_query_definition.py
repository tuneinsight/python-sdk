from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_source_query import DataSourceQuery


T = TypeVar("T", bound="DataSourceQueryDefinition")


@attr.s(auto_attribs=True)
class DataSourceQueryDefinition:
    """defines a query to be executed on a data source along with options.

    Attributes:
        limit_query_rows (Union[Unset, None, int]): limit on the number of rows that are returned by the query. If the
            table is being seeded in the database, then this also affects the new table.
        only_metadata (Union[Unset, bool]): whether to return only the metadata (columns and types) of the table
        query (Union[Unset, DataSourceQuery]): schema used for the query
        tolerate_errors (Union[Unset, bool]): whether to tolerate query errors and avoid returning a http error code.
    """

    limit_query_rows: Union[Unset, None, int] = UNSET
    only_metadata: Union[Unset, bool] = UNSET
    query: Union[Unset, "DataSourceQuery"] = UNSET
    tolerate_errors: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        limit_query_rows = self.limit_query_rows
        only_metadata = self.only_metadata
        query: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.query, Unset):
            query = self.query.to_dict()

        tolerate_errors = self.tolerate_errors

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if limit_query_rows is not UNSET:
            field_dict["limitQueryRows"] = limit_query_rows
        if only_metadata is not UNSET:
            field_dict["onlyMetadata"] = only_metadata
        if query is not UNSET:
            field_dict["query"] = query
        if tolerate_errors is not UNSET:
            field_dict["tolerateErrors"] = tolerate_errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_source_query import DataSourceQuery

        d = src_dict.copy()
        limit_query_rows = d.pop("limitQueryRows", UNSET)

        only_metadata = d.pop("onlyMetadata", UNSET)

        _query = d.pop("query", UNSET)
        query: Union[Unset, DataSourceQuery]
        if isinstance(_query, Unset):
            query = UNSET
        else:
            query = DataSourceQuery.from_dict(_query)

        tolerate_errors = d.pop("tolerateErrors", UNSET)

        data_source_query_definition = cls(
            limit_query_rows=limit_query_rows,
            only_metadata=only_metadata,
            query=query,
            tolerate_errors=tolerate_errors,
        )

        data_source_query_definition.additional_properties = d
        return data_source_query_definition

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
