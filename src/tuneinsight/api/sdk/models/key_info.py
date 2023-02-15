from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyInfo")


@attr.s(auto_attribs=True)
class KeyInfo:
    """information about keys

    Attributes:
        collective (Union[Unset, bool]): whether the key is personal or collective
        rotation_gal_el (Union[Unset, int]): rotation value of the rotation key
    """

    collective: Union[Unset, bool] = UNSET
    rotation_gal_el: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        collective = self.collective
        rotation_gal_el = self.rotation_gal_el

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if collective is not UNSET:
            field_dict["collective"] = collective
        if rotation_gal_el is not UNSET:
            field_dict["rotationGalEl"] = rotation_gal_el

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        collective = d.pop("collective", UNSET)

        rotation_gal_el = d.pop("rotationGalEl", UNSET)

        key_info = cls(
            collective=collective,
            rotation_gal_el=rotation_gal_el,
        )

        key_info.additional_properties = d
        return key_info

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
