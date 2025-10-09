from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatasourceDevOptions")


@attr.s(auto_attribs=True)
class DatasourceDevOptions:
    """Intended for development only, tools that can be used to modify a datasource's behavior to emulate real-world
    problems.

        Attributes:
            crash (Union[Unset, bool]): if true, the datasource returns an error when being queries. If combined with delay,
                the query waits for the delay before crashing.
            delay (Union[Unset, int]): delay, in seconds, between receiving a query and answering it.
    """

    crash: Union[Unset, bool] = UNSET
    delay: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        crash = self.crash
        delay = self.delay

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if crash is not UNSET:
            field_dict["crash"] = crash
        if delay is not UNSET:
            field_dict["delay"] = delay

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        crash = d.pop("crash", UNSET)

        delay = d.pop("delay", UNSET)

        datasource_dev_options = cls(
            crash=crash,
            delay=delay,
        )

        datasource_dev_options.additional_properties = d
        return datasource_dev_options

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
