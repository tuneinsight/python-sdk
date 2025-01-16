from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_source_command_result_result_item import DataSourceCommandResultResultItem


T = TypeVar("T", bound="DataSourceCommandResult")


@attr.s(auto_attribs=True)
class DataSourceCommandResult:
    """Command result.

    Attributes:
        query (Union[Unset, str]):
        result (Union[Unset, List['DataSourceCommandResultResultItem']]):
    """

    query: Union[Unset, str] = UNSET
    result: Union[Unset, List["DataSourceCommandResultResultItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        query = self.query
        result: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.result, Unset):
            result = []
            for result_item_data in self.result:
                result_item = result_item_data.to_dict()

                result.append(result_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if query is not UNSET:
            field_dict["query"] = query
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_source_command_result_result_item import DataSourceCommandResultResultItem

        d = src_dict.copy()
        query = d.pop("query", UNSET)

        result = []
        _result = d.pop("result", UNSET)
        for result_item_data in _result or []:
            result_item = DataSourceCommandResultResultItem.from_dict(result_item_data)

            result.append(result_item)

        data_source_command_result = cls(
            query=query,
            result=result,
        )

        data_source_command_result.additional_properties = d
        return data_source_command_result

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
