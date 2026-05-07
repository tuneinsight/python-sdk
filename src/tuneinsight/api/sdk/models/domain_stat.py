from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainStat")


@attr.s(auto_attribs=True)
class DomainStat:
    """Concept coverage statistics for a single domain.

    Attributes:
        domain (Union[Unset, str]): the domain name.
        label (Union[Unset, str]): the label for this domain
        patient_count (Union[Unset, int]): number of distinct patients with at least one record in this domain.
        total_concepts (Union[Unset, int]): total number of concepts in this domain loaded from terminology files.
    """

    domain: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    patient_count: Union[Unset, int] = UNSET
    total_concepts: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        domain = self.domain
        label = self.label
        patient_count = self.patient_count
        total_concepts = self.total_concepts

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if domain is not UNSET:
            field_dict["domain"] = domain
        if label is not UNSET:
            field_dict["label"] = label
        if patient_count is not UNSET:
            field_dict["patientCount"] = patient_count
        if total_concepts is not UNSET:
            field_dict["totalConcepts"] = total_concepts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        domain = d.pop("domain", UNSET)

        label = d.pop("label", UNSET)

        patient_count = d.pop("patientCount", UNSET)

        total_concepts = d.pop("totalConcepts", UNSET)

        domain_stat = cls(
            domain=domain,
            label=label,
            patient_count=patient_count,
            total_concepts=total_concepts,
        )

        domain_stat.additional_properties = d
        return domain_stat

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
