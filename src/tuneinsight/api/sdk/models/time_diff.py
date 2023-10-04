from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.preprocessing_operation_type import PreprocessingOperationType
from ..models.time_unit import TimeUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="TimeDiff")


@attr.s(auto_attribs=True)
class TimeDiff:
    """
    Attributes:
        type (PreprocessingOperationType): type of preprocessing operation
        filter_na (Union[Unset, bool]): whether or not to filter null values
        output (Union[Unset, str]): the output column that stores the numerical values for the time difference
        start (Union[Unset, str]): column that contains timestamps representing the start of the measured difference
        unit (Union[Unset, TimeUnit]): encoded unit of time
        end (Union[Unset, str]): column that contains timestamps representing the end of the measured difference
    """

    type: PreprocessingOperationType
    filter_na: Union[Unset, bool] = UNSET
    output: Union[Unset, str] = UNSET
    start: Union[Unset, str] = UNSET
    unit: Union[Unset, TimeUnit] = UNSET
    end: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        filter_na = self.filter_na
        output = self.output
        start = self.start
        unit: Union[Unset, str] = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit.value

        end = self.end

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if filter_na is not UNSET:
            field_dict["filterNA"] = filter_na
        if output is not UNSET:
            field_dict["output"] = output
        if start is not UNSET:
            field_dict["start"] = start
        if unit is not UNSET:
            field_dict["unit"] = unit
        if end is not UNSET:
            field_dict["end"] = end

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        filter_na = d.pop("filterNA", UNSET)

        output = d.pop("output", UNSET)

        start = d.pop("start", UNSET)

        _unit = d.pop("unit", UNSET)
        unit: Union[Unset, TimeUnit]
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = TimeUnit(_unit)

        end = d.pop("end", UNSET)

        time_diff = cls(
            type=type,
            filter_na=filter_na,
            output=output,
            start=start,
            unit=unit,
            end=end,
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
