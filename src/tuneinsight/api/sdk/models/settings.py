from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.usage_type import UsageType
from ..models.workflow_type import WorkflowType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.authorization_contract import AuthorizationContract
    from ..models.project_specification import ProjectSpecification


T = TypeVar("T", bound="Settings")


@attr.s(auto_attribs=True)
class Settings:
    """instance settings that is configurable by the administrator.

    Attributes:
        color_theme (Union[Unset, None, str]): Color theme of the instance
        access_with_python (Union[Unset, None, bool]): whether or not to enable the access with Python in Project
            Workflows.
        authorized_project_types (Union[Unset, List[WorkflowType]]): array of project types that are available for
            selection when creating a new project.
        auto_approve_specifications (Union[Unset, List['ProjectSpecification']]): A list of project templates such that
            satisfying at least one automatically authorizes the project.
        auto_reject_specifications (Union[Unset, List['ProjectSpecification']]): A list of project templates that must
            all be satisfied for a project to be authorized.
        client_max_timeout (Union[Unset, int]): custom timeout (seconds) to use for computations
        client_max_timeout_enabled (Union[Unset, None, bool]): whether to enable the computation timeout
        computation_timeout (Union[Unset, int]): custom timeout (seconds) to use for computations
        computation_timeout_enabled (Union[Unset, None, bool]): whether to enable the computation timeout
        data_screening (Union[Unset, None, bool]): whether or not to enable the data screening UI.
        default_contract (Union[Unset, AuthorizationContract]): describes what parts of the computation are allowed to
            change when a project is authorized
        default_data_source (Union[Unset, None, str]): Unique identifier of a data source.
        default_project (Union[Unset, str]): Unique identifier of a project.
        disable_shared_bookmarks (Union[Unset, None, bool]): whether to disable the shared bookmarks
        feasibility_layout (Union[Unset, None, bool]): whether or not to enable the feasibility mode layout.
        selectable_data_source (Union[Unset, None, bool]): whether or not the datasource of the project can be modified.
        set_project_policies (Union[Unset, None, bool]): whether policies can be set for projects.
        sparql_query_builder (Union[Unset, None, bool]): whether or not to enable the SparQL Query Builder.
        usage_type (Union[Unset, UsageType]): enumeration of usage types
    """

    color_theme: Union[Unset, None, str] = UNSET
    access_with_python: Union[Unset, None, bool] = UNSET
    authorized_project_types: Union[Unset, List[WorkflowType]] = UNSET
    auto_approve_specifications: Union[Unset, List["ProjectSpecification"]] = UNSET
    auto_reject_specifications: Union[Unset, List["ProjectSpecification"]] = UNSET
    client_max_timeout: Union[Unset, int] = UNSET
    client_max_timeout_enabled: Union[Unset, None, bool] = UNSET
    computation_timeout: Union[Unset, int] = UNSET
    computation_timeout_enabled: Union[Unset, None, bool] = UNSET
    data_screening: Union[Unset, None, bool] = UNSET
    default_contract: Union[Unset, "AuthorizationContract"] = UNSET
    default_data_source: Union[Unset, None, str] = UNSET
    default_project: Union[Unset, str] = UNSET
    disable_shared_bookmarks: Union[Unset, None, bool] = UNSET
    feasibility_layout: Union[Unset, None, bool] = UNSET
    selectable_data_source: Union[Unset, None, bool] = UNSET
    set_project_policies: Union[Unset, None, bool] = UNSET
    sparql_query_builder: Union[Unset, None, bool] = UNSET
    usage_type: Union[Unset, UsageType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        color_theme = self.color_theme
        access_with_python = self.access_with_python
        authorized_project_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.authorized_project_types, Unset):
            authorized_project_types = []
            for authorized_project_types_item_data in self.authorized_project_types:
                authorized_project_types_item = authorized_project_types_item_data.value

                authorized_project_types.append(authorized_project_types_item)

        auto_approve_specifications: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.auto_approve_specifications, Unset):
            auto_approve_specifications = []
            for auto_approve_specifications_item_data in self.auto_approve_specifications:
                auto_approve_specifications_item = auto_approve_specifications_item_data.to_dict()

                auto_approve_specifications.append(auto_approve_specifications_item)

        auto_reject_specifications: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.auto_reject_specifications, Unset):
            auto_reject_specifications = []
            for auto_reject_specifications_item_data in self.auto_reject_specifications:
                auto_reject_specifications_item = auto_reject_specifications_item_data.to_dict()

                auto_reject_specifications.append(auto_reject_specifications_item)

        client_max_timeout = self.client_max_timeout
        client_max_timeout_enabled = self.client_max_timeout_enabled
        computation_timeout = self.computation_timeout
        computation_timeout_enabled = self.computation_timeout_enabled
        data_screening = self.data_screening
        default_contract: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.default_contract, Unset):
            default_contract = self.default_contract.to_dict()

        default_data_source = self.default_data_source
        default_project = self.default_project
        disable_shared_bookmarks = self.disable_shared_bookmarks
        feasibility_layout = self.feasibility_layout
        selectable_data_source = self.selectable_data_source
        set_project_policies = self.set_project_policies
        sparql_query_builder = self.sparql_query_builder
        usage_type: Union[Unset, str] = UNSET
        if not isinstance(self.usage_type, Unset):
            usage_type = self.usage_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if color_theme is not UNSET:
            field_dict["ColorTheme"] = color_theme
        if access_with_python is not UNSET:
            field_dict["accessWithPython"] = access_with_python
        if authorized_project_types is not UNSET:
            field_dict["authorizedProjectTypes"] = authorized_project_types
        if auto_approve_specifications is not UNSET:
            field_dict["autoApproveSpecifications"] = auto_approve_specifications
        if auto_reject_specifications is not UNSET:
            field_dict["autoRejectSpecifications"] = auto_reject_specifications
        if client_max_timeout is not UNSET:
            field_dict["clientMaxTimeout"] = client_max_timeout
        if client_max_timeout_enabled is not UNSET:
            field_dict["clientMaxTimeoutEnabled"] = client_max_timeout_enabled
        if computation_timeout is not UNSET:
            field_dict["computationTimeout"] = computation_timeout
        if computation_timeout_enabled is not UNSET:
            field_dict["computationTimeoutEnabled"] = computation_timeout_enabled
        if data_screening is not UNSET:
            field_dict["dataScreening"] = data_screening
        if default_contract is not UNSET:
            field_dict["defaultContract"] = default_contract
        if default_data_source is not UNSET:
            field_dict["defaultDataSource"] = default_data_source
        if default_project is not UNSET:
            field_dict["defaultProject"] = default_project
        if disable_shared_bookmarks is not UNSET:
            field_dict["disableSharedBookmarks"] = disable_shared_bookmarks
        if feasibility_layout is not UNSET:
            field_dict["feasibilityLayout"] = feasibility_layout
        if selectable_data_source is not UNSET:
            field_dict["selectableDataSource"] = selectable_data_source
        if set_project_policies is not UNSET:
            field_dict["setProjectPolicies"] = set_project_policies
        if sparql_query_builder is not UNSET:
            field_dict["sparqlQueryBuilder"] = sparql_query_builder
        if usage_type is not UNSET:
            field_dict["usageType"] = usage_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.authorization_contract import AuthorizationContract
        from ..models.project_specification import ProjectSpecification

        d = src_dict.copy()
        color_theme = d.pop("ColorTheme", UNSET)

        access_with_python = d.pop("accessWithPython", UNSET)

        authorized_project_types = []
        _authorized_project_types = d.pop("authorizedProjectTypes", UNSET)
        for authorized_project_types_item_data in _authorized_project_types or []:
            authorized_project_types_item = WorkflowType(authorized_project_types_item_data)

            authorized_project_types.append(authorized_project_types_item)

        auto_approve_specifications = []
        _auto_approve_specifications = d.pop("autoApproveSpecifications", UNSET)
        for auto_approve_specifications_item_data in _auto_approve_specifications or []:
            auto_approve_specifications_item = ProjectSpecification.from_dict(auto_approve_specifications_item_data)

            auto_approve_specifications.append(auto_approve_specifications_item)

        auto_reject_specifications = []
        _auto_reject_specifications = d.pop("autoRejectSpecifications", UNSET)
        for auto_reject_specifications_item_data in _auto_reject_specifications or []:
            auto_reject_specifications_item = ProjectSpecification.from_dict(auto_reject_specifications_item_data)

            auto_reject_specifications.append(auto_reject_specifications_item)

        client_max_timeout = d.pop("clientMaxTimeout", UNSET)

        client_max_timeout_enabled = d.pop("clientMaxTimeoutEnabled", UNSET)

        computation_timeout = d.pop("computationTimeout", UNSET)

        computation_timeout_enabled = d.pop("computationTimeoutEnabled", UNSET)

        data_screening = d.pop("dataScreening", UNSET)

        _default_contract = d.pop("defaultContract", UNSET)
        default_contract: Union[Unset, AuthorizationContract]
        if isinstance(_default_contract, Unset):
            default_contract = UNSET
        else:
            default_contract = AuthorizationContract.from_dict(_default_contract)

        default_data_source = d.pop("defaultDataSource", UNSET)

        default_project = d.pop("defaultProject", UNSET)

        disable_shared_bookmarks = d.pop("disableSharedBookmarks", UNSET)

        feasibility_layout = d.pop("feasibilityLayout", UNSET)

        selectable_data_source = d.pop("selectableDataSource", UNSET)

        set_project_policies = d.pop("setProjectPolicies", UNSET)

        sparql_query_builder = d.pop("sparqlQueryBuilder", UNSET)

        _usage_type = d.pop("usageType", UNSET)
        usage_type: Union[Unset, UsageType]
        if isinstance(_usage_type, Unset):
            usage_type = UNSET
        else:
            usage_type = UsageType(_usage_type)

        settings = cls(
            color_theme=color_theme,
            access_with_python=access_with_python,
            authorized_project_types=authorized_project_types,
            auto_approve_specifications=auto_approve_specifications,
            auto_reject_specifications=auto_reject_specifications,
            client_max_timeout=client_max_timeout,
            client_max_timeout_enabled=client_max_timeout_enabled,
            computation_timeout=computation_timeout,
            computation_timeout_enabled=computation_timeout_enabled,
            data_screening=data_screening,
            default_contract=default_contract,
            default_data_source=default_data_source,
            default_project=default_project,
            disable_shared_bookmarks=disable_shared_bookmarks,
            feasibility_layout=feasibility_layout,
            selectable_data_source=selectable_data_source,
            set_project_policies=set_project_policies,
            sparql_query_builder=sparql_query_builder,
            usage_type=usage_type,
        )

        settings.additional_properties = d
        return settings

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
