from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.credentials_provider_type import CredentialsProviderType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.azure_key_vault_credentials_provider_mappings_item import AzureKeyVaultCredentialsProviderMappingsItem


T = TypeVar("T", bound="AzureKeyVaultCredentialsProvider")


@attr.s(auto_attribs=True)
class AzureKeyVaultCredentialsProvider:
    """
    Attributes:
        type (CredentialsProviderType):
        mappings (Union[Unset, List['AzureKeyVaultCredentialsProviderMappingsItem']]):
    """

    type: CredentialsProviderType
    mappings: Union[Unset, List["AzureKeyVaultCredentialsProviderMappingsItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        mappings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.mappings, Unset):
            mappings = []
            for mappings_item_data in self.mappings:
                mappings_item = mappings_item_data.to_dict()

                mappings.append(mappings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if mappings is not UNSET:
            field_dict["mappings"] = mappings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.azure_key_vault_credentials_provider_mappings_item import (
            AzureKeyVaultCredentialsProviderMappingsItem,
        )

        d = src_dict.copy()
        type = CredentialsProviderType(d.pop("type"))

        mappings = []
        _mappings = d.pop("mappings", UNSET)
        for mappings_item_data in _mappings or []:
            mappings_item = AzureKeyVaultCredentialsProviderMappingsItem.from_dict(mappings_item_data)

            mappings.append(mappings_item)

        azure_key_vault_credentials_provider = cls(
            type=type,
            mappings=mappings,
        )

        azure_key_vault_credentials_provider.additional_properties = d
        return azure_key_vault_credentials_provider

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
