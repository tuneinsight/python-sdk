from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="KekRotationDefinition")


@attr.s(auto_attribs=True)
class KekRotationDefinition:
    """parameters for requesting a KEK rotation

    Attributes:
        new_kek (str): new base64-formatted KEK
    """

    new_kek: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        new_kek = self.new_kek

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "newKEK": new_kek,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        new_kek = d.pop("newKEK")

        kek_rotation_definition = cls(
            new_kek=new_kek,
        )

        kek_rotation_definition.additional_properties = d
        return kek_rotation_definition

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
