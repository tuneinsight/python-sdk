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
        cols (Union[Unset, List[str]]): column(s) to use as index
        drop (Union[Unset, bool]): Delete columns to be used as the new index
        append (Union[Unset, bool]): Whether to append columns to existing index
    """

    type: PreprocessingOperationType
    cols: Union[Unset, List[str]] = UNSET
    drop: Union[Unset, bool] = UNSET
    append: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        cols: Union[Unset, List[str]] = UNSET
        if not isinstance(self.cols, Unset):
            cols = self.cols

        drop = self.drop
        append = self.append

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if cols is not UNSET:
            field_dict["cols"] = cols
        if drop is not UNSET:
            field_dict["drop"] = drop
        if append is not UNSET:
            field_dict["append"] = append

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        cols = cast(List[str], d.pop("cols", UNSET))

        drop = d.pop("drop", UNSET)

        append = d.pop("append", UNSET)

        set_index = cls(
            type=type,
            cols=cols,
            drop=drop,
            append=append,
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
