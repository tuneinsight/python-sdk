from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.data_source_command_result_type import DataSourceCommandResultType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DataSourceCommandResult")


@attr.s(auto_attribs=True)
class DataSourceCommandResult:
    """Abstract subclass representing the output of a datasource command.

    Attributes:
        type (DataSourceCommandResultType): List of output types and structures of datasource commands.
        info (Union[Unset, str]): additional information and context about the command result.
        query (Union[Unset, str]): the query that was executed as part of the datasource command.
    """

    type: DataSourceCommandResultType
    info: Union[Unset, str] = UNSET
    query: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        info = self.info
        query = self.query

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if info is not UNSET:
            field_dict["info"] = info
        if query is not UNSET:
            field_dict["query"] = query

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = DataSourceCommandResultType(d.pop("type"))

        info = d.pop("info", UNSET)

        query = d.pop("query", UNSET)

        data_source_command_result = cls(
            type=type,
            info=info,
            query=query,
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
