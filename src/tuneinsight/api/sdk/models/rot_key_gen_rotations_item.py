from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RotKeyGenRotationsItem")


@attr.s(auto_attribs=True)
class RotKeyGenRotationsItem:
    """
    Attributes:
        value (Union[Unset, int]):
        side (Union[Unset, bool]):
    """

    value: Union[Unset, int] = UNSET
    side: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value = self.value
        side = self.side

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if side is not UNSET:
            field_dict["side"] = side

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        value = d.pop("value", UNSET)

        side = d.pop("side", UNSET)

        rot_key_gen_rotations_item = cls(
            value=value,
            side=side,
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
