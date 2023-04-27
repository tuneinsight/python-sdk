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
        value (str): value with which to compare
        col_name (str): name of column to filter on
        comparator (ComparisonType): type of comparison
        numerical (Union[Unset, bool]): indicate whether the comparison is on numerical values
    """

    type: PreprocessingOperationType
    value: str
    col_name: str
    comparator: ComparisonType
    numerical: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        value = self.value
        col_name = self.col_name
        comparator = self.comparator.value

        numerical = self.numerical

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "value": value,
                "colName": col_name,
                "comparator": comparator,
            }
        )
        if numerical is not UNSET:
            field_dict["numerical"] = numerical

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        value = d.pop("value")

        col_name = d.pop("colName")

        comparator = ComparisonType(d.pop("comparator"))

        numerical = d.pop("numerical", UNSET)

        filter_ = cls(
            type=type,
            value=value,
            col_name=col_name,
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
