from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.preprocessing_operation_type import PreprocessingOperationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PhoneticEncoding")


@attr.s(auto_attribs=True)
class PhoneticEncoding:
    """
    Attributes:
        type (PreprocessingOperationType): type of preprocessing operation
        input_col (str): column to encode values on
        output_col (Union[Unset, str]): name of the column to store the encodings. If not specified, the encodings
            overwrite the input column values.
    """

    type: PreprocessingOperationType
    input_col: str
    output_col: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        input_col = self.input_col
        output_col = self.output_col

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "inputCol": input_col,
            }
        )
        if output_col is not UNSET:
            field_dict["outputCol"] = output_col

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        input_col = d.pop("inputCol")

        output_col = d.pop("outputCol", UNSET)

        phonetic_encoding = cls(
            type=type,
            input_col=input_col,
            output_col=output_col,
        )

        phonetic_encoding.additional_properties = d
        return phonetic_encoding

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
