from typing import Any, Dict, List, Type, TypeVar, Union, cast

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
        value (str): value with which to compare
        col_name (str): name of column to filter on
        numerical (Union[Unset, bool]): indicate whether the comparison is on numerical values
        values (Union[Unset, List[str]]): list of values to pass in when comparison type is 'isin'.
        comparator (Union[Unset, ComparisonType]): type of comparison
    """

    type: PreprocessingOperationType
    value: str
    col_name: str
    numerical: Union[Unset, bool] = UNSET
    values: Union[Unset, List[str]] = UNSET
    comparator: Union[Unset, ComparisonType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        value = self.value
        col_name = self.col_name
        numerical = self.numerical
        values: Union[Unset, List[str]] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        comparator: Union[Unset, str] = UNSET
        if not isinstance(self.comparator, Unset):
            comparator = self.comparator.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "value": value,
                "colName": col_name,
            }
        )
        if numerical is not UNSET:
            field_dict["numerical"] = numerical
        if values is not UNSET:
            field_dict["values"] = values
        if comparator is not UNSET:
            field_dict["comparator"] = comparator

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        value = d.pop("value")

        col_name = d.pop("colName")

        numerical = d.pop("numerical", UNSET)

        values = cast(List[str], d.pop("values", UNSET))

        _comparator = d.pop("comparator", UNSET)
        comparator: Union[Unset, ComparisonType]
        if isinstance(_comparator, Unset):
            comparator = UNSET
        else:
            comparator = ComparisonType(_comparator)

        filter_ = cls(
            type=type,
            value=value,
            col_name=col_name,
            numerical=numerical,
            values=values,
            comparator=comparator,
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
