from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.credentials_provider_type import CredentialsProviderType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credentials import Credentials


T = TypeVar("T", bound="LocalCredentialsProvider")


@attr.s(auto_attribs=True)
class LocalCredentialsProvider:
    """
    Attributes:
        type (CredentialsProviderType):
        credentials (Union[Unset, List['Credentials']]):
    """

    type: CredentialsProviderType
    credentials: Union[Unset, List["Credentials"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        credentials: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = []
            for credentials_item_data in self.credentials:
                credentials_item = credentials_item_data.to_dict()

                credentials.append(credentials_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if credentials is not UNSET:
            field_dict["credentials"] = credentials

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.credentials import Credentials

        d = src_dict.copy()
        type = CredentialsProviderType(d.pop("type"))

        credentials = []
        _credentials = d.pop("credentials", UNSET)
        for credentials_item_data in _credentials or []:
            credentials_item = Credentials.from_dict(credentials_item_data)

            credentials.append(credentials_item)

        local_credentials_provider = cls(
            type=type,
            credentials=credentials,
        )

        local_credentials_provider.additional_properties = d
        return local_credentials_provider

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
