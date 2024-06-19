from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.enc_vector_type import EncVectorType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.encryption import Encryption


T = TypeVar("T", bound="EncVector")


@attr.s(auto_attribs=True)
class EncVector:
    """Vector of encrypted numerical values.

    Attributes:
        encryption (Encryption):
        type (EncVectorType):
        expanded (Union[Unset, List[str]]):
        packed (Union[Unset, str]):
    """

    encryption: "Encryption"
    type: EncVectorType
    expanded: Union[Unset, List[str]] = UNSET
    packed: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        encryption = self.encryption.to_dict()

        type = self.type.value

        expanded: Union[Unset, List[str]] = UNSET
        if not isinstance(self.expanded, Unset):
            expanded = self.expanded

        packed = self.packed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "encryption": encryption,
                "type": type,
            }
        )
        if expanded is not UNSET:
            field_dict["expanded"] = expanded
        if packed is not UNSET:
            field_dict["packed"] = packed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.encryption import Encryption

        d = src_dict.copy()
        encryption = Encryption.from_dict(d.pop("encryption"))

        type = EncVectorType(d.pop("type"))

        expanded = cast(List[str], d.pop("expanded", UNSET))

        packed = d.pop("packed", UNSET)

        enc_vector = cls(
            encryption=encryption,
            type=type,
            expanded=expanded,
            packed=packed,
        )

        enc_vector.additional_properties = d
        return enc_vector

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
