from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.preprocessing_operation_type import PreprocessingOperationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Quantiles")


@attr.s(auto_attribs=True)
class Quantiles:
    """
    Attributes:
        type (PreprocessingOperationType): type of preprocessing operation
        input_column (Union[Unset, str]): column to use as input
        max_ (Union[Unset, float]): maximum value used for normalization Default: 100.0.
        min_ (Union[Unset, float]): minimum value used for normalization
    """

    type: PreprocessingOperationType
    input_column: Union[Unset, str] = UNSET
    max_: Union[Unset, float] = 100.0
    min_: Union[Unset, float] = 0.0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        input_column = self.input_column
        max_ = self.max_
        min_ = self.min_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if input_column is not UNSET:
            field_dict["inputColumn"] = input_column
        if max_ is not UNSET:
            field_dict["max"] = max_
        if min_ is not UNSET:
            field_dict["min"] = min_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        input_column = d.pop("inputColumn", UNSET)

        max_ = d.pop("max", UNSET)

        min_ = d.pop("min", UNSET)

        quantiles = cls(
            type=type,
            input_column=input_column,
            max_=max_,
            min_=min_,
        )

        quantiles.additional_properties = d
        return quantiles

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
