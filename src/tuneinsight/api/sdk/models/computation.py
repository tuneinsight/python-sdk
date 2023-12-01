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
        status (ComputationStatus): Status of the computation.
        definition (ComputationDefinition): Generic computation.
        owner (Union[Unset, str]): identifier of the end user that has requested the computation
        progress (Union[Unset, int]):
        started_at (Union[Unset, str]):
        created_at (Union[Unset, str]):
        description (Union[Unset, str]):
        errors (Union[Unset, List['ComputationError']]): list of errors that occurred during the computation
        measurements (Union[Unset, List['Measurement']]): list of benchmarking measurements done on the computation
        ended_at (Union[Unset, str]):
        visible (Union[Unset, bool]): False if the computation is internal and should not be displayed to the user by
            default
        egress (Union[Unset, int]): keeps track of the number of bytes sent during a computation to serve as a bandwidth
            measure
        ingress (Union[Unset, int]): keeps track of the number of bytes received during a computation to serve as a
            bandwidth measure
        local (Union[Unset, bool]):
        results (Union[Unset, List[str]]): Identifier(s) of the resulting data object(s). Available only when the status
            is completed.
        updated_at (Union[Unset, str]):
    """

    id: str
    status: ComputationStatus
    definition: "ComputationDefinition"
    owner: Union[Unset, str] = UNSET
    progress: Union[Unset, int] = UNSET
    started_at: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    errors: Union[Unset, List["ComputationError"]] = UNSET
    measurements: Union[Unset, List["Measurement"]] = UNSET
    ended_at: Union[Unset, str] = UNSET
    visible: Union[Unset, bool] = UNSET
    egress: Union[Unset, int] = UNSET
    ingress: Union[Unset, int] = UNSET
    local: Union[Unset, bool] = UNSET
    results: Union[Unset, List[str]] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        status = self.status.value

        definition = self.definition.to_dict()

        owner = self.owner
        progress = self.progress
        started_at = self.started_at
        created_at = self.created_at
        description = self.description
        errors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()

                errors.append(errors_item)

        measurements: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.measurements, Unset):
            measurements = []
            for measurements_item_data in self.measurements:
                measurements_item = measurements_item_data.to_dict()

                measurements.append(measurements_item)

        ended_at = self.ended_at
        visible = self.visible
        egress = self.egress
        ingress = self.ingress
        local = self.local
        results: Union[Unset, List[str]] = UNSET
        if not isinstance(self.results, Unset):
            results = self.results

        updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "definition": definition,
            }
        )
        if owner is not UNSET:
            field_dict["owner"] = owner
        if progress is not UNSET:
            field_dict["progress"] = progress
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if errors is not UNSET:
            field_dict["errors"] = errors
        if measurements is not UNSET:
            field_dict["measurements"] = measurements
        if ended_at is not UNSET:
            field_dict["endedAt"] = ended_at
        if visible is not UNSET:
            field_dict["visible"] = visible
        if egress is not UNSET:
            field_dict["egress"] = egress
        if ingress is not UNSET:
            field_dict["ingress"] = ingress
        if local is not UNSET:
            field_dict["local"] = local
        if results is not UNSET:
            field_dict["results"] = results
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.computation_definition import ComputationDefinition
        from ..models.computation_error import ComputationError
        from ..models.measurement import Measurement

        d = src_dict.copy()
        id = d.pop("id")

        status = ComputationStatus(d.pop("status"))

        definition = ComputationDefinition.from_dict(d.pop("definition"))

        owner = d.pop("owner", UNSET)

        progress = d.pop("progress", UNSET)

        started_at = d.pop("startedAt", UNSET)

        created_at = d.pop("createdAt", UNSET)

        description = d.pop("description", UNSET)

        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = ComputationError.from_dict(errors_item_data)

            errors.append(errors_item)

        measurements = []
        _measurements = d.pop("measurements", UNSET)
        for measurements_item_data in _measurements or []:
            measurements_item = Measurement.from_dict(measurements_item_data)

            measurements.append(measurements_item)

        ended_at = d.pop("endedAt", UNSET)

        visible = d.pop("visible", UNSET)

        egress = d.pop("egress", UNSET)

        ingress = d.pop("ingress", UNSET)

        local = d.pop("local", UNSET)

        results = cast(List[str], d.pop("results", UNSET))

        updated_at = d.pop("updatedAt", UNSET)

        computation = cls(
            id=id,
            status=status,
            definition=definition,
            owner=owner,
            progress=progress,
            started_at=started_at,
            created_at=created_at,
            description=description,
            errors=errors,
            measurements=measurements,
            ended_at=ended_at,
            visible=visible,
            egress=egress,
            ingress=ingress,
            local=local,
            results=results,
            updated_at=updated_at,
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
