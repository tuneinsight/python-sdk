from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.group_by_type import GroupByType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupInfo")


@attr.s(auto_attribs=True)
class GroupInfo:
    """information about a column representing a subset of rows in the final result

    Attributes:
        category (Union[Unset, str]): when a group reflects a categorical value, the identifier for this category
        group_by_type (Union[Unset, GroupByType]): type of the groupBy operation specified
        origin_column (Union[Unset, str]): original column from which the group assignment was made
    """

    category: Union[Unset, str] = UNSET
    group_by_type: Union[Unset, GroupByType] = UNSET
    origin_column: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        category = self.category
        group_by_type: Union[Unset, str] = UNSET
        if not isinstance(self.group_by_type, Unset):
            group_by_type = self.group_by_type.value

        origin_column = self.origin_column

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if group_by_type is not UNSET:
            field_dict["groupByType"] = group_by_type
        if origin_column is not UNSET:
            field_dict["originColumn"] = origin_column

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        category = d.pop("category", UNSET)

        _group_by_type = d.pop("groupByType", UNSET)
        group_by_type: Union[Unset, GroupByType]
        if isinstance(_group_by_type, Unset):
            group_by_type = UNSET
        else:
            group_by_type = GroupByType(_group_by_type)

        origin_column = d.pop("originColumn", UNSET)

        group_info = cls(
            category=category,
            group_by_type=group_by_type,
            origin_column=origin_column,
        )

        group_info.additional_properties = d
        return group_info

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
