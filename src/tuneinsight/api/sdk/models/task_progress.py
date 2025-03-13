from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskProgress")


@attr.s(auto_attribs=True)
class TaskProgress:
    """the progress of a remote task, divided in stages and steps

    Attributes:
        num_stages (Union[Unset, float]): the total number of stages in the task
        num_steps (Union[Unset, float]): the total number of steps in the current stage
        running (Union[Unset, bool]): whether the task is still running
        stage_name (Union[Unset, str]): a user-readable description of the current stage of the task
        stage_number (Union[Unset, float]): the number of the current stage
        stages (Union[Unset, List[str]]): a list of the names of the registered stages of the task
        step_number (Union[Unset, float]): the number of the current step of the current stage
    """

    num_stages: Union[Unset, float] = UNSET
    num_steps: Union[Unset, float] = UNSET
    running: Union[Unset, bool] = UNSET
    stage_name: Union[Unset, str] = UNSET
    stage_number: Union[Unset, float] = UNSET
    stages: Union[Unset, List[str]] = UNSET
    step_number: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        num_stages = self.num_stages
        num_steps = self.num_steps
        running = self.running
        stage_name = self.stage_name
        stage_number = self.stage_number
        stages: Union[Unset, List[str]] = UNSET
        if not isinstance(self.stages, Unset):
            stages = self.stages

        step_number = self.step_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if num_stages is not UNSET:
            field_dict["numStages"] = num_stages
        if num_steps is not UNSET:
            field_dict["numSteps"] = num_steps
        if running is not UNSET:
            field_dict["running"] = running
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
        d = src_dict.copy()
        num_stages = d.pop("numStages", UNSET)

        num_steps = d.pop("numSteps", UNSET)

        running = d.pop("running", UNSET)

        stage_name = d.pop("stageName", UNSET)

        stage_number = d.pop("stageNumber", UNSET)

        stages = cast(List[str], d.pop("stages", UNSET))

        step_number = d.pop("stepNumber", UNSET)

        task_progress = cls(
            num_stages=num_stages,
            num_steps=num_steps,
            running=running,
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
