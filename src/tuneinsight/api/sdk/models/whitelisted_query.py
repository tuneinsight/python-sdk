from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cross_standard_query import CrossStandardQuery


T = TypeVar("T", bound="WhitelistedQuery")


@attr.s(auto_attribs=True)
class WhitelistedQuery:
    """A query that is whitelisted in the policy. Every query performed in a project must match on all fields that it
    defines.

        Attributes:
            name (Union[Unset, str]): common name for the query for display purposes.
            raw_query (Union[Unset, str]): the raw query (SQL or API request), if any, that is authorized
            tiql_query (Union[Unset, CrossStandardQuery]): A Cross-Standard Feasibility Query (TIQL). This structure
                represents feasibility queries
                independently of the underlying data structure, and can be used to define workflows at a
                higher level of abstraction. In order to perform the query on a datasource, it will first
                be converted to the appropriate query language by the backend.
                Performing a query results in a cohort, a table containing a fixed set of variables for a
                subset of the records in the data. As such, the query defines two operations: a filtering
                operation that selects which records to extract data from, and a variable extraction that
                defines what values are computed for each extracted record.
    """

    name: Union[Unset, str] = UNSET
    raw_query: Union[Unset, str] = UNSET
    tiql_query: Union[Unset, "CrossStandardQuery"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        raw_query = self.raw_query
        tiql_query: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tiql_query, Unset):
            tiql_query = self.tiql_query.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if raw_query is not UNSET:
            field_dict["rawQuery"] = raw_query
        if tiql_query is not UNSET:
            field_dict["tiqlQuery"] = tiql_query

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cross_standard_query import CrossStandardQuery

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        raw_query = d.pop("rawQuery", UNSET)

        _tiql_query = d.pop("tiqlQuery", UNSET)
        tiql_query: Union[Unset, CrossStandardQuery]
        if isinstance(_tiql_query, Unset):
            tiql_query = UNSET
        else:
            tiql_query = CrossStandardQuery.from_dict(_tiql_query)

        whitelisted_query = cls(
            name=name,
            raw_query=raw_query,
            tiql_query=tiql_query,
        )

        whitelisted_query.additional_properties = d
        return whitelisted_query

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
