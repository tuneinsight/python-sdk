from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.comparison_type import ComparisonType
from ..types import UNSET, Unset

T = TypeVar("T", bound="NumericalComparison")


@attr.s(auto_attribs=True)
class NumericalComparison:
    """Simplified structure that represents a single comparison on a numerical value.
    This defined a comparator and a right-hand comparand. The value being compared is the left-hand comparand.

        Attributes:
            comparator (Union[Unset, ComparisonType]): type of comparison
            right_hand_comparand (Union[Unset, float]):
    """

    comparator: Union[Unset, ComparisonType] = UNSET
    right_hand_comparand: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        comparator: Union[Unset, str] = UNSET
        if not isinstance(self.comparator, Unset):
            comparator = self.comparator.value

        right_hand_comparand = self.right_hand_comparand

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comparator is not UNSET:
            field_dict["comparator"] = comparator
        if right_hand_comparand is not UNSET:
            field_dict["rightHandComparand"] = right_hand_comparand

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _comparator = d.pop("comparator", UNSET)
        comparator: Union[Unset, ComparisonType]
        if isinstance(_comparator, Unset):
            comparator = UNSET
        else:
            comparator = ComparisonType(_comparator)

        right_hand_comparand = d.pop("rightHandComparand", UNSET)

        numerical_comparison = cls(
            comparator=comparator,
            right_hand_comparand=right_hand_comparand,
        )

        numerical_comparison.additional_properties = d
        return numerical_comparison

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
