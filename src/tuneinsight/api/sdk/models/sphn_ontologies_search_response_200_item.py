from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sphn_ontology_search_result import SphnOntologySearchResult


T = TypeVar("T", bound="SphnOntologiesSearchResponse200Item")


@attr.s(auto_attribs=True)
class SphnOntologiesSearchResponse200Item:
    """
    Attributes:
        ontology (Union[Unset, str]):
        results (Union[Unset, List['SphnOntologySearchResult']]):
        total (Union[Unset, int]):
    """

    ontology: Union[Unset, str] = UNSET
    results: Union[Unset, List["SphnOntologySearchResult"]] = UNSET
    total: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ontology = self.ontology
        results: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()

                results.append(results_item)

        total = self.total

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ontology is not UNSET:
            field_dict["ontology"] = ontology
        if results is not UNSET:
            field_dict["results"] = results
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sphn_ontology_search_result import SphnOntologySearchResult

        d = src_dict.copy()
        ontology = d.pop("ontology", UNSET)

        results = []
        _results = d.pop("results", UNSET)
        for results_item_data in _results or []:
            results_item = SphnOntologySearchResult.from_dict(results_item_data)

            results.append(results_item)

        total = d.pop("total", UNSET)

        sphn_ontologies_search_response_200_item = cls(
            ontology=ontology,
            results=results,
            total=total,
        )

        sphn_ontologies_search_response_200_item.additional_properties = d
        return sphn_ontologies_search_response_200_item

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
