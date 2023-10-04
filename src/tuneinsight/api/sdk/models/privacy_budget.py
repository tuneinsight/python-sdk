import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PrivacyBudget")


@attr.s(auto_attribs=True)
class PrivacyBudget:
    """stores information about the status of the privacy budget

    Attributes:
        current_budget (Union[Unset, float]): stores the current value of the budget for the requesting user
        next_allocation (Union[Unset, datetime.datetime]): stores the date and time of the next budget allocation in
            rfc3339 format
    """

    current_budget: Union[Unset, float] = UNSET
    next_allocation: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        current_budget = self.current_budget
        next_allocation: Union[Unset, str] = UNSET
        if not isinstance(self.next_allocation, Unset):
            next_allocation = self.next_allocation.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_budget is not UNSET:
            field_dict["currentBudget"] = current_budget
        if next_allocation is not UNSET:
            field_dict["nextAllocation"] = next_allocation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        current_budget = d.pop("currentBudget", UNSET)

        _next_allocation = d.pop("nextAllocation", UNSET)
        next_allocation: Union[Unset, datetime.datetime]
        if isinstance(_next_allocation, Unset):
            next_allocation = UNSET
        else:
            next_allocation = isoparse(_next_allocation)

        privacy_budget = cls(
            current_budget=current_budget,
            next_allocation=next_allocation,
        )

        privacy_budget.additional_properties = d
        return privacy_budget

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
