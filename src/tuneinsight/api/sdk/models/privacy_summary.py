from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.authorization_status import AuthorizationStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_source import DataSource
    from ..models.execution_quota import ExecutionQuota
    from ..models.privacy_summary_computation import PrivacySummaryComputation
    from ..models.privacy_warning import PrivacyWarning


T = TypeVar("T", bound="PrivacySummary")


@attr.s(auto_attribs=True)
class PrivacySummary:
    """Privacy summary for a project

    Attributes:
        authorization_status (Union[Unset, AuthorizationStatus]): Authorization status of the project
        computation (Union[Unset, PrivacySummaryComputation]): Description of the computation that will be run for the
            project
        data_source (Union[Unset, DataSource]):
        execution_quota (Union[Unset, ExecutionQuota]): stores information about the status of the execution quota
        privacy_warnings (Union[Unset, List['PrivacyWarning']]): list of potential privacy risks in the current
            configuration of the project.
    """

    authorization_status: Union[Unset, AuthorizationStatus] = UNSET
    computation: Union[Unset, "PrivacySummaryComputation"] = UNSET
    data_source: Union[Unset, "DataSource"] = UNSET
    execution_quota: Union[Unset, "ExecutionQuota"] = UNSET
    privacy_warnings: Union[Unset, List["PrivacyWarning"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        authorization_status: Union[Unset, str] = UNSET
        if not isinstance(self.authorization_status, Unset):
            authorization_status = self.authorization_status.value

        computation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.computation, Unset):
            computation = self.computation.to_dict()

        data_source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data_source, Unset):
            data_source = self.data_source.to_dict()

        execution_quota: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.execution_quota, Unset):
            execution_quota = self.execution_quota.to_dict()

        privacy_warnings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.privacy_warnings, Unset):
            privacy_warnings = []
            for privacy_warnings_item_data in self.privacy_warnings:
                privacy_warnings_item = privacy_warnings_item_data.to_dict()

                privacy_warnings.append(privacy_warnings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authorization_status is not UNSET:
            field_dict["authorizationStatus"] = authorization_status
        if computation is not UNSET:
            field_dict["computation"] = computation
        if data_source is not UNSET:
            field_dict["dataSource"] = data_source
        if execution_quota is not UNSET:
            field_dict["executionQuota"] = execution_quota
        if privacy_warnings is not UNSET:
            field_dict["privacyWarnings"] = privacy_warnings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_source import DataSource
        from ..models.execution_quota import ExecutionQuota
        from ..models.privacy_summary_computation import PrivacySummaryComputation
        from ..models.privacy_warning import PrivacyWarning

        d = src_dict.copy()
        _authorization_status = d.pop("authorizationStatus", UNSET)
        authorization_status: Union[Unset, AuthorizationStatus]
        if isinstance(_authorization_status, Unset):
            authorization_status = UNSET
        else:
            authorization_status = AuthorizationStatus(_authorization_status)

        _computation = d.pop("computation", UNSET)
        computation: Union[Unset, PrivacySummaryComputation]
        if isinstance(_computation, Unset):
            computation = UNSET
        else:
            computation = PrivacySummaryComputation.from_dict(_computation)

        _data_source = d.pop("dataSource", UNSET)
        data_source: Union[Unset, DataSource]
        if isinstance(_data_source, Unset):
            data_source = UNSET
        else:
            data_source = DataSource.from_dict(_data_source)

        _execution_quota = d.pop("executionQuota", UNSET)
        execution_quota: Union[Unset, ExecutionQuota]
        if isinstance(_execution_quota, Unset):
            execution_quota = UNSET
        else:
            execution_quota = ExecutionQuota.from_dict(_execution_quota)

        privacy_warnings = []
        _privacy_warnings = d.pop("privacyWarnings", UNSET)
        for privacy_warnings_item_data in _privacy_warnings or []:
            privacy_warnings_item = PrivacyWarning.from_dict(privacy_warnings_item_data)

            privacy_warnings.append(privacy_warnings_item)

        privacy_summary = cls(
            authorization_status=authorization_status,
            computation=computation,
            data_source=data_source,
            execution_quota=execution_quota,
            privacy_warnings=privacy_warnings,
        )

        privacy_summary.additional_properties = d
        return privacy_summary

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
