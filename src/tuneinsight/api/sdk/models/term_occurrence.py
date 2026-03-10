from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.term_distributions import TermDistributions


T = TypeVar("T", bound="TermOccurrence")


@attr.s(auto_attribs=True)
class TermOccurrence:
    """Represents a number of occurrences of a term in a data source.
    More specifically, given a specific term from an ontology, this object
    stores the number of patients that have at least one record referencing this term in the data source.
    Moreover, this object also stores other useful metadata and statistics about the term.

        Attributes:
            count (Union[Unset, None, int]): represents the count of exact occurrences for this term.
            descendant_count (Union[Unset, None, int]): represents the count of descendant (term) occurrences for this term.
            distributions (Union[Unset, TermDistributions]):
            remote (Union[Unset, bool]): indicates whether the occurrence for this term is from a remote instance of from
                the serving instance.
            remote_instance (Union[Unset, str]): instance id of the remote instance that provided this term occurrence.
            term_id (Union[Unset, str]): unique identifier of the term
    """

    count: Union[Unset, None, int] = UNSET
    descendant_count: Union[Unset, None, int] = UNSET
    distributions: Union[Unset, "TermDistributions"] = UNSET
    remote: Union[Unset, bool] = UNSET
    remote_instance: Union[Unset, str] = UNSET
    term_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count = self.count
        descendant_count = self.descendant_count
        distributions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.distributions, Unset):
            distributions = self.distributions.to_dict()

        remote = self.remote
        remote_instance = self.remote_instance
        term_id = self.term_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if descendant_count is not UNSET:
            field_dict["descendantCount"] = descendant_count
        if distributions is not UNSET:
            field_dict["distributions"] = distributions
        if remote is not UNSET:
            field_dict["remote"] = remote
        if remote_instance is not UNSET:
            field_dict["remoteInstance"] = remote_instance
        if term_id is not UNSET:
            field_dict["termId"] = term_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.term_distributions import TermDistributions

        d = src_dict.copy()
        count = d.pop("count", UNSET)

        descendant_count = d.pop("descendantCount", UNSET)

        _distributions = d.pop("distributions", UNSET)
        distributions: Union[Unset, TermDistributions]
        if isinstance(_distributions, Unset):
            distributions = UNSET
        else:
            distributions = TermDistributions.from_dict(_distributions)

        remote = d.pop("remote", UNSET)

        remote_instance = d.pop("remoteInstance", UNSET)

        term_id = d.pop("termId", UNSET)

        term_occurrence = cls(
            count=count,
            descendant_count=descendant_count,
            distributions=distributions,
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
