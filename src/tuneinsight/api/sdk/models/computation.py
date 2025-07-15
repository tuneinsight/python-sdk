from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.computation_status import ComputationStatus
from ..models.run_mode import RunMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.computation_definition import ComputationDefinition
    from ..models.computation_error import ComputationError
    from ..models.measurement import Measurement
    from ..models.participant import Participant
    from ..models.task_progress import TaskProgress


T = TypeVar("T", bound="Computation")


@attr.s(auto_attribs=True)
class Computation:
    """Metadata of a computation.

    Attributes:
        definition (ComputationDefinition): Generic computation.
        id (str): Identifier of a computation, unique across all computing nodes.
        status (ComputationStatus): Status of the computation.
        created_at (Union[Unset, str]):
        data_source_id (Union[Unset, None, str]): Unique identifier of a data source.
        description (Union[Unset, str]):
        egress (Union[Unset, int]): keeps track of the number of bytes sent during a computation to serve as a bandwidth
            measure
        ended_at (Union[Unset, str]):
        errors (Union[Unset, List['ComputationError']]): list of errors that occurred during the computation
        execution_cost (Union[Unset, float]): the cost of the computation when an execution quota has been setup.
        ingress (Union[Unset, int]): keeps track of the number of bytes received during a computation to serve as a
            bandwidth measure
        local (Union[Unset, bool]): deprecated
        measurements (Union[Unset, List['Measurement']]): list of benchmarking measurements done on the computation
        notify_end (Union[Unset, None, bool]): whether to notify the initiating user when the computation has ended.
        output_data_source_id (Union[Unset, None, str]): Unique identifier of a data source.
        owner (Union[Unset, str]): identifier of the end user that has requested the computation
        participants (Union[Unset, List['Participant']]): list of participants that took part (interacted or
            contributed) in this computation.
        progress (Union[Unset, TaskProgress]): the progress of a remote task, divided in stages and steps
        project_id (Union[Unset, str]): Unique identifier of a project.
        result_id (Union[Unset, str]): Unique identifier of a result.
        result_ids (Union[Unset, List[str]]): List of results that have been associated with this computation.
        results (Union[Unset, List[str]]): (DEPRECATED)Identifier(s) of the resulting data object(s). Available only
            when the status is completed.
        run_mode (Union[Unset, RunMode]): Defines the mode in which to run a computation (local, collective, or both)
        started_at (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        visible (Union[Unset, bool]): False if the computation is internal and should not be displayed to the user by
            default
        warnings (Union[Unset, List[str]]): list of warnings that occurred during the computation
    """

    definition: "ComputationDefinition"
    id: str
    status: ComputationStatus
    created_at: Union[Unset, str] = UNSET
    data_source_id: Union[Unset, None, str] = UNSET
    description: Union[Unset, str] = UNSET
    egress: Union[Unset, int] = UNSET
    ended_at: Union[Unset, str] = UNSET
    errors: Union[Unset, List["ComputationError"]] = UNSET
    execution_cost: Union[Unset, float] = UNSET
    ingress: Union[Unset, int] = UNSET
    local: Union[Unset, bool] = UNSET
    measurements: Union[Unset, List["Measurement"]] = UNSET
    notify_end: Union[Unset, None, bool] = UNSET
    output_data_source_id: Union[Unset, None, str] = UNSET
    owner: Union[Unset, str] = UNSET
    participants: Union[Unset, List["Participant"]] = UNSET
    progress: Union[Unset, "TaskProgress"] = UNSET
    project_id: Union[Unset, str] = UNSET
    result_id: Union[Unset, str] = UNSET
    result_ids: Union[Unset, List[str]] = UNSET
    results: Union[Unset, List[str]] = UNSET
    run_mode: Union[Unset, RunMode] = UNSET
    started_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    visible: Union[Unset, bool] = UNSET
    warnings: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        definition = self.definition.to_dict()

        id = self.id
        status = self.status.value

        created_at = self.created_at
        data_source_id = self.data_source_id
        description = self.description
        egress = self.egress
        ended_at = self.ended_at
        errors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()

                errors.append(errors_item)

        execution_cost = self.execution_cost
        ingress = self.ingress
        local = self.local
        measurements: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.measurements, Unset):
            measurements = []
            for measurements_item_data in self.measurements:
                measurements_item = measurements_item_data.to_dict()

                measurements.append(measurements_item)

        notify_end = self.notify_end
        output_data_source_id = self.output_data_source_id
        owner = self.owner
        participants: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.participants, Unset):
            participants = []
            for participants_item_data in self.participants:
                participants_item = participants_item_data.to_dict()

                participants.append(participants_item)

        progress: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.progress, Unset):
            progress = self.progress.to_dict()

        project_id = self.project_id
        result_id = self.result_id
        result_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.result_ids, Unset):
            result_ids = self.result_ids

        results: Union[Unset, List[str]] = UNSET
        if not isinstance(self.results, Unset):
            results = self.results

        run_mode: Union[Unset, str] = UNSET
        if not isinstance(self.run_mode, Unset):
            run_mode = self.run_mode.value

        started_at = self.started_at
        updated_at = self.updated_at
        visible = self.visible
        warnings: Union[Unset, List[str]] = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "definition": definition,
                "id": id,
                "status": status,
            }
        )
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if data_source_id is not UNSET:
            field_dict["dataSourceId"] = data_source_id
        if description is not UNSET:
            field_dict["description"] = description
        if egress is not UNSET:
            field_dict["egress"] = egress
        if ended_at is not UNSET:
            field_dict["endedAt"] = ended_at
        if errors is not UNSET:
            field_dict["errors"] = errors
        if execution_cost is not UNSET:
            field_dict["executionCost"] = execution_cost
        if ingress is not UNSET:
            field_dict["ingress"] = ingress
        if local is not UNSET:
            field_dict["local"] = local
        if measurements is not UNSET:
            field_dict["measurements"] = measurements
        if notify_end is not UNSET:
            field_dict["notifyEnd"] = notify_end
        if output_data_source_id is not UNSET:
            field_dict["outputDataSourceId"] = output_data_source_id
        if owner is not UNSET:
            field_dict["owner"] = owner
        if participants is not UNSET:
            field_dict["participants"] = participants
        if progress is not UNSET:
            field_dict["progress"] = progress
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if result_id is not UNSET:
            field_dict["resultId"] = result_id
        if result_ids is not UNSET:
            field_dict["resultIds"] = result_ids
        if results is not UNSET:
            field_dict["results"] = results
        if run_mode is not UNSET:
            field_dict["runMode"] = run_mode
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if visible is not UNSET:
            field_dict["visible"] = visible
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.computation_definition import ComputationDefinition
        from ..models.computation_error import ComputationError
        from ..models.measurement import Measurement
        from ..models.participant import Participant
        from ..models.task_progress import TaskProgress

        d = src_dict.copy()
        definition = ComputationDefinition.from_dict(d.pop("definition"))

        id = d.pop("id")

        status = ComputationStatus(d.pop("status"))

        created_at = d.pop("createdAt", UNSET)

        data_source_id = d.pop("dataSourceId", UNSET)

        description = d.pop("description", UNSET)

        egress = d.pop("egress", UNSET)

        ended_at = d.pop("endedAt", UNSET)

        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = ComputationError.from_dict(errors_item_data)

            errors.append(errors_item)

        execution_cost = d.pop("executionCost", UNSET)

        ingress = d.pop("ingress", UNSET)

        local = d.pop("local", UNSET)

        measurements = []
        _measurements = d.pop("measurements", UNSET)
        for measurements_item_data in _measurements or []:
            measurements_item = Measurement.from_dict(measurements_item_data)

            measurements.append(measurements_item)

        notify_end = d.pop("notifyEnd", UNSET)

        output_data_source_id = d.pop("outputDataSourceId", UNSET)

        owner = d.pop("owner", UNSET)

        participants = []
        _participants = d.pop("participants", UNSET)
        for participants_item_data in _participants or []:
            participants_item = Participant.from_dict(participants_item_data)

            participants.append(participants_item)

        _progress = d.pop("progress", UNSET)
        progress: Union[Unset, TaskProgress]
        if isinstance(_progress, Unset):
            progress = UNSET
        else:
            progress = TaskProgress.from_dict(_progress)

        project_id = d.pop("projectId", UNSET)

        result_id = d.pop("resultId", UNSET)

        result_ids = cast(List[str], d.pop("resultIds", UNSET))

        results = cast(List[str], d.pop("results", UNSET))

        _run_mode = d.pop("runMode", UNSET)
        run_mode: Union[Unset, RunMode]
        if isinstance(_run_mode, Unset):
            run_mode = UNSET
        else:
            run_mode = RunMode(_run_mode)

        started_at = d.pop("startedAt", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        visible = d.pop("visible", UNSET)

        warnings = cast(List[str], d.pop("warnings", UNSET))

        computation = cls(
            definition=definition,
            id=id,
            status=status,
            created_at=created_at,
            data_source_id=data_source_id,
            description=description,
            egress=egress,
            ended_at=ended_at,
            errors=errors,
            execution_cost=execution_cost,
            ingress=ingress,
            local=local,
            measurements=measurements,
            notify_end=notify_end,
            output_data_source_id=output_data_source_id,
            owner=owner,
            participants=participants,
            progress=progress,
            project_id=project_id,
            result_id=result_id,
            result_ids=result_ids,
            results=results,
            run_mode=run_mode,
            started_at=started_at,
            updated_at=updated_at,
            visible=visible,
            warnings=warnings,
        )

        computation.additional_properties = d
        return computation

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
