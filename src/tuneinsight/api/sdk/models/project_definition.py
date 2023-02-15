from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.authorization_status import AuthorizationStatus
from ..models.topology import Topology
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.computation_definition import ComputationDefinition
    from ..models.project_policy import ProjectPolicy


T = TypeVar("T", bound="ProjectDefinition")


@attr.s(auto_attribs=True)
class ProjectDefinition:
    """
    Attributes:
        allow_clear_query (Union[Unset, bool]): [Dangerous, can lead to cross code data share] True if it is allowed for
            a client to query the data source all participants of the project and return the clear text result
        allow_shared_edit (Union[Unset, bool]): True if this project can be modified after being shared. Modifications
            of a shared project will be broadcasted to the network
        authorization_status (Union[Unset, AuthorizationStatus]): Authorization status of the project
        computation_definition (Union[Unset, ComputationDefinition]): Generic computation.
        created_by_node (Union[Unset, str]): ID of node where the project was first created
        created_by_user (Union[Unset, str]): ID of user who created the project
        data_source_auto_match (Union[Unset, bool]): whether or not to automatically assign the first matching
            datasource when the project is shared with other nodes
        data_source_id (Union[Unset, str]): Unique identifier of a data source.
        description (Union[Unset, str]):
        dpia (Union[Unset, str]):
        local (Union[Unset, bool]): True if the project's computation should run only with local data (not configured
            the network)
        locked (Union[Unset, bool]): True if the project is read-only (likely because it has already been shared)
        name (Union[Unset, str]):
        network_id (Union[Unset, str]): id to uniquely identify the network
        policy (Union[Unset, ProjectPolicy]): represents a policy used to validate requested computations in a
            collaboration
        query (Union[Unset, str]): String of the query a data source into a data object
        query_timeout (Union[Unset, int]): Timeout for the data source queries Default: 30.
        run_async (Union[Unset, bool]): flag indicating if computation should be run asynchronously
        shared (Union[Unset, bool]): True if the project has once been shared across the participants
        topology (Union[Unset, Topology]): Network Topologies. 'star' or 'tree'. In star topology all nodes are
            connected to a central node. In tree topology all nodes are connected and aware of each other.
        unique_id (Union[Unset, str]): Unique identifier of a project.
        workflow_json (Union[Unset, str]): JSON representation of the workflow UI in the frontend
        broadcast (Union[Unset, bool]): Temporary field. Always set to false. Only used for server-server communication
        data_source_type (Union[Unset, str]): Type of the data source to share to other nodes to match with their data
            source of the same type
        participants (Union[Unset, List[str]]): List of nodes involved in the project's collaboration
    """

    allow_clear_query: Union[Unset, bool] = UNSET
    allow_shared_edit: Union[Unset, bool] = UNSET
    authorization_status: Union[Unset, AuthorizationStatus] = UNSET
    computation_definition: Union[Unset, "ComputationDefinition"] = UNSET
    created_by_node: Union[Unset, str] = UNSET
    created_by_user: Union[Unset, str] = UNSET
    data_source_auto_match: Union[Unset, bool] = UNSET
    data_source_id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    dpia: Union[Unset, str] = UNSET
    local: Union[Unset, bool] = UNSET
    locked: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    network_id: Union[Unset, str] = UNSET
    policy: Union[Unset, "ProjectPolicy"] = UNSET
    query: Union[Unset, str] = UNSET
    query_timeout: Union[Unset, int] = 30
    run_async: Union[Unset, bool] = UNSET
    shared: Union[Unset, bool] = UNSET
    topology: Union[Unset, Topology] = UNSET
    unique_id: Union[Unset, str] = UNSET
    workflow_json: Union[Unset, str] = UNSET
    broadcast: Union[Unset, bool] = UNSET
    data_source_type: Union[Unset, str] = UNSET
    participants: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allow_clear_query = self.allow_clear_query
        allow_shared_edit = self.allow_shared_edit
        authorization_status: Union[Unset, str] = UNSET
        if not isinstance(self.authorization_status, Unset):
            authorization_status = self.authorization_status.value

        computation_definition: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.computation_definition, Unset):
            computation_definition = self.computation_definition.to_dict()

        created_by_node = self.created_by_node
        created_by_user = self.created_by_user
        data_source_auto_match = self.data_source_auto_match
        data_source_id = self.data_source_id
        description = self.description
        dpia = self.dpia
        local = self.local
        locked = self.locked
        name = self.name
        network_id = self.network_id
        policy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.policy, Unset):
            policy = self.policy.to_dict()

        query = self.query
        query_timeout = self.query_timeout
        run_async = self.run_async
        shared = self.shared
        topology: Union[Unset, str] = UNSET
        if not isinstance(self.topology, Unset):
            topology = self.topology.value

        unique_id = self.unique_id
        workflow_json = self.workflow_json
        broadcast = self.broadcast
        data_source_type = self.data_source_type
        participants: Union[Unset, List[str]] = UNSET
        if not isinstance(self.participants, Unset):
            participants = self.participants

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allow_clear_query is not UNSET:
            field_dict["allowClearQuery"] = allow_clear_query
        if allow_shared_edit is not UNSET:
            field_dict["allowSharedEdit"] = allow_shared_edit
        if authorization_status is not UNSET:
            field_dict["authorizationStatus"] = authorization_status
        if computation_definition is not UNSET:
            field_dict["computationDefinition"] = computation_definition
        if created_by_node is not UNSET:
            field_dict["createdByNode"] = created_by_node
        if created_by_user is not UNSET:
            field_dict["createdByUser"] = created_by_user
        if data_source_auto_match is not UNSET:
            field_dict["dataSourceAutoMatch"] = data_source_auto_match
        if data_source_id is not UNSET:
            field_dict["dataSourceId"] = data_source_id
        if description is not UNSET:
            field_dict["description"] = description
        if dpia is not UNSET:
            field_dict["dpia"] = dpia
        if local is not UNSET:
            field_dict["local"] = local
        if locked is not UNSET:
            field_dict["locked"] = locked
        if name is not UNSET:
            field_dict["name"] = name
        if network_id is not UNSET:
            field_dict["networkId"] = network_id
        if policy is not UNSET:
            field_dict["policy"] = policy
        if query is not UNSET:
            field_dict["query"] = query
        if query_timeout is not UNSET:
            field_dict["queryTimeout"] = query_timeout
        if run_async is not UNSET:
            field_dict["runAsync"] = run_async
        if shared is not UNSET:
            field_dict["shared"] = shared
        if topology is not UNSET:
            field_dict["topology"] = topology
        if unique_id is not UNSET:
            field_dict["uniqueId"] = unique_id
        if workflow_json is not UNSET:
            field_dict["workflowJSON"] = workflow_json
        if broadcast is not UNSET:
            field_dict["broadcast"] = broadcast
        if data_source_type is not UNSET:
            field_dict["dataSourceType"] = data_source_type
        if participants is not UNSET:
            field_dict["participants"] = participants

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.computation_definition import ComputationDefinition
        from ..models.project_policy import ProjectPolicy

        d = src_dict.copy()
        allow_clear_query = d.pop("allowClearQuery", UNSET)

        allow_shared_edit = d.pop("allowSharedEdit", UNSET)

        _authorization_status = d.pop("authorizationStatus", UNSET)
        authorization_status: Union[Unset, AuthorizationStatus]
        if isinstance(_authorization_status, Unset):
            authorization_status = UNSET
        else:
            authorization_status = AuthorizationStatus(_authorization_status)

        _computation_definition = d.pop("computationDefinition", UNSET)
        computation_definition: Union[Unset, ComputationDefinition]
        if isinstance(_computation_definition, Unset):
            computation_definition = UNSET
        else:
            computation_definition = ComputationDefinition.from_dict(_computation_definition)

        created_by_node = d.pop("createdByNode", UNSET)

        created_by_user = d.pop("createdByUser", UNSET)

        data_source_auto_match = d.pop("dataSourceAutoMatch", UNSET)

        data_source_id = d.pop("dataSourceId", UNSET)

        description = d.pop("description", UNSET)

        dpia = d.pop("dpia", UNSET)

        local = d.pop("local", UNSET)

        locked = d.pop("locked", UNSET)

        name = d.pop("name", UNSET)

        network_id = d.pop("networkId", UNSET)

        _policy = d.pop("policy", UNSET)
        policy: Union[Unset, ProjectPolicy]
        if isinstance(_policy, Unset):
            policy = UNSET
        else:
            policy = ProjectPolicy.from_dict(_policy)

        query = d.pop("query", UNSET)

        query_timeout = d.pop("queryTimeout", UNSET)

        run_async = d.pop("runAsync", UNSET)

        shared = d.pop("shared", UNSET)

        _topology = d.pop("topology", UNSET)
        topology: Union[Unset, Topology]
        if isinstance(_topology, Unset):
            topology = UNSET
        else:
            topology = Topology(_topology)

        unique_id = d.pop("uniqueId", UNSET)

        workflow_json = d.pop("workflowJSON", UNSET)

        broadcast = d.pop("broadcast", UNSET)

        data_source_type = d.pop("dataSourceType", UNSET)

        participants = cast(List[str], d.pop("participants", UNSET))

        project_definition = cls(
            allow_clear_query=allow_clear_query,
            allow_shared_edit=allow_shared_edit,
            authorization_status=authorization_status,
            computation_definition=computation_definition,
            created_by_node=created_by_node,
            created_by_user=created_by_user,
            data_source_auto_match=data_source_auto_match,
            data_source_id=data_source_id,
            description=description,
            dpia=dpia,
            local=local,
            locked=locked,
            name=name,
            network_id=network_id,
            policy=policy,
            query=query,
            query_timeout=query_timeout,
            run_async=run_async,
            shared=shared,
            topology=topology,
            unique_id=unique_id,
            workflow_json=workflow_json,
            broadcast=broadcast,
            data_source_type=data_source_type,
            participants=participants,
        )

        project_definition.additional_properties = d
        return project_definition

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
