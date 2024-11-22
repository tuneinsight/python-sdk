from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.preprocessing_operation_type import PreprocessingOperationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Scale")


@attr.s(auto_attribs=True)
class Scale:
    """
    Attributes:
        type (PreprocessingOperationType): type of preprocessing operation
        input_columns (List[str]): the name of one or more columns to scale by the constant
        scale (float): number by which to scale the columns
        output_columns (Union[Unset, List[str]]): if specified, name of the column created to store the scaled values.
            If not specified, the input column is overwritten in place.
    """

    type: PreprocessingOperationType
    input_columns: List[str]
    scale: float
    output_columns: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        input_columns = self.input_columns

        scale = self.scale
        output_columns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.output_columns, Unset):
            output_columns = self.output_columns

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "inputColumns": input_columns,
                "scale": scale,
            }
        )
        if output_columns is not UNSET:
            field_dict["outputColumns"] = output_columns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        input_columns = cast(List[str], d.pop("inputColumns"))

        scale = d.pop("scale")

        output_columns = cast(List[str], d.pop("outputColumns", UNSET))

        scale = cls(
            type=type,
            input_columns=input_columns,
            scale=scale,
            output_columns=output_columns,
        )

        scale.additional_properties = d
        return scale

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
