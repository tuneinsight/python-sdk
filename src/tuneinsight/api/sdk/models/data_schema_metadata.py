from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataSchemaMetadata")


@attr.s(auto_attribs=True)
class DataSchemaMetadata:
    """additional information about the data structure that applies to all tables.

    Attributes:
        date_format (Union[Unset, str]): the format used to encode date-valued fields in the data.
        death_value (Union[Unset, None, str]): the value to treat as "death" for the vital status. If left empty, any
            non-null value is treated as "death".
    """

    date_format: Union[Unset, str] = UNSET
    death_value: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date_format = self.date_format
        death_value = self.death_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_format is not UNSET:
            field_dict["dateFormat"] = date_format
        if death_value is not UNSET:
            field_dict["deathValue"] = death_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        date_format = d.pop("dateFormat", UNSET)

        death_value = d.pop("deathValue", UNSET)

        data_schema_metadata = cls(
            date_format=date_format,
            death_value=death_value,
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
