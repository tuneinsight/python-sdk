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
        status (ComputationStatus): Status of the computation.
        id (str): Identifier of a computation, unique across all computing nodes.
        measurements (Union[Unset, List['Measurement']]): list of benchmarking measurements done on the computation
        ingress (Union[Unset, int]): keeps track of the number of bytes received during a computation to serve as a
            bandwidth measure
        local (Union[Unset, bool]):
        progress (Union[Unset, int]):
        results (Union[Unset, List[str]]): Identifier(s) of the resulting data object(s). Available only when the status
            is completed.
        visible (Union[Unset, bool]): False if the computation is internal and should not be displayed to the user by
            default
        errors (Union[Unset, List['ComputationError']]): list of errors that occurred during the computation
        description (Union[Unset, str]):
        egress (Union[Unset, int]): keeps track of the number of bytes sent during a computation to serve as a bandwidth
            measure
        owner (Union[Unset, str]): identifier of the end user that has requested the computation
        created_at (Union[Unset, str]):
        started_at (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        ended_at (Union[Unset, str]):
    """

    definition: "ComputationDefinition"
    status: ComputationStatus
    id: str
    measurements: Union[Unset, List["Measurement"]] = UNSET
    ingress: Union[Unset, int] = UNSET
    local: Union[Unset, bool] = UNSET
    progress: Union[Unset, int] = UNSET
    results: Union[Unset, List[str]] = UNSET
    visible: Union[Unset, bool] = UNSET
    errors: Union[Unset, List["ComputationError"]] = UNSET
    description: Union[Unset, str] = UNSET
    egress: Union[Unset, int] = UNSET
    owner: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    started_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    ended_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        definition = self.definition.to_dict()

        status = self.status.value

        id = self.id
        measurements: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.measurements, Unset):
            measurements = []
            for measurements_item_data in self.measurements:
                measurements_item = measurements_item_data.to_dict()

                measurements.append(measurements_item)

        ingress = self.ingress
        local = self.local
        progress = self.progress
        results: Union[Unset, List[str]] = UNSET
        if not isinstance(self.results, Unset):
            results = self.results

        visible = self.visible
        errors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()

                errors.append(errors_item)

        description = self.description
        egress = self.egress
        owner = self.owner
        created_at = self.created_at
        started_at = self.started_at
        updated_at = self.updated_at
        ended_at = self.ended_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "definition": definition,
                "status": status,
                "id": id,
            }
        )
        if measurements is not UNSET:
            field_dict["measurements"] = measurements
        if ingress is not UNSET:
            field_dict["ingress"] = ingress
        if local is not UNSET:
            field_dict["local"] = local
        if progress is not UNSET:
            field_dict["progress"] = progress
        if results is not UNSET:
            field_dict["results"] = results
        if visible is not UNSET:
            field_dict["visible"] = visible
        if errors is not UNSET:
            field_dict["errors"] = errors
        if description is not UNSET:
            field_dict["description"] = description
        if egress is not UNSET:
            field_dict["egress"] = egress
        if owner is not UNSET:
            field_dict["owner"] = owner
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if ended_at is not UNSET:
            field_dict["endedAt"] = ended_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.computation_definition import ComputationDefinition
        from ..models.computation_error import ComputationError
        from ..models.measurement import Measurement

        d = src_dict.copy()
        definition = ComputationDefinition.from_dict(d.pop("definition"))

        status = ComputationStatus(d.pop("status"))

        id = d.pop("id")

        measurements = []
        _measurements = d.pop("measurements", UNSET)
        for measurements_item_data in _measurements or []:
            measurements_item = Measurement.from_dict(measurements_item_data)

            measurements.append(measurements_item)

        ingress = d.pop("ingress", UNSET)

        local = d.pop("local", UNSET)

        progress = d.pop("progress", UNSET)

        results = cast(List[str], d.pop("results", UNSET))

        visible = d.pop("visible", UNSET)

        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = ComputationError.from_dict(errors_item_data)

            errors.append(errors_item)

        description = d.pop("description", UNSET)

        egress = d.pop("egress", UNSET)

        owner = d.pop("owner", UNSET)

        created_at = d.pop("createdAt", UNSET)

        started_at = d.pop("startedAt", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        ended_at = d.pop("endedAt", UNSET)

        computation = cls(
            definition=definition,
            status=status,
            id=id,
            measurements=measurements,
            ingress=ingress,
            local=local,
            progress=progress,
            results=results,
            visible=visible,
            errors=errors,
            description=description,
            egress=egress,
            owner=owner,
            created_at=created_at,
            started_at=started_at,
            updated_at=updated_at,
            ended_at=ended_at,
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
