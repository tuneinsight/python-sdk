from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ColumnSchemaChecksInRange")


@attr.s(auto_attribs=True)
class ColumnSchemaChecksInRange:
    """
    Attributes:
        include_max (Union[Unset, bool]):
        include_min (Union[Unset, bool]):
        max_value (Union[Unset, float]):
        min_value (Union[Unset, float]):
    """

    include_max: Union[Unset, bool] = UNSET
    include_min: Union[Unset, bool] = UNSET
    max_value: Union[Unset, float] = UNSET
    min_value: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        include_max = self.include_max
        include_min = self.include_min
        max_value = self.max_value
        min_value = self.min_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if include_max is not UNSET:
            field_dict["include_max"] = include_max
        if include_min is not UNSET:
            field_dict["include_min"] = include_min
        if max_value is not UNSET:
            field_dict["max_value"] = max_value
        if min_value is not UNSET:
            field_dict["min_value"] = min_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        include_max = d.pop("include_max", UNSET)

        include_min = d.pop("include_min", UNSET)

        max_value = d.pop("max_value", UNSET)

        min_value = d.pop("min_value", UNSET)

        column_schema_checks_in_range = cls(
            include_max=include_max,
            include_min=include_min,
            max_value=max_value,
            min_value=min_value,
        )

        column_schema_checks_in_range.additional_properties = d
        return column_schema_checks_in_range

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
