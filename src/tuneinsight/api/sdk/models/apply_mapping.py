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
        input_ (Union[Unset, str]): column to use as input
        mapping (Union[Unset, StringMapping]): mapping from string -> string
        output (Union[Unset, str]): column to use as output
        default (Union[Unset, str]): default value to assign to items not specified in the dictionary
    """

    type: PreprocessingOperationType
    input_: Union[Unset, str] = UNSET
    mapping: Union[Unset, "StringMapping"] = UNSET
    output: Union[Unset, str] = UNSET
    default: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        input_ = self.input_
        mapping: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mapping, Unset):
            mapping = self.mapping.to_dict()

        output = self.output
        default = self.default

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if input_ is not UNSET:
            field_dict["input"] = input_
        if mapping is not UNSET:
            field_dict["mapping"] = mapping
        if output is not UNSET:
            field_dict["output"] = output
        if default is not UNSET:
            field_dict["default"] = default

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.string_mapping import StringMapping

        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        input_ = d.pop("input", UNSET)

        _mapping = d.pop("mapping", UNSET)
        mapping: Union[Unset, StringMapping]
        if isinstance(_mapping, Unset):
            mapping = UNSET
        else:
            mapping = StringMapping.from_dict(_mapping)

        output = d.pop("output", UNSET)

        default = d.pop("default", UNSET)

        apply_mapping = cls(
            type=type,
            input_=input_,
            mapping=mapping,
            output=output,
            default=default,
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
