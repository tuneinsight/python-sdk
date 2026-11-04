from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="LastPlannedStayConfig")


@attr.s(auto_attribs=True)
class LastPlannedStayConfig:
    """Identifies the table last planned stay of patients at care sites.

    Attributes:
        table_name (str): Name of the table.
        care_site_column (Union[Unset, str]): Column holding the internal care site identifier for the planned stay.
        person_column (Union[Unset, str]): Column holding the patient identifier.
        timestamp_column (Union[Unset, str]): Column holding the date or timestamp of the planned stay.
    """

    table_name: str
    care_site_column: Union[Unset, str] = UNSET
    person_column: Union[Unset, str] = UNSET
    timestamp_column: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        table_name = self.table_name
        care_site_column = self.care_site_column
        person_column = self.person_column
        timestamp_column = self.timestamp_column

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tableName": table_name,
            }
        )
        if care_site_column is not UNSET:
            field_dict["careSiteColumn"] = care_site_column
        if person_column is not UNSET:
            field_dict["personColumn"] = person_column
        if timestamp_column is not UNSET:
            field_dict["timestampColumn"] = timestamp_column

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        table_name = d.pop("tableName")

        care_site_column = d.pop("careSiteColumn", UNSET)

        person_column = d.pop("personColumn", UNSET)

        timestamp_column = d.pop("timestampColumn", UNSET)

        last_planned_stay_config = cls(
            table_name=table_name,
            care_site_column=care_site_column,
            person_column=person_column,
            timestamp_column=timestamp_column,
        )

        last_planned_stay_config.additional_properties = d
        return last_planned_stay_config

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
