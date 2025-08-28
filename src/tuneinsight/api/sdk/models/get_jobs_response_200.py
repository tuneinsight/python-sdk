from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job import Job
    from ..models.labelled_value import LabelledValue


T = TypeVar("T", bound="GetJobsResponse200")


@attr.s(auto_attribs=True)
class GetJobsResponse200:
    """
    Attributes:
        available_states (Union[Unset, List['LabelledValue']]):
        available_types (Union[Unset, List['LabelledValue']]):
        jobs (Union[Unset, List['Job']]):
        total (Union[Unset, int]):
    """

    available_states: Union[Unset, List["LabelledValue"]] = UNSET
    available_types: Union[Unset, List["LabelledValue"]] = UNSET
    jobs: Union[Unset, List["Job"]] = UNSET
    total: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        available_states: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.available_states, Unset):
            available_states = []
            for available_states_item_data in self.available_states:
                available_states_item = available_states_item_data.to_dict()

                available_states.append(available_states_item)

        available_types: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.available_types, Unset):
            available_types = []
            for available_types_item_data in self.available_types:
                available_types_item = available_types_item_data.to_dict()

                available_types.append(available_types_item)

        jobs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.jobs, Unset):
            jobs = []
            for jobs_item_data in self.jobs:
                jobs_item = jobs_item_data.to_dict()

                jobs.append(jobs_item)

        total = self.total

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if available_states is not UNSET:
            field_dict["availableStates"] = available_states
        if available_types is not UNSET:
            field_dict["availableTypes"] = available_types
        if jobs is not UNSET:
            field_dict["jobs"] = jobs
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.job import Job
        from ..models.labelled_value import LabelledValue

        d = src_dict.copy()
        available_states = []
        _available_states = d.pop("availableStates", UNSET)
        for available_states_item_data in _available_states or []:
            available_states_item = LabelledValue.from_dict(available_states_item_data)

            available_states.append(available_states_item)

        available_types = []
        _available_types = d.pop("availableTypes", UNSET)
        for available_types_item_data in _available_types or []:
            available_types_item = LabelledValue.from_dict(available_types_item_data)

            available_types.append(available_types_item)

        jobs = []
        _jobs = d.pop("jobs", UNSET)
        for jobs_item_data in _jobs or []:
            jobs_item = Job.from_dict(jobs_item_data)

            jobs.append(jobs_item)

        total = d.pop("total", UNSET)

        get_jobs_response_200 = cls(
            available_states=available_states,
            available_types=available_types,
            jobs=jobs,
            total=total,
        )

        get_jobs_response_200.additional_properties = d
        return get_jobs_response_200

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
