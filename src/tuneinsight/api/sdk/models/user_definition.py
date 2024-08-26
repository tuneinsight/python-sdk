from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_definition_access import UserDefinitionAccess
    from ..models.user_definition_attributes import UserDefinitionAttributes
    from ..models.user_definition_client_roles import UserDefinitionClientRoles
    from ..models.user_definition_disableable_credential_types_item import UserDefinitionDisableableCredentialTypesItem


T = TypeVar("T", bound="UserDefinition")


@attr.s(auto_attribs=True)
class UserDefinition:
    """
    Attributes:
        access (Union[Unset, UserDefinitionAccess]):
        attributes (Union[Unset, UserDefinitionAttributes]):
        client_roles (Union[Unset, UserDefinitionClientRoles]):
        created_timestamp (Union[Unset, int]):
        disableable_credential_types (Union[Unset, List['UserDefinitionDisableableCredentialTypesItem']]):
        email (Union[Unset, str]):
        email_verified (Union[Unset, bool]):
        enabled (Union[Unset, bool]):
        federation_link (Union[Unset, str]):
        first_name (Union[Unset, str]):
        groups (Union[Unset, List[str]]):
        id (Union[Unset, str]):
        last_name (Union[Unset, str]):
        realm_roles (Union[Unset, List[str]]):
        required_actions (Union[Unset, List[str]]):
        service_account_client_id (Union[Unset, str]):
        totp (Union[Unset, bool]):
        username (Union[Unset, str]):
    """

    access: Union[Unset, "UserDefinitionAccess"] = UNSET
    attributes: Union[Unset, "UserDefinitionAttributes"] = UNSET
    client_roles: Union[Unset, "UserDefinitionClientRoles"] = UNSET
    created_timestamp: Union[Unset, int] = UNSET
    disableable_credential_types: Union[Unset, List["UserDefinitionDisableableCredentialTypesItem"]] = UNSET
    email: Union[Unset, str] = UNSET
    email_verified: Union[Unset, bool] = UNSET
    enabled: Union[Unset, bool] = UNSET
    federation_link: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    groups: Union[Unset, List[str]] = UNSET
    id: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    realm_roles: Union[Unset, List[str]] = UNSET
    required_actions: Union[Unset, List[str]] = UNSET
    service_account_client_id: Union[Unset, str] = UNSET
    totp: Union[Unset, bool] = UNSET
    username: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        client_roles: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.client_roles, Unset):
            client_roles = self.client_roles.to_dict()

        created_timestamp = self.created_timestamp
        disableable_credential_types: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.disableable_credential_types, Unset):
            disableable_credential_types = []
            for disableable_credential_types_item_data in self.disableable_credential_types:
                disableable_credential_types_item = disableable_credential_types_item_data.to_dict()

                disableable_credential_types.append(disableable_credential_types_item)

        email = self.email
        email_verified = self.email_verified
        enabled = self.enabled
        federation_link = self.federation_link
        first_name = self.first_name
        groups: Union[Unset, List[str]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups

        id = self.id
        last_name = self.last_name
        realm_roles: Union[Unset, List[str]] = UNSET
        if not isinstance(self.realm_roles, Unset):
            realm_roles = self.realm_roles

        required_actions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.required_actions, Unset):
            required_actions = self.required_actions

        service_account_client_id = self.service_account_client_id
        totp = self.totp
        username = self.username

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access is not UNSET:
            field_dict["access"] = access
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if client_roles is not UNSET:
            field_dict["clientRoles"] = client_roles
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if disableable_credential_types is not UNSET:
            field_dict["disableableCredentialTypes"] = disableable_credential_types
        if email is not UNSET:
            field_dict["email"] = email
        if email_verified is not UNSET:
            field_dict["emailVerified"] = email_verified
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if federation_link is not UNSET:
            field_dict["federationLink"] = federation_link
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if groups is not UNSET:
            field_dict["groups"] = groups
        if id is not UNSET:
            field_dict["id"] = id
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if realm_roles is not UNSET:
            field_dict["realmRoles"] = realm_roles
        if required_actions is not UNSET:
            field_dict["requiredActions"] = required_actions
        if service_account_client_id is not UNSET:
            field_dict["serviceAccountClientID"] = service_account_client_id
        if totp is not UNSET:
            field_dict["totp"] = totp
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_definition_access import UserDefinitionAccess
        from ..models.user_definition_attributes import UserDefinitionAttributes
        from ..models.user_definition_client_roles import UserDefinitionClientRoles
        from ..models.user_definition_disableable_credential_types_item import (
            UserDefinitionDisableableCredentialTypesItem,
        )

        d = src_dict.copy()
        _access = d.pop("access", UNSET)
        access: Union[Unset, UserDefinitionAccess]
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = UserDefinitionAccess.from_dict(_access)

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, UserDefinitionAttributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = UserDefinitionAttributes.from_dict(_attributes)

        _client_roles = d.pop("clientRoles", UNSET)
        client_roles: Union[Unset, UserDefinitionClientRoles]
        if isinstance(_client_roles, Unset):
            client_roles = UNSET
        else:
            client_roles = UserDefinitionClientRoles.from_dict(_client_roles)

        created_timestamp = d.pop("createdTimestamp", UNSET)

        disableable_credential_types = []
        _disableable_credential_types = d.pop("disableableCredentialTypes", UNSET)
        for disableable_credential_types_item_data in _disableable_credential_types or []:
            disableable_credential_types_item = UserDefinitionDisableableCredentialTypesItem.from_dict(
                disableable_credential_types_item_data
            )

            disableable_credential_types.append(disableable_credential_types_item)

        email = d.pop("email", UNSET)

        email_verified = d.pop("emailVerified", UNSET)

        enabled = d.pop("enabled", UNSET)

        federation_link = d.pop("federationLink", UNSET)

        first_name = d.pop("firstName", UNSET)

        groups = cast(List[str], d.pop("groups", UNSET))

        id = d.pop("id", UNSET)

        last_name = d.pop("lastName", UNSET)

        realm_roles = cast(List[str], d.pop("realmRoles", UNSET))

        required_actions = cast(List[str], d.pop("requiredActions", UNSET))

        service_account_client_id = d.pop("serviceAccountClientID", UNSET)

        totp = d.pop("totp", UNSET)

        username = d.pop("username", UNSET)

        user_definition = cls(
            access=access,
            attributes=attributes,
            client_roles=client_roles,
            created_timestamp=created_timestamp,
            disableable_credential_types=disableable_credential_types,
            email=email,
            email_verified=email_verified,
            enabled=enabled,
            federation_link=federation_link,
            first_name=first_name,
            groups=groups,
            id=id,
            last_name=last_name,
            realm_roles=realm_roles,
            required_actions=required_actions,
            service_account_client_id=service_account_client_id,
            totp=totp,
            username=username,
        )

        user_definition.additional_properties = d
        return user_definition

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
