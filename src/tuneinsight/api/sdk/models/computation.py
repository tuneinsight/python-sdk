from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.computation_status import ComputationStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.computation_definition import ComputationDefinition


T = TypeVar("T", bound="Computation")


@attr.s(auto_attribs=True)
class Computation:
    """Metadata of a computation.

    Attributes:
        status (ComputationStatus): Status of the computation.
        definition (ComputationDefinition): Generic computation.
        id (str): Identifier of a computation, unique across all computing nodes.
        created_at (Union[Unset, str]):
        local (Union[Unset, bool]):
        description (Union[Unset, str]):
        error (Union[Unset, List[str]]): Error messages.
        results (Union[Unset, List[str]]): Identifier(s) of the resulting data object(s). Available only when the status
            is completed.
        updated_at (Union[Unset, str]):
        egress (Union[Unset, int]): keeps track of the number of bytes sent during a computation to serve as a bandwidth
            measure
        started_at (Union[Unset, str]):
        ended_at (Union[Unset, str]):
        ingress (Union[Unset, int]): keeps track of the number of bytes received during a computation to serve as a
            bandwidth measure
        progress (Union[Unset, int]):
        visible (Union[Unset, bool]): False if the computation is internal and should not be displayed to the user by
            default
    """

    status: ComputationStatus
    definition: "ComputationDefinition"
    id: str
    created_at: Union[Unset, str] = UNSET
    local: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    error: Union[Unset, List[str]] = UNSET
    results: Union[Unset, List[str]] = UNSET
    updated_at: Union[Unset, str] = UNSET
    egress: Union[Unset, int] = UNSET
    started_at: Union[Unset, str] = UNSET
    ended_at: Union[Unset, str] = UNSET
    ingress: Union[Unset, int] = UNSET
    progress: Union[Unset, int] = UNSET
    visible: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        definition = self.definition.to_dict()

        id = self.id
        created_at = self.created_at
        local = self.local
        description = self.description
        error: Union[Unset, List[str]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error

        results: Union[Unset, List[str]] = UNSET
        if not isinstance(self.results, Unset):
            results = self.results

        updated_at = self.updated_at
        egress = self.egress
        started_at = self.started_at
        ended_at = self.ended_at
        ingress = self.ingress
        progress = self.progress
        visible = self.visible

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "definition": definition,
                "id": id,
            }
        )
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if local is not UNSET:
            field_dict["local"] = local
        if description is not UNSET:
            field_dict["description"] = description
        if error is not UNSET:
            field_dict["error"] = error
        if results is not UNSET:
            field_dict["results"] = results
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if egress is not UNSET:
            field_dict["egress"] = egress
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if ended_at is not UNSET:
            field_dict["endedAt"] = ended_at
        if ingress is not UNSET:
            field_dict["ingress"] = ingress
        if progress is not UNSET:
            field_dict["progress"] = progress
        if visible is not UNSET:
            field_dict["visible"] = visible

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.computation_definition import ComputationDefinition

        d = src_dict.copy()
        status = ComputationStatus(d.pop("status"))

        definition = ComputationDefinition.from_dict(d.pop("definition"))

        id = d.pop("id")

        created_at = d.pop("createdAt", UNSET)

        local = d.pop("local", UNSET)

        description = d.pop("description", UNSET)

        error = cast(List[str], d.pop("error", UNSET))

        results = cast(List[str], d.pop("results", UNSET))

        updated_at = d.pop("updatedAt", UNSET)

        egress = d.pop("egress", UNSET)

        started_at = d.pop("startedAt", UNSET)

        ended_at = d.pop("endedAt", UNSET)

        ingress = d.pop("ingress", UNSET)

        progress = d.pop("progress", UNSET)

        visible = d.pop("visible", UNSET)

        computation = cls(
            status=status,
            definition=definition,
            id=id,
            created_at=created_at,
            local=local,
            description=description,
            error=error,
            results=results,
            updated_at=updated_at,
            egress=egress,
            started_at=started_at,
            ended_at=ended_at,
            ingress=ingress,
            progress=progress,
            visible=visible,
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
