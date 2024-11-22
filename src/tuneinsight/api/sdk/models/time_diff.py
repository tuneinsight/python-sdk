from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.preprocessing_operation_type import PreprocessingOperationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.duration import Duration


T = TypeVar("T", bound="TimeDiff")


@attr.s(auto_attribs=True)
class TimeDiff:
    """
    Attributes:
        type (PreprocessingOperationType): type of preprocessing operation
        end_column (Union[Unset, str]): column that contains timestamps representing the end of the measured difference
        filter_na (Union[Unset, bool]): whether or not to filter null values
        interval (Union[Unset, Duration]): definition of a date-independent time interval
        output_column (Union[Unset, str]): the output column that stores the numerical values for the time difference
            (if not specified, "duration" is used)
        start_column (Union[Unset, str]): column that contains timestamps representing the start of the measured
            difference
    """

    type: PreprocessingOperationType
    end_column: Union[Unset, str] = UNSET
    filter_na: Union[Unset, bool] = UNSET
    interval: Union[Unset, "Duration"] = UNSET
    output_column: Union[Unset, str] = UNSET
    start_column: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        end_column = self.end_column
        filter_na = self.filter_na
        interval: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.interval, Unset):
            interval = self.interval.to_dict()

        output_column = self.output_column
        start_column = self.start_column

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if end_column is not UNSET:
            field_dict["endColumn"] = end_column
        if filter_na is not UNSET:
            field_dict["filterNA"] = filter_na
        if interval is not UNSET:
            field_dict["interval"] = interval
        if output_column is not UNSET:
            field_dict["outputColumn"] = output_column
        if start_column is not UNSET:
            field_dict["startColumn"] = start_column

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.duration import Duration

        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        end_column = d.pop("endColumn", UNSET)

        filter_na = d.pop("filterNA", UNSET)

        _interval = d.pop("interval", UNSET)
        interval: Union[Unset, Duration]
        if isinstance(_interval, Unset):
            interval = UNSET
        else:
            interval = Duration.from_dict(_interval)

        output_column = d.pop("outputColumn", UNSET)

        start_column = d.pop("startColumn", UNSET)

        time_diff = cls(
            type=type,
            end_column=end_column,
            filter_na=filter_na,
            interval=interval,
            output_column=output_column,
            start_column=start_column,
        )

        time_diff.additional_properties = d
        return time_diff

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
