from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.job_progress_status import JobProgressStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="JobProgress")


@attr.s(auto_attribs=True)
class JobProgress:
    """the progress of an ongoing or complete catalog build or any other related job.

    Attributes:
        current_steps (Union[Unset, List[str]]): holds the list of step names that are currently running.
        done (Union[Unset, int]): the number of steps that were completed.
        last_updated (Union[Unset, None, str]):
        progress (Union[Unset, float]): the job progress percentage between 0 and 100.
        status (Union[Unset, JobProgressStatus]):
        time_left (Union[Unset, int]): the estimated time left in seconds.
        total_steps (Union[Unset, int]): the total number of steps that should be completed.
    """

    current_steps: Union[Unset, List[str]] = UNSET
    done: Union[Unset, int] = UNSET
    last_updated: Union[Unset, None, str] = UNSET
    progress: Union[Unset, float] = UNSET
    status: Union[Unset, JobProgressStatus] = UNSET
    time_left: Union[Unset, int] = UNSET
    total_steps: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        current_steps: Union[Unset, List[str]] = UNSET
        if not isinstance(self.current_steps, Unset):
            current_steps = self.current_steps

        done = self.done
        last_updated = self.last_updated
        progress = self.progress
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        time_left = self.time_left
        total_steps = self.total_steps

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_steps is not UNSET:
            field_dict["currentSteps"] = current_steps
        if done is not UNSET:
            field_dict["done"] = done
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if progress is not UNSET:
            field_dict["progress"] = progress
        if status is not UNSET:
            field_dict["status"] = status
        if time_left is not UNSET:
            field_dict["timeLeft"] = time_left
        if total_steps is not UNSET:
            field_dict["totalSteps"] = total_steps

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        current_steps = cast(List[str], d.pop("currentSteps", UNSET))

        done = d.pop("done", UNSET)

        last_updated = d.pop("lastUpdated", UNSET)

        progress = d.pop("progress", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, JobProgressStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = JobProgressStatus(_status)

        time_left = d.pop("timeLeft", UNSET)

        total_steps = d.pop("totalSteps", UNSET)

        job_progress = cls(
            current_steps=current_steps,
            done=done,
            last_updated=last_updated,
            progress=progress,
            status=status,
            time_left=time_left,
            total_steps=total_steps,
        )

        job_progress.additional_properties = d
        return job_progress

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
