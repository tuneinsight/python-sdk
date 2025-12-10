from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ontology_search_result import OntologySearchResult


T = TypeVar("T", bound="TiqlValue")


@attr.s(auto_attribs=True)
class TiqlValue:
    """a possible value that a field can take.

    Attributes:
        terminology (Union[Unset, OntologySearchResult]): Definition of an ontology search result
        value (Union[Unset, str]): the string representation of a value for this field.
    """

    terminology: Union[Unset, "OntologySearchResult"] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        terminology: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.terminology, Unset):
            terminology = self.terminology.to_dict()

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if terminology is not UNSET:
            field_dict["terminology"] = terminology
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ontology_search_result import OntologySearchResult

        d = src_dict.copy()
        _terminology = d.pop("terminology", UNSET)
        terminology: Union[Unset, OntologySearchResult]
        if isinstance(_terminology, Unset):
            terminology = UNSET
        else:
            terminology = OntologySearchResult.from_dict(_terminology)

        value = d.pop("value", UNSET)

        tiql_value = cls(
            terminology=terminology,
            value=value,
        )

        tiql_value.additional_properties = d
        return tiql_value

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
