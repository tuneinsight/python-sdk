from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TiqlConcept")


@attr.s(auto_attribs=True)
class TiqlConcept:
    """a concept in the data, i.e. a set of attributes in the data containing one or more records for a statistical unit.

    Attributes:
        description (Union[Unset, str]): user-friendly description for this concept to be shown to the user.
        label (Union[Unset, str]): the displayed name for this concept
        name (Union[Unset, str]): the unique name for this concept.
    """

    description: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        label = self.label
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if label is not UNSET:
            field_dict["label"] = label
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        label = d.pop("label", UNSET)

        name = d.pop("name", UNSET)

        tiql_concept = cls(
            description=description,
            label=label,
            name=name,
        )

        tiql_concept.additional_properties = d
        return tiql_concept

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
