from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="IndividualNotificationConfig")


@attr.s(auto_attribs=True)
class IndividualNotificationConfig:
    """Identifies the table recording individual patient notification.

    Attributes:
        table_name (str): Name of the table in the database.
        care_site_column (Union[Unset, str]): Column holding the internal care site identifier.
        notified_statuses (Union[Unset, List[str]]): Status values that count as already notified, meaning the patient
            should not be re-sent a notification.
        person_column (Union[Unset, str]): Column holding the patient identifier.
        processing_id_column (Union[Unset, str]): Column holding the project identifier associated with the notification
            if the processing type is "project".
        processing_type_column (Union[Unset, str]): Column holding the type of processing for the notification (types
            defined in the Andor API).
        status_column (Union[Unset, str]): Column holding the current status of the notification.
    """

    table_name: str
    care_site_column: Union[Unset, str] = UNSET
    notified_statuses: Union[Unset, List[str]] = UNSET
    person_column: Union[Unset, str] = UNSET
    processing_id_column: Union[Unset, str] = UNSET
    processing_type_column: Union[Unset, str] = UNSET
    status_column: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        table_name = self.table_name
        care_site_column = self.care_site_column
        notified_statuses: Union[Unset, List[str]] = UNSET
        if not isinstance(self.notified_statuses, Unset):
            notified_statuses = self.notified_statuses

        person_column = self.person_column
        processing_id_column = self.processing_id_column
        processing_type_column = self.processing_type_column
        status_column = self.status_column

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tableName": table_name,
            }
        )
        if care_site_column is not UNSET:
            field_dict["careSiteColumn"] = care_site_column
        if notified_statuses is not UNSET:
            field_dict["notifiedStatuses"] = notified_statuses
        if person_column is not UNSET:
            field_dict["personColumn"] = person_column
        if processing_id_column is not UNSET:
            field_dict["processingIdColumn"] = processing_id_column
        if processing_type_column is not UNSET:
            field_dict["processingTypeColumn"] = processing_type_column
        if status_column is not UNSET:
            field_dict["statusColumn"] = status_column

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        table_name = d.pop("tableName")

        care_site_column = d.pop("careSiteColumn", UNSET)

        notified_statuses = cast(List[str], d.pop("notifiedStatuses", UNSET))

        person_column = d.pop("personColumn", UNSET)

        processing_id_column = d.pop("processingIdColumn", UNSET)

        processing_type_column = d.pop("processingTypeColumn", UNSET)

        status_column = d.pop("statusColumn", UNSET)

        individual_notification_config = cls(
            table_name=table_name,
            care_site_column=care_site_column,
            notified_statuses=notified_statuses,
            person_column=person_column,
            processing_id_column=processing_id_column,
            processing_type_column=processing_type_column,
            status_column=status_column,
        )

        individual_notification_config.additional_properties = d
        return individual_notification_config

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
