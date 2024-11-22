from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Measurement")


@attr.s(auto_attribs=True)
class Measurement:
    """measurement done during a specific part of a computation

    Attributes:
        allocated (Union[Unset, int]): total number of bytes allocated during this part.
        description (Union[Unset, str]): description of the computation part.
        egress (Union[Unset, None, int]): number of outgoing bytes to the network
        end (Union[Unset, str]): end time of the measurement. (RFC 3339 Nano format)
        ingress (Union[Unset, None, int]): number of incoming bytes from the network
        name (Union[Unset, str]): name of the computation part.
        network_time (Union[Unset, None, int]): total time waiting for messages from the network during the measurement
            in milliseconds
        peak_memory (Union[Unset, None, int]): highest amount of memory allocated during the measurement in bytes
        periodic_allocations (Union[Unset, List[int]]): periodic measures of bytes allocated during this part.
        periodic_stats_interval (Union[Unset, int]): the interval used for the periodic measurements in milliseconds
        start (Union[Unset, str]): start time of the measurement. (RFC 3339 Nano format)
        time (Union[Unset, None, int]): total time of the measurement in milliseconds
    """

    allocated: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    egress: Union[Unset, None, int] = UNSET
    end: Union[Unset, str] = UNSET
    ingress: Union[Unset, None, int] = UNSET
    name: Union[Unset, str] = UNSET
    network_time: Union[Unset, None, int] = UNSET
    peak_memory: Union[Unset, None, int] = UNSET
    periodic_allocations: Union[Unset, List[int]] = UNSET
    periodic_stats_interval: Union[Unset, int] = UNSET
    start: Union[Unset, str] = UNSET
    time: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allocated = self.allocated
        description = self.description
        egress = self.egress
        end = self.end
        ingress = self.ingress
        name = self.name
        network_time = self.network_time
        peak_memory = self.peak_memory
        periodic_allocations: Union[Unset, List[int]] = UNSET
        if not isinstance(self.periodic_allocations, Unset):
            periodic_allocations = self.periodic_allocations

        periodic_stats_interval = self.periodic_stats_interval
        start = self.start
        time = self.time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allocated is not UNSET:
            field_dict["allocated"] = allocated
        if description is not UNSET:
            field_dict["description"] = description
        if egress is not UNSET:
            field_dict["egress"] = egress
        if end is not UNSET:
            field_dict["end"] = end
        if ingress is not UNSET:
            field_dict["ingress"] = ingress
        if name is not UNSET:
            field_dict["name"] = name
        if network_time is not UNSET:
            field_dict["networkTime"] = network_time
        if peak_memory is not UNSET:
            field_dict["peakMemory"] = peak_memory
        if periodic_allocations is not UNSET:
            field_dict["periodicAllocations"] = periodic_allocations
        if periodic_stats_interval is not UNSET:
            field_dict["periodicStatsInterval"] = periodic_stats_interval
        if start is not UNSET:
            field_dict["start"] = start
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        allocated = d.pop("allocated", UNSET)

        description = d.pop("description", UNSET)

        egress = d.pop("egress", UNSET)

        end = d.pop("end", UNSET)

        ingress = d.pop("ingress", UNSET)

        name = d.pop("name", UNSET)

        network_time = d.pop("networkTime", UNSET)

        peak_memory = d.pop("peakMemory", UNSET)

        periodic_allocations = cast(List[int], d.pop("periodicAllocations", UNSET))

        periodic_stats_interval = d.pop("periodicStatsInterval", UNSET)

        start = d.pop("start", UNSET)

        time = d.pop("time", UNSET)

        measurement = cls(
            allocated=allocated,
            description=description,
            egress=egress,
            end=end,
            ingress=ingress,
            name=name,
            network_time=network_time,
            peak_memory=peak_memory,
            periodic_allocations=periodic_allocations,
            periodic_stats_interval=periodic_stats_interval,
            start=start,
            time=time,
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
