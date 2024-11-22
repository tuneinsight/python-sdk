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
        input_column (str): column to one-hot encode
        prefix (Union[Unset, str]): optional prefix string to prepend to one-hot column names (if specified, an
            underscore is added to the prefix)
        specified_types (Union[Unset, List[str]]): if specified, values for which to create a one-hot encoding column
            (possible missing columns will be added)
        strict (Union[Unset, bool]): if true, only values in the specified types are used to produce dummies (requires
            specifiedTypes). This is required when using differential privacy.
    """

    type: PreprocessingOperationType
    input_column: str
    prefix: Union[Unset, str] = UNSET
    specified_types: Union[Unset, List[str]] = UNSET
    strict: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        input_column = self.input_column
        prefix = self.prefix
        specified_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.specified_types, Unset):
            specified_types = self.specified_types

        strict = self.strict

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "inputColumn": input_column,
            }
        )
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if specified_types is not UNSET:
            field_dict["specifiedTypes"] = specified_types
        if strict is not UNSET:
            field_dict["strict"] = strict

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        input_column = d.pop("inputColumn")

        prefix = d.pop("prefix", UNSET)

        specified_types = cast(List[str], d.pop("specifiedTypes", UNSET))

        strict = d.pop("strict", UNSET)

        one_hot_encoding = cls(
            type=type,
            input_column=input_column,
            prefix=prefix,
            specified_types=specified_types,
            strict=strict,
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
