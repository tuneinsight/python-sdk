from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.content_type import ContentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.result_contextual_info import ResultContextualInfo


T = TypeVar("T", bound="EncryptedMaskShares")


@attr.s(auto_attribs=True)
class EncryptedMaskShares:
    """
    Attributes:
        type (ContentType): Type of the content
        value (str): marshaled encrypted content of mask shares
        contextual_info (Union[Unset, ResultContextualInfo]): contextual information about the content retrieved
        num_parties (Union[Unset, float]): number of parties that contributed to the mask shares
        num_shares (Union[Unset, float]): number of shares per party (i.e. number of keyswitched ciphertexts in the
            result)
    """

    type: ContentType
    value: str
    contextual_info: Union[Unset, "ResultContextualInfo"] = UNSET
    num_parties: Union[Unset, float] = UNSET
    num_shares: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        value = self.value
        contextual_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contextual_info, Unset):
            contextual_info = self.contextual_info.to_dict()

        num_parties = self.num_parties
        num_shares = self.num_shares

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "value": value,
            }
        )
        if contextual_info is not UNSET:
            field_dict["contextualInfo"] = contextual_info
        if num_parties is not UNSET:
            field_dict["numParties"] = num_parties
        if num_shares is not UNSET:
            field_dict["numShares"] = num_shares

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.result_contextual_info import ResultContextualInfo

        d = src_dict.copy()
        type = ContentType(d.pop("type"))

        value = d.pop("value")

        _contextual_info = d.pop("contextualInfo", UNSET)
        contextual_info: Union[Unset, ResultContextualInfo]
        if isinstance(_contextual_info, Unset):
            contextual_info = UNSET
        else:
            contextual_info = ResultContextualInfo.from_dict(_contextual_info)

        num_parties = d.pop("numParties", UNSET)

        num_shares = d.pop("numShares", UNSET)

        encrypted_mask_shares = cls(
            type=type,
            value=value,
            contextual_info=contextual_info,
            num_parties=num_parties,
            num_shares=num_shares,
        )

        encrypted_mask_shares.additional_properties = d
        return encrypted_mask_shares

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
