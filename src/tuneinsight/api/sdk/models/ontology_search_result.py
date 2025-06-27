from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OntologySearchResult")


@attr.s(auto_attribs=True)
class OntologySearchResult:
    """Definition of an ontology search result

    Attributes:
        breadcrumb (Union[Unset, str]):
        children (Union[Unset, str]):
        code (Union[Unset, str]):
        description (Union[Unset, str]):
        level (Union[Unset, float]):
        name (Union[Unset, str]):
        occurrence (Union[Unset, None, float]):
        occurrence_network (Union[Unset, None, float]):
        ontology (Union[Unset, str]):
        parents (Union[Unset, str]):
        uri (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    breadcrumb: Union[Unset, str] = UNSET
    children: Union[Unset, str] = UNSET
    code: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    level: Union[Unset, float] = UNSET
    name: Union[Unset, str] = UNSET
    occurrence: Union[Unset, None, float] = UNSET
    occurrence_network: Union[Unset, None, float] = UNSET
    ontology: Union[Unset, str] = UNSET
    parents: Union[Unset, str] = UNSET
    uri: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        breadcrumb = self.breadcrumb
        children = self.children
        code = self.code
        description = self.description
        level = self.level
        name = self.name
        occurrence = self.occurrence
        occurrence_network = self.occurrence_network
        ontology = self.ontology
        parents = self.parents
        uri = self.uri
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if breadcrumb is not UNSET:
            field_dict["breadcrumb"] = breadcrumb
        if children is not UNSET:
            field_dict["children"] = children
        if code is not UNSET:
            field_dict["code"] = code
        if description is not UNSET:
            field_dict["description"] = description
        if level is not UNSET:
            field_dict["level"] = level
        if name is not UNSET:
            field_dict["name"] = name
        if occurrence is not UNSET:
            field_dict["occurrence"] = occurrence
        if occurrence_network is not UNSET:
            field_dict["occurrenceNetwork"] = occurrence_network
        if ontology is not UNSET:
            field_dict["ontology"] = ontology
        if parents is not UNSET:
            field_dict["parents"] = parents
        if uri is not UNSET:
            field_dict["uri"] = uri
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        breadcrumb = d.pop("breadcrumb", UNSET)

        children = d.pop("children", UNSET)

        code = d.pop("code", UNSET)

        description = d.pop("description", UNSET)

        level = d.pop("level", UNSET)

        name = d.pop("name", UNSET)

        occurrence = d.pop("occurrence", UNSET)

        occurrence_network = d.pop("occurrenceNetwork", UNSET)

        ontology = d.pop("ontology", UNSET)

        parents = d.pop("parents", UNSET)

        uri = d.pop("uri", UNSET)

        version = d.pop("version", UNSET)

        ontology_search_result = cls(
            breadcrumb=breadcrumb,
            children=children,
            code=code,
            description=description,
            level=level,
            name=name,
            occurrence=occurrence,
            occurrence_network=occurrence_network,
            ontology=ontology,
            parents=parents,
            uri=uri,
            version=version,
        )

        ontology_search_result.additional_properties = d
        return ontology_search_result

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
