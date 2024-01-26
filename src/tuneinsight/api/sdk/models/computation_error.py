from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.computation_error_type import ComputationErrorType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ComputationError")


@attr.s(auto_attribs=True)
class ComputationError:
    """error that occurred when running a computation

    Attributes:
        timestamp (Union[Unset, str]): time at which the error ocurred
        type (Union[Unset, ComputationErrorType]): error type identifier
        message (Union[Unset, str]): the error message
        origin (Union[Unset, str]): node instance id that caused the error
    """

    timestamp: Union[Unset, str] = UNSET
    type: Union[Unset, ComputationErrorType] = UNSET
    message: Union[Unset, str] = UNSET
    origin: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp = self.timestamp
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        message = self.message
        origin = self.origin

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if type is not UNSET:
            field_dict["type"] = type
        if message is not UNSET:
            field_dict["message"] = message
        if origin is not UNSET:
            field_dict["origin"] = origin

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        timestamp = d.pop("timestamp", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, ComputationErrorType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ComputationErrorType(_type)

        message = d.pop("message", UNSET)

        origin = d.pop("origin", UNSET)

        computation_error = cls(
            timestamp=timestamp,
            type=type,
            message=message,
            origin=origin,
        )

        computation_error.additional_properties = d
        return computation_error

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
