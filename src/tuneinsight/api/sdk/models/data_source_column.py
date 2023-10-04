from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.column_type_group import ColumnTypeGroup
from ..types import UNSET, Unset

T = TypeVar("T", bound="DataSourceColumn")


@attr.s(auto_attribs=True)
class DataSourceColumn:
    """column of a datasource includes name and type

    Attributes:
        type_group (Union[Unset, ColumnTypeGroup]): represents a type group indicating the way the data may actually be
            processed
        name (Union[Unset, str]):
        type (Union[Unset, str]):
    """

    type_group: Union[Unset, ColumnTypeGroup] = UNSET
    name: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type_group: Union[Unset, str] = UNSET
        if not isinstance(self.type_group, Unset):
            type_group = self.type_group.value

        name = self.name
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_group is not UNSET:
            field_dict["typeGroup"] = type_group
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type_group = d.pop("typeGroup", UNSET)
        type_group: Union[Unset, ColumnTypeGroup]
        if isinstance(_type_group, Unset):
            type_group = UNSET
        else:
            type_group = ColumnTypeGroup(_type_group)

        name = d.pop("name", UNSET)

        type = d.pop("type", UNSET)

        data_source_column = cls(
            type_group=type_group,
            name=name,
            type=type,
        )

        data_source_column.additional_properties = d
        return data_source_column

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
