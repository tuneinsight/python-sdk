from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.comparison_type import ComparisonType
from ..models.preprocessing_operation_type import PreprocessingOperationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Filter")


@attr.s(auto_attribs=True)
class Filter:
    """
    Attributes:
        type (PreprocessingOperationType): type of preprocessing operation
        col_name (str): name of column to filter on
        value (str): value with which to compare
        comparator (Union[Unset, ComparisonType]): type of comparison
        numerical (Union[Unset, bool]): indicate whether the comparison is on numerical values
    """

    type: PreprocessingOperationType
    col_name: str
    value: str
    comparator: Union[Unset, ComparisonType] = UNSET
    numerical: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        col_name = self.col_name
        value = self.value
        comparator: Union[Unset, str] = UNSET
        if not isinstance(self.comparator, Unset):
            comparator = self.comparator.value

        numerical = self.numerical

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "colName": col_name,
                "value": value,
            }
        )
        if comparator is not UNSET:
            field_dict["comparator"] = comparator
        if numerical is not UNSET:
            field_dict["numerical"] = numerical

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        col_name = d.pop("colName")

        value = d.pop("value")

        _comparator = d.pop("comparator", UNSET)
        comparator: Union[Unset, ComparisonType]
        if isinstance(_comparator, Unset):
            comparator = UNSET
        else:
            comparator = ComparisonType(_comparator)

        numerical = d.pop("numerical", UNSET)

        filter_ = cls(
            type=type,
            col_name=col_name,
            value=value,
            comparator=comparator,
            numerical=numerical,
        )

        filter_.additional_properties = d
        return filter_

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
