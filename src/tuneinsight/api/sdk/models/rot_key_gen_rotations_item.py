from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RotKeyGenRotationsItem")


@attr.s(auto_attribs=True)
class RotKeyGenRotationsItem:
    """
    Attributes:
        side (Union[Unset, bool]):
        value (Union[Unset, int]):
    """

    side: Union[Unset, bool] = UNSET
    value: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        side = self.side
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if side is not UNSET:
            field_dict["side"] = side
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        side = d.pop("side", UNSET)

        value = d.pop("value", UNSET)

        rot_key_gen_rotations_item = cls(
            side=side,
            value=value,
        )

        rot_key_gen_rotations_item.additional_properties = d
        return rot_key_gen_rotations_item

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
