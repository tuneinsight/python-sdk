from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.execution_quota_parameters_scope import ExecutionQuotaParametersScope
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.duration import Duration


T = TypeVar("T", bound="ExecutionQuotaParameters")


@attr.s(auto_attribs=True)
class ExecutionQuotaParameters:
    """Execution quota settings.
    The unit of the execution quota depends on the computation and other policies.
    If differential privacy is applied, it is in terms of the the epsilon value (ϵ) of the privacy budget.
    If the computation is a private set intersection, each query consumes budget equal to the size of the querying set.
    Otherwise, a unit represents one computation.

        Attributes:
            allocation (Union[Unset, float]): quota allocated initially.
            allocation_interval (Union[Unset, Duration]): definition of a date-independent time interval
            increment (Union[Unset, float]): value incremented after each allocation interval
            local_computations_use_budget (Union[Unset, bool]): whether local computations consume the execution quota
            max_allocation (Union[Unset, float]): maximum value that can be taken by the execution quota
            scope (Union[Unset, ExecutionQuotaParametersScope]): scope of the quota (default is project)
            users_share_quota (Union[Unset, bool]): if true, all users share the same budget within the scope. Otherwise,
                each user is allocated the full budget independently of others (default).
    """

    allocation: Union[Unset, float] = UNSET
    allocation_interval: Union[Unset, "Duration"] = UNSET
    increment: Union[Unset, float] = UNSET
    local_computations_use_budget: Union[Unset, bool] = False
    max_allocation: Union[Unset, float] = UNSET
    scope: Union[Unset, ExecutionQuotaParametersScope] = UNSET
    users_share_quota: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allocation = self.allocation
        allocation_interval: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.allocation_interval, Unset):
            allocation_interval = self.allocation_interval.to_dict()

        increment = self.increment
        local_computations_use_budget = self.local_computations_use_budget
        max_allocation = self.max_allocation
        scope: Union[Unset, str] = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.value

        users_share_quota = self.users_share_quota

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allocation is not UNSET:
            field_dict["allocation"] = allocation
        if allocation_interval is not UNSET:
            field_dict["allocationInterval"] = allocation_interval
        if increment is not UNSET:
            field_dict["increment"] = increment
        if local_computations_use_budget is not UNSET:
            field_dict["localComputationsUseBudget"] = local_computations_use_budget
        if max_allocation is not UNSET:
            field_dict["maxAllocation"] = max_allocation
        if scope is not UNSET:
            field_dict["scope"] = scope
        if users_share_quota is not UNSET:
            field_dict["usersShareQuota"] = users_share_quota

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.duration import Duration

        d = src_dict.copy()
        allocation = d.pop("allocation", UNSET)

        _allocation_interval = d.pop("allocationInterval", UNSET)
        allocation_interval: Union[Unset, Duration]
        if isinstance(_allocation_interval, Unset):
            allocation_interval = UNSET
        else:
            allocation_interval = Duration.from_dict(_allocation_interval)

        increment = d.pop("increment", UNSET)

        local_computations_use_budget = d.pop("localComputationsUseBudget", UNSET)

        max_allocation = d.pop("maxAllocation", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: Union[Unset, ExecutionQuotaParametersScope]
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = ExecutionQuotaParametersScope(_scope)

        users_share_quota = d.pop("usersShareQuota", UNSET)

        execution_quota_parameters = cls(
            allocation=allocation,
            allocation_interval=allocation_interval,
            increment=increment,
            local_computations_use_budget=local_computations_use_budget,
            max_allocation=max_allocation,
            scope=scope,
            users_share_quota=users_share_quota,
        )

        execution_quota_parameters.additional_properties = d
        return execution_quota_parameters

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
