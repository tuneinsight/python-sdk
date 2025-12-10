from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Vocabulary")


@attr.s(auto_attribs=True)
class Vocabulary:
    """object that identifies a terminology vocabulary.

    Attributes:
        name (Union[Unset, str]): name of the vocabulary (ICD10, SNOMED, LOINC,...)
        version (Union[Unset, str]): version of the vocabulary.
    """

    name: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        version = d.pop("version", UNSET)

        vocabulary = cls(
            name=name,
            version=version,
        )

        vocabulary.additional_properties = d
        return vocabulary

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
