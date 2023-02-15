from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.column_info import ColumnInfo


T = TypeVar("T", bound="ResultContextualInfo")


@attr.s(auto_attribs=True)
class ResultContextualInfo:
    """contextual information about the content retrieved

    Attributes:
        columns_info (Union[Unset, List['ColumnInfo']]): columns description
    """

    columns_info: Union[Unset, List["ColumnInfo"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        columns_info: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.columns_info, Unset):
            columns_info = []
            for columns_info_item_data in self.columns_info:
                columns_info_item = columns_info_item_data.to_dict()

                columns_info.append(columns_info_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if columns_info is not UNSET:
            field_dict["columnsInfo"] = columns_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.column_info import ColumnInfo

        d = src_dict.copy()
        columns_info = []
        _columns_info = d.pop("columnsInfo", UNSET)
        for columns_info_item_data in _columns_info or []:
            columns_info_item = ColumnInfo.from_dict(columns_info_item_data)

            columns_info.append(columns_info_item)

        result_contextual_info = cls(
            columns_info=columns_info,
        )

        result_contextual_info.additional_properties = d
        return result_contextual_info

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
