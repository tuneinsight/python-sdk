from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.participant import Participant


T = TypeVar("T", bound="GetProjectStatusResponse200")


@attr.s(auto_attribs=True)
class GetProjectStatusResponse200:
    """
    Attributes:
        num_contributors (Union[Unset, int]): counts the current number of contributors in this project.
            This field is returned when the 'remote' parameter is set to true for the requesting instance to know if the
            project can be run.
        num_ready_contributors (Union[Unset, int]): counts the number of contributors in this project that are ready to
            run the project (connected data source + authorized the project).
            This field is returned when the 'remote' parameter is set to true for the requesting instance to know if the
            project can be run.
        participant (Union[Unset, Participant]): Node participating in a project
        remote_participants (Union[Unset, List['Participant']]):
    """

    num_contributors: Union[Unset, int] = UNSET
    num_ready_contributors: Union[Unset, int] = UNSET
    participant: Union[Unset, "Participant"] = UNSET
    remote_participants: Union[Unset, List["Participant"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        num_contributors = self.num_contributors
        num_ready_contributors = self.num_ready_contributors
        participant: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.participant, Unset):
            participant = self.participant.to_dict()

        remote_participants: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.remote_participants, Unset):
            remote_participants = []
            for remote_participants_item_data in self.remote_participants:
                remote_participants_item = remote_participants_item_data.to_dict()

                remote_participants.append(remote_participants_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if num_contributors is not UNSET:
            field_dict["numContributors"] = num_contributors
        if num_ready_contributors is not UNSET:
            field_dict["numReadyContributors"] = num_ready_contributors
        if participant is not UNSET:
            field_dict["participant"] = participant
        if remote_participants is not UNSET:
            field_dict["remoteParticipants"] = remote_participants

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.participant import Participant

        d = src_dict.copy()
        num_contributors = d.pop("numContributors", UNSET)

        num_ready_contributors = d.pop("numReadyContributors", UNSET)

        _participant = d.pop("participant", UNSET)
        participant: Union[Unset, Participant]
        if isinstance(_participant, Unset):
            participant = UNSET
        else:
            participant = Participant.from_dict(_participant)

        remote_participants = []
        _remote_participants = d.pop("remoteParticipants", UNSET)
        for remote_participants_item_data in _remote_participants or []:
            remote_participants_item = Participant.from_dict(remote_participants_item_data)

            remote_participants.append(remote_participants_item)

        get_project_status_response_200 = cls(
            num_contributors=num_contributors,
            num_ready_contributors=num_ready_contributors,
            participant=participant,
            remote_participants=remote_participants,
        )

        get_project_status_response_200.additional_properties = d
        return get_project_status_response_200

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
