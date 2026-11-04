from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeathConfig")


@attr.s(auto_attribs=True)
class DeathConfig:
    """Identifies the table recording patient deaths. Deceased patients are excluded from individual notification.

    Attributes:
        table_name (str): Name of the table in the database.
        person_column (Union[Unset, str]): Column holding the patient identifier.
    """

    table_name: str
    person_column: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        table_name = self.table_name
        person_column = self.person_column

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tableName": table_name,
            }
        )
        if person_column is not UNSET:
            field_dict["personColumn"] = person_column

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        table_name = d.pop("tableName")

        person_column = d.pop("personColumn", UNSET)

        death_config = cls(
            table_name=table_name,
            person_column=person_column,
        )

        death_config.additional_properties = d
        return death_config

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
