from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryOutputVariable")


@attr.s(auto_attribs=True)
class QueryOutputVariable:
    """represents a variable/field of the table that is output from a cross-standard query.

    Attributes:
        name (Union[Unset, str]): The name of the variable to extract
        series (Union[Unset, str]): The series containing this variable
        type (Union[Unset, str]): The type of the variable to extract (e.g., string, integer, date, etc.)
    """

    name: Union[Unset, str] = UNSET
    series: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        series = self.series
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if series is not UNSET:
            field_dict["series"] = series
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        series = d.pop("series", UNSET)

        type = d.pop("type", UNSET)

        query_output_variable = cls(
            name=name,
            series=series,
            type=type,
        )

        query_output_variable.additional_properties = d
        return query_output_variable

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
