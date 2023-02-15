from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.preprocessing_operation_type import PreprocessingOperationType
from ..models.time_unit import TimeUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="Survival")


@attr.s(auto_attribs=True)
class Survival:
    """
    Attributes:
        type (PreprocessingOperationType): type of preprocessing operation
        duration_col (Union[Unset, str]): the name of the column that stores the duration for each sample, the values
            stored must be integers Default: 'duration'.
        end_event (Union[Unset, str]): the column that must contain the timestamps of the end event (can be empty if no
            event happened)
        event_col (Union[Unset, str]): the name of the column that stores the event status for each sample Default:
            'event'.
        event_val (Union[Unset, str]): the event value indicating a survival event (i.e. death)
        num_frames (Union[Unset, int]): the number of time frames to take into account starting from the start of the
            survival
        start_event (Union[Unset, str]): the event column that must contain the timestamps of the start of the trial
        unit (Union[Unset, TimeUnit]): encoded unit of time
    """

    type: PreprocessingOperationType
    duration_col: Union[Unset, str] = "duration"
    end_event: Union[Unset, str] = UNSET
    event_col: Union[Unset, str] = "event"
    event_val: Union[Unset, str] = UNSET
    num_frames: Union[Unset, int] = UNSET
    start_event: Union[Unset, str] = UNSET
    unit: Union[Unset, TimeUnit] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        duration_col = self.duration_col
        end_event = self.end_event
        event_col = self.event_col
        event_val = self.event_val
        num_frames = self.num_frames
        start_event = self.start_event
        unit: Union[Unset, str] = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if duration_col is not UNSET:
            field_dict["durationCol"] = duration_col
        if end_event is not UNSET:
            field_dict["endEvent"] = end_event
        if event_col is not UNSET:
            field_dict["eventCol"] = event_col
        if event_val is not UNSET:
            field_dict["eventVal"] = event_val
        if num_frames is not UNSET:
            field_dict["numFrames"] = num_frames
        if start_event is not UNSET:
            field_dict["startEvent"] = start_event
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        duration_col = d.pop("durationCol", UNSET)

        end_event = d.pop("endEvent", UNSET)

        event_col = d.pop("eventCol", UNSET)

        event_val = d.pop("eventVal", UNSET)

        num_frames = d.pop("numFrames", UNSET)

        start_event = d.pop("startEvent", UNSET)

        _unit = d.pop("unit", UNSET)
        unit: Union[Unset, TimeUnit]
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = TimeUnit(_unit)

        survival = cls(
            type=type,
            duration_col=duration_col,
            end_event=end_event,
            event_col=event_col,
            event_val=event_val,
            num_frames=num_frames,
            start_event=start_event,
            unit=unit,
        )

        survival.additional_properties = d
        return survival

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
