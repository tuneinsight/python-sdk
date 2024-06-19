from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ColumnProperties")


@attr.s(auto_attribs=True)
class ColumnProperties:
    """properties related to a selected column in a dataset.

    Attributes:
        lower_bound (Union[Unset, float]): optional minimum value the values in the column can take (used only when
            clipping for differential privacy)
        name (Union[Unset, str]): name of the column in the dataset.
        upper_bound (Union[Unset, float]): optional maximum value the values in the column can take (used only when
            clipping for differential privacy)
    """

    lower_bound: Union[Unset, float] = UNSET
    name: Union[Unset, str] = UNSET
    upper_bound: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        lower_bound = self.lower_bound
        name = self.name
        upper_bound = self.upper_bound

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lower_bound is not UNSET:
            field_dict["lowerBound"] = lower_bound
        if name is not UNSET:
            field_dict["name"] = name
        if upper_bound is not UNSET:
            field_dict["upperBound"] = upper_bound

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        lower_bound = d.pop("lowerBound", UNSET)

        name = d.pop("name", UNSET)

        upper_bound = d.pop("upperBound", UNSET)

        column_properties = cls(
            lower_bound=lower_bound,
            name=name,
            upper_bound=upper_bound,
        )

        column_properties.additional_properties = d
        return column_properties

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
