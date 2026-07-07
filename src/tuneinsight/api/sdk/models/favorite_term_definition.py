from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="FavoriteTermDefinition")


@attr.s(auto_attribs=True)
class FavoriteTermDefinition:
    """fields of a favorite term.

    Attributes:
        description (Union[Unset, str]): optional description for the favorite term.
        name (Union[Unset, str]): optional name of the favorite term.
        term_id (Union[Unset, str]): ID of the favorited ontology term.
    """

    description: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    term_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        name = self.name
        term_id = self.term_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if term_id is not UNSET:
            field_dict["termID"] = term_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        term_id = d.pop("termID", UNSET)

        favorite_term_definition = cls(
            description=description,
            name=name,
            term_id=term_id,
        )

        favorite_term_definition.additional_properties = d
        return favorite_term_definition

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
