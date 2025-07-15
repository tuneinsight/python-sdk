from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DisplayedRole")


@attr.s(auto_attribs=True)
class DisplayedRole:
    """information about a role.

    Attributes:
        description (Union[Unset, str]): description of the role.
        displayed_name (Union[Unset, str]): readable name for the role.
        icon (Union[Unset, str]): icon to display for the role.
        name (Union[Unset, str]): string value of the role.
        permissions (Union[Unset, List[str]]): list of high-level capabilities associated with the role. (not the same
            as the technical capabilities)
    """

    description: Union[Unset, str] = UNSET
    displayed_name: Union[Unset, str] = UNSET
    icon: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    permissions: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        displayed_name = self.displayed_name
        icon = self.icon
        name = self.name
        permissions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if displayed_name is not UNSET:
            field_dict["displayedName"] = displayed_name
        if icon is not UNSET:
            field_dict["icon"] = icon
        if name is not UNSET:
            field_dict["name"] = name
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        displayed_name = d.pop("displayedName", UNSET)

        icon = d.pop("icon", UNSET)

        name = d.pop("name", UNSET)

        permissions = cast(List[str], d.pop("permissions", UNSET))

        displayed_role = cls(
            description=description,
            displayed_name=displayed_name,
            icon=icon,
            name=name,
            permissions=permissions,
        )

        displayed_role.additional_properties = d
        return displayed_role

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
