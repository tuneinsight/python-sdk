from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.authorization_status import AuthorizationStatus
from ..models.project_status import ProjectStatus
from ..models.topology import Topology
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.computation import Computation
    from ..models.computation_definition import ComputationDefinition
    from ..models.participant import Participant
    from ..models.privacy_summary import PrivacySummary
    from ..models.project_policy import ProjectPolicy


T = TypeVar("T", bound="Project")


@attr.s(auto_attribs=True)
class Project:
    """Project entity definition.

    Attributes:
        computation_definition (Union[Unset, ComputationDefinition]): Generic computation.
        dpia (Union[Unset, str]):
        policy (Union[Unset, ProjectPolicy]): represents a policy used to validate requested computations in a
            collaboration
        query (Union[Unset, str]): String of the query a data source into a data object
        unique_id (Union[Unset, str]): Unique identifier of a project.
        allow_shared_edit (Union[Unset, bool]): True if this project can be modified after being shared. Modifications
            of a shared project will be broadcasted to the network
        created_by_user (Union[Unset, str]): ID of user who created the project
        data_source_id (Union[Unset, None, str]): Unique identifier of a data source.
        description (Union[Unset, None, str]):
        locked (Union[Unset, bool]): True if the project is read-only (likely because it has already been shared)
        shared (Union[Unset, bool]): True if the project has once been shared across the participants
        allow_clear_query (Union[Unset, bool]): [Dangerous, can lead to cross code data share] True if it is allowed for
            a client to query the data source all participants of the project and return the clear text result
        query_timeout (Union[Unset, int]): Timeout for the data source queries Default: 30.
        authorization_status (Union[Unset, AuthorizationStatus]): Authorization status of the project
        created_by_node (Union[Unset, str]): ID of node where the project was first created
        data_source_auto_match (Union[Unset, bool]): whether or not to automatically assign the first matching
            datasource when the project is shared with other nodes
        local (Union[Unset, None, bool]): True if the project's computation should run only with local data (not
            configured the network)
        name (Union[Unset, str]):
        network_id (Union[Unset, str]): id to uniquely identify the network
        run_async (Union[Unset, bool]): flag indicating if computation should be run asynchronously
        topology (Union[Unset, Topology]): Network Topologies. 'star' or 'tree'. In star topology all nodes are
            connected to a central node. In tree topology all nodes are connected and aware of each other.
        workflow_json (Union[Unset, str]): JSON representation of the workflow UI in the frontend
        computations (Union[Unset, List['Computation']]): List of computations of the project
        created_at (Union[Unset, str]):
        error (Union[Unset, str]): Description of a potential error that happened during the project lifespan
        participants (Union[Unset, List['Participant']]): List of participants in the project
        privacy_summary (Union[Unset, PrivacySummary]): Privacy summary for a project
        status (Union[Unset, ProjectStatus]): Stages of a project workflow
        updated_at (Union[Unset, str]):
    """

    computation_definition: Union[Unset, "ComputationDefinition"] = UNSET
    dpia: Union[Unset, str] = UNSET
    policy: Union[Unset, "ProjectPolicy"] = UNSET
    query: Union[Unset, str] = UNSET
    unique_id: Union[Unset, str] = UNSET
    allow_shared_edit: Union[Unset, bool] = UNSET
    created_by_user: Union[Unset, str] = UNSET
    data_source_id: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    locked: Union[Unset, bool] = UNSET
    shared: Union[Unset, bool] = UNSET
    allow_clear_query: Union[Unset, bool] = UNSET
    query_timeout: Union[Unset, int] = 30
    authorization_status: Union[Unset, AuthorizationStatus] = UNSET
    created_by_node: Union[Unset, str] = UNSET
    data_source_auto_match: Union[Unset, bool] = UNSET
    local: Union[Unset, None, bool] = UNSET
    name: Union[Unset, str] = UNSET
    network_id: Union[Unset, str] = UNSET
    run_async: Union[Unset, bool] = UNSET
    topology: Union[Unset, Topology] = UNSET
    workflow_json: Union[Unset, str] = UNSET
    computations: Union[Unset, List["Computation"]] = UNSET
    created_at: Union[Unset, str] = UNSET
    error: Union[Unset, str] = UNSET
    participants: Union[Unset, List["Participant"]] = UNSET
    privacy_summary: Union[Unset, "PrivacySummary"] = UNSET
    status: Union[Unset, ProjectStatus] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        computation_definition: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.computation_definition, Unset):
            computation_definition = self.computation_definition.to_dict()

        dpia = self.dpia
        policy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.policy, Unset):
            policy = self.policy.to_dict()

        query = self.query
        unique_id = self.unique_id
        allow_shared_edit = self.allow_shared_edit
        created_by_user = self.created_by_user
        data_source_id = self.data_source_id
        description = self.description
        locked = self.locked
        shared = self.shared
        allow_clear_query = self.allow_clear_query
        query_timeout = self.query_timeout
        authorization_status: Union[Unset, str] = UNSET
        if not isinstance(self.authorization_status, Unset):
            authorization_status = self.authorization_status.value

        created_by_node = self.created_by_node
        data_source_auto_match = self.data_source_auto_match
        local = self.local
        name = self.name
        network_id = self.network_id
        run_async = self.run_async
        topology: Union[Unset, str] = UNSET
        if not isinstance(self.topology, Unset):
            topology = self.topology.value

        workflow_json = self.workflow_json
        computations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.computations, Unset):
            computations = []
            for computations_item_data in self.computations:
                computations_item = computations_item_data.to_dict()

                computations.append(computations_item)

        created_at = self.created_at
        error = self.error
        participants: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.participants, Unset):
            participants = []
            for participants_item_data in self.participants:
                participants_item = participants_item_data.to_dict()

                participants.append(participants_item)

        privacy_summary: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.privacy_summary, Unset):
            privacy_summary = self.privacy_summary.to_dict()

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if computation_definition is not UNSET:
            field_dict["computationDefinition"] = computation_definition
        if dpia is not UNSET:
            field_dict["dpia"] = dpia
        if policy is not UNSET:
            field_dict["policy"] = policy
        if query is not UNSET:
            field_dict["query"] = query
        if unique_id is not UNSET:
            field_dict["uniqueId"] = unique_id
        if allow_shared_edit is not UNSET:
            field_dict["allowSharedEdit"] = allow_shared_edit
        if created_by_user is not UNSET:
            field_dict["createdByUser"] = created_by_user
        if data_source_id is not UNSET:
            field_dict["dataSourceId"] = data_source_id
        if description is not UNSET:
            field_dict["description"] = description
        if locked is not UNSET:
            field_dict["locked"] = locked
        if shared is not UNSET:
            field_dict["shared"] = shared
        if allow_clear_query is not UNSET:
            field_dict["allowClearQuery"] = allow_clear_query
        if query_timeout is not UNSET:
            field_dict["queryTimeout"] = query_timeout
        if authorization_status is not UNSET:
            field_dict["authorizationStatus"] = authorization_status
        if created_by_node is not UNSET:
            field_dict["createdByNode"] = created_by_node
        if data_source_auto_match is not UNSET:
            field_dict["dataSourceAutoMatch"] = data_source_auto_match
        if local is not UNSET:
            field_dict["local"] = local
        if name is not UNSET:
            field_dict["name"] = name
        if network_id is not UNSET:
            field_dict["networkId"] = network_id
        if run_async is not UNSET:
            field_dict["runAsync"] = run_async
        if topology is not UNSET:
            field_dict["topology"] = topology
        if workflow_json is not UNSET:
            field_dict["workflowJSON"] = workflow_json
        if computations is not UNSET:
            field_dict["computations"] = computations
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if error is not UNSET:
            field_dict["error"] = error
        if participants is not UNSET:
            field_dict["participants"] = participants
        if privacy_summary is not UNSET:
            field_dict["privacySummary"] = privacy_summary
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.computation import Computation
        from ..models.computation_definition import ComputationDefinition
        from ..models.participant import Participant
        from ..models.privacy_summary import PrivacySummary
        from ..models.project_policy import ProjectPolicy

        d = src_dict.copy()
        _computation_definition = d.pop("computationDefinition", UNSET)
        computation_definition: Union[Unset, ComputationDefinition]
        if isinstance(_computation_definition, Unset):
            computation_definition = UNSET
        else:
            computation_definition = ComputationDefinition.from_dict(_computation_definition)

        dpia = d.pop("dpia", UNSET)

        _policy = d.pop("policy", UNSET)
        policy: Union[Unset, ProjectPolicy]
        if isinstance(_policy, Unset):
            policy = UNSET
        else:
            policy = ProjectPolicy.from_dict(_policy)

        query = d.pop("query", UNSET)

        unique_id = d.pop("uniqueId", UNSET)

        allow_shared_edit = d.pop("allowSharedEdit", UNSET)

        created_by_user = d.pop("createdByUser", UNSET)

        data_source_id = d.pop("dataSourceId", UNSET)

        description = d.pop("description", UNSET)

        locked = d.pop("locked", UNSET)

        shared = d.pop("shared", UNSET)

        allow_clear_query = d.pop("allowClearQuery", UNSET)

        query_timeout = d.pop("queryTimeout", UNSET)

        _authorization_status = d.pop("authorizationStatus", UNSET)
        authorization_status: Union[Unset, AuthorizationStatus]
        if isinstance(_authorization_status, Unset):
            authorization_status = UNSET
        else:
            authorization_status = AuthorizationStatus(_authorization_status)

        created_by_node = d.pop("createdByNode", UNSET)

        data_source_auto_match = d.pop("dataSourceAutoMatch", UNSET)

        local = d.pop("local", UNSET)

        name = d.pop("name", UNSET)

        network_id = d.pop("networkId", UNSET)

        run_async = d.pop("runAsync", UNSET)

        _topology = d.pop("topology", UNSET)
        topology: Union[Unset, Topology]
        if isinstance(_topology, Unset):
            topology = UNSET
        else:
            topology = Topology(_topology)

        workflow_json = d.pop("workflowJSON", UNSET)

        computations = []
        _computations = d.pop("computations", UNSET)
        for computations_item_data in _computations or []:
            computations_item = Computation.from_dict(computations_item_data)

            computations.append(computations_item)

        created_at = d.pop("createdAt", UNSET)

        error = d.pop("error", UNSET)

        participants = []
        _participants = d.pop("participants", UNSET)
        for participants_item_data in _participants or []:
            participants_item = Participant.from_dict(participants_item_data)

            participants.append(participants_item)

        _privacy_summary = d.pop("privacySummary", UNSET)
        privacy_summary: Union[Unset, PrivacySummary]
        if isinstance(_privacy_summary, Unset):
            privacy_summary = UNSET
        else:
            privacy_summary = PrivacySummary.from_dict(_privacy_summary)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ProjectStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ProjectStatus(_status)

        updated_at = d.pop("updatedAt", UNSET)

        project = cls(
            computation_definition=computation_definition,
            dpia=dpia,
            policy=policy,
            query=query,
            unique_id=unique_id,
            allow_shared_edit=allow_shared_edit,
            created_by_user=created_by_user,
            data_source_id=data_source_id,
            description=description,
            locked=locked,
            shared=shared,
            allow_clear_query=allow_clear_query,
            query_timeout=query_timeout,
            authorization_status=authorization_status,
            created_by_node=created_by_node,
            data_source_auto_match=data_source_auto_match,
            local=local,
            name=name,
            network_id=network_id,
            run_async=run_async,
            topology=topology,
            workflow_json=workflow_json,
            computations=computations,
            created_at=created_at,
            error=error,
            participants=participants,
            privacy_summary=privacy_summary,
            status=status,
            updated_at=updated_at,
        )

        project.additional_properties = d
        return project

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
