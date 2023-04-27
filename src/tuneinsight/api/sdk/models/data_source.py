from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.data_source_consent_type import DataSourceConsentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_source_metadata import DataSourceMetadata


T = TypeVar("T", bound="DataSource")


@attr.s(auto_attribs=True)
class DataSource:
    """
    Attributes:
        type (Union[Unset, str]):
        unique_id (Union[Unset, None, str]): Unique identifier of a data source.
        attributes (Union[Unset, List[str]]):
        consent_type (Union[Unset, DataSourceConsentType]): Consent type given to the data source.
        name (Union[Unset, str]):
        metadata (Union[Unset, DataSourceMetadata]): metadata about a datasource
        updated_at (Union[Unset, str]):
        created_at (Union[Unset, str]):
    """

    type: Union[Unset, str] = UNSET
    unique_id: Union[Unset, None, str] = UNSET
    attributes: Union[Unset, List[str]] = UNSET
    consent_type: Union[Unset, DataSourceConsentType] = UNSET
    name: Union[Unset, str] = UNSET
    metadata: Union[Unset, "DataSourceMetadata"] = UNSET
    updated_at: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        unique_id = self.unique_id
        attributes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes

        consent_type: Union[Unset, str] = UNSET
        if not isinstance(self.consent_type, Unset):
            consent_type = self.consent_type.value

        name = self.name
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        updated_at = self.updated_at
        created_at = self.created_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if unique_id is not UNSET:
            field_dict["uniqueId"] = unique_id
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if consent_type is not UNSET:
            field_dict["consentType"] = consent_type
        if name is not UNSET:
            field_dict["name"] = name
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_source_metadata import DataSourceMetadata

        d = src_dict.copy()
        type = d.pop("type", UNSET)

        unique_id = d.pop("uniqueId", UNSET)

        attributes = cast(List[str], d.pop("attributes", UNSET))

        _consent_type = d.pop("consentType", UNSET)
        consent_type: Union[Unset, DataSourceConsentType]
        if isinstance(_consent_type, Unset):
            consent_type = UNSET
        else:
            consent_type = DataSourceConsentType(_consent_type)

        name = d.pop("name", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, DataSourceMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = DataSourceMetadata.from_dict(_metadata)

        updated_at = d.pop("updatedAt", UNSET)

        created_at = d.pop("createdAt", UNSET)

        data_source = cls(
            type=type,
            unique_id=unique_id,
            attributes=attributes,
            consent_type=consent_type,
            name=name,
            metadata=metadata,
            updated_at=updated_at,
            created_at=created_at,
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
