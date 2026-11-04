from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OppositionConfig")


@attr.s(auto_attribs=True)
class OppositionConfig:
    """Identifies the table recording patient oppositions to data processing.

    Attributes:
        table_name (str): Name of the table in the database.
        care_site_column (Union[Unset, str]): Column holding the internal care site identifier.
        general_column (Union[Unset, str]): Column indicating whether the opposition applies to all data processing, not
            just a specific project.
        general_value (Union[Unset, str]): The value in generalColumn that means the opposition is general (applies to
            all processing).
        person_column (Union[Unset, str]): Column holding the patient identifier.
        project_column (Union[Unset, str]): Column holding the project identifier that the opposition is scoped to.
            Empty or null means the opposition is not project scoped.
        valid_column (Union[Unset, str]): Column indicating whether the opposition has been reviewed and deemed valid.
        valid_value (Union[Unset, str]): The value in validColumn that means the opposition is valid.
    """

    table_name: str
    care_site_column: Union[Unset, str] = UNSET
    general_column: Union[Unset, str] = UNSET
    general_value: Union[Unset, str] = UNSET
    person_column: Union[Unset, str] = UNSET
    project_column: Union[Unset, str] = UNSET
    valid_column: Union[Unset, str] = UNSET
    valid_value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        table_name = self.table_name
        care_site_column = self.care_site_column
        general_column = self.general_column
        general_value = self.general_value
        person_column = self.person_column
        project_column = self.project_column
        valid_column = self.valid_column
        valid_value = self.valid_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tableName": table_name,
            }
        )
        if care_site_column is not UNSET:
            field_dict["careSiteColumn"] = care_site_column
        if general_column is not UNSET:
            field_dict["generalColumn"] = general_column
        if general_value is not UNSET:
            field_dict["generalValue"] = general_value
        if person_column is not UNSET:
            field_dict["personColumn"] = person_column
        if project_column is not UNSET:
            field_dict["projectColumn"] = project_column
        if valid_column is not UNSET:
            field_dict["validColumn"] = valid_column
        if valid_value is not UNSET:
            field_dict["validValue"] = valid_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        table_name = d.pop("tableName")

        care_site_column = d.pop("careSiteColumn", UNSET)

        general_column = d.pop("generalColumn", UNSET)

        general_value = d.pop("generalValue", UNSET)

        person_column = d.pop("personColumn", UNSET)

        project_column = d.pop("projectColumn", UNSET)

        valid_column = d.pop("validColumn", UNSET)

        valid_value = d.pop("validValue", UNSET)

        opposition_config = cls(
            table_name=table_name,
            care_site_column=care_site_column,
            general_column=general_column,
            general_value=general_value,
            person_column=person_column,
            project_column=project_column,
            valid_column=valid_column,
            valid_value=valid_value,
        )

        opposition_config.additional_properties = d
        return opposition_config

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
