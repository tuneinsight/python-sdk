from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advanced_builder_field import AdvancedBuilderField
    from ..models.data_schema_metadata_care_sites import DataSchemaMetadataCareSites
    from ..models.patient_notification_fields import PatientNotificationFields


T = TypeVar("T", bound="DataSchemaMetadata")


@attr.s(auto_attribs=True)
class DataSchemaMetadata:
    """additional information about the data structure that applies to all tables.

    Attributes:
        care_sites (Union[Unset, DataSchemaMetadataCareSites]): information on fields related to care site metadata.
            Each field links to an optional care site attributes that can be retrieved from any table in the data source.
        date_format (Union[Unset, str]): the format used to encode date-valued fields in the data.
        death_value (Union[Unset, None, str]): the value to treat as "death" for the vital status. If left empty, any
            non-null value is treated as "death".
        patient_notification (Union[Unset, PatientNotificationFields]): Groups the table configurations used to select
            patients eligible for individual notification.
        patient_visit_care_site_id (Union[Unset, AdvancedBuilderField]): Configuration for an advanced builder parameter
            field.
    """

    care_sites: Union[Unset, "DataSchemaMetadataCareSites"] = UNSET
    date_format: Union[Unset, str] = UNSET
    death_value: Union[Unset, None, str] = UNSET
    patient_notification: Union[Unset, "PatientNotificationFields"] = UNSET
    patient_visit_care_site_id: Union[Unset, "AdvancedBuilderField"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        care_sites: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.care_sites, Unset):
            care_sites = self.care_sites.to_dict()

        date_format = self.date_format
        death_value = self.death_value
        patient_notification: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.patient_notification, Unset):
            patient_notification = self.patient_notification.to_dict()

        patient_visit_care_site_id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.patient_visit_care_site_id, Unset):
            patient_visit_care_site_id = self.patient_visit_care_site_id.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if care_sites is not UNSET:
            field_dict["careSites"] = care_sites
        if date_format is not UNSET:
            field_dict["dateFormat"] = date_format
        if death_value is not UNSET:
            field_dict["deathValue"] = death_value
        if patient_notification is not UNSET:
            field_dict["patientNotification"] = patient_notification
        if patient_visit_care_site_id is not UNSET:
            field_dict["patientVisitCareSiteId"] = patient_visit_care_site_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.advanced_builder_field import AdvancedBuilderField
        from ..models.data_schema_metadata_care_sites import DataSchemaMetadataCareSites
        from ..models.patient_notification_fields import PatientNotificationFields

        d = src_dict.copy()
        _care_sites = d.pop("careSites", UNSET)
        care_sites: Union[Unset, DataSchemaMetadataCareSites]
        if isinstance(_care_sites, Unset):
            care_sites = UNSET
        else:
            care_sites = DataSchemaMetadataCareSites.from_dict(_care_sites)

        date_format = d.pop("dateFormat", UNSET)

        death_value = d.pop("deathValue", UNSET)

        _patient_notification = d.pop("patientNotification", UNSET)
        patient_notification: Union[Unset, PatientNotificationFields]
        if isinstance(_patient_notification, Unset):
            patient_notification = UNSET
        else:
            patient_notification = PatientNotificationFields.from_dict(_patient_notification)

        _patient_visit_care_site_id = d.pop("patientVisitCareSiteId", UNSET)
        patient_visit_care_site_id: Union[Unset, AdvancedBuilderField]
        if isinstance(_patient_visit_care_site_id, Unset):
            patient_visit_care_site_id = UNSET
        else:
            patient_visit_care_site_id = AdvancedBuilderField.from_dict(_patient_visit_care_site_id)

        data_schema_metadata = cls(
            care_sites=care_sites,
            date_format=date_format,
            death_value=death_value,
            patient_notification=patient_notification,
            patient_visit_care_site_id=patient_visit_care_site_id,
        )

        data_schema_metadata.additional_properties = d
        return data_schema_metadata

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
