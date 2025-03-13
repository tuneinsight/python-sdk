from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DateFormat")


@attr.s(auto_attribs=True)
class DateFormat:
    """format for a date or timestamp in a dataset.

    Attributes:
        format_ (Union[Unset, str]): The go time format string for this date format.
            This string is equal to the date 2006-01-02 15:04:05 in this format.
            See https://golang.org/pkg/time/#pkg-constants
        name (Union[Unset, str]): common name for this format.
    """

    format_: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        format_ = self.format_
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if format_ is not UNSET:
            field_dict["format"] = format_
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        format_ = d.pop("format", UNSET)

        name = d.pop("name", UNSET)

        date_format = cls(
            format_=format_,
            name=name,
        )

        date_format.additional_properties = d
        return date_format

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
