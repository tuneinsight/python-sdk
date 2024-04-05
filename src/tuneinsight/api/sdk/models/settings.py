from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.workflow_type import WorkflowType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Settings")


@attr.s(auto_attribs=True)
class Settings:
    """instance settings that is configurable by the administrator.

    Attributes:
        authorized_project_types (Union[Unset, List[WorkflowType]]): array of project types that are available for
            selection when creating a new project.
        default_data_source (Union[Unset, None, str]): Unique identifier of a data source.
        selectable_data_source (Union[Unset, None, bool]): whether or not the datasource of the project can be modified.
        set_project_policies (Union[Unset, None, bool]): whether policies can be set for projects.
    """

    authorized_project_types: Union[Unset, List[WorkflowType]] = UNSET
    default_data_source: Union[Unset, None, str] = UNSET
    selectable_data_source: Union[Unset, None, bool] = UNSET
    set_project_policies: Union[Unset, None, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        authorized_project_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.authorized_project_types, Unset):
            authorized_project_types = []
            for authorized_project_types_item_data in self.authorized_project_types:
                authorized_project_types_item = authorized_project_types_item_data.value

                authorized_project_types.append(authorized_project_types_item)

        default_data_source = self.default_data_source
        selectable_data_source = self.selectable_data_source
        set_project_policies = self.set_project_policies

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authorized_project_types is not UNSET:
            field_dict["authorizedProjectTypes"] = authorized_project_types
        if default_data_source is not UNSET:
            field_dict["defaultDataSource"] = default_data_source
        if selectable_data_source is not UNSET:
            field_dict["selectableDataSource"] = selectable_data_source
        if set_project_policies is not UNSET:
            field_dict["setProjectPolicies"] = set_project_policies

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        authorized_project_types = []
        _authorized_project_types = d.pop("authorizedProjectTypes", UNSET)
        for authorized_project_types_item_data in _authorized_project_types or []:
            authorized_project_types_item = WorkflowType(authorized_project_types_item_data)

            authorized_project_types.append(authorized_project_types_item)

        default_data_source = d.pop("defaultDataSource", UNSET)

        selectable_data_source = d.pop("selectableDataSource", UNSET)

        set_project_policies = d.pop("setProjectPolicies", UNSET)

        settings = cls(
            authorized_project_types=authorized_project_types,
            default_data_source=default_data_source,
            selectable_data_source=selectable_data_source,
            set_project_policies=set_project_policies,
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
