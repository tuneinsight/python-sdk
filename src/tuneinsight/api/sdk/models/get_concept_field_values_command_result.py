from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.data_source_command_result_type import DataSourceCommandResultType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tiql_value import TiqlValue


T = TypeVar("T", bound="GetConceptFieldValuesCommandResult")


@attr.s(auto_attribs=True)
class GetConceptFieldValuesCommandResult:
    """The result of a getConceptFieldValuesCommand datasource command, returning a list of possible values.

    Attributes:
        type (DataSourceCommandResultType): List of output types and structures of datasource commands.
        info (Union[Unset, str]): additional information and context about the command result.
        query (Union[Unset, str]): the query that was executed as part of the datasource command.
        values (Union[Unset, List['TiqlValue']]): the value that this concept can take.
    """

    type: DataSourceCommandResultType
    info: Union[Unset, str] = UNSET
    query: Union[Unset, str] = UNSET
    values: Union[Unset, List["TiqlValue"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        info = self.info
        query = self.query
        values: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()

                values.append(values_item)

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
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tiql_value import TiqlValue

        d = src_dict.copy()
        type = DataSourceCommandResultType(d.pop("type"))

        info = d.pop("info", UNSET)

        query = d.pop("query", UNSET)

        values = []
        _values = d.pop("values", UNSET)
        for values_item_data in _values or []:
            values_item = TiqlValue.from_dict(values_item_data)

            values.append(values_item)

        get_concept_field_values_command_result = cls(
            type=type,
            info=info,
            query=query,
            values=values,
        )

        get_concept_field_values_command_result.additional_properties = d
        return get_concept_field_values_command_result

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
