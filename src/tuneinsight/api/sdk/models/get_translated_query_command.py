from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.data_source_command_type import DataSourceCommandType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_source_query import DataSourceQuery


T = TypeVar("T", bound="GetTranslatedQueryCommand")


@attr.s(auto_attribs=True)
class GetTranslatedQueryCommand:
    """This command returns the translated query string for a given TIQL query.

    Attributes:
        type (DataSourceCommandType): List of datasource commands that can be performed.
        query (Union[Unset, DataSourceQuery]): schema used for the query
    """

    type: DataSourceCommandType
    query: Union[Unset, "DataSourceQuery"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        query: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.query, Unset):
            query = self.query.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if query is not UNSET:
            field_dict["query"] = query

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_source_query import DataSourceQuery

        d = src_dict.copy()
        type = DataSourceCommandType(d.pop("type"))

        _query = d.pop("query", UNSET)
        query: Union[Unset, DataSourceQuery]
        if isinstance(_query, Unset):
            query = UNSET
        else:
            query = DataSourceQuery.from_dict(_query)

        get_translated_query_command = cls(
            type=type,
            query=query,
        )

        get_translated_query_command.additional_properties = d
        return get_translated_query_command

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
