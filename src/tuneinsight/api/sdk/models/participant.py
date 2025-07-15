from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.authorization_status import AuthorizationStatus
from ..models.participation_status import ParticipationStatus
from ..models.project_status import ProjectStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.availability_status import AvailabilityStatus
    from ..models.contribution_error import ContributionError
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
        contribution_error (Union[Unset, ContributionError]): represents a non-fatal error that is flagged whenever a
            participant fails to contribute data to a computation.
        data_sources (Union[Unset, List['DataSource']]): list of data sources exposed by this node
        input_metadata (Union[Unset, DataSourceMetadata]): metadata about a datasource
        is_contributor (Union[Unset, None, bool]):
        matches_auto_approve_specifications (Union[Unset, List['AvailabilityStatus']]): whether this project can be
            auto-approved by any of the instance's auto-approve specifications.
        matches_auto_reject_specifications (Union[Unset, List['AvailabilityStatus']]): whether this project would be
            auto-rejected by any of the instance's auto-reject specifications.
        node (Union[Unset, Node]): Node or agent of the network
        non_contributing_reason (Union[Unset, str]): Reason why the participant is not contributing to the project.
            Only shown when the participant is not a contributor in the computation.
        participation_status (Union[Unset, ParticipationStatus]): participation state of a project's participant
        query_time (Union[Unset, None, int]): Time in milliseconds that the participant took to run the query on its
            data source.
        selected_data_source (Union[Unset, None, str]): Unique identifier of a data source.
        status (Union[Unset, ProjectStatus]): Stages of a project workflow
    """

    authorization_status: Union[Unset, AuthorizationStatus] = UNSET
    can_run_project: Union[Unset, "AvailabilityStatus"] = UNSET
    connected_data_source: Union[Unset, "DataSource"] = UNSET
    contribution_error: Union[Unset, "ContributionError"] = UNSET
    data_sources: Union[Unset, List["DataSource"]] = UNSET
    input_metadata: Union[Unset, "DataSourceMetadata"] = UNSET
    is_contributor: Union[Unset, None, bool] = UNSET
    matches_auto_approve_specifications: Union[Unset, List["AvailabilityStatus"]] = UNSET
    matches_auto_reject_specifications: Union[Unset, List["AvailabilityStatus"]] = UNSET
    node: Union[Unset, "Node"] = UNSET
    non_contributing_reason: Union[Unset, str] = UNSET
    participation_status: Union[Unset, ParticipationStatus] = UNSET
    query_time: Union[Unset, None, int] = UNSET
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

        contribution_error: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contribution_error, Unset):
            contribution_error = self.contribution_error.to_dict()

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
        matches_auto_approve_specifications: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.matches_auto_approve_specifications, Unset):
            matches_auto_approve_specifications = []
            for matches_auto_approve_specifications_item_data in self.matches_auto_approve_specifications:
                matches_auto_approve_specifications_item = matches_auto_approve_specifications_item_data.to_dict()

                matches_auto_approve_specifications.append(matches_auto_approve_specifications_item)

        matches_auto_reject_specifications: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.matches_auto_reject_specifications, Unset):
            matches_auto_reject_specifications = []
            for matches_auto_reject_specifications_item_data in self.matches_auto_reject_specifications:
                matches_auto_reject_specifications_item = matches_auto_reject_specifications_item_data.to_dict()

                matches_auto_reject_specifications.append(matches_auto_reject_specifications_item)

        node: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.node, Unset):
            node = self.node.to_dict()

        non_contributing_reason = self.non_contributing_reason
        participation_status: Union[Unset, str] = UNSET
        if not isinstance(self.participation_status, Unset):
            participation_status = self.participation_status.value

        query_time = self.query_time
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
        if contribution_error is not UNSET:
            field_dict["contributionError"] = contribution_error
        if data_sources is not UNSET:
            field_dict["dataSources"] = data_sources
        if input_metadata is not UNSET:
            field_dict["inputMetadata"] = input_metadata
        if is_contributor is not UNSET:
            field_dict["isContributor"] = is_contributor
        if matches_auto_approve_specifications is not UNSET:
            field_dict["matchesAutoApproveSpecifications"] = matches_auto_approve_specifications
        if matches_auto_reject_specifications is not UNSET:
            field_dict["matchesAutoRejectSpecifications"] = matches_auto_reject_specifications
        if node is not UNSET:
            field_dict["node"] = node
        if non_contributing_reason is not UNSET:
            field_dict["nonContributingReason"] = non_contributing_reason
        if participation_status is not UNSET:
            field_dict["participationStatus"] = participation_status
        if query_time is not UNSET:
            field_dict["queryTime"] = query_time
        if selected_data_source is not UNSET:
            field_dict["selectedDataSource"] = selected_data_source
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.availability_status import AvailabilityStatus
        from ..models.contribution_error import ContributionError
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

        _contribution_error = d.pop("contributionError", UNSET)
        contribution_error: Union[Unset, ContributionError]
        if isinstance(_contribution_error, Unset):
            contribution_error = UNSET
        else:
            contribution_error = ContributionError.from_dict(_contribution_error)

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

        matches_auto_approve_specifications = []
        _matches_auto_approve_specifications = d.pop("matchesAutoApproveSpecifications", UNSET)
        for matches_auto_approve_specifications_item_data in _matches_auto_approve_specifications or []:
            matches_auto_approve_specifications_item = AvailabilityStatus.from_dict(
                matches_auto_approve_specifications_item_data
            )

            matches_auto_approve_specifications.append(matches_auto_approve_specifications_item)

        matches_auto_reject_specifications = []
        _matches_auto_reject_specifications = d.pop("matchesAutoRejectSpecifications", UNSET)
        for matches_auto_reject_specifications_item_data in _matches_auto_reject_specifications or []:
            matches_auto_reject_specifications_item = AvailabilityStatus.from_dict(
                matches_auto_reject_specifications_item_data
            )

            matches_auto_reject_specifications.append(matches_auto_reject_specifications_item)

        _node = d.pop("node", UNSET)
        node: Union[Unset, Node]
        if isinstance(_node, Unset):
            node = UNSET
        else:
            node = Node.from_dict(_node)

        non_contributing_reason = d.pop("nonContributingReason", UNSET)

        _participation_status = d.pop("participationStatus", UNSET)
        participation_status: Union[Unset, ParticipationStatus]
        if isinstance(_participation_status, Unset):
            participation_status = UNSET
        else:
            participation_status = ParticipationStatus(_participation_status)

        query_time = d.pop("queryTime", UNSET)

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
            contribution_error=contribution_error,
            data_sources=data_sources,
            input_metadata=input_metadata,
            is_contributor=is_contributor,
            matches_auto_approve_specifications=matches_auto_approve_specifications,
            matches_auto_reject_specifications=matches_auto_reject_specifications,
            node=node,
            non_contributing_reason=non_contributing_reason,
            participation_status=participation_status,
            query_time=query_time,
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
