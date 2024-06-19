from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.access_scope import AccessScope
from ..models.data_source_consent_type import DataSourceConsentType
from ..models.data_source_type import DataSourceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credentials import Credentials
    from ..models.data_source_config import DataSourceConfig
    from ..models.data_source_definition_structure_template_json import DataSourceDefinitionStructureTemplateJSON


T = TypeVar("T", bound="DataSourceDefinition")


@attr.s(auto_attribs=True)
class DataSourceDefinition:
    """parameters used to create and modify a data source

    Attributes:
        id (Union[Unset, None, str]): Unique identifier of a data source.
        access_scope (Union[Unset, AccessScope]): defines the scope of access given to a resource
        authorized_users (Union[Unset, List[str]]):
        configuration (Union[Unset, DataSourceConfig]): data source configuration
        consent_type (Union[Unset, DataSourceConsentType]): Consent type given to the data source.
        name (Union[Unset, str]):
        structure_template_json (Union[Unset, DataSourceDefinitionStructureTemplateJSON]): data source's structure
            template (used to determine the query builder structure, if provided)
        type (Union[Unset, DataSourceType]):
        attributes (Union[Unset, List[str]]): optional list of attributes.
        clear_if_exists (Union[Unset, bool]): If true and a data source with the same name already exists, delete it.
        credentials (Union[Unset, Credentials]): The credentials needed to access the data source.
        is_mock (Union[Unset, bool]): Whether this datasource contains mock/synthetic data and should not be used in
            production.
    """

    id: Union[Unset, None, str] = UNSET
    access_scope: Union[Unset, AccessScope] = UNSET
    authorized_users: Union[Unset, List[str]] = UNSET
    configuration: Union[Unset, "DataSourceConfig"] = UNSET
    consent_type: Union[Unset, DataSourceConsentType] = UNSET
    name: Union[Unset, str] = UNSET
    structure_template_json: Union[Unset, "DataSourceDefinitionStructureTemplateJSON"] = UNSET
    type: Union[Unset, DataSourceType] = UNSET
    attributes: Union[Unset, List[str]] = UNSET
    clear_if_exists: Union[Unset, bool] = False
    credentials: Union[Unset, "Credentials"] = UNSET
    is_mock: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        access_scope: Union[Unset, str] = UNSET
        if not isinstance(self.access_scope, Unset):
            access_scope = self.access_scope.value

        authorized_users: Union[Unset, List[str]] = UNSET
        if not isinstance(self.authorized_users, Unset):
            authorized_users = self.authorized_users

        configuration: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = self.configuration.to_dict()

        consent_type: Union[Unset, str] = UNSET
        if not isinstance(self.consent_type, Unset):
            consent_type = self.consent_type.value

        name = self.name
        structure_template_json: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.structure_template_json, Unset):
            structure_template_json = self.structure_template_json.to_dict()

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        attributes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes

        clear_if_exists = self.clear_if_exists
        credentials: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = self.credentials.to_dict()

        is_mock = self.is_mock

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if access_scope is not UNSET:
            field_dict["accessScope"] = access_scope
        if authorized_users is not UNSET:
            field_dict["authorizedUsers"] = authorized_users
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if consent_type is not UNSET:
            field_dict["consentType"] = consent_type
        if name is not UNSET:
            field_dict["name"] = name
        if structure_template_json is not UNSET:
            field_dict["structureTemplateJSON"] = structure_template_json
        if type is not UNSET:
            field_dict["type"] = type
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if clear_if_exists is not UNSET:
            field_dict["clearIfExists"] = clear_if_exists
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if is_mock is not UNSET:
            field_dict["isMock"] = is_mock

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.credentials import Credentials
        from ..models.data_source_config import DataSourceConfig
        from ..models.data_source_definition_structure_template_json import DataSourceDefinitionStructureTemplateJSON

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _access_scope = d.pop("accessScope", UNSET)
        access_scope: Union[Unset, AccessScope]
        if isinstance(_access_scope, Unset):
            access_scope = UNSET
        else:
            access_scope = AccessScope(_access_scope)

        authorized_users = cast(List[str], d.pop("authorizedUsers", UNSET))

        _configuration = d.pop("configuration", UNSET)
        configuration: Union[Unset, DataSourceConfig]
        if isinstance(_configuration, Unset):
            configuration = UNSET
        else:
            configuration = DataSourceConfig.from_dict(_configuration)

        _consent_type = d.pop("consentType", UNSET)
        consent_type: Union[Unset, DataSourceConsentType]
        if isinstance(_consent_type, Unset):
            consent_type = UNSET
        else:
            consent_type = DataSourceConsentType(_consent_type)

        name = d.pop("name", UNSET)

        _structure_template_json = d.pop("structureTemplateJSON", UNSET)
        structure_template_json: Union[Unset, DataSourceDefinitionStructureTemplateJSON]
        if isinstance(_structure_template_json, Unset):
            structure_template_json = UNSET
        else:
            structure_template_json = DataSourceDefinitionStructureTemplateJSON.from_dict(_structure_template_json)

        _type = d.pop("type", UNSET)
        type: Union[Unset, DataSourceType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DataSourceType(_type)

        attributes = cast(List[str], d.pop("attributes", UNSET))

        clear_if_exists = d.pop("clearIfExists", UNSET)

        _credentials = d.pop("credentials", UNSET)
        credentials: Union[Unset, Credentials]
        if isinstance(_credentials, Unset):
            credentials = UNSET
        else:
            credentials = Credentials.from_dict(_credentials)

        is_mock = d.pop("isMock", UNSET)

        data_source_definition = cls(
            id=id,
            access_scope=access_scope,
            authorized_users=authorized_users,
            configuration=configuration,
            consent_type=consent_type,
            name=name,
            structure_template_json=structure_template_json,
            type=type,
            attributes=attributes,
            clear_if_exists=clear_if_exists,
            credentials=credentials,
            is_mock=is_mock,
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
