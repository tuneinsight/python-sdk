from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AvailabilityStatus")


@attr.s(auto_attribs=True)
class AvailabilityStatus:
    """generic object that holds information about whether a resource or action is available to the user.

    Attributes:
        available (bool): indicates whether the action is available to the user.
        context (Union[Unset, str]): optional additional text providing context on this status (not necessarily user-
            friendly, typically in JSON).
        reason (Union[Unset, str]): user-friendly text indicated why this action is available to the user or why it is
            not.
    """

    available: bool
    context: Union[Unset, str] = UNSET
    reason: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        available = self.available
        context = self.context
        reason = self.reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "available": available,
            }
        )
        if context is not UNSET:
            field_dict["context"] = context
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        available = d.pop("available")

        context = d.pop("context", UNSET)

        reason = d.pop("reason", UNSET)

        availability_status = cls(
            available=available,
            context=context,
            reason=reason,
        )

        availability_status.additional_properties = d
        return availability_status

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
