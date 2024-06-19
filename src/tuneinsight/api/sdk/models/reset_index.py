from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.preprocessing_operation_type import PreprocessingOperationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ResetIndex")


@attr.s(auto_attribs=True)
class ResetIndex:
    """
    Attributes:
        type (PreprocessingOperationType): type of preprocessing operation
        drop (Union[Unset, bool]): whether to drop the index as a column
        level (Union[Unset, List[str]]): which levels to remove from the index (all by default)
    """

    type: PreprocessingOperationType
    drop: Union[Unset, bool] = UNSET
    level: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        drop = self.drop
        level: Union[Unset, List[str]] = UNSET
        if not isinstance(self.level, Unset):
            level = self.level

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if drop is not UNSET:
            field_dict["drop"] = drop
        if level is not UNSET:
            field_dict["level"] = level

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        drop = d.pop("drop", UNSET)

        level = cast(List[str], d.pop("level", UNSET))

        reset_index = cls(
            type=type,
            drop=drop,
            level=level,
        )

        reset_index.additional_properties = d
        return reset_index

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
