from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unit_filter import UnitFilter


T = TypeVar("T", bound="TiqlField")


@attr.s(auto_attribs=True)
class TiqlField:
    """a field on a concept, i.e. a "table" in the data containing multiple records for a statistical unit.

    Attributes:
        concept (Union[Unset, str]): the unique name of the concept that this field is on (if none, this is a field
            directly on the patient record).
        label (Union[Unset, str]): the displayed name for this field.
        max_value (Union[Unset, None, float]): If this field is numeric, the maximum value it can take.
        min_value (Union[Unset, None, float]): If this field is numeric, the minimum value it can take.
        name (Union[Unset, str]): the unique name for this field on its concept.
        scope (Union[Unset, str]): if provided, the ontology that the data values are taken from.
        type (Union[Unset, str]): type of the underlying data (number, freeform string, or categorical from an
            ontology).
        unit (Union[Unset, UnitFilter]): Filters to apply to columns of the input dataset to ensure that they have the
            correct units.
    """

    concept: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    max_value: Union[Unset, None, float] = UNSET
    min_value: Union[Unset, None, float] = UNSET
    name: Union[Unset, str] = UNSET
    scope: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    unit: Union[Unset, "UnitFilter"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        concept = self.concept
        label = self.label
        max_value = self.max_value
        min_value = self.min_value
        name = self.name
        scope = self.scope
        type = self.type
        unit: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if concept is not UNSET:
            field_dict["concept"] = concept
        if label is not UNSET:
            field_dict["label"] = label
        if max_value is not UNSET:
            field_dict["maxValue"] = max_value
        if min_value is not UNSET:
            field_dict["minValue"] = min_value
        if name is not UNSET:
            field_dict["name"] = name
        if scope is not UNSET:
            field_dict["scope"] = scope
        if type is not UNSET:
            field_dict["type"] = type
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.unit_filter import UnitFilter

        d = src_dict.copy()
        concept = d.pop("concept", UNSET)

        label = d.pop("label", UNSET)

        max_value = d.pop("maxValue", UNSET)

        min_value = d.pop("minValue", UNSET)

        name = d.pop("name", UNSET)

        scope = d.pop("scope", UNSET)

        type = d.pop("type", UNSET)

        _unit = d.pop("unit", UNSET)
        unit: Union[Unset, UnitFilter]
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = UnitFilter.from_dict(_unit)

        tiql_field = cls(
            concept=concept,
            label=label,
            max_value=max_value,
            min_value=min_value,
            name=name,
            scope=scope,
            type=type,
            unit=unit,
        )

        tiql_field.additional_properties = d
        return tiql_field

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
