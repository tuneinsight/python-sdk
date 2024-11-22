from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.preprocessing_operation_type import PreprocessingOperationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExtractDictField")


@attr.s(auto_attribs=True)
class ExtractDictField:
    """
    Attributes:
        type (PreprocessingOperationType): type of preprocessing operation
        field (str): name of the dictionary field to extract (i.e., dict[field])
        default (Union[Unset, str]): default value in case the field is not found or the dictionary is not valid.
        input_columns (Union[Unset, List[str]]): dictionary-valued columns from which to extract the field
        output_columns (Union[Unset, List[str]]): If specified, names of the new columns created with the extracted
            values. If not specified, no new columns are created and the operation is in-place.
    """

    type: PreprocessingOperationType
    field: str
    default: Union[Unset, str] = UNSET
    input_columns: Union[Unset, List[str]] = UNSET
    output_columns: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        field = self.field
        default = self.default
        input_columns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.input_columns, Unset):
            input_columns = self.input_columns

        output_columns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.output_columns, Unset):
            output_columns = self.output_columns

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "field": field,
            }
        )
        if default is not UNSET:
            field_dict["default"] = default
        if input_columns is not UNSET:
            field_dict["inputColumns"] = input_columns
        if output_columns is not UNSET:
            field_dict["outputColumns"] = output_columns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        field = d.pop("field")

        default = d.pop("default", UNSET)

        input_columns = cast(List[str], d.pop("inputColumns", UNSET))

        output_columns = cast(List[str], d.pop("outputColumns", UNSET))

        extract_dict_field = cls(
            type=type,
            field=field,
            default=default,
            input_columns=input_columns,
            output_columns=output_columns,
        )

        extract_dict_field.additional_properties = d
        return extract_dict_field

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
