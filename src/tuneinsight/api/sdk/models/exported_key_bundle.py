from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportedKeyBundle")


@attr.s(auto_attribs=True)
class ExportedKeyBundle:
    """encrypted KEK (key encryption key) bundle exported with a password.

    Attributes:
        encrypted_ke_ks (Union[Unset, str]):
        key_ids (Union[Unset, List[str]]):
        number_of_keys (Union[Unset, int]):
        salt (Union[Unset, str]):
        version (Union[Unset, int]):
    """

    encrypted_ke_ks: Union[Unset, str] = UNSET
    key_ids: Union[Unset, List[str]] = UNSET
    number_of_keys: Union[Unset, int] = UNSET
    salt: Union[Unset, str] = UNSET
    version: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        encrypted_ke_ks = self.encrypted_ke_ks
        key_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.key_ids, Unset):
            key_ids = self.key_ids

        number_of_keys = self.number_of_keys
        salt = self.salt
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if encrypted_ke_ks is not UNSET:
            field_dict["encryptedKEKs"] = encrypted_ke_ks
        if key_ids is not UNSET:
            field_dict["keyIds"] = key_ids
        if number_of_keys is not UNSET:
            field_dict["numberOfKeys"] = number_of_keys
        if salt is not UNSET:
            field_dict["salt"] = salt
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        encrypted_ke_ks = d.pop("encryptedKEKs", UNSET)

        key_ids = cast(List[str], d.pop("keyIds", UNSET))

        number_of_keys = d.pop("numberOfKeys", UNSET)

        salt = d.pop("salt", UNSET)

        version = d.pop("version", UNSET)

        exported_key_bundle = cls(
            encrypted_ke_ks=encrypted_ke_ks,
            key_ids=key_ids,
            number_of_keys=number_of_keys,
            salt=salt,
            version=version,
        )

        exported_key_bundle.additional_properties = d
        return exported_key_bundle

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
