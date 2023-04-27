from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.data_source_consent_type import DataSourceConsentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DataSourceBase")


@attr.s(auto_attribs=True)
class DataSourceBase:
    """Common fields for a data source GET/POST

    Attributes:
        type (Union[Unset, str]):
        unique_id (Union[Unset, None, str]): Unique identifier of a data source.
        attributes (Union[Unset, List[str]]):
        consent_type (Union[Unset, DataSourceConsentType]): Consent type given to the data source.
        name (Union[Unset, str]):
    """

    type: Union[Unset, str] = UNSET
    unique_id: Union[Unset, None, str] = UNSET
    attributes: Union[Unset, List[str]] = UNSET
    consent_type: Union[Unset, DataSourceConsentType] = UNSET
    name: Union[Unset, str] = UNSET
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
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

        data_source_base = cls(
            type=type,
            unique_id=unique_id,
            attributes=attributes,
            consent_type=consent_type,
            name=name,
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
