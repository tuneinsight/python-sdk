from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.column_info_scope import ColumnInfoScope
from ..models.column_info_value_type import ColumnInfoValueType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_info import GroupInfo


T = TypeVar("T", bound="ColumnInfo")


@attr.s(auto_attribs=True)
class ColumnInfo:
    """contextual information about a column of the resulting matrix

    Attributes:
        group_info (Union[Unset, GroupInfo]): information about a column representing a subset of rows in the final
            result
        origin_column (Union[Unset, str]): names of the column from which the value is computed
        origin_value (Union[Unset, str]): when originColumn is a categorical column, original value for the count
        scope (Union[Unset, ColumnInfoScope]): row set involved in the result, all for all rows, subgroup for a subset
            depending on a group
        value_type (Union[Unset, ColumnInfoValueType]): type of value stored in the column, can either be a count of
            rows or a sum of values
    """

    group_info: Union[Unset, "GroupInfo"] = UNSET
    origin_column: Union[Unset, str] = UNSET
    origin_value: Union[Unset, str] = UNSET
    scope: Union[Unset, ColumnInfoScope] = UNSET
    value_type: Union[Unset, ColumnInfoValueType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        group_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.group_info, Unset):
            group_info = self.group_info.to_dict()

        origin_column = self.origin_column
        origin_value = self.origin_value
        scope: Union[Unset, str] = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.value

        value_type: Union[Unset, str] = UNSET
        if not isinstance(self.value_type, Unset):
            value_type = self.value_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_info is not UNSET:
            field_dict["groupInfo"] = group_info
        if origin_column is not UNSET:
            field_dict["originColumn"] = origin_column
        if origin_value is not UNSET:
            field_dict["originValue"] = origin_value
        if scope is not UNSET:
            field_dict["scope"] = scope
        if value_type is not UNSET:
            field_dict["valueType"] = value_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.group_info import GroupInfo

        d = src_dict.copy()
        _group_info = d.pop("groupInfo", UNSET)
        group_info: Union[Unset, GroupInfo]
        if isinstance(_group_info, Unset):
            group_info = UNSET
        else:
            group_info = GroupInfo.from_dict(_group_info)

        origin_column = d.pop("originColumn", UNSET)

        origin_value = d.pop("originValue", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: Union[Unset, ColumnInfoScope]
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = ColumnInfoScope(_scope)

        _value_type = d.pop("valueType", UNSET)
        value_type: Union[Unset, ColumnInfoValueType]
        if isinstance(_value_type, Unset):
            value_type = UNSET
        else:
            value_type = ColumnInfoValueType(_value_type)

        column_info = cls(
            group_info=group_info,
            origin_column=origin_column,
            origin_value=origin_value,
            scope=scope,
            value_type=value_type,
        )

        column_info.additional_properties = d
        return column_info

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
