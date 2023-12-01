import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.privacy_budget_parameters_scope import PrivacyBudgetParametersScope
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.duration import Duration


T = TypeVar("T", bound="PrivacyBudgetParameters")


@attr.s(auto_attribs=True)
class PrivacyBudgetParameters:
    """Differential privacy budget settings.
    The unit of the privacy budget is in terms of epsilon value (ϵ).
    More precisely, if a computation adds noise that is equivalent ϵ=0.1 then 0.1 of the privacy budget is used.

        Attributes:
            increment (Union[Unset, float]): value incremented after each allocation interval
            max_allocation (Union[Unset, float]): maximum value that can be taken by the privacy budget
            scope (Union[Unset, PrivacyBudgetParametersScope]): scope of the budget
            start (Union[Unset, datetime.datetime]): date time at which the budget is effective
            allocation (Union[Unset, float]): budget allocated initially.
            allocation_interval (Union[Unset, Duration]): definition of a date-independent time interval
    """

    increment: Union[Unset, float] = UNSET
    max_allocation: Union[Unset, float] = UNSET
    scope: Union[Unset, PrivacyBudgetParametersScope] = UNSET
    start: Union[Unset, datetime.datetime] = UNSET
    allocation: Union[Unset, float] = UNSET
    allocation_interval: Union[Unset, "Duration"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        increment = self.increment
        max_allocation = self.max_allocation
        scope: Union[Unset, str] = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.value

        start: Union[Unset, str] = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()

        allocation = self.allocation
        allocation_interval: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.allocation_interval, Unset):
            allocation_interval = self.allocation_interval.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if increment is not UNSET:
            field_dict["increment"] = increment
        if max_allocation is not UNSET:
            field_dict["maxAllocation"] = max_allocation
        if scope is not UNSET:
            field_dict["scope"] = scope
        if start is not UNSET:
            field_dict["start"] = start
        if allocation is not UNSET:
            field_dict["allocation"] = allocation
        if allocation_interval is not UNSET:
            field_dict["allocationInterval"] = allocation_interval

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.duration import Duration

        d = src_dict.copy()
        increment = d.pop("increment", UNSET)

        max_allocation = d.pop("maxAllocation", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: Union[Unset, PrivacyBudgetParametersScope]
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = PrivacyBudgetParametersScope(_scope)

        _start = d.pop("start", UNSET)
        start: Union[Unset, datetime.datetime]
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = isoparse(_start)

        allocation = d.pop("allocation", UNSET)

        _allocation_interval = d.pop("allocationInterval", UNSET)
        allocation_interval: Union[Unset, Duration]
        if isinstance(_allocation_interval, Unset):
            allocation_interval = UNSET
        else:
            allocation_interval = Duration.from_dict(_allocation_interval)

        privacy_budget_parameters = cls(
            increment=increment,
            max_allocation=max_allocation,
            scope=scope,
            start=start,
            allocation=allocation,
            allocation_interval=allocation_interval,
        )

        privacy_budget_parameters.additional_properties = d
        return privacy_budget_parameters

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
