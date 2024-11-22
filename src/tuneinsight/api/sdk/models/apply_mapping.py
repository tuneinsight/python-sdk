from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.preprocessing_operation_type import PreprocessingOperationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.string_mapping import StringMapping


T = TypeVar("T", bound="ApplyMapping")


@attr.s(auto_attribs=True)
class ApplyMapping:
    """
    Attributes:
        type (PreprocessingOperationType): type of preprocessing operation
        default (Union[Unset, str]): default value to assign to items not specified in the dictionary
        input_column (Union[Unset, str]): column to use as input
        mapping (Union[Unset, StringMapping]): mapping from string -> string
        output_column (Union[Unset, str]): column to use as output. If not specified, the input column is used (in
            place).
    """

    type: PreprocessingOperationType
    default: Union[Unset, str] = UNSET
    input_column: Union[Unset, str] = UNSET
    mapping: Union[Unset, "StringMapping"] = UNSET
    output_column: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        default = self.default
        input_column = self.input_column
        mapping: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mapping, Unset):
            mapping = self.mapping.to_dict()

        output_column = self.output_column

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if default is not UNSET:
            field_dict["default"] = default
        if input_column is not UNSET:
            field_dict["inputColumn"] = input_column
        if mapping is not UNSET:
            field_dict["mapping"] = mapping
        if output_column is not UNSET:
            field_dict["outputColumn"] = output_column

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.string_mapping import StringMapping

        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        default = d.pop("default", UNSET)

        input_column = d.pop("inputColumn", UNSET)

        _mapping = d.pop("mapping", UNSET)
        mapping: Union[Unset, StringMapping]
        if isinstance(_mapping, Unset):
            mapping = UNSET
        else:
            mapping = StringMapping.from_dict(_mapping)

        output_column = d.pop("outputColumn", UNSET)

        apply_mapping = cls(
            type=type,
            default=default,
            input_column=input_column,
            mapping=mapping,
            output_column=output_column,
        )

        apply_mapping.additional_properties = d
        return apply_mapping

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
