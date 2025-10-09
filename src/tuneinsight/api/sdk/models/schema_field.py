from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SchemaField")


@attr.s(auto_attribs=True)
class SchemaField:
    """Definition of a table field or column, within a data schema definition.

    Attributes:
        field_type (Union[Unset, str]): The data type of the field (e.g., "string", "integer", "date").
        label (Union[Unset, str]): Human-readable label for the field (e.g., "Gender").
        name (Union[Unset, str]): The column name in the database (e.g., "gender").
    """

    field_type: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_type = self.field_type
        label = self.label
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_type is not UNSET:
            field_dict["fieldType"] = field_type
        if label is not UNSET:
            field_dict["label"] = label
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field_type = d.pop("fieldType", UNSET)

        label = d.pop("label", UNSET)

        name = d.pop("name", UNSET)

        schema_field = cls(
            field_type=field_type,
            label=label,
            name=name,
        )

        schema_field.additional_properties = d
        return schema_field

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
