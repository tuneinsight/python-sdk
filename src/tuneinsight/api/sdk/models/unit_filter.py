from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UnitFilter")


@attr.s(auto_attribs=True)
class UnitFilter:
    """Filters to apply to columns of the input dataset to ensure that they have the correct units.

    Attributes:
        allow_empty_units (Union[Unset, bool]): if true, records without a unit ("") will also be included.
        unit (Union[Unset, str]): the expected unit (records with different units for the column will be filtered out).
        unit_column (Union[Unset, str]): the name of the column in the data that contains the units of the numerical
            values.
        unit_metadata (Union[Unset, str]): optional metadata for the unit, used by the frontend (e.g. the JSON for
            autocomplete)
        value_column (Union[Unset, str]): the name of the column in the data that contains the numerical values.
            Currently not used.
    """

    allow_empty_units: Union[Unset, bool] = UNSET
    unit: Union[Unset, str] = UNSET
    unit_column: Union[Unset, str] = UNSET
    unit_metadata: Union[Unset, str] = UNSET
    value_column: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allow_empty_units = self.allow_empty_units
        unit = self.unit
        unit_column = self.unit_column
        unit_metadata = self.unit_metadata
        value_column = self.value_column

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allow_empty_units is not UNSET:
            field_dict["allowEmptyUnits"] = allow_empty_units
        if unit is not UNSET:
            field_dict["unit"] = unit
        if unit_column is not UNSET:
            field_dict["unitColumn"] = unit_column
        if unit_metadata is not UNSET:
            field_dict["unitMetadata"] = unit_metadata
        if value_column is not UNSET:
            field_dict["valueColumn"] = value_column

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        allow_empty_units = d.pop("allowEmptyUnits", UNSET)

        unit = d.pop("unit", UNSET)

        unit_column = d.pop("unitColumn", UNSET)

        unit_metadata = d.pop("unitMetadata", UNSET)

        value_column = d.pop("valueColumn", UNSET)

        unit_filter = cls(
            allow_empty_units=allow_empty_units,
            unit=unit,
            unit_column=unit_column,
            unit_metadata=unit_metadata,
            value_column=value_column,
        )

        unit_filter.additional_properties = d
        return unit_filter

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
