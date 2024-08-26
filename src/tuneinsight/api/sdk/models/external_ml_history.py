from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalMlHistory")


@attr.s(auto_attribs=True)
class ExternalMlHistory:
    """Training history of external ML containing the evolution of the metrics during training

    Attributes:
        end_timestamps (List[List[float]]): Ending timestamps of local training epochs in unix milliseconds timestamps
        metrics (List[str]): Metrics at each round at each local epoch
        start_timestamps (List[List[float]]): Starting timestamps of local training epochs in unix milliseconds
            timestamps
        init_metrics (Union[Unset, List[str]]): Metrics at each round before local training
        init_timestamps (Union[Unset, List[float]]): Init timestamps of local training in unix milliseconds timestamps
    """

    end_timestamps: List[List[float]]
    metrics: List[str]
    start_timestamps: List[List[float]]
    init_metrics: Union[Unset, List[str]] = UNSET
    init_timestamps: Union[Unset, List[float]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        end_timestamps = []
        for end_timestamps_item_data in self.end_timestamps:
            end_timestamps_item = end_timestamps_item_data

            end_timestamps.append(end_timestamps_item)

        metrics = self.metrics

        start_timestamps = []
        for start_timestamps_item_data in self.start_timestamps:
            start_timestamps_item = start_timestamps_item_data

            start_timestamps.append(start_timestamps_item)

        init_metrics: Union[Unset, List[str]] = UNSET
        if not isinstance(self.init_metrics, Unset):
            init_metrics = self.init_metrics

        init_timestamps: Union[Unset, List[float]] = UNSET
        if not isinstance(self.init_timestamps, Unset):
            init_timestamps = self.init_timestamps

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endTimestamps": end_timestamps,
                "metrics": metrics,
                "startTimestamps": start_timestamps,
            }
        )
        if init_metrics is not UNSET:
            field_dict["initMetrics"] = init_metrics
        if init_timestamps is not UNSET:
            field_dict["initTimestamps"] = init_timestamps

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        end_timestamps = []
        _end_timestamps = d.pop("endTimestamps")
        for end_timestamps_item_data in _end_timestamps:
            end_timestamps_item = cast(List[float], end_timestamps_item_data)

            end_timestamps.append(end_timestamps_item)

        metrics = cast(List[str], d.pop("metrics"))

        start_timestamps = []
        _start_timestamps = d.pop("startTimestamps")
        for start_timestamps_item_data in _start_timestamps:
            start_timestamps_item = cast(List[float], start_timestamps_item_data)

            start_timestamps.append(start_timestamps_item)

        init_metrics = cast(List[str], d.pop("initMetrics", UNSET))

        init_timestamps = cast(List[float], d.pop("initTimestamps", UNSET))

        external_ml_history = cls(
            end_timestamps=end_timestamps,
            metrics=metrics,
            start_timestamps=start_timestamps,
            init_metrics=init_metrics,
            init_timestamps=init_timestamps,
        )

        external_ml_history.additional_properties = d
        return external_ml_history

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
