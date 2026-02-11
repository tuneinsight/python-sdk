import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.goroutine import Goroutine
    from ..models.runtime_stats_top_goroutines import RuntimeStatsTopGoroutines


T = TypeVar("T", bound="RuntimeStats")


@attr.s(auto_attribs=True)
class RuntimeStats:
    """Runtime metrics snapshot.

    Attributes:
        allocated_bytes (Union[Unset, int]): current memory usage in bytes.
        app_routines (Union[Unset, List['Goroutine']]): list of running app-related goroutines with their stack
            information.
        num_app_goroutines (Union[Unset, int]): total number of app-related goroutines running on the instance.
        num_goroutines (Union[Unset, int]): total number of goroutines running on the instance.
        num_system_goroutines (Union[Unset, int]): total number of system-related goroutines (not directly spawned by
            application code)
        running_computations (Union[Unset, int]): number of running computations.
        system_routines (Union[Unset, List['Goroutine']]): list of running system-related goroutines with their stack
            information.
        timestamp (Union[Unset, datetime.datetime]):
        top_goroutines (Union[Unset, RuntimeStatsTopGoroutines]): Top goroutine entrypoints with their occurrence count
            (by lowest-level function name).
    """

    allocated_bytes: Union[Unset, int] = UNSET
    app_routines: Union[Unset, List["Goroutine"]] = UNSET
    num_app_goroutines: Union[Unset, int] = UNSET
    num_goroutines: Union[Unset, int] = UNSET
    num_system_goroutines: Union[Unset, int] = UNSET
    running_computations: Union[Unset, int] = UNSET
    system_routines: Union[Unset, List["Goroutine"]] = UNSET
    timestamp: Union[Unset, datetime.datetime] = UNSET
    top_goroutines: Union[Unset, "RuntimeStatsTopGoroutines"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allocated_bytes = self.allocated_bytes
        app_routines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.app_routines, Unset):
            app_routines = []
            for app_routines_item_data in self.app_routines:
                app_routines_item = app_routines_item_data.to_dict()

                app_routines.append(app_routines_item)

        num_app_goroutines = self.num_app_goroutines
        num_goroutines = self.num_goroutines
        num_system_goroutines = self.num_system_goroutines
        running_computations = self.running_computations
        system_routines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.system_routines, Unset):
            system_routines = []
            for system_routines_item_data in self.system_routines:
                system_routines_item = system_routines_item_data.to_dict()

                system_routines.append(system_routines_item)

        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        top_goroutines: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.top_goroutines, Unset):
            top_goroutines = self.top_goroutines.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allocated_bytes is not UNSET:
            field_dict["allocatedBytes"] = allocated_bytes
        if app_routines is not UNSET:
            field_dict["appRoutines"] = app_routines
        if num_app_goroutines is not UNSET:
            field_dict["numAppGoroutines"] = num_app_goroutines
        if num_goroutines is not UNSET:
            field_dict["numGoroutines"] = num_goroutines
        if num_system_goroutines is not UNSET:
            field_dict["numSystemGoroutines"] = num_system_goroutines
        if running_computations is not UNSET:
            field_dict["runningComputations"] = running_computations
        if system_routines is not UNSET:
            field_dict["systemRoutines"] = system_routines
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if top_goroutines is not UNSET:
            field_dict["topGoroutines"] = top_goroutines

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.goroutine import Goroutine
        from ..models.runtime_stats_top_goroutines import RuntimeStatsTopGoroutines

        d = src_dict.copy()
        allocated_bytes = d.pop("allocatedBytes", UNSET)

        app_routines = []
        _app_routines = d.pop("appRoutines", UNSET)
        for app_routines_item_data in _app_routines or []:
            app_routines_item = Goroutine.from_dict(app_routines_item_data)

            app_routines.append(app_routines_item)

        num_app_goroutines = d.pop("numAppGoroutines", UNSET)

        num_goroutines = d.pop("numGoroutines", UNSET)

        num_system_goroutines = d.pop("numSystemGoroutines", UNSET)

        running_computations = d.pop("runningComputations", UNSET)

        system_routines = []
        _system_routines = d.pop("systemRoutines", UNSET)
        for system_routines_item_data in _system_routines or []:
            system_routines_item = Goroutine.from_dict(system_routines_item_data)

            system_routines.append(system_routines_item)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        _top_goroutines = d.pop("topGoroutines", UNSET)
        top_goroutines: Union[Unset, RuntimeStatsTopGoroutines]
        if isinstance(_top_goroutines, Unset):
            top_goroutines = UNSET
        else:
            top_goroutines = RuntimeStatsTopGoroutines.from_dict(_top_goroutines)

        runtime_stats = cls(
            allocated_bytes=allocated_bytes,
            app_routines=app_routines,
            num_app_goroutines=num_app_goroutines,
            num_goroutines=num_goroutines,
            num_system_goroutines=num_system_goroutines,
            running_computations=running_computations,
            system_routines=system_routines,
            timestamp=timestamp,
            top_goroutines=top_goroutines,
        )

        runtime_stats.additional_properties = d
        return runtime_stats

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
