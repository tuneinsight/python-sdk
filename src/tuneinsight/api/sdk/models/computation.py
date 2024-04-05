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
        local (Union[Unset, bool]):
        measurements (Union[Unset, List['Measurement']]): list of benchmarking measurements done on the computation
        owner (Union[Unset, str]): identifier of the end user that has requested the computation
        updated_at (Union[Unset, str]):
        visible (Union[Unset, bool]): False if the computation is internal and should not be displayed to the user by
            default
        description (Union[Unset, str]):
        egress (Union[Unset, int]): keeps track of the number of bytes sent during a computation to serve as a bandwidth
            measure
        ended_at (Union[Unset, str]):
        created_at (Union[Unset, str]):
        errors (Union[Unset, List['ComputationError']]): list of errors that occurred during the computation
        execution_cost (Union[Unset, float]): the cost of the computation when an execution quota has been setup.
        progress (Union[Unset, int]):
        started_at (Union[Unset, str]):
        warnings (Union[Unset, List[str]]): list of warnings that occurred during the computation
        ingress (Union[Unset, int]): keeps track of the number of bytes received during a computation to serve as a
            bandwidth measure
        results (Union[Unset, List[str]]): Identifier(s) of the resulting data object(s). Available only when the status
            is completed.
    """

    definition: "ComputationDefinition"
    id: str
    status: ComputationStatus
    local: Union[Unset, bool] = UNSET
    measurements: Union[Unset, List["Measurement"]] = UNSET
    owner: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    visible: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    egress: Union[Unset, int] = UNSET
    ended_at: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    errors: Union[Unset, List["ComputationError"]] = UNSET
    execution_cost: Union[Unset, float] = UNSET
    progress: Union[Unset, int] = UNSET
    started_at: Union[Unset, str] = UNSET
    warnings: Union[Unset, List[str]] = UNSET
    ingress: Union[Unset, int] = UNSET
    results: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        definition = self.definition.to_dict()

        id = self.id
        status = self.status.value

        local = self.local
        measurements: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.measurements, Unset):
            measurements = []
            for measurements_item_data in self.measurements:
                measurements_item = measurements_item_data.to_dict()

                measurements.append(measurements_item)

        owner = self.owner
        updated_at = self.updated_at
        visible = self.visible
        description = self.description
        egress = self.egress
        ended_at = self.ended_at
        created_at = self.created_at
        errors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()

                errors.append(errors_item)

        execution_cost = self.execution_cost
        progress = self.progress
        started_at = self.started_at
        warnings: Union[Unset, List[str]] = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        ingress = self.ingress
        results: Union[Unset, List[str]] = UNSET
        if not isinstance(self.results, Unset):
            results = self.results

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "definition": definition,
                "id": id,
                "status": status,
            }
        )
        if local is not UNSET:
            field_dict["local"] = local
        if measurements is not UNSET:
            field_dict["measurements"] = measurements
        if owner is not UNSET:
            field_dict["owner"] = owner
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if visible is not UNSET:
            field_dict["visible"] = visible
        if description is not UNSET:
            field_dict["description"] = description
        if egress is not UNSET:
            field_dict["egress"] = egress
        if ended_at is not UNSET:
            field_dict["endedAt"] = ended_at
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if errors is not UNSET:
            field_dict["errors"] = errors
        if execution_cost is not UNSET:
            field_dict["executionCost"] = execution_cost
        if progress is not UNSET:
            field_dict["progress"] = progress
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if ingress is not UNSET:
            field_dict["ingress"] = ingress
        if results is not UNSET:
            field_dict["results"] = results

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

        local = d.pop("local", UNSET)

        measurements = []
        _measurements = d.pop("measurements", UNSET)
        for measurements_item_data in _measurements or []:
            measurements_item = Measurement.from_dict(measurements_item_data)

            measurements.append(measurements_item)

        owner = d.pop("owner", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        visible = d.pop("visible", UNSET)

        description = d.pop("description", UNSET)

        egress = d.pop("egress", UNSET)

        ended_at = d.pop("endedAt", UNSET)

        created_at = d.pop("createdAt", UNSET)

        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = ComputationError.from_dict(errors_item_data)

            errors.append(errors_item)

        execution_cost = d.pop("executionCost", UNSET)

        progress = d.pop("progress", UNSET)

        started_at = d.pop("startedAt", UNSET)

        warnings = cast(List[str], d.pop("warnings", UNSET))

        ingress = d.pop("ingress", UNSET)

        results = cast(List[str], d.pop("results", UNSET))

        computation = cls(
            definition=definition,
            id=id,
            status=status,
            local=local,
            measurements=measurements,
            owner=owner,
            updated_at=updated_at,
            visible=visible,
            description=description,
            egress=egress,
            ended_at=ended_at,
            created_at=created_at,
            errors=errors,
            execution_cost=execution_cost,
            progress=progress,
            started_at=started_at,
            warnings=warnings,
            ingress=ingress,
            results=results,
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
