from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.contribution_error_type import ContributionErrorType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContributionError")


@attr.s(auto_attribs=True)
class ContributionError:
    """represents a non-fatal error that is flagged whenever a participant fails to contribute data to a computation.

    Attributes:
        message (Union[Unset, str]): error message that can be displayed to end users.
        type (Union[Unset, ContributionErrorType]): contribution error type
    """

    message: Union[Unset, str] = UNSET
    type: Union[Unset, ContributionErrorType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        message = d.pop("message", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, ContributionErrorType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ContributionErrorType(_type)

        contribution_error = cls(
            message=message,
            type=type,
        )

        contribution_error.additional_properties = d
        return contribution_error

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
