import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecutionQuota")


@attr.s(auto_attribs=True)
class ExecutionQuota:
    """stores information about the status of the execution quota

    Attributes:
        next_allocation (Union[Unset, datetime.datetime]): stores the date and time of the next quota allocation in
            rfc3339 format
        remaining_quota (Union[Unset, None, float]): stores the current value of the quota for the requesting user
    """

    next_allocation: Union[Unset, datetime.datetime] = UNSET
    remaining_quota: Union[Unset, None, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        next_allocation: Union[Unset, str] = UNSET
        if not isinstance(self.next_allocation, Unset):
            next_allocation = self.next_allocation.isoformat()

        remaining_quota = self.remaining_quota

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if next_allocation is not UNSET:
            field_dict["nextAllocation"] = next_allocation
        if remaining_quota is not UNSET:
            field_dict["remainingQuota"] = remaining_quota

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _next_allocation = d.pop("nextAllocation", UNSET)
        next_allocation: Union[Unset, datetime.datetime]
        if isinstance(_next_allocation, Unset):
            next_allocation = UNSET
        else:
            next_allocation = isoparse(_next_allocation)

        remaining_quota = d.pop("remainingQuota", UNSET)

        execution_quota = cls(
            next_allocation=next_allocation,
            remaining_quota=remaining_quota,
        )

        execution_quota.additional_properties = d
        return execution_quota

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
