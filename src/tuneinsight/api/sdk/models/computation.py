from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.computation_status import ComputationStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.computation_definition import ComputationDefinition
    from ..models.computation_error import ComputationError
    from ..models.measurement import Measurement


T = TypeVar("T", bound="Computation")


@attr.s(auto_attribs=True)
class Computation:
    """Metadata of a computation.

    Attributes:
        status (ComputationStatus): Status of the computation.
        id (str): Identifier of a computation, unique across all computing nodes.
        definition (ComputationDefinition): Generic computation.
        results (Union[Unset, List[str]]): Identifier(s) of the resulting data object(s). Available only when the status
            is completed.
        started_at (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        created_at (Union[Unset, str]):
        execution_cost (Union[Unset, float]): the cost of the computation when an execution quota has been setup.
        errors (Union[Unset, List['ComputationError']]): list of errors that occurred during the computation
        progress (Union[Unset, int]):
        ended_at (Union[Unset, str]):
        warnings (Union[Unset, List[str]]): list of warnings that occurred during the computation
        data_source_id (Union[Unset, None, str]): Unique identifier of a data source.
        project_id (Union[Unset, str]): Unique identifier of a project.
        ingress (Union[Unset, int]): keeps track of the number of bytes received during a computation to serve as a
            bandwidth measure
        local (Union[Unset, bool]):
        measurements (Union[Unset, List['Measurement']]): list of benchmarking measurements done on the computation
        owner (Union[Unset, str]): identifier of the end user that has requested the computation
        result_id (Union[Unset, str]): Unique identifier of a result.
        visible (Union[Unset, bool]): False if the computation is internal and should not be displayed to the user by
            default
        description (Union[Unset, str]):
        egress (Union[Unset, int]): keeps track of the number of bytes sent during a computation to serve as a bandwidth
            measure
    """

    status: ComputationStatus
    id: str
    definition: "ComputationDefinition"
    results: Union[Unset, List[str]] = UNSET
    started_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    execution_cost: Union[Unset, float] = UNSET
    errors: Union[Unset, List["ComputationError"]] = UNSET
    progress: Union[Unset, int] = UNSET
    ended_at: Union[Unset, str] = UNSET
    warnings: Union[Unset, List[str]] = UNSET
    data_source_id: Union[Unset, None, str] = UNSET
    project_id: Union[Unset, str] = UNSET
    ingress: Union[Unset, int] = UNSET
    local: Union[Unset, bool] = UNSET
    measurements: Union[Unset, List["Measurement"]] = UNSET
    owner: Union[Unset, str] = UNSET
    result_id: Union[Unset, str] = UNSET
    visible: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    egress: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        id = self.id
        definition = self.definition.to_dict()

        results: Union[Unset, List[str]] = UNSET
        if not isinstance(self.results, Unset):
            results = self.results

        started_at = self.started_at
        updated_at = self.updated_at
        created_at = self.created_at
        execution_cost = self.execution_cost
        errors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()

                errors.append(errors_item)

        progress = self.progress
        ended_at = self.ended_at
        warnings: Union[Unset, List[str]] = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        data_source_id = self.data_source_id
        project_id = self.project_id
        ingress = self.ingress
        local = self.local
        measurements: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.measurements, Unset):
            measurements = []
            for measurements_item_data in self.measurements:
                measurements_item = measurements_item_data.to_dict()

                measurements.append(measurements_item)

        owner = self.owner
        result_id = self.result_id
        visible = self.visible
        description = self.description
        egress = self.egress

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "id": id,
                "definition": definition,
            }
        )
        if results is not UNSET:
            field_dict["results"] = results
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if execution_cost is not UNSET:
            field_dict["executionCost"] = execution_cost
        if errors is not UNSET:
            field_dict["errors"] = errors
        if progress is not UNSET:
            field_dict["progress"] = progress
        if ended_at is not UNSET:
            field_dict["endedAt"] = ended_at
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if data_source_id is not UNSET:
            field_dict["dataSourceId"] = data_source_id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if ingress is not UNSET:
            field_dict["ingress"] = ingress
        if local is not UNSET:
            field_dict["local"] = local
        if measurements is not UNSET:
            field_dict["measurements"] = measurements
        if owner is not UNSET:
            field_dict["owner"] = owner
        if result_id is not UNSET:
            field_dict["resultId"] = result_id
        if visible is not UNSET:
            field_dict["visible"] = visible
        if description is not UNSET:
            field_dict["description"] = description
        if egress is not UNSET:
            field_dict["egress"] = egress

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.computation_definition import ComputationDefinition
        from ..models.computation_error import ComputationError
        from ..models.measurement import Measurement

        d = src_dict.copy()
        status = ComputationStatus(d.pop("status"))

        id = d.pop("id")

        definition = ComputationDefinition.from_dict(d.pop("definition"))

        results = cast(List[str], d.pop("results", UNSET))

        started_at = d.pop("startedAt", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        created_at = d.pop("createdAt", UNSET)

        execution_cost = d.pop("executionCost", UNSET)

        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = ComputationError.from_dict(errors_item_data)

            errors.append(errors_item)

        progress = d.pop("progress", UNSET)

        ended_at = d.pop("endedAt", UNSET)

        warnings = cast(List[str], d.pop("warnings", UNSET))

        data_source_id = d.pop("dataSourceId", UNSET)

        project_id = d.pop("projectId", UNSET)

        ingress = d.pop("ingress", UNSET)

        local = d.pop("local", UNSET)

        measurements = []
        _measurements = d.pop("measurements", UNSET)
        for measurements_item_data in _measurements or []:
            measurements_item = Measurement.from_dict(measurements_item_data)

            measurements.append(measurements_item)

        owner = d.pop("owner", UNSET)

        result_id = d.pop("resultId", UNSET)

        visible = d.pop("visible", UNSET)

        description = d.pop("description", UNSET)

        egress = d.pop("egress", UNSET)

        computation = cls(
            status=status,
            id=id,
            definition=definition,
            results=results,
            started_at=started_at,
            updated_at=updated_at,
            created_at=created_at,
            execution_cost=execution_cost,
            errors=errors,
            progress=progress,
            ended_at=ended_at,
            warnings=warnings,
            data_source_id=data_source_id,
            project_id=project_id,
            ingress=ingress,
            local=local,
            measurements=measurements,
            owner=owner,
            result_id=result_id,
            visible=visible,
            description=description,
            egress=egress,
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
