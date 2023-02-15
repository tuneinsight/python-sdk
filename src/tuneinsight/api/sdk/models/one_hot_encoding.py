from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.preprocessing_operation_type import PreprocessingOperationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OneHotEncoding")


@attr.s(auto_attribs=True)
class OneHotEncoding:
    """
    Attributes:
        type (PreprocessingOperationType): type of preprocessing operation
        input_col (str): column to convert to one-hot-encoding
        prefix (Union[Unset, str]): prefix string to prepend to one-hot column names
        specified_types (Union[Unset, List[str]]): specified types to one-hot encode, if specified, then possible
            missing columns will be added
    """

    type: PreprocessingOperationType
    input_col: str
    prefix: Union[Unset, str] = UNSET
    specified_types: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        input_col = self.input_col
        prefix = self.prefix
        specified_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.specified_types, Unset):
            specified_types = self.specified_types

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "inputCol": input_col,
            }
        )
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if specified_types is not UNSET:
            field_dict["specifiedTypes"] = specified_types

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        input_col = d.pop("inputCol")

        prefix = d.pop("prefix", UNSET)

        specified_types = cast(List[str], d.pop("specifiedTypes", UNSET))

        one_hot_encoding = cls(
            type=type,
            input_col=input_col,
            prefix=prefix,
            specified_types=specified_types,
        )

        one_hot_encoding.additional_properties = d
        return one_hot_encoding

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
