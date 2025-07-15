from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.advanced_filter_type import AdvancedFilterType
from ..models.comparison_type import ComparisonType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AtomicFilter")


@attr.s(auto_attribs=True)
class AtomicFilter:
    """A filter performing a single comparison between a variable and a value or another variable.
    The left-hand variable must either be a feature of the record, or the name of a feature of an
    entry in a series (if as part of a seriesFilter). The comparison can be made either against
    a static value (rightHandValue) or another variable (defined for the query).

        Attributes:
            type (AdvancedFilterType): A type of filter for cross-standard queries.
            comparator (Union[Unset, ComparisonType]): type of comparison
            left_hand_variable (Union[Unset, str]):
            right_hand_value (Union[Unset, str]):
            right_hand_variable (Union[Unset, str]):
    """

    type: AdvancedFilterType
    comparator: Union[Unset, ComparisonType] = UNSET
    left_hand_variable: Union[Unset, str] = UNSET
    right_hand_value: Union[Unset, str] = UNSET
    right_hand_variable: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        comparator: Union[Unset, str] = UNSET
        if not isinstance(self.comparator, Unset):
            comparator = self.comparator.value

        left_hand_variable = self.left_hand_variable
        right_hand_value = self.right_hand_value
        right_hand_variable = self.right_hand_variable

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if comparator is not UNSET:
            field_dict["comparator"] = comparator
        if left_hand_variable is not UNSET:
            field_dict["leftHandVariable"] = left_hand_variable
        if right_hand_value is not UNSET:
            field_dict["rightHandValue"] = right_hand_value
        if right_hand_variable is not UNSET:
            field_dict["rightHandVariable"] = right_hand_variable

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = AdvancedFilterType(d.pop("type"))

        _comparator = d.pop("comparator", UNSET)
        comparator: Union[Unset, ComparisonType]
        if isinstance(_comparator, Unset):
            comparator = UNSET
        else:
            comparator = ComparisonType(_comparator)

        left_hand_variable = d.pop("leftHandVariable", UNSET)

        right_hand_value = d.pop("rightHandValue", UNSET)

        right_hand_variable = d.pop("rightHandVariable", UNSET)

        atomic_filter = cls(
            type=type,
            comparator=comparator,
            left_hand_variable=left_hand_variable,
            right_hand_value=right_hand_value,
            right_hand_variable=right_hand_variable,
        )

        atomic_filter.additional_properties = d
        return atomic_filter

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
