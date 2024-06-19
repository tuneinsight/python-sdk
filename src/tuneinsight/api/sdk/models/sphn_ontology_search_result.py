from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SphnOntologySearchResult")


@attr.s(auto_attribs=True)
class SphnOntologySearchResult:
    """Definition of an ontology search result

    Attributes:
        breadcrumb (Union[Unset, str]):
        code (Union[Unset, str]):
        description (Union[Unset, str]):
        name (Union[Unset, str]):
    """

    breadcrumb: Union[Unset, str] = UNSET
    code: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        breadcrumb = self.breadcrumb
        code = self.code
        description = self.description
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if breadcrumb is not UNSET:
            field_dict["breadcrumb"] = breadcrumb
        if code is not UNSET:
            field_dict["code"] = code
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        breadcrumb = d.pop("breadcrumb", UNSET)

        code = d.pop("code", UNSET)

        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        sphn_ontology_search_result = cls(
            breadcrumb=breadcrumb,
            code=code,
            description=description,
            name=name,
        )

        sphn_ontology_search_result.additional_properties = d
        return sphn_ontology_search_result

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
