from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="WhitelistedQuery")


@attr.s(auto_attribs=True)
class WhitelistedQuery:
    """represents a query that is whitelisted in the policy.

    Attributes:
        name (Union[Unset, str]): common name for the query for display purposes.
        raw_query (Union[Unset, str]): the raw query that is authorized
    """

    name: Union[Unset, str] = UNSET
    raw_query: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        raw_query = self.raw_query

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if raw_query is not UNSET:
            field_dict["rawQuery"] = raw_query

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        raw_query = d.pop("rawQuery", UNSET)

        whitelisted_query = cls(
            name=name,
            raw_query=raw_query,
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
