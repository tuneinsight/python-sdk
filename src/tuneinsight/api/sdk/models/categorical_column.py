from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CategoricalColumn")


@attr.s(auto_attribs=True)
class CategoricalColumn:
    """definition of a column in a dataset with categorical data specifying expected values

    Attributes:
        name (Union[Unset, str]): name of the column
        other_label (Union[Unset, str]): label to give to values that do not fall into the values array Default:
            'other'.
        values (Union[Unset, List[str]]): list of string values to find in the column
    """

    name: Union[Unset, str] = UNSET
    other_label: Union[Unset, str] = "other"
    values: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        other_label = self.other_label
        values: Union[Unset, List[str]] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if other_label is not UNSET:
            field_dict["otherLabel"] = other_label
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        other_label = d.pop("otherLabel", UNSET)

        values = cast(List[str], d.pop("values", UNSET))

        categorical_column = cls(
            name=name,
            other_label=other_label,
            values=values,
        )

        categorical_column.additional_properties = d
        return categorical_column

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
