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
        definition (ComputationDefinition): Generic computation.
        id (str): Identifier of a computation, unique across all computing nodes.
        status (ComputationStatus): Status of the computation.
        errors (Union[Unset, List['ComputationError']]): list of errors that occurred during the computation
        ingress (Union[Unset, int]): keeps track of the number of bytes received during a computation to serve as a
            bandwidth measure
        warnings (Union[Unset, List[str]]): list of warnings that occurred during the computation
        description (Union[Unset, str]):
        local (Union[Unset, bool]):
        measurements (Union[Unset, List['Measurement']]): list of benchmarking measurements done on the computation
        started_at (Union[Unset, str]):
        visible (Union[Unset, bool]): False if the computation is internal and should not be displayed to the user by
            default
        created_at (Union[Unset, str]):
        ended_at (Union[Unset, str]):
        owner (Union[Unset, str]): identifier of the end user that has requested the computation
        project_id (Union[Unset, str]): Unique identifier of a project.
        results (Union[Unset, List[str]]): Identifier(s) of the resulting data object(s). Available only when the status
            is completed.
        updated_at (Union[Unset, str]):
        egress (Union[Unset, int]): keeps track of the number of bytes sent during a computation to serve as a bandwidth
            measure
        execution_cost (Union[Unset, float]): the cost of the computation when an execution quota has been setup.
        progress (Union[Unset, int]):
        data_source_id (Union[Unset, None, str]): Unique identifier of a data source.
    """

    definition: "ComputationDefinition"
    id: str
    status: ComputationStatus
    errors: Union[Unset, List["ComputationError"]] = UNSET
    ingress: Union[Unset, int] = UNSET
    warnings: Union[Unset, List[str]] = UNSET
    description: Union[Unset, str] = UNSET
    local: Union[Unset, bool] = UNSET
    measurements: Union[Unset, List["Measurement"]] = UNSET
    started_at: Union[Unset, str] = UNSET
    visible: Union[Unset, bool] = UNSET
    created_at: Union[Unset, str] = UNSET
    ended_at: Union[Unset, str] = UNSET
    owner: Union[Unset, str] = UNSET
    project_id: Union[Unset, str] = UNSET
    results: Union[Unset, List[str]] = UNSET
    updated_at: Union[Unset, str] = UNSET
    egress: Union[Unset, int] = UNSET
    execution_cost: Union[Unset, float] = UNSET
    progress: Union[Unset, int] = UNSET
    data_source_id: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        definition = self.definition.to_dict()

        id = self.id
        status = self.status.value

        errors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()

                errors.append(errors_item)

        ingress = self.ingress
        warnings: Union[Unset, List[str]] = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        description = self.description
        local = self.local
        measurements: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.measurements, Unset):
            measurements = []
            for measurements_item_data in self.measurements:
                measurements_item = measurements_item_data.to_dict()

                measurements.append(measurements_item)

        started_at = self.started_at
        visible = self.visible
        created_at = self.created_at
        ended_at = self.ended_at
        owner = self.owner
        project_id = self.project_id
        results: Union[Unset, List[str]] = UNSET
        if not isinstance(self.results, Unset):
            results = self.results

        updated_at = self.updated_at
        egress = self.egress
        execution_cost = self.execution_cost
        progress = self.progress
        data_source_id = self.data_source_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "definition": definition,
                "id": id,
                "status": status,
            }
        )
        if errors is not UNSET:
            field_dict["errors"] = errors
        if ingress is not UNSET:
            field_dict["ingress"] = ingress
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if description is not UNSET:
            field_dict["description"] = description
        if local is not UNSET:
            field_dict["local"] = local
        if measurements is not UNSET:
            field_dict["measurements"] = measurements
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if visible is not UNSET:
            field_dict["visible"] = visible
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if ended_at is not UNSET:
            field_dict["endedAt"] = ended_at
        if owner is not UNSET:
            field_dict["owner"] = owner
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if results is not UNSET:
            field_dict["results"] = results
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if egress is not UNSET:
            field_dict["egress"] = egress
        if execution_cost is not UNSET:
            field_dict["executionCost"] = execution_cost
        if progress is not UNSET:
            field_dict["progress"] = progress
        if data_source_id is not UNSET:
            field_dict["dataSourceId"] = data_source_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.computation_definition import ComputationDefinition
        from ..models.computation_error import ComputationError
        from ..models.measurement import Measurement

        d = src_dict.copy()
        definition = ComputationDefinition.from_dict(d.pop("definition"))

        id = d.pop("id")

        status = ComputationStatus(d.pop("status"))

        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = ComputationError.from_dict(errors_item_data)

            errors.append(errors_item)

        ingress = d.pop("ingress", UNSET)

        warnings = cast(List[str], d.pop("warnings", UNSET))

        description = d.pop("description", UNSET)

        local = d.pop("local", UNSET)

        measurements = []
        _measurements = d.pop("measurements", UNSET)
        for measurements_item_data in _measurements or []:
            measurements_item = Measurement.from_dict(measurements_item_data)

            measurements.append(measurements_item)

        started_at = d.pop("startedAt", UNSET)

        visible = d.pop("visible", UNSET)

        created_at = d.pop("createdAt", UNSET)

        ended_at = d.pop("endedAt", UNSET)

        owner = d.pop("owner", UNSET)

        project_id = d.pop("projectId", UNSET)

        results = cast(List[str], d.pop("results", UNSET))

        updated_at = d.pop("updatedAt", UNSET)

        egress = d.pop("egress", UNSET)

        execution_cost = d.pop("executionCost", UNSET)

        progress = d.pop("progress", UNSET)

        data_source_id = d.pop("dataSourceId", UNSET)

        computation = cls(
            definition=definition,
            id=id,
            status=status,
            errors=errors,
            ingress=ingress,
            warnings=warnings,
            description=description,
            local=local,
            measurements=measurements,
            started_at=started_at,
            visible=visible,
            created_at=created_at,
            ended_at=ended_at,
            owner=owner,
            project_id=project_id,
            results=results,
            updated_at=updated_at,
            egress=egress,
            execution_cost=execution_cost,
            progress=progress,
            data_source_id=data_source_id,
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
