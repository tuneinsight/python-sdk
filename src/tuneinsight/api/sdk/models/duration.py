from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.time_unit import TimeUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="Duration")


@attr.s(auto_attribs=True)
class Duration:
    """definition of a date-independent time interval

    Attributes:
        unit (Union[Unset, TimeUnit]): encoded unit of time
        value (Union[Unset, float]): integer value of the duration
    """

    unit: Union[Unset, TimeUnit] = UNSET
    value: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unit: Union[Unset, str] = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit.value

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unit is not UNSET:
            field_dict["unit"] = unit
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _unit = d.pop("unit", UNSET)
        unit: Union[Unset, TimeUnit]
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = TimeUnit(_unit)

        value = d.pop("value", UNSET)

        duration = cls(
            unit=unit,
            value=value,
        )

        duration.additional_properties = d
        return duration

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
