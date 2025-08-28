from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="JobLog")


@attr.s(auto_attribs=True)
class JobLog:
    """log from a background job.

    Attributes:
        level (Union[Unset, str]): log level
        msg (Union[Unset, str]):
        time (Union[Unset, str]):
    """

    level: Union[Unset, str] = UNSET
    msg: Union[Unset, str] = UNSET
    time: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        level = self.level
        msg = self.msg
        time = self.time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if level is not UNSET:
            field_dict["level"] = level
        if msg is not UNSET:
            field_dict["msg"] = msg
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        level = d.pop("level", UNSET)

        msg = d.pop("msg", UNSET)

        time = d.pop("time", UNSET)

        job_log = cls(
            level=level,
            msg=msg,
            time=time,
        )

        job_log.additional_properties = d
        return job_log

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
