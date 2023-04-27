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
        definition (ComputationDefinition): Generic computation.
        id (str): Identifier of a computation, unique across all computing nodes.
        status (ComputationStatus): Status of the computation.
        created_at (Union[Unset, str]):
        description (Union[Unset, str]):
        egress (Union[Unset, int]): keeps track of the number of bytes sent during a computation to serve as a bandwidth
            measure
        ended_at (Union[Unset, str]):
        error (Union[Unset, List[str]]): Error messages.
        ingress (Union[Unset, int]): keeps track of the number of bytes received during a computation to serve as a
            bandwidth measure
        local (Union[Unset, bool]):
        progress (Union[Unset, int]):
        results (Union[Unset, List[str]]): Identifier(s) of the resulting data object(s). Available only when the status
            is completed.
        started_at (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        visible (Union[Unset, bool]): False if the computation is internal and should not be displayed to the user by
            default
    """

    definition: "ComputationDefinition"
    id: str
    status: ComputationStatus
    created_at: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    egress: Union[Unset, int] = UNSET
    ended_at: Union[Unset, str] = UNSET
    error: Union[Unset, List[str]] = UNSET
    ingress: Union[Unset, int] = UNSET
    local: Union[Unset, bool] = UNSET
    progress: Union[Unset, int] = UNSET
    results: Union[Unset, List[str]] = UNSET
    started_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    visible: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        definition = self.definition.to_dict()

        id = self.id
        status = self.status.value

        created_at = self.created_at
        description = self.description
        egress = self.egress
        ended_at = self.ended_at
        error: Union[Unset, List[str]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error

        ingress = self.ingress
        local = self.local
        progress = self.progress
        results: Union[Unset, List[str]] = UNSET
        if not isinstance(self.results, Unset):
            results = self.results

        started_at = self.started_at
        updated_at = self.updated_at
        visible = self.visible

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
        if description is not UNSET:
            field_dict["description"] = description
        if egress is not UNSET:
            field_dict["egress"] = egress
        if ended_at is not UNSET:
            field_dict["endedAt"] = ended_at
        if error is not UNSET:
            field_dict["error"] = error
        if ingress is not UNSET:
            field_dict["ingress"] = ingress
        if local is not UNSET:
            field_dict["local"] = local
        if progress is not UNSET:
            field_dict["progress"] = progress
        if results is not UNSET:
            field_dict["results"] = results
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if visible is not UNSET:
            field_dict["visible"] = visible

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.computation_definition import ComputationDefinition

        d = src_dict.copy()
        definition = ComputationDefinition.from_dict(d.pop("definition"))

        id = d.pop("id")

        status = ComputationStatus(d.pop("status"))

        created_at = d.pop("createdAt", UNSET)

        description = d.pop("description", UNSET)

        egress = d.pop("egress", UNSET)

        ended_at = d.pop("endedAt", UNSET)

        error = cast(List[str], d.pop("error", UNSET))

        ingress = d.pop("ingress", UNSET)

        local = d.pop("local", UNSET)

        progress = d.pop("progress", UNSET)

        results = cast(List[str], d.pop("results", UNSET))

        started_at = d.pop("startedAt", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        visible = d.pop("visible", UNSET)

        computation = cls(
            definition=definition,
            id=id,
            status=status,
            created_at=created_at,
            description=description,
            egress=egress,
            ended_at=ended_at,
            error=error,
            ingress=ingress,
            local=local,
            progress=progress,
            results=results,
            started_at=started_at,
            updated_at=updated_at,
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
