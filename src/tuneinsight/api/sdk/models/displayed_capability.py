from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.capability import Capability
from ..types import UNSET, Unset

T = TypeVar("T", bound="DisplayedCapability")


@attr.s(auto_attribs=True)
class DisplayedCapability:
    """information about a capability.

    Attributes:
        category (Union[Unset, str]): category of the capability (ie. projects,data sources,...)
        description (Union[Unset, str]): description of the capability.
        displayed_name (Union[Unset, str]): readable name for the capability.
        name (Union[Unset, Capability]):
    """

    category: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    displayed_name: Union[Unset, str] = UNSET
    name: Union[Unset, Capability] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        category = self.category
        description = self.description
        displayed_name = self.displayed_name
        name: Union[Unset, str] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if description is not UNSET:
            field_dict["description"] = description
        if displayed_name is not UNSET:
            field_dict["displayedName"] = displayed_name
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        category = d.pop("category", UNSET)

        description = d.pop("description", UNSET)

        displayed_name = d.pop("displayedName", UNSET)

        _name = d.pop("name", UNSET)
        name: Union[Unset, Capability]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = Capability(_name)

        displayed_capability = cls(
            category=category,
            description=description,
            displayed_name=displayed_name,
            name=name,
        )

        displayed_capability.additional_properties = d
        return displayed_capability

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
