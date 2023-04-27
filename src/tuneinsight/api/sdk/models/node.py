from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization import Organization


T = TypeVar("T", bound="Node")


@attr.s(auto_attribs=True)
class Node:
    """Node or agent of the network

    Attributes:
        name (Union[Unset, str]):
        organization (Union[Unset, Organization]): Organization taking part in a project
        url (Union[Unset, str]):
        api_path (Union[Unset, str]):
        current (Union[Unset, bool]):
        is_root (Union[Unset, bool]): True if the node is the root node in a tree topology network.
    """

    name: Union[Unset, str] = UNSET
    organization: Union[Unset, "Organization"] = UNSET
    url: Union[Unset, str] = UNSET
    api_path: Union[Unset, str] = UNSET
    current: Union[Unset, bool] = UNSET
    is_root: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        organization: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        url = self.url
        api_path = self.api_path
        current = self.current
        is_root = self.is_root

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if organization is not UNSET:
            field_dict["organization"] = organization
        if url is not UNSET:
            field_dict["url"] = url
        if api_path is not UNSET:
            field_dict["apiPath"] = api_path
        if current is not UNSET:
            field_dict["current"] = current
        if is_root is not UNSET:
            field_dict["isRoot"] = is_root

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.organization import Organization

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, Organization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = Organization.from_dict(_organization)

        url = d.pop("url", UNSET)

        api_path = d.pop("apiPath", UNSET)

        current = d.pop("current", UNSET)

        is_root = d.pop("isRoot", UNSET)

        node = cls(
            name=name,
            organization=organization,
            url=url,
            api_path=api_path,
            current=current,
            is_root=is_root,
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
