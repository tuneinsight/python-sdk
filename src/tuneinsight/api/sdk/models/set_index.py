from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.preprocessing_operation_type import PreprocessingOperationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SetIndex")


@attr.s(auto_attribs=True)
class SetIndex:
    """
    Attributes:
        type (PreprocessingOperationType): type of preprocessing operation
        drop (Union[Unset, bool]): Delete columns to be used as the new index
        append (Union[Unset, bool]): Whether to append columns to existing index
        cols (Union[Unset, List[str]]): column(s) to use as index
    """

    type: PreprocessingOperationType
    drop: Union[Unset, bool] = UNSET
    append: Union[Unset, bool] = UNSET
    cols: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        drop = self.drop
        append = self.append
        cols: Union[Unset, List[str]] = UNSET
        if not isinstance(self.cols, Unset):
            cols = self.cols

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if drop is not UNSET:
            field_dict["drop"] = drop
        if append is not UNSET:
            field_dict["append"] = append
        if cols is not UNSET:
            field_dict["cols"] = cols

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        drop = d.pop("drop", UNSET)

        append = d.pop("append", UNSET)

        cols = cast(List[str], d.pop("cols", UNSET))

        set_index = cls(
            type=type,
            drop=drop,
            append=append,
            cols=cols,
        )

        set_index.additional_properties = d
        return set_index

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
