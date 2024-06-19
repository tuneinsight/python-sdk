from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Measurement")


@attr.s(auto_attribs=True)
class Measurement:
    """measurement done during a specific part of a computation

    Attributes:
        allocated (Union[Unset, int]): total number of bytes allocated during this part.
        end (Union[Unset, str]): end time of the measurement. (RFC 3339 Nano format)
        ingress (Union[Unset, None, int]): number of incoming bytes from the network
        name (Union[Unset, str]): name of the computation part.
        periodic_allocations (Union[Unset, List[int]]): periodic measures of bytes allocated during this part.
        start (Union[Unset, str]): start time of the measurement. (RFC 3339 Nano format)
        time (Union[Unset, None, int]): total time of the measurement in milliseconds
        description (Union[Unset, str]): description of the computation part.
        egress (Union[Unset, None, int]): number of outgoing bytes to the network
    """

    allocated: Union[Unset, int] = UNSET
    end: Union[Unset, str] = UNSET
    ingress: Union[Unset, None, int] = UNSET
    name: Union[Unset, str] = UNSET
    periodic_allocations: Union[Unset, List[int]] = UNSET
    start: Union[Unset, str] = UNSET
    time: Union[Unset, None, int] = UNSET
    description: Union[Unset, str] = UNSET
    egress: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allocated = self.allocated
        end = self.end
        ingress = self.ingress
        name = self.name
        periodic_allocations: Union[Unset, List[int]] = UNSET
        if not isinstance(self.periodic_allocations, Unset):
            periodic_allocations = self.periodic_allocations

        start = self.start
        time = self.time
        description = self.description
        egress = self.egress

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allocated is not UNSET:
            field_dict["allocated"] = allocated
        if end is not UNSET:
            field_dict["end"] = end
        if ingress is not UNSET:
            field_dict["ingress"] = ingress
        if name is not UNSET:
            field_dict["name"] = name
        if periodic_allocations is not UNSET:
            field_dict["periodicAllocations"] = periodic_allocations
        if start is not UNSET:
            field_dict["start"] = start
        if time is not UNSET:
            field_dict["time"] = time
        if description is not UNSET:
            field_dict["description"] = description
        if egress is not UNSET:
            field_dict["egress"] = egress

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        allocated = d.pop("allocated", UNSET)

        end = d.pop("end", UNSET)

        ingress = d.pop("ingress", UNSET)

        name = d.pop("name", UNSET)

        periodic_allocations = cast(List[int], d.pop("periodicAllocations", UNSET))

        start = d.pop("start", UNSET)

        time = d.pop("time", UNSET)

        description = d.pop("description", UNSET)

        egress = d.pop("egress", UNSET)

        measurement = cls(
            allocated=allocated,
            end=end,
            ingress=ingress,
            name=name,
            periodic_allocations=periodic_allocations,
            start=start,
            time=time,
            description=description,
            egress=egress,
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
