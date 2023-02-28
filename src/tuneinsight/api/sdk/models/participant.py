from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.authorization_status import AuthorizationStatus
from ..models.data_source_metadata import DataSourceMetadata
from ..models.node import Node
from ..models.project_status import ProjectStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Participant")


@attr.s(auto_attribs=True)
class Participant:
    """Node participating in a project

    Attributes:
        authorization_status (Union[Unset, AuthorizationStatus]): Authorization status of the project
        input_metadata (Union[Unset, DataSourceMetadata]): metadata about a datasource
        node (Union[Unset, Node]): Node or agent of the network
        status (Union[Unset, ProjectStatus]): Stages of a project workflow
    """

    authorization_status: Union[Unset, AuthorizationStatus] = UNSET
    input_metadata: Union[Unset, DataSourceMetadata] = UNSET
    node: Union[Unset, Node] = UNSET
    status: Union[Unset, ProjectStatus] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        authorization_status: Union[Unset, str] = UNSET
        if not isinstance(self.authorization_status, Unset):
            authorization_status = self.authorization_status.value

        input_metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.input_metadata, Unset):
            input_metadata = self.input_metadata.to_dict()

        node: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.node, Unset):
            node = self.node.to_dict()

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authorization_status is not UNSET:
            field_dict["authorizationStatus"] = authorization_status
        if input_metadata is not UNSET:
            field_dict["inputMetadata"] = input_metadata
        if node is not UNSET:
            field_dict["node"] = node
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _authorization_status = d.pop("authorizationStatus", UNSET)
        authorization_status: Union[Unset, AuthorizationStatus]
        if isinstance(_authorization_status, Unset):
            authorization_status = UNSET
        else:
            authorization_status = AuthorizationStatus(_authorization_status)

        _input_metadata = d.pop("inputMetadata", UNSET)
        input_metadata: Union[Unset, DataSourceMetadata]
        if isinstance(_input_metadata, Unset):
            input_metadata = UNSET
        else:
            input_metadata = DataSourceMetadata.from_dict(_input_metadata)

        _node = d.pop("node", UNSET)
        node: Union[Unset, Node]
        if isinstance(_node, Unset):
            node = UNSET
        else:
            node = Node.from_dict(_node)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ProjectStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ProjectStatus(_status)

        participant = cls(
            authorization_status=authorization_status,
            input_metadata=input_metadata,
            node=node,
            status=status,
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
