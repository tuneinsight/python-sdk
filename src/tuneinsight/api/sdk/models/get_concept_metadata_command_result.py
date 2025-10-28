from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.data_source_command_result_type import DataSourceCommandResultType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tiql_concept import TiqlConcept
    from ..models.tiql_field import TiqlField


T = TypeVar("T", bound="GetConceptMetadataCommandResult")


@attr.s(auto_attribs=True)
class GetConceptMetadataCommandResult:
    """The result of a getConceptMetadata datasource command, returning the metadata of a concept variable.

    Attributes:
        type (DataSourceCommandResultType): List of output types and structures of datasource commands.
        info (Union[Unset, str]): additional information and context about the command result.
        query (Union[Unset, str]): the query that was executed as part of the datasource command.
        concept (Union[Unset, TiqlConcept]): a concept in the data, i.e. a set of attributes in the data containing one
            or more records for a statistical unit.
        fields (Union[Unset, List['TiqlField']]):
    """

    type: DataSourceCommandResultType
    info: Union[Unset, str] = UNSET
    query: Union[Unset, str] = UNSET
    concept: Union[Unset, "TiqlConcept"] = UNSET
    fields: Union[Unset, List["TiqlField"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        info = self.info
        query = self.query
        concept: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.concept, Unset):
            concept = self.concept.to_dict()

        fields: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()

                fields.append(fields_item)

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
        if concept is not UNSET:
            field_dict["concept"] = concept
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tiql_concept import TiqlConcept
        from ..models.tiql_field import TiqlField

        d = src_dict.copy()
        type = DataSourceCommandResultType(d.pop("type"))

        info = d.pop("info", UNSET)

        query = d.pop("query", UNSET)

        _concept = d.pop("concept", UNSET)
        concept: Union[Unset, TiqlConcept]
        if isinstance(_concept, Unset):
            concept = UNSET
        else:
            concept = TiqlConcept.from_dict(_concept)

        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = TiqlField.from_dict(fields_item_data)

            fields.append(fields_item)

        get_concept_metadata_command_result = cls(
            type=type,
            info=info,
            query=query,
            concept=concept,
            fields=fields,
        )

        get_concept_metadata_command_result.additional_properties = d
        return get_concept_metadata_command_result

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
