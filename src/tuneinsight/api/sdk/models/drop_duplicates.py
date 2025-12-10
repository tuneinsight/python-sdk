from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.drop_duplicates_keep import DropDuplicatesKeep
from ..models.preprocessing_operation_type import PreprocessingOperationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DropDuplicates")


@attr.s(auto_attribs=True)
class DropDuplicates:
    """
    Attributes:
        type (PreprocessingOperationType): type of preprocessing operation
        columns (Union[Unset, List[str]]): the columns to use as keys for deduplication. If none are provided, all
            columns are used.
        keep (Union[Unset, DropDuplicatesKeep]): determines which duplicate (if any) to keep. Default:
            DropDuplicatesKeep.FIRST.
    """

    type: PreprocessingOperationType
    columns: Union[Unset, List[str]] = UNSET
    keep: Union[Unset, DropDuplicatesKeep] = DropDuplicatesKeep.FIRST
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        columns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.columns, Unset):
            columns = self.columns

        keep: Union[Unset, str] = UNSET
        if not isinstance(self.keep, Unset):
            keep = self.keep.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if columns is not UNSET:
            field_dict["columns"] = columns
        if keep is not UNSET:
            field_dict["keep"] = keep

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        columns = cast(List[str], d.pop("columns", UNSET))

        _keep = d.pop("keep", UNSET)
        keep: Union[Unset, DropDuplicatesKeep]
        if isinstance(_keep, Unset):
            keep = UNSET
        else:
            keep = DropDuplicatesKeep(_keep)

        drop_duplicates = cls(
            type=type,
            columns=columns,
            keep=keep,
        )

        drop_duplicates.additional_properties = d
        return drop_duplicates

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
