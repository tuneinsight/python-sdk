from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.data_source_command_result_type import DataSourceCommandResultType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tiql_concept import TiqlConcept


T = TypeVar("T", bound="GetMetadataCommandResult")


@attr.s(auto_attribs=True)
class GetMetadataCommandResult:
    """The result of a getMetadata datasource command, returning the metadata of a datasource.

    Attributes:
        type (DataSourceCommandResultType): List of output types and structures of datasource commands.
        info (Union[Unset, str]): additional information and context about the command result.
        query (Union[Unset, str]): the query that was executed as part of the datasource command.
        concepts (Union[Unset, List['TiqlConcept']]): The list of all named concepts in this datasource.
    """

    type: DataSourceCommandResultType
    info: Union[Unset, str] = UNSET
    query: Union[Unset, str] = UNSET
    concepts: Union[Unset, List["TiqlConcept"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        info = self.info
        query = self.query
        concepts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.concepts, Unset):
            concepts = []
            for concepts_item_data in self.concepts:
                concepts_item = concepts_item_data.to_dict()

                concepts.append(concepts_item)

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
        if concepts is not UNSET:
            field_dict["concepts"] = concepts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tiql_concept import TiqlConcept

        d = src_dict.copy()
        type = DataSourceCommandResultType(d.pop("type"))

        info = d.pop("info", UNSET)

        query = d.pop("query", UNSET)

        concepts = []
        _concepts = d.pop("concepts", UNSET)
        for concepts_item_data in _concepts or []:
            concepts_item = TiqlConcept.from_dict(concepts_item_data)

            concepts.append(concepts_item)

        get_metadata_command_result = cls(
            type=type,
            info=info,
            query=query,
            concepts=concepts,
        )

        get_metadata_command_result.additional_properties = d
        return get_metadata_command_result

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
