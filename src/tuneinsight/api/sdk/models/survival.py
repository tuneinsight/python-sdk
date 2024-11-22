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
        num_frames (int): the number of time frames to take into account starting from the start of the survival
        duration_column (Union[Unset, str]): the name of the column that stores the duration for each sample, the values
            stored must be integers Default: 'duration'.
        end_event_column (Union[Unset, str]): the column that contains the timestamps of the end event (can be empty if
            no event happened)
        event_column (Union[Unset, str]): the name of the column that stores the event status for each sample Default:
            'event_status'.
        event_value (Union[Unset, str]): the event value indicating a survival event (i.e. death), default 1. Default:
            '1'.
        interval (Union[Unset, Duration]): definition of a date-independent time interval
        start_event_column (Union[Unset, str]): the event column that contains the timestamps of the start of the trial
    """

    type: PreprocessingOperationType
    num_frames: int
    duration_column: Union[Unset, str] = "duration"
    end_event_column: Union[Unset, str] = UNSET
    event_column: Union[Unset, str] = "event_status"
    event_value: Union[Unset, str] = "1"
    interval: Union[Unset, "Duration"] = UNSET
    start_event_column: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        num_frames = self.num_frames
        duration_column = self.duration_column
        end_event_column = self.end_event_column
        event_column = self.event_column
        event_value = self.event_value
        interval: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.interval, Unset):
            interval = self.interval.to_dict()

        start_event_column = self.start_event_column

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "numFrames": num_frames,
            }
        )
        if duration_column is not UNSET:
            field_dict["durationColumn"] = duration_column
        if end_event_column is not UNSET:
            field_dict["endEventColumn"] = end_event_column
        if event_column is not UNSET:
            field_dict["eventColumn"] = event_column
        if event_value is not UNSET:
            field_dict["eventValue"] = event_value
        if interval is not UNSET:
            field_dict["interval"] = interval
        if start_event_column is not UNSET:
            field_dict["startEventColumn"] = start_event_column

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.duration import Duration

        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        num_frames = d.pop("numFrames")

        duration_column = d.pop("durationColumn", UNSET)

        end_event_column = d.pop("endEventColumn", UNSET)

        event_column = d.pop("eventColumn", UNSET)

        event_value = d.pop("eventValue", UNSET)

        _interval = d.pop("interval", UNSET)
        interval: Union[Unset, Duration]
        if isinstance(_interval, Unset):
            interval = UNSET
        else:
            interval = Duration.from_dict(_interval)

        start_event_column = d.pop("startEventColumn", UNSET)

        survival = cls(
            type=type,
            num_frames=num_frames,
            duration_column=duration_column,
            end_event_column=end_event_column,
            event_column=event_column,
            event_value=event_value,
            interval=interval,
            start_event_column=start_event_column,
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
