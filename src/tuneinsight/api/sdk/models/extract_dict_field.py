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
        field (str): name of the dictionary field to extract
        cols (Union[Unset, List[str]]): cols from which to extract field
        names (Union[Unset, List[str]]): names of new columns with extracted fields (if none, no new columns are
            created)
    """

    type: PreprocessingOperationType
    field: str
    cols: Union[Unset, List[str]] = UNSET
    names: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        field = self.field
        cols: Union[Unset, List[str]] = UNSET
        if not isinstance(self.cols, Unset):
            cols = self.cols

        names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.names, Unset):
            names = self.names

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "field": field,
            }
        )
        if cols is not UNSET:
            field_dict["cols"] = cols
        if names is not UNSET:
            field_dict["names"] = names

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        field = d.pop("field")

        cols = cast(List[str], d.pop("cols", UNSET))

        names = cast(List[str], d.pop("names", UNSET))

        extract_dict_field = cls(
            type=type,
            field=field,
            cols=cols,
            names=names,
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
