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
        is_contributor (Union[Unset, bool]): Indicates if this instance does contribute data.
        name (Union[Unset, str]):
        organization (Union[Unset, Organization]): Organization taking part in a project
        url (Union[Unset, str]):
        certificate (Union[Unset, str]): Certificate of the node, in base64-encoded DER format.
        has_user_management (Union[Unset, bool]): True if the node has the user management APIs enabled.
        is_root (Union[Unset, bool]): True if the node is the root node in a tree topology network.
        api_path (Union[Unset, str]):
        current (Union[Unset, bool]): True if this node is the current one (root node).
    """

    is_contributor: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    organization: Union[Unset, "Organization"] = UNSET
    url: Union[Unset, str] = UNSET
    certificate: Union[Unset, str] = UNSET
    has_user_management: Union[Unset, bool] = UNSET
    is_root: Union[Unset, bool] = UNSET
    api_path: Union[Unset, str] = UNSET
    current: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_contributor = self.is_contributor
        name = self.name
        organization: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        url = self.url
        certificate = self.certificate
        has_user_management = self.has_user_management
        is_root = self.is_root
        api_path = self.api_path
        current = self.current

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_contributor is not UNSET:
            field_dict["isContributor"] = is_contributor
        if name is not UNSET:
            field_dict["name"] = name
        if organization is not UNSET:
            field_dict["organization"] = organization
        if url is not UNSET:
            field_dict["url"] = url
        if certificate is not UNSET:
            field_dict["certificate"] = certificate
        if has_user_management is not UNSET:
            field_dict["hasUserManagement"] = has_user_management
        if is_root is not UNSET:
            field_dict["isRoot"] = is_root
        if api_path is not UNSET:
            field_dict["apiPath"] = api_path
        if current is not UNSET:
            field_dict["current"] = current

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.organization import Organization

        d = src_dict.copy()
        is_contributor = d.pop("isContributor", UNSET)

        name = d.pop("name", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, Organization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = Organization.from_dict(_organization)

        url = d.pop("url", UNSET)

        certificate = d.pop("certificate", UNSET)

        has_user_management = d.pop("hasUserManagement", UNSET)

        is_root = d.pop("isRoot", UNSET)

        api_path = d.pop("apiPath", UNSET)

        current = d.pop("current", UNSET)

        node = cls(
            is_contributor=is_contributor,
            name=name,
            organization=organization,
            url=url,
            certificate=certificate,
            has_user_management=has_user_management,
            is_root=is_root,
            api_path=api_path,
            current=current,
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
