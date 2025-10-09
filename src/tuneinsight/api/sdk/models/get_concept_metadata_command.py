from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.data_source_command_type import DataSourceCommandType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetConceptMetadataCommand")


@attr.s(auto_attribs=True)
class GetConceptMetadataCommand:
    """This command returns metadata for a concept in the datasource, including a text description
    of the concept and the list and types of fields available on this concept. If the concept
    is empty, this instead returns all fields directly associated with the user record (core concept).

        Attributes:
            type (DataSourceCommandType): List of datasource commands that can be performed.
            concept (Union[Unset, str]): A string uniquely representing the concept for which the metadata is fetched.
                If left empty, the variable is assumed to be a field directly associated with the record.
    """

    type: DataSourceCommandType
    concept: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        concept = self.concept

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if concept is not UNSET:
            field_dict["concept"] = concept

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = DataSourceCommandType(d.pop("type"))

        concept = d.pop("concept", UNSET)

        get_concept_metadata_command = cls(
            type=type,
            concept=concept,
        )

        get_concept_metadata_command.additional_properties = d
        return get_concept_metadata_command

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
