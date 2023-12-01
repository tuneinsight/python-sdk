from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.access_scope import AccessScope
from ..models.data_source_consent_type import DataSourceConsentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_source_metadata import DataSourceMetadata
    from ..models.local_data_selection import LocalDataSelection


T = TypeVar("T", bound="DataSource")


@attr.s(auto_attribs=True)
class DataSource:
    """
    Attributes:
        access_scope (Union[Unset, AccessScope]): defines the scope of access given to a resource
        attributes (Union[Unset, List[str]]):
        authorized_users (Union[Unset, List[str]]):
        consent_type (Union[Unset, DataSourceConsentType]): Consent type given to the data source.
        name (Union[Unset, str]):
        type (Union[Unset, str]):
        unique_id (Union[Unset, None, str]): Unique identifier of a data source.
        created_at (Union[Unset, str]):
        metadata (Union[Unset, DataSourceMetadata]): metadata about a datasource
        selections (Union[Unset, List['LocalDataSelection']]): list of local data selections associated with the data
            source
        updated_at (Union[Unset, str]):
    """

    access_scope: Union[Unset, AccessScope] = UNSET
    attributes: Union[Unset, List[str]] = UNSET
    authorized_users: Union[Unset, List[str]] = UNSET
    consent_type: Union[Unset, DataSourceConsentType] = UNSET
    name: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    unique_id: Union[Unset, None, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    metadata: Union[Unset, "DataSourceMetadata"] = UNSET
    selections: Union[Unset, List["LocalDataSelection"]] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access_scope: Union[Unset, str] = UNSET
        if not isinstance(self.access_scope, Unset):
            access_scope = self.access_scope.value

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
        created_at = self.created_at
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        selections: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.selections, Unset):
            selections = []
            for selections_item_data in self.selections:
                selections_item = selections_item_data.to_dict()

                selections.append(selections_item)

        updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_scope is not UNSET:
            field_dict["accessScope"] = access_scope
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
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if selections is not UNSET:
            field_dict["selections"] = selections
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_source_metadata import DataSourceMetadata
        from ..models.local_data_selection import LocalDataSelection

        d = src_dict.copy()
        _access_scope = d.pop("accessScope", UNSET)
        access_scope: Union[Unset, AccessScope]
        if isinstance(_access_scope, Unset):
            access_scope = UNSET
        else:
            access_scope = AccessScope(_access_scope)

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

        created_at = d.pop("createdAt", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, DataSourceMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = DataSourceMetadata.from_dict(_metadata)

        selections = []
        _selections = d.pop("selections", UNSET)
        for selections_item_data in _selections or []:
            selections_item = LocalDataSelection.from_dict(selections_item_data)

            selections.append(selections_item)

        updated_at = d.pop("updatedAt", UNSET)

        data_source = cls(
            access_scope=access_scope,
            attributes=attributes,
            authorized_users=authorized_users,
            consent_type=consent_type,
            name=name,
            type=type,
            unique_id=unique_id,
            created_at=created_at,
            metadata=metadata,
            selections=selections,
            updated_at=updated_at,
        )

        data_source.additional_properties = d
        return data_source

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
