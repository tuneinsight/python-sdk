from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.data_source_consent_type import DataSourceConsentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credentials_provider import CredentialsProvider
    from ..models.data_source_config import DataSourceConfig


T = TypeVar("T", bound="DataSourceDefinition")


@attr.s(auto_attribs=True)
class DataSourceDefinition:
    """
    Attributes:
        attributes (Union[Unset, List[str]]):
        consent_type (Union[Unset, DataSourceConsentType]): Consent type given to the data source.
        name (Union[Unset, str]):
        type (Union[Unset, str]):
        unique_id (Union[Unset, str]): Unique identifier of a data source.
        config (Union[Unset, DataSourceConfig]): Configuration of data source that depends on the type.
        credentials_provider (Union[Unset, CredentialsProvider]): The provider of the credentials needed to access the
            data source.
    """

    attributes: Union[Unset, List[str]] = UNSET
    consent_type: Union[Unset, DataSourceConsentType] = UNSET
    name: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    unique_id: Union[Unset, str] = UNSET
    config: Union[Unset, "DataSourceConfig"] = UNSET
    credentials_provider: Union[Unset, "CredentialsProvider"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attributes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes

        consent_type: Union[Unset, str] = UNSET
        if not isinstance(self.consent_type, Unset):
            consent_type = self.consent_type.value

        name = self.name
        type = self.type
        unique_id = self.unique_id
        config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        credentials_provider: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credentials_provider, Unset):
            credentials_provider = self.credentials_provider.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if consent_type is not UNSET:
            field_dict["consentType"] = consent_type
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type
        if unique_id is not UNSET:
            field_dict["uniqueId"] = unique_id
        if config is not UNSET:
            field_dict["config"] = config
        if credentials_provider is not UNSET:
            field_dict["credentialsProvider"] = credentials_provider

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.credentials_provider import CredentialsProvider
        from ..models.data_source_config import DataSourceConfig

        d = src_dict.copy()
        attributes = cast(List[str], d.pop("attributes", UNSET))

        _consent_type = d.pop("consentType", UNSET)
        consent_type: Union[Unset, DataSourceConsentType]
        if isinstance(_consent_type, Unset):
            consent_type = UNSET
        else:
            consent_type = DataSourceConsentType(_consent_type)

        name = d.pop("name", UNSET)

        type = d.pop("type", UNSET)

        unique_id = d.pop("uniqueId", UNSET)

        _config = d.pop("config", UNSET)
        config: Union[Unset, DataSourceConfig]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = DataSourceConfig.from_dict(_config)

        _credentials_provider = d.pop("credentialsProvider", UNSET)
        credentials_provider: Union[Unset, CredentialsProvider]
        if isinstance(_credentials_provider, Unset):
            credentials_provider = UNSET
        else:
            credentials_provider = CredentialsProvider.from_dict(_credentials_provider)

        data_source_definition = cls(
            attributes=attributes,
            consent_type=consent_type,
            name=name,
            type=type,
            unique_id=unique_id,
            config=config,
            credentials_provider=credentials_provider,
        )

        data_source_definition.additional_properties = d
        return data_source_definition

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
