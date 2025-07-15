from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.task_progress_payload import TaskProgressPayload


T = TypeVar("T", bound="TaskProgress")


@attr.s(auto_attribs=True)
class TaskProgress:
    """the progress of a remote task, divided in stages and steps

    Attributes:
        running (bool): whether the task is still running
        cancelled (Union[Unset, bool]): whether the task has been cancelled
        failed (Union[Unset, bool]): whether the task has failed
        num_stages (Union[Unset, float]): the total number of stages in the task
        num_steps (Union[Unset, float]): the total number of steps in the current stage
        payload (Union[Unset, TaskProgressPayload]): result or output of the task, returned when finished
        stage_name (Union[Unset, str]): a user-readable description of the current stage of the task
        stage_number (Union[Unset, float]): the number of the current stage
        stages (Union[Unset, List[str]]): a list of the names of the registered stages of the task
        step_number (Union[Unset, float]): the number of the current step of the current stage
    """

    running: bool
    cancelled: Union[Unset, bool] = UNSET
    failed: Union[Unset, bool] = UNSET
    num_stages: Union[Unset, float] = UNSET
    num_steps: Union[Unset, float] = UNSET
    payload: Union[Unset, "TaskProgressPayload"] = UNSET
    stage_name: Union[Unset, str] = UNSET
    stage_number: Union[Unset, float] = UNSET
    stages: Union[Unset, List[str]] = UNSET
    step_number: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        running = self.running
        cancelled = self.cancelled
        failed = self.failed
        num_stages = self.num_stages
        num_steps = self.num_steps
        payload: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        stage_name = self.stage_name
        stage_number = self.stage_number
        stages: Union[Unset, List[str]] = UNSET
        if not isinstance(self.stages, Unset):
            stages = self.stages

        step_number = self.step_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "running": running,
            }
        )
        if cancelled is not UNSET:
            field_dict["cancelled"] = cancelled
        if failed is not UNSET:
            field_dict["failed"] = failed
        if num_stages is not UNSET:
            field_dict["numStages"] = num_stages
        if num_steps is not UNSET:
            field_dict["numSteps"] = num_steps
        if payload is not UNSET:
            field_dict["payload"] = payload
        if stage_name is not UNSET:
            field_dict["stageName"] = stage_name
        if stage_number is not UNSET:
            field_dict["stageNumber"] = stage_number
        if stages is not UNSET:
            field_dict["stages"] = stages
        if step_number is not UNSET:
            field_dict["stepNumber"] = step_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.task_progress_payload import TaskProgressPayload

        d = src_dict.copy()
        running = d.pop("running")

        cancelled = d.pop("cancelled", UNSET)

        failed = d.pop("failed", UNSET)

        num_stages = d.pop("numStages", UNSET)

        num_steps = d.pop("numSteps", UNSET)

        _payload = d.pop("payload", UNSET)
        payload: Union[Unset, TaskProgressPayload]
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = TaskProgressPayload.from_dict(_payload)

        stage_name = d.pop("stageName", UNSET)

        stage_number = d.pop("stageNumber", UNSET)

        stages = cast(List[str], d.pop("stages", UNSET))

        step_number = d.pop("stepNumber", UNSET)

        task_progress = cls(
            running=running,
            cancelled=cancelled,
            failed=failed,
            num_stages=num_stages,
            num_steps=num_steps,
            payload=payload,
            stage_name=stage_name,
            stage_number=stage_number,
            stages=stages,
            step_number=step_number,
        )

        task_progress.additional_properties = d
        return task_progress

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
