from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.threshold_type import ThresholdType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Threshold")


@attr.s(auto_attribs=True)
class Threshold:
    """represents a threshold, which can be made relative of the dataset size

    Attributes:
        fixed_value (Union[Unset, int]): value of the fixed threshold
        relative_factor (Union[Unset, float]): when the threshold is relative to the dataset size, factor of this
            dataset size
        type (Union[Unset, ThresholdType]):
    """

    fixed_value: Union[Unset, int] = UNSET
    relative_factor: Union[Unset, float] = UNSET
    type: Union[Unset, ThresholdType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fixed_value = self.fixed_value
        relative_factor = self.relative_factor
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fixed_value is not UNSET:
            field_dict["fixedValue"] = fixed_value
        if relative_factor is not UNSET:
            field_dict["relativeFactor"] = relative_factor
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        fixed_value = d.pop("fixedValue", UNSET)

        relative_factor = d.pop("relativeFactor", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, ThresholdType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ThresholdType(_type)

        threshold = cls(
            fixed_value=fixed_value,
            relative_factor=relative_factor,
            type=type,
        )

        threshold.additional_properties = d
        return threshold

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
