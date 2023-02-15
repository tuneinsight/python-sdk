from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Encryption")


@attr.s(auto_attribs=True)
class Encryption:
    """
    Attributes:
        cryptosystem (Union[Unset, str]):
        key (Union[Unset, str]):
    """

    cryptosystem: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cryptosystem = self.cryptosystem
        key = self.key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cryptosystem is not UNSET:
            field_dict["cryptosystem"] = cryptosystem
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cryptosystem = d.pop("cryptosystem", UNSET)

        key = d.pop("key", UNSET)

        encryption = cls(
            cryptosystem=cryptosystem,
            key=key,
        )

        encryption.additional_properties = d
        return encryption

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
