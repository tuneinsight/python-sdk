from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AzureKeyVaultCredentialsProviderMappingsItem")


@attr.s(auto_attribs=True)
class AzureKeyVaultCredentialsProviderMappingsItem:
    """
    Attributes:
        creds_id (Union[Unset, str]):
        secret_id (Union[Unset, str]):
    """

    creds_id: Union[Unset, str] = UNSET
    secret_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        creds_id = self.creds_id
        secret_id = self.secret_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if creds_id is not UNSET:
            field_dict["credsID"] = creds_id
        if secret_id is not UNSET:
            field_dict["secretID"] = secret_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        creds_id = d.pop("credsID", UNSET)

        secret_id = d.pop("secretID", UNSET)

        azure_key_vault_credentials_provider_mappings_item = cls(
            creds_id=creds_id,
            secret_id=secret_id,
        )

        azure_key_vault_credentials_provider_mappings_item.additional_properties = d
        return azure_key_vault_credentials_provider_mappings_item

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
