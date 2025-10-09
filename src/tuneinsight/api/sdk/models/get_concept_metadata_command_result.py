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
        field (Union[Unset, List['TiqlField']]):
    """

    type: DataSourceCommandResultType
    info: Union[Unset, str] = UNSET
    query: Union[Unset, str] = UNSET
    concept: Union[Unset, "TiqlConcept"] = UNSET
    field: Union[Unset, List["TiqlField"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        info = self.info
        query = self.query
        concept: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.concept, Unset):
            concept = self.concept.to_dict()

        field: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.field, Unset):
            field = []
            for field_item_data in self.field:
                field_item = field_item_data.to_dict()

                field.append(field_item)

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
        if field is not UNSET:
            field_dict["field"] = field

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

        field = []
        _field = d.pop("field", UNSET)
        for field_item_data in _field or []:
            field_item = TiqlField.from_dict(field_item_data)

            field.append(field_item)

        get_concept_metadata_command_result = cls(
            type=type,
            info=info,
            query=query,
            concept=concept,
            field=field,
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
