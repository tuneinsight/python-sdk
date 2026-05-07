from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_stat import DomainStat
    from ..models.term_distributions import TermDistributions


T = TypeVar("T", bound="TerminologyStatsResponse")


@attr.s(auto_attribs=True)
class TerminologyStatsResponse:
    """
    Attributes:
        data_source_name (Union[Unset, str]): name of the data source used to build the catalog.
        distributions (Union[Unset, TermDistributions]):
        domain_stats (Union[Unset, List['DomainStat']]):
        origins (Union[Unset, List[str]]): names of the origin instances from which the catalog was built.
        total_concepts (Union[Unset, int]): total count of distinct concepts in the data source.
        total_patients (Union[Unset, int]): total count of distinct patients in the data source.
        updated_at (Union[Unset, str]): last time the catalog was built at.
        vocabulary_stats (Union[Unset, List[str]]):
    """

    data_source_name: Union[Unset, str] = UNSET
    distributions: Union[Unset, "TermDistributions"] = UNSET
    domain_stats: Union[Unset, List["DomainStat"]] = UNSET
    origins: Union[Unset, List[str]] = UNSET
    total_concepts: Union[Unset, int] = UNSET
    total_patients: Union[Unset, int] = UNSET
    updated_at: Union[Unset, str] = UNSET
    vocabulary_stats: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data_source_name = self.data_source_name
        distributions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.distributions, Unset):
            distributions = self.distributions.to_dict()

        domain_stats: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.domain_stats, Unset):
            domain_stats = []
            for domain_stats_item_data in self.domain_stats:
                domain_stats_item = domain_stats_item_data.to_dict()

                domain_stats.append(domain_stats_item)

        origins: Union[Unset, List[str]] = UNSET
        if not isinstance(self.origins, Unset):
            origins = self.origins

        total_concepts = self.total_concepts
        total_patients = self.total_patients
        updated_at = self.updated_at
        vocabulary_stats: Union[Unset, List[str]] = UNSET
        if not isinstance(self.vocabulary_stats, Unset):
            vocabulary_stats = self.vocabulary_stats

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_source_name is not UNSET:
            field_dict["dataSourceName"] = data_source_name
        if distributions is not UNSET:
            field_dict["distributions"] = distributions
        if domain_stats is not UNSET:
            field_dict["domainStats"] = domain_stats
        if origins is not UNSET:
            field_dict["origins"] = origins
        if total_concepts is not UNSET:
            field_dict["totalConcepts"] = total_concepts
        if total_patients is not UNSET:
            field_dict["totalPatients"] = total_patients
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if vocabulary_stats is not UNSET:
            field_dict["vocabularyStats"] = vocabulary_stats

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_stat import DomainStat
        from ..models.term_distributions import TermDistributions

        d = src_dict.copy()
        data_source_name = d.pop("dataSourceName", UNSET)

        _distributions = d.pop("distributions", UNSET)
        distributions: Union[Unset, TermDistributions]
        if isinstance(_distributions, Unset):
            distributions = UNSET
        else:
            distributions = TermDistributions.from_dict(_distributions)

        domain_stats = []
        _domain_stats = d.pop("domainStats", UNSET)
        for domain_stats_item_data in _domain_stats or []:
            domain_stats_item = DomainStat.from_dict(domain_stats_item_data)

            domain_stats.append(domain_stats_item)

        origins = cast(List[str], d.pop("origins", UNSET))

        total_concepts = d.pop("totalConcepts", UNSET)

        total_patients = d.pop("totalPatients", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        vocabulary_stats = cast(List[str], d.pop("vocabularyStats", UNSET))

        terminology_stats_response = cls(
            data_source_name=data_source_name,
            distributions=distributions,
            domain_stats=domain_stats,
            origins=origins,
            total_concepts=total_concepts,
            total_patients=total_patients,
            updated_at=updated_at,
            vocabulary_stats=vocabulary_stats,
        )

        terminology_stats_response.additional_properties = d
        return terminology_stats_response

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
