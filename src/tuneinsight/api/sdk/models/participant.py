from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.authorization_status import AuthorizationStatus
from ..models.participation_status import ParticipationStatus
from ..models.project_status import ProjectStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_source_metadata import DataSourceMetadata
    from ..models.node import Node


T = TypeVar("T", bound="Participant")


@attr.s(auto_attribs=True)
class Participant:
    """Node participating in a project

    Attributes:
        input_metadata (Union[Unset, DataSourceMetadata]): metadata about a datasource
        is_contributor (Union[Unset, None, bool]):
        node (Union[Unset, Node]): Node or agent of the network
        participation_status (Union[Unset, ParticipationStatus]): participation state of a project's participant
        status (Union[Unset, ProjectStatus]): Stages of a project workflow
        authorization_status (Union[Unset, AuthorizationStatus]): Authorization status of the project
    """

    input_metadata: Union[Unset, "DataSourceMetadata"] = UNSET
    is_contributor: Union[Unset, None, bool] = UNSET
    node: Union[Unset, "Node"] = UNSET
    participation_status: Union[Unset, ParticipationStatus] = UNSET
    status: Union[Unset, ProjectStatus] = UNSET
    authorization_status: Union[Unset, AuthorizationStatus] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        input_metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.input_metadata, Unset):
            input_metadata = self.input_metadata.to_dict()

        is_contributor = self.is_contributor
        node: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.node, Unset):
            node = self.node.to_dict()

        participation_status: Union[Unset, str] = UNSET
        if not isinstance(self.participation_status, Unset):
            participation_status = self.participation_status.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        authorization_status: Union[Unset, str] = UNSET
        if not isinstance(self.authorization_status, Unset):
            authorization_status = self.authorization_status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if input_metadata is not UNSET:
            field_dict["inputMetadata"] = input_metadata
        if is_contributor is not UNSET:
            field_dict["isContributor"] = is_contributor
        if node is not UNSET:
            field_dict["node"] = node
        if participation_status is not UNSET:
            field_dict["participationStatus"] = participation_status
        if status is not UNSET:
            field_dict["status"] = status
        if authorization_status is not UNSET:
            field_dict["authorizationStatus"] = authorization_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_source_metadata import DataSourceMetadata
        from ..models.node import Node

        d = src_dict.copy()
        _input_metadata = d.pop("inputMetadata", UNSET)
        input_metadata: Union[Unset, DataSourceMetadata]
        if isinstance(_input_metadata, Unset):
            input_metadata = UNSET
        else:
            input_metadata = DataSourceMetadata.from_dict(_input_metadata)

        is_contributor = d.pop("isContributor", UNSET)

        _node = d.pop("node", UNSET)
        node: Union[Unset, Node]
        if isinstance(_node, Unset):
            node = UNSET
        else:
            node = Node.from_dict(_node)

        _participation_status = d.pop("participationStatus", UNSET)
        participation_status: Union[Unset, ParticipationStatus]
        if isinstance(_participation_status, Unset):
            participation_status = UNSET
        else:
            participation_status = ParticipationStatus(_participation_status)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ProjectStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ProjectStatus(_status)

        _authorization_status = d.pop("authorizationStatus", UNSET)
        authorization_status: Union[Unset, AuthorizationStatus]
        if isinstance(_authorization_status, Unset):
            authorization_status = UNSET
        else:
            authorization_status = AuthorizationStatus(_authorization_status)

        participant = cls(
            input_metadata=input_metadata,
            is_contributor=is_contributor,
            node=node,
            participation_status=participation_status,
            status=status,
            authorization_status=authorization_status,
        )

        participant.additional_properties = d
        return participant

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
