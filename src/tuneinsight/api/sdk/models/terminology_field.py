from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.terminology_reference_type import TerminologyReferenceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vocabulary import Vocabulary


T = TypeVar("T", bound="TerminologyField")


@attr.s(auto_attribs=True)
class TerminologyField:
    """Parameters that must be provided to schema fields when the field's values are terminology references.

    Attributes:
        reference_method (Union[Unset, TerminologyReferenceType]): enumeration of methods that can be used to find the
            terminology associated with a value, i.e., what part of the ontology is used in the data (human-readable name,
            standard code, or URI).
        vocabularies (Union[Unset, List['Vocabulary']]): the list of accepted vocabularies that can be referenced by the
            field.
    """

    reference_method: Union[Unset, TerminologyReferenceType] = UNSET
    vocabularies: Union[Unset, List["Vocabulary"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reference_method: Union[Unset, str] = UNSET
        if not isinstance(self.reference_method, Unset):
            reference_method = self.reference_method.value

        vocabularies: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.vocabularies, Unset):
            vocabularies = []
            for vocabularies_item_data in self.vocabularies:
                vocabularies_item = vocabularies_item_data.to_dict()

                vocabularies.append(vocabularies_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reference_method is not UNSET:
            field_dict["referenceMethod"] = reference_method
        if vocabularies is not UNSET:
            field_dict["vocabularies"] = vocabularies

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.vocabulary import Vocabulary

        d = src_dict.copy()
        _reference_method = d.pop("referenceMethod", UNSET)
        reference_method: Union[Unset, TerminologyReferenceType]
        if isinstance(_reference_method, Unset):
            reference_method = UNSET
        else:
            reference_method = TerminologyReferenceType(_reference_method)

        vocabularies = []
        _vocabularies = d.pop("vocabularies", UNSET)
        for vocabularies_item_data in _vocabularies or []:
            vocabularies_item = Vocabulary.from_dict(vocabularies_item_data)

            vocabularies.append(vocabularies_item)

        terminology_field = cls(
            reference_method=reference_method,
            vocabularies=vocabularies,
        )

        terminology_field.additional_properties = d
        return terminology_field

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
