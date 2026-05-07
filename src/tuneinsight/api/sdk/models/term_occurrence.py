from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.confidence_interval import ConfidenceInterval
    from ..models.term_distributions import TermDistributions
    from ..models.term_occurrence_per_care_site_count import TermOccurrencePerCareSiteCount


T = TypeVar("T", bound="TermOccurrence")


@attr.s(auto_attribs=True)
class TermOccurrence:
    """Represents a number of occurrences of a term in a data source.
    More specifically, given a specific term from an ontology, this object
    stores the number of patients that have at least one record referencing this term in the data source.
    Moreover, this object also stores other useful metadata and statistics about the term.

        Attributes:
            care_sites (Union[Unset, List[str]]): the list of care sites which contributed to this occurrence.
            confidence_interval (Union[Unset, ConfidenceInterval]): a confidence interval on a noisy or otherwise
                uncertainty value.
            count (Union[Unset, None, int]): represents the count of exact occurrences for this term.
            data_source_id (Union[Unset, str]): data source id this occurrence was computed from.
            distributions (Union[Unset, TermDistributions]):
            per_care_site_count (Union[Unset, TermOccurrencePerCareSiteCount]): when the occurrence is aggregated, this
                field stores the individual count per care site.
            remote (Union[Unset, bool]): indicates whether the occurrence for this term is from a remote instance of from
                the serving instance.
            remote_instance (Union[Unset, str]): instance id of the remote instance that provided this term occurrence.
            term_id (Union[Unset, str]): unique identifier of the term
    """

    care_sites: Union[Unset, List[str]] = UNSET
    confidence_interval: Union[Unset, "ConfidenceInterval"] = UNSET
    count: Union[Unset, None, int] = UNSET
    data_source_id: Union[Unset, str] = UNSET
    distributions: Union[Unset, "TermDistributions"] = UNSET
    per_care_site_count: Union[Unset, "TermOccurrencePerCareSiteCount"] = UNSET
    remote: Union[Unset, bool] = UNSET
    remote_instance: Union[Unset, str] = UNSET
    term_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        care_sites: Union[Unset, List[str]] = UNSET
        if not isinstance(self.care_sites, Unset):
            care_sites = self.care_sites

        confidence_interval: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.confidence_interval, Unset):
            confidence_interval = self.confidence_interval.to_dict()

        count = self.count
        data_source_id = self.data_source_id
        distributions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.distributions, Unset):
            distributions = self.distributions.to_dict()

        per_care_site_count: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.per_care_site_count, Unset):
            per_care_site_count = self.per_care_site_count.to_dict()

        remote = self.remote
        remote_instance = self.remote_instance
        term_id = self.term_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if care_sites is not UNSET:
            field_dict["careSites"] = care_sites
        if confidence_interval is not UNSET:
            field_dict["confidenceInterval"] = confidence_interval
        if count is not UNSET:
            field_dict["count"] = count
        if data_source_id is not UNSET:
            field_dict["dataSourceId"] = data_source_id
        if distributions is not UNSET:
            field_dict["distributions"] = distributions
        if per_care_site_count is not UNSET:
            field_dict["perCareSiteCount"] = per_care_site_count
        if remote is not UNSET:
            field_dict["remote"] = remote
        if remote_instance is not UNSET:
            field_dict["remoteInstance"] = remote_instance
        if term_id is not UNSET:
            field_dict["termId"] = term_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.confidence_interval import ConfidenceInterval
        from ..models.term_distributions import TermDistributions
        from ..models.term_occurrence_per_care_site_count import TermOccurrencePerCareSiteCount

        d = src_dict.copy()
        care_sites = cast(List[str], d.pop("careSites", UNSET))

        _confidence_interval = d.pop("confidenceInterval", UNSET)
        confidence_interval: Union[Unset, ConfidenceInterval]
        if isinstance(_confidence_interval, Unset):
            confidence_interval = UNSET
        else:
            confidence_interval = ConfidenceInterval.from_dict(_confidence_interval)

        count = d.pop("count", UNSET)

        data_source_id = d.pop("dataSourceId", UNSET)

        _distributions = d.pop("distributions", UNSET)
        distributions: Union[Unset, TermDistributions]
        if isinstance(_distributions, Unset):
            distributions = UNSET
        else:
            distributions = TermDistributions.from_dict(_distributions)

        _per_care_site_count = d.pop("perCareSiteCount", UNSET)
        per_care_site_count: Union[Unset, TermOccurrencePerCareSiteCount]
        if isinstance(_per_care_site_count, Unset):
            per_care_site_count = UNSET
        else:
            per_care_site_count = TermOccurrencePerCareSiteCount.from_dict(_per_care_site_count)

        remote = d.pop("remote", UNSET)

        remote_instance = d.pop("remoteInstance", UNSET)

        term_id = d.pop("termId", UNSET)

        term_occurrence = cls(
            care_sites=care_sites,
            confidence_interval=confidence_interval,
            count=count,
            data_source_id=data_source_id,
            distributions=distributions,
            per_care_site_count=per_care_site_count,
            remote=remote,
            remote_instance=remote_instance,
            term_id=term_id,
        )

        term_occurrence.additional_properties = d
        return term_occurrence

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
