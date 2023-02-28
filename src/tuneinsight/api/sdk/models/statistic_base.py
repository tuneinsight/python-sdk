from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.filter_ import Filter
from ..types import UNSET, Unset

T = TypeVar("T", bound="StatisticBase")


@attr.s(auto_attribs=True)
class StatisticBase:
    """common information of a computed statistic

    Attributes:
        filter_ (Union[Unset, Filter]):
        name (Union[Unset, str]): given name of the statistic
        variable (Union[Unset, str]): target variable in the dataset from the which the statistic is computed
    """

    filter_: Union[Unset, Filter] = UNSET
    name: Union[Unset, str] = UNSET
    variable: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        filter_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        name = self.name
        variable = self.variable

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if name is not UNSET:
            field_dict["name"] = name
        if variable is not UNSET:
            field_dict["variable"] = variable

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _filter_ = d.pop("filter", UNSET)
        filter_: Union[Unset, Filter]
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = Filter.from_dict(_filter_)

        name = d.pop("name", UNSET)

        variable = d.pop("variable", UNSET)

        statistic_base = cls(
            filter_=filter_,
            name=name,
            variable=variable,
        )

        statistic_base.additional_properties = d
        return statistic_base

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
