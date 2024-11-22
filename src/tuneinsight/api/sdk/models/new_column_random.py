from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewColumnRandom")


@attr.s(auto_attribs=True)
class NewColumnRandom:
    """if specified, the column is filled with random normal values.

    Attributes:
        loc (Union[Unset, float]): the mean of the normal
        scale (Union[Unset, float]): the standard deviation of the normal Default: 1.0.
    """

    loc: Union[Unset, float] = 0.0
    scale: Union[Unset, float] = 1.0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        loc = self.loc
        scale = self.scale

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if loc is not UNSET:
            field_dict["loc"] = loc
        if scale is not UNSET:
            field_dict["scale"] = scale

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        loc = d.pop("loc", UNSET)

        scale = d.pop("scale", UNSET)

        new_column_random = cls(
            loc=loc,
            scale=scale,
        )

        new_column_random.additional_properties = d
        return new_column_random

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
