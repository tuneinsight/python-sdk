from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.authorization_status import AuthorizationStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_source import DataSource
    from ..models.privacy_budget import PrivacyBudget
    from ..models.privacy_summary_computation import PrivacySummaryComputation


T = TypeVar("T", bound="PrivacySummary")


@attr.s(auto_attribs=True)
class PrivacySummary:
    """Privacy summary for a project

    Attributes:
        computation (Union[Unset, PrivacySummaryComputation]): Description of the computation that will be run for the
            project
        data_source (Union[Unset, DataSource]):
        privacy_budget (Union[Unset, PrivacyBudget]): stores information about the status of the privacy budget
        authorization_status (Union[Unset, AuthorizationStatus]): Authorization status of the project
    """

    computation: Union[Unset, "PrivacySummaryComputation"] = UNSET
    data_source: Union[Unset, "DataSource"] = UNSET
    privacy_budget: Union[Unset, "PrivacyBudget"] = UNSET
    authorization_status: Union[Unset, AuthorizationStatus] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        computation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.computation, Unset):
            computation = self.computation.to_dict()

        data_source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data_source, Unset):
            data_source = self.data_source.to_dict()

        privacy_budget: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.privacy_budget, Unset):
            privacy_budget = self.privacy_budget.to_dict()

        authorization_status: Union[Unset, str] = UNSET
        if not isinstance(self.authorization_status, Unset):
            authorization_status = self.authorization_status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if computation is not UNSET:
            field_dict["computation"] = computation
        if data_source is not UNSET:
            field_dict["dataSource"] = data_source
        if privacy_budget is not UNSET:
            field_dict["privacyBudget"] = privacy_budget
        if authorization_status is not UNSET:
            field_dict["authorizationStatus"] = authorization_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_source import DataSource
        from ..models.privacy_budget import PrivacyBudget
        from ..models.privacy_summary_computation import PrivacySummaryComputation

        d = src_dict.copy()
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

        _privacy_budget = d.pop("privacyBudget", UNSET)
        privacy_budget: Union[Unset, PrivacyBudget]
        if isinstance(_privacy_budget, Unset):
            privacy_budget = UNSET
        else:
            privacy_budget = PrivacyBudget.from_dict(_privacy_budget)

        _authorization_status = d.pop("authorizationStatus", UNSET)
        authorization_status: Union[Unset, AuthorizationStatus]
        if isinstance(_authorization_status, Unset):
            authorization_status = UNSET
        else:
            authorization_status = AuthorizationStatus(_authorization_status)

        privacy_summary = cls(
            computation=computation,
            data_source=data_source,
            privacy_budget=privacy_budget,
            authorization_status=authorization_status,
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
