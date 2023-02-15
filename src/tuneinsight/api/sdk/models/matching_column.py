from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="MatchingColumn")


@attr.s(auto_attribs=True)
class MatchingColumn:
    """column description for matching

    Attributes:
        fuzzy (Union[Unset, bool]): whether or not to fuzzy encode the column
        name (Union[Unset, str]):
    """

    fuzzy: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fuzzy = self.fuzzy
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fuzzy is not UNSET:
            field_dict["fuzzy"] = fuzzy
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        fuzzy = d.pop("fuzzy", UNSET)

        name = d.pop("name", UNSET)

        matching_column = cls(
            fuzzy=fuzzy,
            name=name,
        )

        matching_column.additional_properties = d
        return matching_column

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
