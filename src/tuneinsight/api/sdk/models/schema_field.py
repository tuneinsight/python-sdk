from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.terminology_field import TerminologyField


T = TypeVar("T", bound="SchemaField")


@attr.s(auto_attribs=True)
class SchemaField:
    """Definition of a table field or column, within a data schema definition.

    Attributes:
        description (Union[Unset, str]): optional description for this field.
        field_type (Union[Unset, str]): The data type of the field (e.g., "string", "integer", "date").
        label (Union[Unset, str]): Human-readable label for the field (e.g., "Gender").
        name (Union[Unset, str]): The column name in the database (e.g., "gender").
        terminology (Union[Unset, TerminologyField]): Parameters that must be provided to schema fields when the field's
            values are terminology references.
    """

    description: Union[Unset, str] = UNSET
    field_type: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    terminology: Union[Unset, "TerminologyField"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        field_type = self.field_type
        label = self.label
        name = self.name
        terminology: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.terminology, Unset):
            terminology = self.terminology.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if field_type is not UNSET:
            field_dict["fieldType"] = field_type
        if label is not UNSET:
            field_dict["label"] = label
        if name is not UNSET:
            field_dict["name"] = name
        if terminology is not UNSET:
            field_dict["terminology"] = terminology

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.terminology_field import TerminologyField

        d = src_dict.copy()
        description = d.pop("description", UNSET)

        field_type = d.pop("fieldType", UNSET)

        label = d.pop("label", UNSET)

        name = d.pop("name", UNSET)

        _terminology = d.pop("terminology", UNSET)
        terminology: Union[Unset, TerminologyField]
        if isinstance(_terminology, Unset):
            terminology = UNSET
        else:
            terminology = TerminologyField.from_dict(_terminology)

        schema_field = cls(
            description=description,
            field_type=field_type,
            label=label,
            name=name,
            terminology=terminology,
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
