from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.data_source_command_type import DataSourceCommandType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetConceptFieldValuesCommand")


@attr.s(auto_attribs=True)
class GetConceptFieldValuesCommand:
    """This command searches for acceptable values for a specific field of a concept. It should be used to
    provide suggestions for values input by the user.

        Attributes:
            type (DataSourceCommandType): List of datasource commands that can be performed.
            concept (Union[Unset, str]): A string uniquely representing the concept that the field retrieved is a part of.
                If left empty, the field is assumed to be directly associated with the record.
            field (Union[Unset, str]): A string uniquely representing the field for which values are search. If concept is
                provided, this field is taken in the context of that concept.
            max_results (Union[Unset, int]): The maximum number of values to return (100 by default).
            search_string (Union[Unset, str]): A partial string input by the user, used to filter results.
    """

    type: DataSourceCommandType
    concept: Union[Unset, str] = UNSET
    field: Union[Unset, str] = UNSET
    max_results: Union[Unset, int] = UNSET
    search_string: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        concept = self.concept
        field = self.field
        max_results = self.max_results
        search_string = self.search_string

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if concept is not UNSET:
            field_dict["concept"] = concept
        if field is not UNSET:
            field_dict["field"] = field
        if max_results is not UNSET:
            field_dict["maxResults"] = max_results
        if search_string is not UNSET:
            field_dict["searchString"] = search_string

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = DataSourceCommandType(d.pop("type"))

        concept = d.pop("concept", UNSET)

        field = d.pop("field", UNSET)

        max_results = d.pop("maxResults", UNSET)

        search_string = d.pop("searchString", UNSET)

        get_concept_field_values_command = cls(
            type=type,
            concept=concept,
            field=field,
            max_results=max_results,
            search_string=search_string,
        )

        get_concept_field_values_command.additional_properties = d
        return get_concept_field_values_command

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
