from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.ontology_type import OntologyType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_stat import DomainStat
    from ..models.term_distributions import TermDistributions


T = TypeVar("T", bound="TerminologyStatsResponse")


@attr.s(auto_attribs=True)
class TerminologyStatsResponse:
    """
    Attributes:
        catalog_vocabularies (Union[Unset, List[OntologyType]]): contains the filtered list of ontologies/vocabularies
            that are loaded, activated and present in the catalog's data from all sources.
        data_source_name (Union[Unset, str]): name of the data source used to build the catalog.
        distributions (Union[Unset, TermDistributions]):
        domain_stats (Union[Unset, List['DomainStat']]):
        enabled_vocabularies (Union[Unset, List[OntologyType]]): contains the filtered list of ontologies/vocabularies
            that are loaded in the instance and activated in the settings.
        loaded_vocabularies (Union[Unset, List[OntologyType]]): contains the list of ontologies/vocabularies that have
            been loaded in the instance.
        origins (Union[Unset, List[str]]): names of the origin instances from which the catalog was built.
        total_concepts (Union[Unset, int]): total count of distinct concepts in the data source.
        total_patients (Union[Unset, int]): total count of distinct patients in the data source.
        updated_at (Union[Unset, str]): last time the catalog was built at.
    """

    catalog_vocabularies: Union[Unset, List[OntologyType]] = UNSET
    data_source_name: Union[Unset, str] = UNSET
    distributions: Union[Unset, "TermDistributions"] = UNSET
    domain_stats: Union[Unset, List["DomainStat"]] = UNSET
    enabled_vocabularies: Union[Unset, List[OntologyType]] = UNSET
    loaded_vocabularies: Union[Unset, List[OntologyType]] = UNSET
    origins: Union[Unset, List[str]] = UNSET
    total_concepts: Union[Unset, int] = UNSET
    total_patients: Union[Unset, int] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        catalog_vocabularies: Union[Unset, List[str]] = UNSET
        if not isinstance(self.catalog_vocabularies, Unset):
            catalog_vocabularies = []
            for catalog_vocabularies_item_data in self.catalog_vocabularies:
                catalog_vocabularies_item = catalog_vocabularies_item_data.value

                catalog_vocabularies.append(catalog_vocabularies_item)

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

        enabled_vocabularies: Union[Unset, List[str]] = UNSET
        if not isinstance(self.enabled_vocabularies, Unset):
            enabled_vocabularies = []
            for enabled_vocabularies_item_data in self.enabled_vocabularies:
                enabled_vocabularies_item = enabled_vocabularies_item_data.value

                enabled_vocabularies.append(enabled_vocabularies_item)

        loaded_vocabularies: Union[Unset, List[str]] = UNSET
        if not isinstance(self.loaded_vocabularies, Unset):
            loaded_vocabularies = []
            for loaded_vocabularies_item_data in self.loaded_vocabularies:
                loaded_vocabularies_item = loaded_vocabularies_item_data.value

                loaded_vocabularies.append(loaded_vocabularies_item)

        origins: Union[Unset, List[str]] = UNSET
        if not isinstance(self.origins, Unset):
            origins = self.origins

        total_concepts = self.total_concepts
        total_patients = self.total_patients
        updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if catalog_vocabularies is not UNSET:
            field_dict["catalogVocabularies"] = catalog_vocabularies
        if data_source_name is not UNSET:
            field_dict["dataSourceName"] = data_source_name
        if distributions is not UNSET:
            field_dict["distributions"] = distributions
        if domain_stats is not UNSET:
            field_dict["domainStats"] = domain_stats
        if enabled_vocabularies is not UNSET:
            field_dict["enabledVocabularies"] = enabled_vocabularies
        if loaded_vocabularies is not UNSET:
            field_dict["loadedVocabularies"] = loaded_vocabularies
        if origins is not UNSET:
            field_dict["origins"] = origins
        if total_concepts is not UNSET:
            field_dict["totalConcepts"] = total_concepts
        if total_patients is not UNSET:
            field_dict["totalPatients"] = total_patients
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_stat import DomainStat
        from ..models.term_distributions import TermDistributions

        d = src_dict.copy()
        catalog_vocabularies = []
        _catalog_vocabularies = d.pop("catalogVocabularies", UNSET)
        for catalog_vocabularies_item_data in _catalog_vocabularies or []:
            catalog_vocabularies_item = OntologyType(catalog_vocabularies_item_data)

            catalog_vocabularies.append(catalog_vocabularies_item)

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

        enabled_vocabularies = []
        _enabled_vocabularies = d.pop("enabledVocabularies", UNSET)
        for enabled_vocabularies_item_data in _enabled_vocabularies or []:
            enabled_vocabularies_item = OntologyType(enabled_vocabularies_item_data)

            enabled_vocabularies.append(enabled_vocabularies_item)

        loaded_vocabularies = []
        _loaded_vocabularies = d.pop("loadedVocabularies", UNSET)
        for loaded_vocabularies_item_data in _loaded_vocabularies or []:
            loaded_vocabularies_item = OntologyType(loaded_vocabularies_item_data)

            loaded_vocabularies.append(loaded_vocabularies_item)

        origins = cast(List[str], d.pop("origins", UNSET))

        total_concepts = d.pop("totalConcepts", UNSET)

        total_patients = d.pop("totalPatients", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        terminology_stats_response = cls(
            catalog_vocabularies=catalog_vocabularies,
            data_source_name=data_source_name,
            distributions=distributions,
            domain_stats=domain_stats,
            enabled_vocabularies=enabled_vocabularies,
            loaded_vocabularies=loaded_vocabularies,
            origins=origins,
            total_concepts=total_concepts,
            total_patients=total_patients,
            updated_at=updated_at,
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
