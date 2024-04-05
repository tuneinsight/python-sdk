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
        first_name (Union[Unset, str]):
        attributes (Union[Unset, UserDefinitionAttributes]):
        created_timestamp (Union[Unset, int]):
        enabled (Union[Unset, bool]):
        email (Union[Unset, str]):
        groups (Union[Unset, List[str]]):
        last_name (Union[Unset, str]):
        totp (Union[Unset, bool]):
        access (Union[Unset, UserDefinitionAccess]):
        client_roles (Union[Unset, UserDefinitionClientRoles]):
        disableable_credential_types (Union[Unset, List['UserDefinitionDisableableCredentialTypesItem']]):
        federation_link (Union[Unset, str]):
        realm_roles (Union[Unset, List[str]]):
        service_account_client_id (Union[Unset, str]):
        username (Union[Unset, str]):
        email_verified (Union[Unset, bool]):
        id (Union[Unset, str]):
        required_actions (Union[Unset, List[str]]):
    """

    first_name: Union[Unset, str] = UNSET
    attributes: Union[Unset, "UserDefinitionAttributes"] = UNSET
    created_timestamp: Union[Unset, int] = UNSET
    enabled: Union[Unset, bool] = UNSET
    email: Union[Unset, str] = UNSET
    groups: Union[Unset, List[str]] = UNSET
    last_name: Union[Unset, str] = UNSET
    totp: Union[Unset, bool] = UNSET
    access: Union[Unset, "UserDefinitionAccess"] = UNSET
    client_roles: Union[Unset, "UserDefinitionClientRoles"] = UNSET
    disableable_credential_types: Union[Unset, List["UserDefinitionDisableableCredentialTypesItem"]] = UNSET
    federation_link: Union[Unset, str] = UNSET
    realm_roles: Union[Unset, List[str]] = UNSET
    service_account_client_id: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    email_verified: Union[Unset, bool] = UNSET
    id: Union[Unset, str] = UNSET
    required_actions: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        first_name = self.first_name
        attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        created_timestamp = self.created_timestamp
        enabled = self.enabled
        email = self.email
        groups: Union[Unset, List[str]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups

        last_name = self.last_name
        totp = self.totp
        access: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        client_roles: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.client_roles, Unset):
            client_roles = self.client_roles.to_dict()

        disableable_credential_types: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.disableable_credential_types, Unset):
            disableable_credential_types = []
            for disableable_credential_types_item_data in self.disableable_credential_types:
                disableable_credential_types_item = disableable_credential_types_item_data.to_dict()

                disableable_credential_types.append(disableable_credential_types_item)

        federation_link = self.federation_link
        realm_roles: Union[Unset, List[str]] = UNSET
        if not isinstance(self.realm_roles, Unset):
            realm_roles = self.realm_roles

        service_account_client_id = self.service_account_client_id
        username = self.username
        email_verified = self.email_verified
        id = self.id
        required_actions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.required_actions, Unset):
            required_actions = self.required_actions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if email is not UNSET:
            field_dict["email"] = email
        if groups is not UNSET:
            field_dict["groups"] = groups
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if totp is not UNSET:
            field_dict["totp"] = totp
        if access is not UNSET:
            field_dict["access"] = access
        if client_roles is not UNSET:
            field_dict["clientRoles"] = client_roles
        if disableable_credential_types is not UNSET:
            field_dict["disableableCredentialTypes"] = disableable_credential_types
        if federation_link is not UNSET:
            field_dict["federationLink"] = federation_link
        if realm_roles is not UNSET:
            field_dict["realmRoles"] = realm_roles
        if service_account_client_id is not UNSET:
            field_dict["serviceAccountClientID"] = service_account_client_id
        if username is not UNSET:
            field_dict["username"] = username
        if email_verified is not UNSET:
            field_dict["emailVerified"] = email_verified
        if id is not UNSET:
            field_dict["id"] = id
        if required_actions is not UNSET:
            field_dict["requiredActions"] = required_actions

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
        first_name = d.pop("firstName", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, UserDefinitionAttributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = UserDefinitionAttributes.from_dict(_attributes)

        created_timestamp = d.pop("createdTimestamp", UNSET)

        enabled = d.pop("enabled", UNSET)

        email = d.pop("email", UNSET)

        groups = cast(List[str], d.pop("groups", UNSET))

        last_name = d.pop("lastName", UNSET)

        totp = d.pop("totp", UNSET)

        _access = d.pop("access", UNSET)
        access: Union[Unset, UserDefinitionAccess]
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = UserDefinitionAccess.from_dict(_access)

        _client_roles = d.pop("clientRoles", UNSET)
        client_roles: Union[Unset, UserDefinitionClientRoles]
        if isinstance(_client_roles, Unset):
            client_roles = UNSET
        else:
            client_roles = UserDefinitionClientRoles.from_dict(_client_roles)

        disableable_credential_types = []
        _disableable_credential_types = d.pop("disableableCredentialTypes", UNSET)
        for disableable_credential_types_item_data in _disableable_credential_types or []:
            disableable_credential_types_item = UserDefinitionDisableableCredentialTypesItem.from_dict(
                disableable_credential_types_item_data
            )

            disableable_credential_types.append(disableable_credential_types_item)

        federation_link = d.pop("federationLink", UNSET)

        realm_roles = cast(List[str], d.pop("realmRoles", UNSET))

        service_account_client_id = d.pop("serviceAccountClientID", UNSET)

        username = d.pop("username", UNSET)

        email_verified = d.pop("emailVerified", UNSET)

        id = d.pop("id", UNSET)

        required_actions = cast(List[str], d.pop("requiredActions", UNSET))

        user_definition = cls(
            first_name=first_name,
            attributes=attributes,
            created_timestamp=created_timestamp,
            enabled=enabled,
            email=email,
            groups=groups,
            last_name=last_name,
            totp=totp,
            access=access,
            client_roles=client_roles,
            disableable_credential_types=disableable_credential_types,
            federation_link=federation_link,
            realm_roles=realm_roles,
            service_account_client_id=service_account_client_id,
            username=username,
            email_verified=email_verified,
            id=id,
            required_actions=required_actions,
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
