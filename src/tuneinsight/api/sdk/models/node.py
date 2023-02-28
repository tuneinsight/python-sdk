from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.organization import Organization
from ..types import UNSET, Unset

T = TypeVar("T", bound="Node")


@attr.s(auto_attribs=True)
class Node:
    """Node or agent of the network

    Attributes:
        api_path (Union[Unset, str]):
        current (Union[Unset, bool]):
        name (Union[Unset, str]):
        organization (Union[Unset, Organization]): Organization taking part in a project
        url (Union[Unset, str]):
    """

    api_path: Union[Unset, str] = UNSET
    current: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    organization: Union[Unset, Organization] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        api_path = self.api_path
        current = self.current
        name = self.name
        organization: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_path is not UNSET:
            field_dict["apiPath"] = api_path
        if current is not UNSET:
            field_dict["current"] = current
        if name is not UNSET:
            field_dict["name"] = name
        if organization is not UNSET:
            field_dict["organization"] = organization
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        api_path = d.pop("apiPath", UNSET)

        current = d.pop("current", UNSET)

        name = d.pop("name", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, Organization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = Organization.from_dict(_organization)

        url = d.pop("url", UNSET)

        node = cls(
            api_path=api_path,
            current=current,
            name=name,
            organization=organization,
            url=url,
        )

        node.additional_properties = d
        return node

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
