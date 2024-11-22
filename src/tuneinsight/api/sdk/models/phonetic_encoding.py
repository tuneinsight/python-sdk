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
        input_column (str): column containing the values to encode
        output_column (Union[Unset, str]): if specified, name of the column created to store the encodings. If not
            specified, the encodings overwrite the input column values in place.
    """

    type: PreprocessingOperationType
    input_column: str
    output_column: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        input_column = self.input_column
        output_column = self.output_column

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "inputColumn": input_column,
            }
        )
        if output_column is not UNSET:
            field_dict["outputColumn"] = output_column

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        input_column = d.pop("inputColumn")

        output_column = d.pop("outputColumn", UNSET)

        phonetic_encoding = cls(
            type=type,
            input_column=input_column,
            output_column=output_column,
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
