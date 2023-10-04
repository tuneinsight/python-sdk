from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Measurement")


@attr.s(auto_attribs=True)
class Measurement:
    """measurement done during a specific part of a computation

    Attributes:
        start (Union[Unset, str]): start time of the measurement. (RFC 3339 Nano format)
        allocated (Union[Unset, int]): total number of bytes allocated during this part.
        description (Union[Unset, str]): description of the computation part.
        end (Union[Unset, str]): end time of the measurement. (RFC 3339 Nano format)
        name (Union[Unset, str]): name of the computation part.
    """

    start: Union[Unset, str] = UNSET
    allocated: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    end: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start = self.start
        allocated = self.allocated
        description = self.description
        end = self.end
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start is not UNSET:
            field_dict["start"] = start
        if allocated is not UNSET:
            field_dict["allocated"] = allocated
        if description is not UNSET:
            field_dict["description"] = description
        if end is not UNSET:
            field_dict["end"] = end
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        start = d.pop("start", UNSET)

        allocated = d.pop("allocated", UNSET)

        description = d.pop("description", UNSET)

        end = d.pop("end", UNSET)

        name = d.pop("name", UNSET)

        measurement = cls(
            start=start,
            allocated=allocated,
            description=description,
            end=end,
            name=name,
        )

        measurement.additional_properties = d
        return measurement

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
