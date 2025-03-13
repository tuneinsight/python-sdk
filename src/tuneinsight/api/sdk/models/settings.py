from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

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
        auto_approve_specification (Union[Unset, ProjectSpecification]): Specifies parts of a project (called "checked
            project").
        auto_reject_specification (Union[Unset, ProjectSpecification]): Specifies parts of a project (called "checked
            project").
        data_screening (Union[Unset, None, bool]): whether or not to enable the data screening UI.
        default_contract (Union[Unset, AuthorizationContract]): describes what parts of the computation are allowed to
            change when a project is authorized
        default_data_source (Union[Unset, None, str]): Unique identifier of a data source.
        default_project (Union[Unset, str]): Unique identifier of a project.
        feasibility_layout (Union[Unset, None, bool]): whether or not to enable the feasibility mode layout.
        selectable_data_source (Union[Unset, None, bool]): whether or not the datasource of the project can be modified.
        set_project_policies (Union[Unset, None, bool]): whether policies can be set for projects.
        sparql_query_builder (Union[Unset, None, bool]): whether or not to enable the SparQL Query Builder.
    """

    color_theme: Union[Unset, None, str] = UNSET
    access_with_python: Union[Unset, None, bool] = UNSET
    authorized_project_types: Union[Unset, List[WorkflowType]] = UNSET
    auto_approve_specification: Union[Unset, "ProjectSpecification"] = UNSET
    auto_reject_specification: Union[Unset, "ProjectSpecification"] = UNSET
    data_screening: Union[Unset, None, bool] = UNSET
    default_contract: Union[Unset, "AuthorizationContract"] = UNSET
    default_data_source: Union[Unset, None, str] = UNSET
    default_project: Union[Unset, str] = UNSET
    feasibility_layout: Union[Unset, None, bool] = UNSET
    selectable_data_source: Union[Unset, None, bool] = UNSET
    set_project_policies: Union[Unset, None, bool] = UNSET
    sparql_query_builder: Union[Unset, None, bool] = UNSET
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

        auto_approve_specification: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.auto_approve_specification, Unset):
            auto_approve_specification = self.auto_approve_specification.to_dict()

        auto_reject_specification: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.auto_reject_specification, Unset):
            auto_reject_specification = self.auto_reject_specification.to_dict()

        data_screening = self.data_screening
        default_contract: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.default_contract, Unset):
            default_contract = self.default_contract.to_dict()

        default_data_source = self.default_data_source
        default_project = self.default_project
        feasibility_layout = self.feasibility_layout
        selectable_data_source = self.selectable_data_source
        set_project_policies = self.set_project_policies
        sparql_query_builder = self.sparql_query_builder

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if color_theme is not UNSET:
            field_dict["ColorTheme"] = color_theme
        if access_with_python is not UNSET:
            field_dict["accessWithPython"] = access_with_python
        if authorized_project_types is not UNSET:
            field_dict["authorizedProjectTypes"] = authorized_project_types
        if auto_approve_specification is not UNSET:
            field_dict["autoApproveSpecification"] = auto_approve_specification
        if auto_reject_specification is not UNSET:
            field_dict["autoRejectSpecification"] = auto_reject_specification
        if data_screening is not UNSET:
            field_dict["dataScreening"] = data_screening
        if default_contract is not UNSET:
            field_dict["defaultContract"] = default_contract
        if default_data_source is not UNSET:
            field_dict["defaultDataSource"] = default_data_source
        if default_project is not UNSET:
            field_dict["defaultProject"] = default_project
        if feasibility_layout is not UNSET:
            field_dict["feasibilityLayout"] = feasibility_layout
        if selectable_data_source is not UNSET:
            field_dict["selectableDataSource"] = selectable_data_source
        if set_project_policies is not UNSET:
            field_dict["setProjectPolicies"] = set_project_policies
        if sparql_query_builder is not UNSET:
            field_dict["sparqlQueryBuilder"] = sparql_query_builder

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

        _auto_approve_specification = d.pop("autoApproveSpecification", UNSET)
        auto_approve_specification: Union[Unset, ProjectSpecification]
        if isinstance(_auto_approve_specification, Unset):
            auto_approve_specification = UNSET
        else:
            auto_approve_specification = ProjectSpecification.from_dict(_auto_approve_specification)

        _auto_reject_specification = d.pop("autoRejectSpecification", UNSET)
        auto_reject_specification: Union[Unset, ProjectSpecification]
        if isinstance(_auto_reject_specification, Unset):
            auto_reject_specification = UNSET
        else:
            auto_reject_specification = ProjectSpecification.from_dict(_auto_reject_specification)

        data_screening = d.pop("dataScreening", UNSET)

        _default_contract = d.pop("defaultContract", UNSET)
        default_contract: Union[Unset, AuthorizationContract]
        if isinstance(_default_contract, Unset):
            default_contract = UNSET
        else:
            default_contract = AuthorizationContract.from_dict(_default_contract)

        default_data_source = d.pop("defaultDataSource", UNSET)

        default_project = d.pop("defaultProject", UNSET)

        feasibility_layout = d.pop("feasibilityLayout", UNSET)

        selectable_data_source = d.pop("selectableDataSource", UNSET)

        set_project_policies = d.pop("setProjectPolicies", UNSET)

        sparql_query_builder = d.pop("sparqlQueryBuilder", UNSET)

        settings = cls(
            color_theme=color_theme,
            access_with_python=access_with_python,
            authorized_project_types=authorized_project_types,
            auto_approve_specification=auto_approve_specification,
            auto_reject_specification=auto_reject_specification,
            data_screening=data_screening,
            default_contract=default_contract,
            default_data_source=default_data_source,
            default_project=default_project,
            feasibility_layout=feasibility_layout,
            selectable_data_source=selectable_data_source,
            set_project_policies=set_project_policies,
            sparql_query_builder=sparql_query_builder,
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
