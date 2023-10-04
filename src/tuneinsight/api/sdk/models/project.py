from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.authorization_status import AuthorizationStatus
from ..models.client import Client
from ..models.project_base_workflow_type import ProjectBaseWorkflowType
from ..models.project_status import ProjectStatus
from ..models.topology import Topology
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.computation import Computation
    from ..models.computation_definition import ComputationDefinition
    from ..models.computation_policy import ComputationPolicy
    from ..models.data_source_query import DataSourceQuery
    from ..models.local_data_selection_definition import LocalDataSelectionDefinition
    from ..models.participant import Participant
    from ..models.privacy_summary import PrivacySummary


T = TypeVar("T", bound="Project")


@attr.s(auto_attribs=True)
class Project:
    """Project entity definition.

    Attributes:
        created_by_user (Union[Unset, str]): ID of user who created the project
        unique_id (Union[Unset, str]): Unique identifier of a project.
        name (Union[Unset, str]):
        policy (Union[Unset, ComputationPolicy]): policy to validate a specific computation
        query_timeout (Union[Unset, int]): Timeout for the data source queries Default: 30.
        topology (Union[Unset, Topology]): Network Topologies. 'star' or 'tree'. In star topology all nodes are
            connected to a central node. In tree topology all nodes are connected and aware of each other.
        allow_shared_edit (Union[Unset, bool]): True if this project can be modified after being shared. Modifications
            of a shared project will be broadcasted to the network
        data_source_auto_match (Union[Unset, bool]): whether or not to automatically assign the first matching
            datasource when the project is shared with other nodes
        local (Union[Unset, None, bool]): True if the project's computation should run only with local data (not
            configured the network)
        locked (Union[Unset, bool]): True if the project is read-only (likely because it has already been shared)
        workflow_type (Union[Unset, ProjectBaseWorkflowType]): type of the workflow UI in the frontend
        created_by_node (Union[Unset, str]): ID of node where the project was first created
        description (Union[Unset, None, str]):
        local_data_selection_definition (Union[Unset, LocalDataSelectionDefinition]): datasource selection definition. A
            selection is a "query" or data selection definition to run on the datasource
        query (Union[Unset, DataSourceQuery]): schema used for the query
        allow_clear_query (Union[Unset, bool]): [Dangerous, can lead to cross code data share] True if it is allowed for
            a client to query the data source all participants of the project and return the clear text result
        authorization_status (Union[Unset, AuthorizationStatus]): Authorization status of the project
        authorized_users (Union[Unset, List[str]]): The IDs of the users who can run the project
        computation_definition (Union[Unset, ComputationDefinition]): Generic computation.
        workflow_json (Union[Unset, str]): JSON representation of the workflow UI in the frontend
        run_async (Union[Unset, bool]): flag indicating if computation should be run asynchronously
        shared (Union[Unset, bool]): True if the project has once been shared across the participants
        created_with_client (Union[Unset, Client]): Type of client that communicates with the agent API
        data_source_id (Union[Unset, None, str]): Unique identifier of a data source.
        dpia (Union[Unset, str]):
        network_id (Union[Unset, str]): id to uniquely identify the network
        participants (Union[Unset, List['Participant']]): List of participants in the project
        privacy_summary (Union[Unset, PrivacySummary]): Privacy summary for a project
        status (Union[Unset, ProjectStatus]): Stages of a project workflow
        updated_at (Union[Unset, str]):
        workflow_description (Union[Unset, str]): dynamically generated markdown description of the distributed workflow
            that is currently configured with the project.
            Not to be confused with the project description which is set by the user that has created the project for
            informative purposes.
        computations (Union[Unset, List['Computation']]): List of computations of the project
        created_at (Union[Unset, str]):
        error (Union[Unset, str]): Description of a potential error that happened during the project lifespan
    """

    created_by_user: Union[Unset, str] = UNSET
    unique_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    policy: Union[Unset, "ComputationPolicy"] = UNSET
    query_timeout: Union[Unset, int] = 30
    topology: Union[Unset, Topology] = UNSET
    allow_shared_edit: Union[Unset, bool] = UNSET
    data_source_auto_match: Union[Unset, bool] = UNSET
    local: Union[Unset, None, bool] = UNSET
    locked: Union[Unset, bool] = UNSET
    workflow_type: Union[Unset, ProjectBaseWorkflowType] = UNSET
    created_by_node: Union[Unset, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    local_data_selection_definition: Union[Unset, "LocalDataSelectionDefinition"] = UNSET
    query: Union[Unset, "DataSourceQuery"] = UNSET
    allow_clear_query: Union[Unset, bool] = UNSET
    authorization_status: Union[Unset, AuthorizationStatus] = UNSET
    authorized_users: Union[Unset, List[str]] = UNSET
    computation_definition: Union[Unset, "ComputationDefinition"] = UNSET
    workflow_json: Union[Unset, str] = UNSET
    run_async: Union[Unset, bool] = UNSET
    shared: Union[Unset, bool] = UNSET
    created_with_client: Union[Unset, Client] = UNSET
    data_source_id: Union[Unset, None, str] = UNSET
    dpia: Union[Unset, str] = UNSET
    network_id: Union[Unset, str] = UNSET
    participants: Union[Unset, List["Participant"]] = UNSET
    privacy_summary: Union[Unset, "PrivacySummary"] = UNSET
    status: Union[Unset, ProjectStatus] = UNSET
    updated_at: Union[Unset, str] = UNSET
    workflow_description: Union[Unset, str] = UNSET
    computations: Union[Unset, List["Computation"]] = UNSET
    created_at: Union[Unset, str] = UNSET
    error: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_by_user = self.created_by_user
        unique_id = self.unique_id
        name = self.name
        policy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.policy, Unset):
            policy = self.policy.to_dict()

        query_timeout = self.query_timeout
        topology: Union[Unset, str] = UNSET
        if not isinstance(self.topology, Unset):
            topology = self.topology.value

        allow_shared_edit = self.allow_shared_edit
        data_source_auto_match = self.data_source_auto_match
        local = self.local
        locked = self.locked
        workflow_type: Union[Unset, str] = UNSET
        if not isinstance(self.workflow_type, Unset):
            workflow_type = self.workflow_type.value

        created_by_node = self.created_by_node
        description = self.description
        local_data_selection_definition: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.local_data_selection_definition, Unset):
            local_data_selection_definition = self.local_data_selection_definition.to_dict()

        query: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.query, Unset):
            query = self.query.to_dict()

        allow_clear_query = self.allow_clear_query
        authorization_status: Union[Unset, str] = UNSET
        if not isinstance(self.authorization_status, Unset):
            authorization_status = self.authorization_status.value

        authorized_users: Union[Unset, List[str]] = UNSET
        if not isinstance(self.authorized_users, Unset):
            authorized_users = self.authorized_users

        computation_definition: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.computation_definition, Unset):
            computation_definition = self.computation_definition.to_dict()

        workflow_json = self.workflow_json
        run_async = self.run_async
        shared = self.shared
        created_with_client: Union[Unset, str] = UNSET
        if not isinstance(self.created_with_client, Unset):
            created_with_client = self.created_with_client.value

        data_source_id = self.data_source_id
        dpia = self.dpia
        network_id = self.network_id
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
        workflow_description = self.workflow_description
        computations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.computations, Unset):
            computations = []
            for computations_item_data in self.computations:
                computations_item = computations_item_data.to_dict()

                computations.append(computations_item)

        created_at = self.created_at
        error = self.error

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_by_user is not UNSET:
            field_dict["createdByUser"] = created_by_user
        if unique_id is not UNSET:
            field_dict["uniqueId"] = unique_id
        if name is not UNSET:
            field_dict["name"] = name
        if policy is not UNSET:
            field_dict["policy"] = policy
        if query_timeout is not UNSET:
            field_dict["queryTimeout"] = query_timeout
        if topology is not UNSET:
            field_dict["topology"] = topology
        if allow_shared_edit is not UNSET:
            field_dict["allowSharedEdit"] = allow_shared_edit
        if data_source_auto_match is not UNSET:
            field_dict["dataSourceAutoMatch"] = data_source_auto_match
        if local is not UNSET:
            field_dict["local"] = local
        if locked is not UNSET:
            field_dict["locked"] = locked
        if workflow_type is not UNSET:
            field_dict["workflowType"] = workflow_type
        if created_by_node is not UNSET:
            field_dict["createdByNode"] = created_by_node
        if description is not UNSET:
            field_dict["description"] = description
        if local_data_selection_definition is not UNSET:
            field_dict["localDataSelectionDefinition"] = local_data_selection_definition
        if query is not UNSET:
            field_dict["query"] = query
        if allow_clear_query is not UNSET:
            field_dict["allowClearQuery"] = allow_clear_query
        if authorization_status is not UNSET:
            field_dict["authorizationStatus"] = authorization_status
        if authorized_users is not UNSET:
            field_dict["authorizedUsers"] = authorized_users
        if computation_definition is not UNSET:
            field_dict["computationDefinition"] = computation_definition
        if workflow_json is not UNSET:
            field_dict["workflowJSON"] = workflow_json
        if run_async is not UNSET:
            field_dict["runAsync"] = run_async
        if shared is not UNSET:
            field_dict["shared"] = shared
        if created_with_client is not UNSET:
            field_dict["createdWithClient"] = created_with_client
        if data_source_id is not UNSET:
            field_dict["dataSourceId"] = data_source_id
        if dpia is not UNSET:
            field_dict["dpia"] = dpia
        if network_id is not UNSET:
            field_dict["networkId"] = network_id
        if participants is not UNSET:
            field_dict["participants"] = participants
        if privacy_summary is not UNSET:
            field_dict["privacySummary"] = privacy_summary
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if workflow_description is not UNSET:
            field_dict["workflowDescription"] = workflow_description
        if computations is not UNSET:
            field_dict["computations"] = computations
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.computation import Computation
        from ..models.computation_definition import ComputationDefinition
        from ..models.computation_policy import ComputationPolicy
        from ..models.data_source_query import DataSourceQuery
        from ..models.local_data_selection_definition import LocalDataSelectionDefinition
        from ..models.participant import Participant
        from ..models.privacy_summary import PrivacySummary

        d = src_dict.copy()
        created_by_user = d.pop("createdByUser", UNSET)

        unique_id = d.pop("uniqueId", UNSET)

        name = d.pop("name", UNSET)

        _policy = d.pop("policy", UNSET)
        policy: Union[Unset, ComputationPolicy]
        if isinstance(_policy, Unset):
            policy = UNSET
        else:
            policy = ComputationPolicy.from_dict(_policy)

        query_timeout = d.pop("queryTimeout", UNSET)

        _topology = d.pop("topology", UNSET)
        topology: Union[Unset, Topology]
        if isinstance(_topology, Unset):
            topology = UNSET
        else:
            topology = Topology(_topology)

        allow_shared_edit = d.pop("allowSharedEdit", UNSET)

        data_source_auto_match = d.pop("dataSourceAutoMatch", UNSET)

        local = d.pop("local", UNSET)

        locked = d.pop("locked", UNSET)

        _workflow_type = d.pop("workflowType", UNSET)
        workflow_type: Union[Unset, ProjectBaseWorkflowType]
        if isinstance(_workflow_type, Unset):
            workflow_type = UNSET
        else:
            workflow_type = ProjectBaseWorkflowType(_workflow_type)

        created_by_node = d.pop("createdByNode", UNSET)

        description = d.pop("description", UNSET)

        _local_data_selection_definition = d.pop("localDataSelectionDefinition", UNSET)
        local_data_selection_definition: Union[Unset, LocalDataSelectionDefinition]
        if isinstance(_local_data_selection_definition, Unset):
            local_data_selection_definition = UNSET
        else:
            local_data_selection_definition = LocalDataSelectionDefinition.from_dict(_local_data_selection_definition)

        _query = d.pop("query", UNSET)
        query: Union[Unset, DataSourceQuery]
        if isinstance(_query, Unset):
            query = UNSET
        else:
            query = DataSourceQuery.from_dict(_query)

        allow_clear_query = d.pop("allowClearQuery", UNSET)

        _authorization_status = d.pop("authorizationStatus", UNSET)
        authorization_status: Union[Unset, AuthorizationStatus]
        if isinstance(_authorization_status, Unset):
            authorization_status = UNSET
        else:
            authorization_status = AuthorizationStatus(_authorization_status)

        authorized_users = cast(List[str], d.pop("authorizedUsers", UNSET))

        _computation_definition = d.pop("computationDefinition", UNSET)
        computation_definition: Union[Unset, ComputationDefinition]
        if isinstance(_computation_definition, Unset):
            computation_definition = UNSET
        else:
            computation_definition = ComputationDefinition.from_dict(_computation_definition)

        workflow_json = d.pop("workflowJSON", UNSET)

        run_async = d.pop("runAsync", UNSET)

        shared = d.pop("shared", UNSET)

        _created_with_client = d.pop("createdWithClient", UNSET)
        created_with_client: Union[Unset, Client]
        if isinstance(_created_with_client, Unset):
            created_with_client = UNSET
        else:
            created_with_client = Client(_created_with_client)

        data_source_id = d.pop("dataSourceId", UNSET)

        dpia = d.pop("dpia", UNSET)

        network_id = d.pop("networkId", UNSET)

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

        workflow_description = d.pop("workflowDescription", UNSET)

        computations = []
        _computations = d.pop("computations", UNSET)
        for computations_item_data in _computations or []:
            computations_item = Computation.from_dict(computations_item_data)

            computations.append(computations_item)

        created_at = d.pop("createdAt", UNSET)

        error = d.pop("error", UNSET)

        project = cls(
            created_by_user=created_by_user,
            unique_id=unique_id,
            name=name,
            policy=policy,
            query_timeout=query_timeout,
            topology=topology,
            allow_shared_edit=allow_shared_edit,
            data_source_auto_match=data_source_auto_match,
            local=local,
            locked=locked,
            workflow_type=workflow_type,
            created_by_node=created_by_node,
            description=description,
            local_data_selection_definition=local_data_selection_definition,
            query=query,
            allow_clear_query=allow_clear_query,
            authorization_status=authorization_status,
            authorized_users=authorized_users,
            computation_definition=computation_definition,
            workflow_json=workflow_json,
            run_async=run_async,
            shared=shared,
            created_with_client=created_with_client,
            data_source_id=data_source_id,
            dpia=dpia,
            network_id=network_id,
            participants=participants,
            privacy_summary=privacy_summary,
            status=status,
            updated_at=updated_at,
            workflow_description=workflow_description,
            computations=computations,
            created_at=created_at,
            error=error,
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
