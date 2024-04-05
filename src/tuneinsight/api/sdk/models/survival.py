from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.preprocessing_operation_type import PreprocessingOperationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.duration import Duration


T = TypeVar("T", bound="Survival")


@attr.s(auto_attribs=True)
class Survival:
    """
    Attributes:
        type (PreprocessingOperationType): type of preprocessing operation
        event_col (Union[Unset, str]): the name of the column that stores the event status for each sample Default:
            'event'.
        event_val (Union[Unset, str]): the event value indicating a survival event (i.e. death)
        interval (Union[Unset, Duration]): definition of a date-independent time interval
        num_frames (Union[Unset, int]): the number of time frames to take into account starting from the start of the
            survival
        start_event (Union[Unset, str]): the event column that must contain the timestamps of the start of the trial
        duration_col (Union[Unset, str]): the name of the column that stores the duration for each sample, the values
            stored must be integers Default: 'duration'.
        end_event (Union[Unset, str]): the column that must contain the timestamps of the end event (can be empty if no
            event happened)
    """

    type: PreprocessingOperationType
    event_col: Union[Unset, str] = "event"
    event_val: Union[Unset, str] = UNSET
    interval: Union[Unset, "Duration"] = UNSET
    num_frames: Union[Unset, int] = UNSET
    start_event: Union[Unset, str] = UNSET
    duration_col: Union[Unset, str] = "duration"
    end_event: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        event_col = self.event_col
        event_val = self.event_val
        interval: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.interval, Unset):
            interval = self.interval.to_dict()

        num_frames = self.num_frames
        start_event = self.start_event
        duration_col = self.duration_col
        end_event = self.end_event

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if event_col is not UNSET:
            field_dict["eventCol"] = event_col
        if event_val is not UNSET:
            field_dict["eventVal"] = event_val
        if interval is not UNSET:
            field_dict["interval"] = interval
        if num_frames is not UNSET:
            field_dict["numFrames"] = num_frames
        if start_event is not UNSET:
            field_dict["startEvent"] = start_event
        if duration_col is not UNSET:
            field_dict["durationCol"] = duration_col
        if end_event is not UNSET:
            field_dict["endEvent"] = end_event

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.duration import Duration

        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        event_col = d.pop("eventCol", UNSET)

        event_val = d.pop("eventVal", UNSET)

        _interval = d.pop("interval", UNSET)
        interval: Union[Unset, Duration]
        if isinstance(_interval, Unset):
            interval = UNSET
        else:
            interval = Duration.from_dict(_interval)

        num_frames = d.pop("numFrames", UNSET)

        start_event = d.pop("startEvent", UNSET)

        duration_col = d.pop("durationCol", UNSET)

        end_event = d.pop("endEvent", UNSET)

        survival = cls(
            type=type,
            event_col=event_col,
            event_val=event_val,
            interval=interval,
            num_frames=num_frames,
            start_event=start_event,
            duration_col=duration_col,
            end_event=end_event,
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
