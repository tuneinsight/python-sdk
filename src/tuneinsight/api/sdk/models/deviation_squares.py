from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.preprocessing_operation_type import PreprocessingOperationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviationSquares")


@attr.s(auto_attribs=True)
class DeviationSquares:
    """
    Attributes:
        type (PreprocessingOperationType): type of preprocessing operation
        count (Union[Unset, float]): dataset count used for computing the variance, if < 2 then the sum of squares will
            be divided by 1
        input_column (Union[Unset, str]): column to use as input
        mean (Union[Unset, float]): mean to compute the deviation from
        output_column (Union[Unset, str]): column to use as output
    """

    type: PreprocessingOperationType
    count: Union[Unset, float] = UNSET
    input_column: Union[Unset, str] = UNSET
    mean: Union[Unset, float] = UNSET
    output_column: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        count = self.count
        input_column = self.input_column
        mean = self.mean
        output_column = self.output_column

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if count is not UNSET:
            field_dict["count"] = count
        if input_column is not UNSET:
            field_dict["inputColumn"] = input_column
        if mean is not UNSET:
            field_dict["mean"] = mean
        if output_column is not UNSET:
            field_dict["outputColumn"] = output_column

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        count = d.pop("count", UNSET)

        input_column = d.pop("inputColumn", UNSET)

        mean = d.pop("mean", UNSET)

        output_column = d.pop("outputColumn", UNSET)

        deviation_squares = cls(
            type=type,
            count=count,
            input_column=input_column,
            mean=mean,
            output_column=output_column,
        )

        deviation_squares.additional_properties = d
        return deviation_squares

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
