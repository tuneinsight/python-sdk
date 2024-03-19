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
        id (str): Identifier of a computation, unique across all computing nodes.
        definition (ComputationDefinition): Generic computation.
        status (ComputationStatus): Status of the computation.
        updated_at (Union[Unset, str]):
        execution_cost (Union[Unset, float]): the cost of the computation when an execution quota has been setup.
        started_at (Union[Unset, str]):
        visible (Union[Unset, bool]): False if the computation is internal and should not be displayed to the user by
            default
        warnings (Union[Unset, List[str]]): list of warnings that occurred during the computation
        description (Union[Unset, str]):
        measurements (Union[Unset, List['Measurement']]): list of benchmarking measurements done on the computation
        owner (Union[Unset, str]): identifier of the end user that has requested the computation
        progress (Union[Unset, int]):
        ingress (Union[Unset, int]): keeps track of the number of bytes received during a computation to serve as a
            bandwidth measure
        local (Union[Unset, bool]):
        results (Union[Unset, List[str]]): Identifier(s) of the resulting data object(s). Available only when the status
            is completed.
        created_at (Union[Unset, str]):
        egress (Union[Unset, int]): keeps track of the number of bytes sent during a computation to serve as a bandwidth
            measure
        ended_at (Union[Unset, str]):
        errors (Union[Unset, List['ComputationError']]): list of errors that occurred during the computation
    """

    id: str
    definition: "ComputationDefinition"
    status: ComputationStatus
    updated_at: Union[Unset, str] = UNSET
    execution_cost: Union[Unset, float] = UNSET
    started_at: Union[Unset, str] = UNSET
    visible: Union[Unset, bool] = UNSET
    warnings: Union[Unset, List[str]] = UNSET
    description: Union[Unset, str] = UNSET
    measurements: Union[Unset, List["Measurement"]] = UNSET
    owner: Union[Unset, str] = UNSET
    progress: Union[Unset, int] = UNSET
    ingress: Union[Unset, int] = UNSET
    local: Union[Unset, bool] = UNSET
    results: Union[Unset, List[str]] = UNSET
    created_at: Union[Unset, str] = UNSET
    egress: Union[Unset, int] = UNSET
    ended_at: Union[Unset, str] = UNSET
    errors: Union[Unset, List["ComputationError"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        definition = self.definition.to_dict()

        status = self.status.value

        updated_at = self.updated_at
        execution_cost = self.execution_cost
        started_at = self.started_at
        visible = self.visible
        warnings: Union[Unset, List[str]] = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        description = self.description
        measurements: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.measurements, Unset):
            measurements = []
            for measurements_item_data in self.measurements:
                measurements_item = measurements_item_data.to_dict()

                measurements.append(measurements_item)

        owner = self.owner
        progress = self.progress
        ingress = self.ingress
        local = self.local
        results: Union[Unset, List[str]] = UNSET
        if not isinstance(self.results, Unset):
            results = self.results

        created_at = self.created_at
        egress = self.egress
        ended_at = self.ended_at
        errors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()

                errors.append(errors_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "definition": definition,
                "status": status,
            }
        )
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if execution_cost is not UNSET:
            field_dict["executionCost"] = execution_cost
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if visible is not UNSET:
            field_dict["visible"] = visible
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if description is not UNSET:
            field_dict["description"] = description
        if measurements is not UNSET:
            field_dict["measurements"] = measurements
        if owner is not UNSET:
            field_dict["owner"] = owner
        if progress is not UNSET:
            field_dict["progress"] = progress
        if ingress is not UNSET:
            field_dict["ingress"] = ingress
        if local is not UNSET:
            field_dict["local"] = local
        if results is not UNSET:
            field_dict["results"] = results
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if egress is not UNSET:
            field_dict["egress"] = egress
        if ended_at is not UNSET:
            field_dict["endedAt"] = ended_at
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.computation_definition import ComputationDefinition
        from ..models.computation_error import ComputationError
        from ..models.measurement import Measurement

        d = src_dict.copy()
        id = d.pop("id")

        definition = ComputationDefinition.from_dict(d.pop("definition"))

        status = ComputationStatus(d.pop("status"))

        updated_at = d.pop("updatedAt", UNSET)

        execution_cost = d.pop("executionCost", UNSET)

        started_at = d.pop("startedAt", UNSET)

        visible = d.pop("visible", UNSET)

        warnings = cast(List[str], d.pop("warnings", UNSET))

        description = d.pop("description", UNSET)

        measurements = []
        _measurements = d.pop("measurements", UNSET)
        for measurements_item_data in _measurements or []:
            measurements_item = Measurement.from_dict(measurements_item_data)

            measurements.append(measurements_item)

        owner = d.pop("owner", UNSET)

        progress = d.pop("progress", UNSET)

        ingress = d.pop("ingress", UNSET)

        local = d.pop("local", UNSET)

        results = cast(List[str], d.pop("results", UNSET))

        created_at = d.pop("createdAt", UNSET)

        egress = d.pop("egress", UNSET)

        ended_at = d.pop("endedAt", UNSET)

        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = ComputationError.from_dict(errors_item_data)

            errors.append(errors_item)

        computation = cls(
            id=id,
            definition=definition,
            status=status,
            updated_at=updated_at,
            execution_cost=execution_cost,
            started_at=started_at,
            visible=visible,
            warnings=warnings,
            description=description,
            measurements=measurements,
            owner=owner,
            progress=progress,
            ingress=ingress,
            local=local,
            results=results,
            created_at=created_at,
            egress=egress,
            ended_at=ended_at,
            errors=errors,
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
