from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job_progress import JobProgress


T = TypeVar("T", bound="CatalogProgressResponse")


@attr.s(auto_attribs=True)
class CatalogProgressResponse:
    """this object is returned when fetching the catalog status, it contains the progress information about loading
    ontologies (which should be completed before building the catalog) and progress information about building the
    catalog.

        Attributes:
            allocate_budget_status (Union[Unset, JobProgress]): the progress of an ongoing or complete catalog build or any
                other related job.
            build_catalog_status (Union[Unset, JobProgress]): the progress of an ongoing or complete catalog build or any
                other related job.
            build_network_catalog_status (Union[Unset, JobProgress]): the progress of an ongoing or complete catalog build
                or any other related job.
            load_ontologies_status (Union[Unset, JobProgress]): the progress of an ongoing or complete catalog build or any
                other related job.
    """

    allocate_budget_status: Union[Unset, "JobProgress"] = UNSET
    build_catalog_status: Union[Unset, "JobProgress"] = UNSET
    build_network_catalog_status: Union[Unset, "JobProgress"] = UNSET
    load_ontologies_status: Union[Unset, "JobProgress"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allocate_budget_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.allocate_budget_status, Unset):
            allocate_budget_status = self.allocate_budget_status.to_dict()

        build_catalog_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.build_catalog_status, Unset):
            build_catalog_status = self.build_catalog_status.to_dict()

        build_network_catalog_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.build_network_catalog_status, Unset):
            build_network_catalog_status = self.build_network_catalog_status.to_dict()

        load_ontologies_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.load_ontologies_status, Unset):
            load_ontologies_status = self.load_ontologies_status.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allocate_budget_status is not UNSET:
            field_dict["allocateBudgetStatus"] = allocate_budget_status
        if build_catalog_status is not UNSET:
            field_dict["buildCatalogStatus"] = build_catalog_status
        if build_network_catalog_status is not UNSET:
            field_dict["buildNetworkCatalogStatus"] = build_network_catalog_status
        if load_ontologies_status is not UNSET:
            field_dict["loadOntologiesStatus"] = load_ontologies_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.job_progress import JobProgress

        d = src_dict.copy()
        _allocate_budget_status = d.pop("allocateBudgetStatus", UNSET)
        allocate_budget_status: Union[Unset, JobProgress]
        if isinstance(_allocate_budget_status, Unset):
            allocate_budget_status = UNSET
        else:
            allocate_budget_status = JobProgress.from_dict(_allocate_budget_status)

        _build_catalog_status = d.pop("buildCatalogStatus", UNSET)
        build_catalog_status: Union[Unset, JobProgress]
        if isinstance(_build_catalog_status, Unset):
            build_catalog_status = UNSET
        else:
            build_catalog_status = JobProgress.from_dict(_build_catalog_status)

        _build_network_catalog_status = d.pop("buildNetworkCatalogStatus", UNSET)
        build_network_catalog_status: Union[Unset, JobProgress]
        if isinstance(_build_network_catalog_status, Unset):
            build_network_catalog_status = UNSET
        else:
            build_network_catalog_status = JobProgress.from_dict(_build_network_catalog_status)

        _load_ontologies_status = d.pop("loadOntologiesStatus", UNSET)
        load_ontologies_status: Union[Unset, JobProgress]
        if isinstance(_load_ontologies_status, Unset):
            load_ontologies_status = UNSET
        else:
            load_ontologies_status = JobProgress.from_dict(_load_ontologies_status)

        catalog_progress_response = cls(
            allocate_budget_status=allocate_budget_status,
            build_catalog_status=build_catalog_status,
            build_network_catalog_status=build_network_catalog_status,
            load_ontologies_status=load_ontologies_status,
        )

        catalog_progress_response.additional_properties = d
        return catalog_progress_response

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
