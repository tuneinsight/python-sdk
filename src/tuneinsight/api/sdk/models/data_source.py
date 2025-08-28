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
    from ..models.data_source_metadata import DataSourceMetadata
    from ..models.data_source_status import DataSourceStatus
    from ..models.dataset_schema import DatasetSchema
    from ..models.datasource_policy import DatasourcePolicy
    from ..models.local_data_selection import LocalDataSelection


T = TypeVar("T", bound="DataSource")


@attr.s(auto_attribs=True)
class DataSource:
    """
    Attributes:
        access_scope (Union[Unset, AccessScope]): defines the scope of access given to a resource
        attributes (Union[Unset, List[str]]): optional list of attributes.
        authorized_networks (Union[Unset, List[str]]): as with authorized users, this specifies the list of networks (by
            network name) that can access this data source,
            when the scope is set to network. If no network is provided, then the data source will be visible
            to all nodes connected to this instance.
        authorized_users (Union[Unset, List[str]]):
        cache_duration (Union[Unset, None, int]): Duration in hours for which the query results are cached (if unset, no
            cache is used).
        clear_if_exists (Union[Unset, bool]): If true and a data source with the same name already exists, delete it.
        configuration (Union[Unset, DataSourceConfig]): data source configuration
        consent_type (Union[Unset, DataSourceConsentType]): Consent type given to the data source.
        credentials (Union[Unset, Credentials]): The credentials needed to access the data source.
        id (Union[Unset, None, str]): Unique identifier of a data source.
        is_mock (Union[Unset, bool]): Whether this datasource contains mock/synthetic data and should not be used in
            production.
        name (Union[Unset, str]):
        policy (Union[Unset, DatasourcePolicy]): policy required by a datasource for the data to be used in a project.
        query_enabled (Union[Unset, None, bool]): Whether this data source can be directly queried by authorized users
            to retrieve the raw data.
            Note that a data source can still be queried when used in a computation from a project.
        structure_template_json (Union[Unset, DataSourceDefinitionStructureTemplateJSON]): data source's structure
            template (used to determine the query builder structure, if provided)
        type (Union[Unset, DataSourceType]):
        created_at (Union[Unset, str]):
        inferred_schemas (Union[Unset, List['DatasetSchema']]): list of all inferred data schemas for tables in this
            data
        last_up_at (Union[Unset, str]): timestamp of the most recent successful health check for the data source.
        metadata (Union[Unset, DataSourceMetadata]): metadata about a datasource
        owner (Union[Unset, str]):
        projects (Union[Unset, List[str]]): ids of connected projects
        selections (Union[Unset, List['LocalDataSelection']]): list of local data selections associated with the data
            source
        status (Union[Unset, DataSourceStatus]): regroups data source health check status information
        status_updated_at (Union[Unset, str]): time at which the status was last updated.
        updated_at (Union[Unset, str]):
    """

    access_scope: Union[Unset, AccessScope] = UNSET
    attributes: Union[Unset, List[str]] = UNSET
    authorized_networks: Union[Unset, List[str]] = UNSET
    authorized_users: Union[Unset, List[str]] = UNSET
    cache_duration: Union[Unset, None, int] = UNSET
    clear_if_exists: Union[Unset, bool] = False
    configuration: Union[Unset, "DataSourceConfig"] = UNSET
    consent_type: Union[Unset, DataSourceConsentType] = UNSET
    credentials: Union[Unset, "Credentials"] = UNSET
    id: Union[Unset, None, str] = UNSET
    is_mock: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    policy: Union[Unset, "DatasourcePolicy"] = UNSET
    query_enabled: Union[Unset, None, bool] = UNSET
    structure_template_json: Union[Unset, "DataSourceDefinitionStructureTemplateJSON"] = UNSET
    type: Union[Unset, DataSourceType] = UNSET
    created_at: Union[Unset, str] = UNSET
    inferred_schemas: Union[Unset, List["DatasetSchema"]] = UNSET
    last_up_at: Union[Unset, str] = UNSET
    metadata: Union[Unset, "DataSourceMetadata"] = UNSET
    owner: Union[Unset, str] = UNSET
    projects: Union[Unset, List[str]] = UNSET
    selections: Union[Unset, List["LocalDataSelection"]] = UNSET
    status: Union[Unset, "DataSourceStatus"] = UNSET
    status_updated_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access_scope: Union[Unset, str] = UNSET
        if not isinstance(self.access_scope, Unset):
            access_scope = self.access_scope.value

        attributes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes

        authorized_networks: Union[Unset, List[str]] = UNSET
        if not isinstance(self.authorized_networks, Unset):
            authorized_networks = self.authorized_networks

        authorized_users: Union[Unset, List[str]] = UNSET
        if not isinstance(self.authorized_users, Unset):
            authorized_users = self.authorized_users

        cache_duration = self.cache_duration
        clear_if_exists = self.clear_if_exists
        configuration: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = self.configuration.to_dict()

        consent_type: Union[Unset, str] = UNSET
        if not isinstance(self.consent_type, Unset):
            consent_type = self.consent_type.value

        credentials: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = self.credentials.to_dict()

        id = self.id
        is_mock = self.is_mock
        name = self.name
        policy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.policy, Unset):
            policy = self.policy.to_dict()

        query_enabled = self.query_enabled
        structure_template_json: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.structure_template_json, Unset):
            structure_template_json = self.structure_template_json.to_dict()

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        created_at = self.created_at
        inferred_schemas: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.inferred_schemas, Unset):
            inferred_schemas = []
            for inferred_schemas_item_data in self.inferred_schemas:
                inferred_schemas_item = inferred_schemas_item_data.to_dict()

                inferred_schemas.append(inferred_schemas_item)

        last_up_at = self.last_up_at
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        owner = self.owner
        projects: Union[Unset, List[str]] = UNSET
        if not isinstance(self.projects, Unset):
            projects = self.projects

        selections: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.selections, Unset):
            selections = []
            for selections_item_data in self.selections:
                selections_item = selections_item_data.to_dict()

                selections.append(selections_item)

        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        status_updated_at = self.status_updated_at
        updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_scope is not UNSET:
            field_dict["accessScope"] = access_scope
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if authorized_networks is not UNSET:
            field_dict["authorizedNetworks"] = authorized_networks
        if authorized_users is not UNSET:
            field_dict["authorizedUsers"] = authorized_users
        if cache_duration is not UNSET:
            field_dict["cacheDuration"] = cache_duration
        if clear_if_exists is not UNSET:
            field_dict["clearIfExists"] = clear_if_exists
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if consent_type is not UNSET:
            field_dict["consentType"] = consent_type
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if id is not UNSET:
            field_dict["id"] = id
        if is_mock is not UNSET:
            field_dict["isMock"] = is_mock
        if name is not UNSET:
            field_dict["name"] = name
        if policy is not UNSET:
            field_dict["policy"] = policy
        if query_enabled is not UNSET:
            field_dict["queryEnabled"] = query_enabled
        if structure_template_json is not UNSET:
            field_dict["structureTemplateJSON"] = structure_template_json
        if type is not UNSET:
            field_dict["type"] = type
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if inferred_schemas is not UNSET:
            field_dict["inferredSchemas"] = inferred_schemas
        if last_up_at is not UNSET:
            field_dict["lastUpAt"] = last_up_at
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if owner is not UNSET:
            field_dict["owner"] = owner
        if projects is not UNSET:
            field_dict["projects"] = projects
        if selections is not UNSET:
            field_dict["selections"] = selections
        if status is not UNSET:
            field_dict["status"] = status
        if status_updated_at is not UNSET:
            field_dict["statusUpdatedAt"] = status_updated_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.credentials import Credentials
        from ..models.data_source_config import DataSourceConfig
        from ..models.data_source_definition_structure_template_json import DataSourceDefinitionStructureTemplateJSON
        from ..models.data_source_metadata import DataSourceMetadata
        from ..models.data_source_status import DataSourceStatus
        from ..models.dataset_schema import DatasetSchema
        from ..models.datasource_policy import DatasourcePolicy
        from ..models.local_data_selection import LocalDataSelection

        d = src_dict.copy()
        _access_scope = d.pop("accessScope", UNSET)
        access_scope: Union[Unset, AccessScope]
        if isinstance(_access_scope, Unset):
            access_scope = UNSET
        else:
            access_scope = AccessScope(_access_scope)

        attributes = cast(List[str], d.pop("attributes", UNSET))

        authorized_networks = cast(List[str], d.pop("authorizedNetworks", UNSET))

        authorized_users = cast(List[str], d.pop("authorizedUsers", UNSET))

        cache_duration = d.pop("cacheDuration", UNSET)

        clear_if_exists = d.pop("clearIfExists", UNSET)

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

        _credentials = d.pop("credentials", UNSET)
        credentials: Union[Unset, Credentials]
        if isinstance(_credentials, Unset):
            credentials = UNSET
        else:
            credentials = Credentials.from_dict(_credentials)

        id = d.pop("id", UNSET)

        is_mock = d.pop("isMock", UNSET)

        name = d.pop("name", UNSET)

        _policy = d.pop("policy", UNSET)
        policy: Union[Unset, DatasourcePolicy]
        if isinstance(_policy, Unset):
            policy = UNSET
        else:
            policy = DatasourcePolicy.from_dict(_policy)

        query_enabled = d.pop("queryEnabled", UNSET)

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

        created_at = d.pop("createdAt", UNSET)

        inferred_schemas = []
        _inferred_schemas = d.pop("inferredSchemas", UNSET)
        for inferred_schemas_item_data in _inferred_schemas or []:
            inferred_schemas_item = DatasetSchema.from_dict(inferred_schemas_item_data)

            inferred_schemas.append(inferred_schemas_item)

        last_up_at = d.pop("lastUpAt", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, DataSourceMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = DataSourceMetadata.from_dict(_metadata)

        owner = d.pop("owner", UNSET)

        projects = cast(List[str], d.pop("projects", UNSET))

        selections = []
        _selections = d.pop("selections", UNSET)
        for selections_item_data in _selections or []:
            selections_item = LocalDataSelection.from_dict(selections_item_data)

            selections.append(selections_item)

        _status = d.pop("status", UNSET)
        status: Union[Unset, DataSourceStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = DataSourceStatus.from_dict(_status)

        status_updated_at = d.pop("statusUpdatedAt", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        data_source = cls(
            access_scope=access_scope,
            attributes=attributes,
            authorized_networks=authorized_networks,
            authorized_users=authorized_users,
            cache_duration=cache_duration,
            clear_if_exists=clear_if_exists,
            configuration=configuration,
            consent_type=consent_type,
            credentials=credentials,
            id=id,
            is_mock=is_mock,
            name=name,
            policy=policy,
            query_enabled=query_enabled,
            structure_template_json=structure_template_json,
            type=type,
            created_at=created_at,
            inferred_schemas=inferred_schemas,
            last_up_at=last_up_at,
            metadata=metadata,
            owner=owner,
            projects=projects,
            selections=selections,
            status=status,
            status_updated_at=status_updated_at,
            updated_at=updated_at,
        )

        data_source.additional_properties = d
        return data_source

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
