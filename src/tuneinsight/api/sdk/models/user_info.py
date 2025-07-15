from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.displayed_capability import DisplayedCapability
    from ..models.displayed_role import DisplayedRole
    from ..models.user_group import UserGroup


T = TypeVar("T", bound="UserInfo")


@attr.s(auto_attribs=True)
class UserInfo:
    """regroups information about a user, relevant to authorization.

    Attributes:
        capabilities (Union[Unset, List['DisplayedCapability']]):
        groups (Union[Unset, List['UserGroup']]):
        local (Union[Unset, bool]): whether the user is part of this instance's organization or not.
        roles (Union[Unset, List['DisplayedRole']]):
    """

    capabilities: Union[Unset, List["DisplayedCapability"]] = UNSET
    groups: Union[Unset, List["UserGroup"]] = UNSET
    local: Union[Unset, bool] = UNSET
    roles: Union[Unset, List["DisplayedRole"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        capabilities: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = []
            for capabilities_item_data in self.capabilities:
                capabilities_item = capabilities_item_data.to_dict()

                capabilities.append(capabilities_item)

        groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()

                groups.append(groups_item)

        local = self.local
        roles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item = roles_item_data.to_dict()

                roles.append(roles_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if groups is not UNSET:
            field_dict["groups"] = groups
        if local is not UNSET:
            field_dict["local"] = local
        if roles is not UNSET:
            field_dict["roles"] = roles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.displayed_capability import DisplayedCapability
        from ..models.displayed_role import DisplayedRole
        from ..models.user_group import UserGroup

        d = src_dict.copy()
        capabilities = []
        _capabilities = d.pop("capabilities", UNSET)
        for capabilities_item_data in _capabilities or []:
            capabilities_item = DisplayedCapability.from_dict(capabilities_item_data)

            capabilities.append(capabilities_item)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = UserGroup.from_dict(groups_item_data)

            groups.append(groups_item)

        local = d.pop("local", UNSET)

        roles = []
        _roles = d.pop("roles", UNSET)
        for roles_item_data in _roles or []:
            roles_item = DisplayedRole.from_dict(roles_item_data)

            roles.append(roles_item)

        user_info = cls(
            capabilities=capabilities,
            groups=groups,
            local=local,
            roles=roles,
        )

        user_info.additional_properties = d
        return user_info

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
