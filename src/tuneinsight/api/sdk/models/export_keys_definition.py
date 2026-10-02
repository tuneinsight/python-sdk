from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportKeysDefinition")


@attr.s(auto_attribs=True)
class ExportKeysDefinition:
    """parameters for exporting keys

    Attributes:
        password (str): password used to encrypt the exported keys
        limit_keys (Union[Unset, int]): maximum number of keys to export; 0 exports all
    """

    password: str
    limit_keys: Union[Unset, int] = 0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        password = self.password
        limit_keys = self.limit_keys

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "password": password,
            }
        )
        if limit_keys is not UNSET:
            field_dict["limitKeys"] = limit_keys

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        password = d.pop("password")

        limit_keys = d.pop("limitKeys", UNSET)

        export_keys_definition = cls(
            password=password,
            limit_keys=limit_keys,
        )

        export_keys_definition.additional_properties = d
        return export_keys_definition

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
