from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.authorization_status import AuthorizationStatus
from ..models.participation_status import ParticipationStatus
from ..models.project_status import ProjectStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.availability_status import AvailabilityStatus
    from ..models.data_source import DataSource
    from ..models.data_source_metadata import DataSourceMetadata
    from ..models.node import Node


T = TypeVar("T", bound="Participant")


@attr.s(auto_attribs=True)
class Participant:
    """Node participating in a project

    Attributes:
        authorization_status (Union[Unset, AuthorizationStatus]): Authorization status of the project
        can_run_project (Union[Unset, AvailabilityStatus]): generic object that holds information about whether a
            resource or action is available to the user.
        connected_data_source (Union[Unset, DataSource]):
        data_sources (Union[Unset, List['DataSource']]): list of data sources exposed by this node
        input_metadata (Union[Unset, DataSourceMetadata]): metadata about a datasource
        is_contributor (Union[Unset, None, bool]):
        node (Union[Unset, Node]): Node or agent of the network
        participation_status (Union[Unset, ParticipationStatus]): participation state of a project's participant
        selected_data_source (Union[Unset, None, str]): Unique identifier of a data source.
        status (Union[Unset, ProjectStatus]): Stages of a project workflow
    """

    authorization_status: Union[Unset, AuthorizationStatus] = UNSET
    can_run_project: Union[Unset, "AvailabilityStatus"] = UNSET
    connected_data_source: Union[Unset, "DataSource"] = UNSET
    data_sources: Union[Unset, List["DataSource"]] = UNSET
    input_metadata: Union[Unset, "DataSourceMetadata"] = UNSET
    is_contributor: Union[Unset, None, bool] = UNSET
    node: Union[Unset, "Node"] = UNSET
    participation_status: Union[Unset, ParticipationStatus] = UNSET
    selected_data_source: Union[Unset, None, str] = UNSET
    status: Union[Unset, ProjectStatus] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        authorization_status: Union[Unset, str] = UNSET
        if not isinstance(self.authorization_status, Unset):
            authorization_status = self.authorization_status.value

        can_run_project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.can_run_project, Unset):
            can_run_project = self.can_run_project.to_dict()

        connected_data_source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.connected_data_source, Unset):
            connected_data_source = self.connected_data_source.to_dict()

        data_sources: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data_sources, Unset):
            data_sources = []
            for data_sources_item_data in self.data_sources:
                data_sources_item = data_sources_item_data.to_dict()

                data_sources.append(data_sources_item)

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

        selected_data_source = self.selected_data_source
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authorization_status is not UNSET:
            field_dict["authorizationStatus"] = authorization_status
        if can_run_project is not UNSET:
            field_dict["canRunProject"] = can_run_project
        if connected_data_source is not UNSET:
            field_dict["connectedDataSource"] = connected_data_source
        if data_sources is not UNSET:
            field_dict["dataSources"] = data_sources
        if input_metadata is not UNSET:
            field_dict["inputMetadata"] = input_metadata
        if is_contributor is not UNSET:
            field_dict["isContributor"] = is_contributor
        if node is not UNSET:
            field_dict["node"] = node
        if participation_status is not UNSET:
            field_dict["participationStatus"] = participation_status
        if selected_data_source is not UNSET:
            field_dict["selectedDataSource"] = selected_data_source
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.availability_status import AvailabilityStatus
        from ..models.data_source import DataSource
        from ..models.data_source_metadata import DataSourceMetadata
        from ..models.node import Node

        d = src_dict.copy()
        _authorization_status = d.pop("authorizationStatus", UNSET)
        authorization_status: Union[Unset, AuthorizationStatus]
        if isinstance(_authorization_status, Unset):
            authorization_status = UNSET
        else:
            authorization_status = AuthorizationStatus(_authorization_status)

        _can_run_project = d.pop("canRunProject", UNSET)
        can_run_project: Union[Unset, AvailabilityStatus]
        if isinstance(_can_run_project, Unset):
            can_run_project = UNSET
        else:
            can_run_project = AvailabilityStatus.from_dict(_can_run_project)

        _connected_data_source = d.pop("connectedDataSource", UNSET)
        connected_data_source: Union[Unset, DataSource]
        if isinstance(_connected_data_source, Unset):
            connected_data_source = UNSET
        else:
            connected_data_source = DataSource.from_dict(_connected_data_source)

        data_sources = []
        _data_sources = d.pop("dataSources", UNSET)
        for data_sources_item_data in _data_sources or []:
            data_sources_item = DataSource.from_dict(data_sources_item_data)

            data_sources.append(data_sources_item)

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

        selected_data_source = d.pop("selectedDataSource", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ProjectStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ProjectStatus(_status)

        participant = cls(
            authorization_status=authorization_status,
            can_run_project=can_run_project,
            connected_data_source=connected_data_source,
            data_sources=data_sources,
            input_metadata=input_metadata,
            is_contributor=is_contributor,
            node=node,
            participation_status=participation_status,
            selected_data_source=selected_data_source,
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
