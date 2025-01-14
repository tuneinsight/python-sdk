from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.computation_definition import ComputationDefinition
    from ..models.participant import Participant


T = TypeVar("T", bound="ProtocolDefinition")


@attr.s(auto_attribs=True)
class ProtocolDefinition:
    """A new protocol request definition

    Attributes:
        computation (Union[Unset, ComputationDefinition]): Generic computation.
        computation_id (Union[Unset, str]): Identifier of a computation, unique across all computing nodes.
        participants (Union[Unset, List['Participant']]):
        requesting_instance (Union[Unset, str]): identifier/alias/name of the instance that has requested the
            computation
    """

    computation: Union[Unset, "ComputationDefinition"] = UNSET
    computation_id: Union[Unset, str] = UNSET
    participants: Union[Unset, List["Participant"]] = UNSET
    requesting_instance: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        computation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.computation, Unset):
            computation = self.computation.to_dict()

        computation_id = self.computation_id
        participants: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.participants, Unset):
            participants = []
            for participants_item_data in self.participants:
                participants_item = participants_item_data.to_dict()

                participants.append(participants_item)

        requesting_instance = self.requesting_instance

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if computation is not UNSET:
            field_dict["computation"] = computation
        if computation_id is not UNSET:
            field_dict["computationId"] = computation_id
        if participants is not UNSET:
            field_dict["participants"] = participants
        if requesting_instance is not UNSET:
            field_dict["requestingInstance"] = requesting_instance

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.computation_definition import ComputationDefinition
        from ..models.participant import Participant

        d = src_dict.copy()
        _computation = d.pop("computation", UNSET)
        computation: Union[Unset, ComputationDefinition]
        if isinstance(_computation, Unset):
            computation = UNSET
        else:
            computation = ComputationDefinition.from_dict(_computation)

        computation_id = d.pop("computationId", UNSET)

        participants = []
        _participants = d.pop("participants", UNSET)
        for participants_item_data in _participants or []:
            participants_item = Participant.from_dict(participants_item_data)

            participants.append(participants_item)

        requesting_instance = d.pop("requestingInstance", UNSET)

        protocol_definition = cls(
            computation=computation,
            computation_id=computation_id,
            participants=participants,
            requesting_instance=requesting_instance,
        )

        protocol_definition.additional_properties = d
        return protocol_definition

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
