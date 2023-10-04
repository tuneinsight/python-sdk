from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.preprocessing_operation_type import PreprocessingOperationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Dropna")


@attr.s(auto_attribs=True)
class Dropna:
    """
    Attributes:
        type (PreprocessingOperationType): type of preprocessing operation
        subset (Union[Unset, List[str]]):
    """

    type: PreprocessingOperationType
    subset: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        subset: Union[Unset, List[str]] = UNSET
        if not isinstance(self.subset, Unset):
            subset = self.subset

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if subset is not UNSET:
            field_dict["subset"] = subset

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        subset = cast(List[str], d.pop("subset", UNSET))

        dropna = cls(
            type=type,
            subset=subset,
        )

        dropna.additional_properties = d
        return dropna

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
