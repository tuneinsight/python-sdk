from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.health_status import HealthStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="DataSourceStatus")


@attr.s(auto_attribs=True)
class DataSourceStatus:
    """regroups data source health check status information

    Attributes:
        error (Union[Unset, str]): healthcheck reported error string.
        ping_time_ms (Union[Unset, int]): data source health check time in milliseconds.
        status (Union[Unset, HealthStatus]):
    """

    error: Union[Unset, str] = UNSET
    ping_time_ms: Union[Unset, int] = UNSET
    status: Union[Unset, HealthStatus] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error = self.error
        ping_time_ms = self.ping_time_ms
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if ping_time_ms is not UNSET:
            field_dict["pingTimeMs"] = ping_time_ms
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        error = d.pop("error", UNSET)

        ping_time_ms = d.pop("pingTimeMs", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, HealthStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = HealthStatus(_status)

        data_source_status = cls(
            error=error,
            ping_time_ms=ping_time_ms,
            status=status,
        )

        data_source_status.additional_properties = d
        return data_source_status

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
