from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.access_scope import AccessScope
from ..models.data_source_consent_type import DataSourceConsentType
from ..models.data_source_type import DataSourceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credentials import Credentials
    from ..models.data_source_config import DataSourceConfig
    from ..models.data_source_metadata import DataSourceMetadata
    from ..models.local_data_selection import LocalDataSelection


T = TypeVar("T", bound="DataSource")


@attr.s(auto_attribs=True)
class DataSource:
    """
    Attributes:
        consent_type (Union[Unset, DataSourceConsentType]): Consent type given to the data source.
        id (Union[Unset, None, str]): Unique identifier of a data source.
        name (Union[Unset, str]):
        authorized_users (Union[Unset, List[str]]):
        clear_if_exists (Union[Unset, bool]): If true and a data source with the same name already exists, delete it.
        configuration (Union[Unset, DataSourceConfig]): data source configuration
        credentials (Union[Unset, Credentials]): The credentials needed to access the data source.
        is_mock (Union[Unset, bool]): Whether this datasource contains mock/synthetic data and should not be used in
            production.
        structure_template_json (Union[Unset, str]): data source's structure template (used to determine the query
            builder structure, if provided)
        type (Union[Unset, DataSourceType]):
        access_scope (Union[Unset, AccessScope]): defines the scope of access given to a resource
        attributes (Union[Unset, List[str]]): optional list of attributes.
        created_at (Union[Unset, str]):
        metadata (Union[Unset, DataSourceMetadata]): metadata about a datasource
        owner (Union[Unset, str]):
        projects (Union[Unset, List[str]]): ids of connected projects
        selections (Union[Unset, List['LocalDataSelection']]): list of local data selections associated with the data
            source
        updated_at (Union[Unset, str]):
    """

    consent_type: Union[Unset, DataSourceConsentType] = UNSET
    id: Union[Unset, None, str] = UNSET
    name: Union[Unset, str] = UNSET
    authorized_users: Union[Unset, List[str]] = UNSET
    clear_if_exists: Union[Unset, bool] = False
    configuration: Union[Unset, "DataSourceConfig"] = UNSET
    credentials: Union[Unset, "Credentials"] = UNSET
    is_mock: Union[Unset, bool] = UNSET
    structure_template_json: Union[Unset, str] = UNSET
    type: Union[Unset, DataSourceType] = UNSET
    access_scope: Union[Unset, AccessScope] = UNSET
    attributes: Union[Unset, List[str]] = UNSET
    created_at: Union[Unset, str] = UNSET
    metadata: Union[Unset, "DataSourceMetadata"] = UNSET
    owner: Union[Unset, str] = UNSET
    projects: Union[Unset, List[str]] = UNSET
    selections: Union[Unset, List["LocalDataSelection"]] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        consent_type: Union[Unset, str] = UNSET
        if not isinstance(self.consent_type, Unset):
            consent_type = self.consent_type.value

        id = self.id
        name = self.name
        authorized_users: Union[Unset, List[str]] = UNSET
        if not isinstance(self.authorized_users, Unset):
            authorized_users = self.authorized_users

        clear_if_exists = self.clear_if_exists
        configuration: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = self.configuration.to_dict()

        credentials: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = self.credentials.to_dict()

        is_mock = self.is_mock
        structure_template_json = self.structure_template_json
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        access_scope: Union[Unset, str] = UNSET
        if not isinstance(self.access_scope, Unset):
            access_scope = self.access_scope.value

        attributes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes

        created_at = self.created_at
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

        updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if consent_type is not UNSET:
            field_dict["consentType"] = consent_type
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if authorized_users is not UNSET:
            field_dict["authorizedUsers"] = authorized_users
        if clear_if_exists is not UNSET:
            field_dict["clearIfExists"] = clear_if_exists
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if is_mock is not UNSET:
            field_dict["isMock"] = is_mock
        if structure_template_json is not UNSET:
            field_dict["structureTemplateJSON"] = structure_template_json
        if type is not UNSET:
            field_dict["type"] = type
        if access_scope is not UNSET:
            field_dict["accessScope"] = access_scope
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if owner is not UNSET:
            field_dict["owner"] = owner
        if projects is not UNSET:
            field_dict["projects"] = projects
        if selections is not UNSET:
            field_dict["selections"] = selections
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.credentials import Credentials
        from ..models.data_source_config import DataSourceConfig
        from ..models.data_source_metadata import DataSourceMetadata
        from ..models.local_data_selection import LocalDataSelection

        d = src_dict.copy()
        _consent_type = d.pop("consentType", UNSET)
        consent_type: Union[Unset, DataSourceConsentType]
        if isinstance(_consent_type, Unset):
            consent_type = UNSET
        else:
            consent_type = DataSourceConsentType(_consent_type)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        authorized_users = cast(List[str], d.pop("authorizedUsers", UNSET))

        clear_if_exists = d.pop("clearIfExists", UNSET)

        _configuration = d.pop("configuration", UNSET)
        configuration: Union[Unset, DataSourceConfig]
        if isinstance(_configuration, Unset):
            configuration = UNSET
        else:
            configuration = DataSourceConfig.from_dict(_configuration)

        _credentials = d.pop("credentials", UNSET)
        credentials: Union[Unset, Credentials]
        if isinstance(_credentials, Unset):
            credentials = UNSET
        else:
            credentials = Credentials.from_dict(_credentials)

        is_mock = d.pop("isMock", UNSET)

        structure_template_json = d.pop("structureTemplateJSON", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, DataSourceType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DataSourceType(_type)

        _access_scope = d.pop("accessScope", UNSET)
        access_scope: Union[Unset, AccessScope]
        if isinstance(_access_scope, Unset):
            access_scope = UNSET
        else:
            access_scope = AccessScope(_access_scope)

        attributes = cast(List[str], d.pop("attributes", UNSET))

        created_at = d.pop("createdAt", UNSET)

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

        updated_at = d.pop("updatedAt", UNSET)

        data_source = cls(
            consent_type=consent_type,
            id=id,
            name=name,
            authorized_users=authorized_users,
            clear_if_exists=clear_if_exists,
            configuration=configuration,
            credentials=credentials,
            is_mock=is_mock,
            structure_template_json=structure_template_json,
            type=type,
            access_scope=access_scope,
            attributes=attributes,
            created_at=created_at,
            metadata=metadata,
            owner=owner,
            projects=projects,
            selections=selections,
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
