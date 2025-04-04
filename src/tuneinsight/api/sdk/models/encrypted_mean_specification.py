from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="EncryptedMeanSpecification")


@attr.s(auto_attribs=True)
class EncryptedMeanSpecification:
    """advanced specification for the encrypted mean operation.

    Attributes:
        min_participants (Union[Unset, float]): minimum value that should be set to the `minParticipants` field of the
            computation definition.
    """

    min_participants: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        min_participants = self.min_participants

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if min_participants is not UNSET:
            field_dict["minParticipants"] = min_participants

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        min_participants = d.pop("minParticipants", UNSET)

        encrypted_mean_specification = cls(
            min_participants=min_participants,
        )

        encrypted_mean_specification.additional_properties = d
        return encrypted_mean_specification

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
