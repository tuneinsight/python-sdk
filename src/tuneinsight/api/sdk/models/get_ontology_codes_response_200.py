from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ontology_search_result import OntologySearchResult


T = TypeVar("T", bound="GetOntologyCodesResponse200")


@attr.s(auto_attribs=True)
class GetOntologyCodesResponse200:
    """
    Attributes:
        results (Union[Unset, List['OntologySearchResult']]):
        total (Union[Unset, int]):
    """

    results: Union[Unset, List["OntologySearchResult"]] = UNSET
    total: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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
        if results is not UNSET:
            field_dict["results"] = results
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ontology_search_result import OntologySearchResult

        d = src_dict.copy()
        results = []
        _results = d.pop("results", UNSET)
        for results_item_data in _results or []:
            results_item = OntologySearchResult.from_dict(results_item_data)

            results.append(results_item)

        total = d.pop("total", UNSET)

        get_ontology_codes_response_200 = cls(
            results=results,
            total=total,
        )

        get_ontology_codes_response_200.additional_properties = d
        return get_ontology_codes_response_200

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
