from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.job_state import JobState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job_error import JobError
    from ..models.job_log import JobLog
    from ..models.job_params import JobParams


T = TypeVar("T", bound="Job")


@attr.s(auto_attribs=True)
class Job:
    """model representing a background job that is run on the instance.

    Attributes:
        attempted_at (Union[Unset, str]): The time at which the job was last attempted.
        errors (Union[Unset, List['JobError']]):
        finalized_at (Union[Unset, str]): The time at which the job completed or errored.
        id (Union[Unset, int]): id of the job (in the integer format of the river library)
        logs (Union[Unset, List['JobLog']]):
        params (Union[Unset, JobParams]): arbitrary parameters for the job (JSON)
        scheduled_at (Union[Unset, str]): The time at which the job was scheduled.
        state (Union[Unset, JobState]): state of this job.
        type (Union[Unset, str]): the type of job that is being run
    """

    attempted_at: Union[Unset, str] = UNSET
    errors: Union[Unset, List["JobError"]] = UNSET
    finalized_at: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    logs: Union[Unset, List["JobLog"]] = UNSET
    params: Union[Unset, "JobParams"] = UNSET
    scheduled_at: Union[Unset, str] = UNSET
    state: Union[Unset, JobState] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attempted_at = self.attempted_at
        errors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()

                errors.append(errors_item)

        finalized_at = self.finalized_at
        id = self.id
        logs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.logs, Unset):
            logs = []
            for logs_item_data in self.logs:
                logs_item = logs_item_data.to_dict()

                logs.append(logs_item)

        params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        scheduled_at = self.scheduled_at
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attempted_at is not UNSET:
            field_dict["attemptedAt"] = attempted_at
        if errors is not UNSET:
            field_dict["errors"] = errors
        if finalized_at is not UNSET:
            field_dict["finalizedAt"] = finalized_at
        if id is not UNSET:
            field_dict["id"] = id
        if logs is not UNSET:
            field_dict["logs"] = logs
        if params is not UNSET:
            field_dict["params"] = params
        if scheduled_at is not UNSET:
            field_dict["scheduledAt"] = scheduled_at
        if state is not UNSET:
            field_dict["state"] = state
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.job_error import JobError
        from ..models.job_log import JobLog
        from ..models.job_params import JobParams

        d = src_dict.copy()
        attempted_at = d.pop("attemptedAt", UNSET)

        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = JobError.from_dict(errors_item_data)

            errors.append(errors_item)

        finalized_at = d.pop("finalizedAt", UNSET)

        id = d.pop("id", UNSET)

        logs = []
        _logs = d.pop("logs", UNSET)
        for logs_item_data in _logs or []:
            logs_item = JobLog.from_dict(logs_item_data)

            logs.append(logs_item)

        _params = d.pop("params", UNSET)
        params: Union[Unset, JobParams]
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = JobParams.from_dict(_params)

        scheduled_at = d.pop("scheduledAt", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, JobState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = JobState(_state)

        type = d.pop("type", UNSET)

        job = cls(
            attempted_at=attempted_at,
            errors=errors,
            finalized_at=finalized_at,
            id=id,
            logs=logs,
            params=params,
            scheduled_at=scheduled_at,
            state=state,
            type=type,
        )

        job.additional_properties = d
        return job

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
