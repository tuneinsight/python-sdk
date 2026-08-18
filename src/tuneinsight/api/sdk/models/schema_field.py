from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.schema_field_special_handler import SchemaFieldSpecialHandler
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.terminology_field import TerminologyField


T = TypeVar("T", bound="SchemaField")


@attr.s(auto_attribs=True)
class SchemaField:
    """Definition of a table field or column, within a data schema definition. In FHIR, this is an element of a resource,
    possibly nested with a JSONPath.

        Attributes:
            description (Union[Unset, str]): optional description for this field.
            field_type (Union[Unset, str]): The data type of the field (e.g., "string", "integer", "date").
            hidden (Union[Unset, bool]): whether this field should be hidden from the user in the frontend interfaces.
            label (Union[Unset, str]): Human-readable label for the field (e.g., "Gender").
            name (Union[Unset, str]): The column name in the database (e.g., "gender"), or JSONPath to the value in the FHIR
                resource.
            needs_unit (Union[Unset, bool]): whether this field requires a unit. This is used to determine whether to
                include a unit parameter for this field in the query builder.
            source_concept (Union[Unset, str]): the concept that this field belongs to, if applicable.
            special_handler (Union[Unset, SchemaFieldSpecialHandler]): Optional. Declares that this field requires special
                query rewriting and preprocessing logic.
                Used for fields that are not encoded as is in the data, but deduced automatically from other fields.
            target_column (Union[Unset, str]): when the field is a foreign key to another table, this indicates which column
                in the target table to join on (defaults to the identifier column of the target table).
            terminology (Union[Unset, TerminologyField]): Parameters that must be provided to schema fields when the field's
                values are terminology references.
            via (Union[Unset, str]): when the field is not directly on the main table, this indicates the path of relations
                to take to reach this field from the main table.
    """

    description: Union[Unset, str] = UNSET
    field_type: Union[Unset, str] = UNSET
    hidden: Union[Unset, bool] = UNSET
    label: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    needs_unit: Union[Unset, bool] = UNSET
    source_concept: Union[Unset, str] = UNSET
    special_handler: Union[Unset, SchemaFieldSpecialHandler] = UNSET
    target_column: Union[Unset, str] = UNSET
    terminology: Union[Unset, "TerminologyField"] = UNSET
    via: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        field_type = self.field_type
        hidden = self.hidden
        label = self.label
        name = self.name
        needs_unit = self.needs_unit
        source_concept = self.source_concept
        special_handler: Union[Unset, str] = UNSET
        if not isinstance(self.special_handler, Unset):
            special_handler = self.special_handler.value

        target_column = self.target_column
        terminology: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.terminology, Unset):
            terminology = self.terminology.to_dict()

        via = self.via

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if field_type is not UNSET:
            field_dict["fieldType"] = field_type
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if label is not UNSET:
            field_dict["label"] = label
        if name is not UNSET:
            field_dict["name"] = name
        if needs_unit is not UNSET:
            field_dict["needsUnit"] = needs_unit
        if source_concept is not UNSET:
            field_dict["sourceConcept"] = source_concept
        if special_handler is not UNSET:
            field_dict["specialHandler"] = special_handler
        if target_column is not UNSET:
            field_dict["targetColumn"] = target_column
        if terminology is not UNSET:
            field_dict["terminology"] = terminology
        if via is not UNSET:
            field_dict["via"] = via

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.terminology_field import TerminologyField

        d = src_dict.copy()
        description = d.pop("description", UNSET)

        field_type = d.pop("fieldType", UNSET)

        hidden = d.pop("hidden", UNSET)

        label = d.pop("label", UNSET)

        name = d.pop("name", UNSET)

        needs_unit = d.pop("needsUnit", UNSET)

        source_concept = d.pop("sourceConcept", UNSET)

        _special_handler = d.pop("specialHandler", UNSET)
        special_handler: Union[Unset, SchemaFieldSpecialHandler]
        if isinstance(_special_handler, Unset):
            special_handler = UNSET
        else:
            special_handler = SchemaFieldSpecialHandler(_special_handler)

        target_column = d.pop("targetColumn", UNSET)

        _terminology = d.pop("terminology", UNSET)
        terminology: Union[Unset, TerminologyField]
        if isinstance(_terminology, Unset):
            terminology = UNSET
        else:
            terminology = TerminologyField.from_dict(_terminology)

        via = d.pop("via", UNSET)

        schema_field = cls(
            description=description,
            field_type=field_type,
            hidden=hidden,
            label=label,
            name=name,
            needs_unit=needs_unit,
            source_concept=source_concept,
            special_handler=special_handler,
            target_column=target_column,
            terminology=terminology,
            via=via,
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
