from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.participant import Participant


T = TypeVar("T", bound="ProjectParticipantStatus")


@attr.s(auto_attribs=True)
class ProjectParticipantStatus:
    """regroups a project ID with the project's participant information.

    Attributes:
        participant (Union[Unset, Participant]): Node participating in a project
        project_id (Union[Unset, str]): Unique identifier of a project.
    """

    participant: Union[Unset, "Participant"] = UNSET
    project_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        participant: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.participant, Unset):
            participant = self.participant.to_dict()

        project_id = self.project_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if participant is not UNSET:
            field_dict["participant"] = participant
        if project_id is not UNSET:
            field_dict["projectId"] = project_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.participant import Participant

        d = src_dict.copy()
        _participant = d.pop("participant", UNSET)
        participant: Union[Unset, Participant]
        if isinstance(_participant, Unset):
            participant = UNSET
        else:
            participant = Participant.from_dict(_participant)

        project_id = d.pop("projectId", UNSET)

        project_participant_status = cls(
            participant=participant,
            project_id=project_id,
        )

        project_participant_status.additional_properties = d
        return project_participant_status

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
