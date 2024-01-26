from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.access_scope import AccessScope
from ..models.data_source_consent_type import DataSourceConsentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DataSourceBase")


@attr.s(auto_attribs=True)
class DataSourceBase:
    """Common fields for a data source GET/POST

    Attributes:
        attributes (Union[Unset, List[str]]):
        authorized_users (Union[Unset, List[str]]):
        consent_type (Union[Unset, DataSourceConsentType]): Consent type given to the data source.
        name (Union[Unset, str]):
        type (Union[Unset, str]):
        unique_id (Union[Unset, None, str]): Unique identifier of a data source.
        access_scope (Union[Unset, AccessScope]): defines the scope of access given to a resource
    """

    attributes: Union[Unset, List[str]] = UNSET
    authorized_users: Union[Unset, List[str]] = UNSET
    consent_type: Union[Unset, DataSourceConsentType] = UNSET
    name: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    unique_id: Union[Unset, None, str] = UNSET
    access_scope: Union[Unset, AccessScope] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attributes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes

        authorized_users: Union[Unset, List[str]] = UNSET
        if not isinstance(self.authorized_users, Unset):
            authorized_users = self.authorized_users

        consent_type: Union[Unset, str] = UNSET
        if not isinstance(self.consent_type, Unset):
            consent_type = self.consent_type.value

        name = self.name
        type = self.type
        unique_id = self.unique_id
        access_scope: Union[Unset, str] = UNSET
        if not isinstance(self.access_scope, Unset):
            access_scope = self.access_scope.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if authorized_users is not UNSET:
            field_dict["authorizedUsers"] = authorized_users
        if consent_type is not UNSET:
            field_dict["consentType"] = consent_type
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type
        if unique_id is not UNSET:
            field_dict["uniqueId"] = unique_id
        if access_scope is not UNSET:
            field_dict["accessScope"] = access_scope

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        attributes = cast(List[str], d.pop("attributes", UNSET))

        authorized_users = cast(List[str], d.pop("authorizedUsers", UNSET))

        _consent_type = d.pop("consentType", UNSET)
        consent_type: Union[Unset, DataSourceConsentType]
        if isinstance(_consent_type, Unset):
            consent_type = UNSET
        else:
            consent_type = DataSourceConsentType(_consent_type)

        name = d.pop("name", UNSET)

        type = d.pop("type", UNSET)

        unique_id = d.pop("uniqueId", UNSET)

        _access_scope = d.pop("accessScope", UNSET)
        access_scope: Union[Unset, AccessScope]
        if isinstance(_access_scope, Unset):
            access_scope = UNSET
        else:
            access_scope = AccessScope(_access_scope)

        data_source_base = cls(
            attributes=attributes,
            authorized_users=authorized_users,
            consent_type=consent_type,
            name=name,
            type=type,
            unique_id=unique_id,
            access_scope=access_scope,
        )

        data_source_base.additional_properties = d
        return data_source_base

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
