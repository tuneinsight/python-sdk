from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.authorization_status import AuthorizationStatus
from ..models.client import Client
from ..models.project_base_workflow_type import ProjectBaseWorkflowType
from ..models.topology import Topology
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.computation_definition import ComputationDefinition
    from ..models.computation_policy import ComputationPolicy
    from ..models.data_source_query import DataSourceQuery
    from ..models.local_data_selection_definition import LocalDataSelectionDefinition


T = TypeVar("T", bound="ProjectBase")


@attr.s(auto_attribs=True)
class ProjectBase:
    """Common fields of a project (for get, patch and post)

    Attributes:
        data_source_auto_match (Union[Unset, bool]): whether or not to automatically assign the first matching
            datasource when the project is shared with other nodes
        name (Union[Unset, str]):
        query (Union[Unset, DataSourceQuery]): schema used for the query
        run_async (Union[Unset, bool]): flag indicating if computation should be run asynchronously
        topology (Union[Unset, Topology]): Network Topologies. 'star' or 'tree'. In star topology all nodes are
            connected to a central node. In tree topology all nodes are connected and aware of each other.
        allow_clear_query (Union[Unset, bool]): [Dangerous, can lead to cross code data share] True if it is allowed for
            a client to query the data source all participants of the project and return the clear text result
        workflow_json (Union[Unset, str]): JSON representation of the workflow UI in the frontend
        query_timeout (Union[Unset, int]): Timeout for the data source queries Default: 30.
        authorization_status (Union[Unset, AuthorizationStatus]): Authorization status of the project
        compute_only (Union[Unset, bool]): indicates that the current project participant only computes but does not
            contribute any data
        created_with_client (Union[Unset, Client]): Type of client that communicates with the agent API
        description (Union[Unset, None, str]):
        local (Union[Unset, None, bool]): True if the project's computation should run only with local data (not
            configured the network)
        created_by_node (Union[Unset, str]): ID of node where the project was first created
        workflow_type (Union[Unset, ProjectBaseWorkflowType]): type of the workflow UI in the frontend
        authorized_users (Union[Unset, List[str]]): The IDs of the users who can run the project
        locked (Union[Unset, None, bool]): True if the project is read-only (likely because it has already been shared)
        allow_shared_edit (Union[Unset, bool]): True if this project can be modified after being shared. Modifications
            of a shared project will be broadcasted to the network
        local_data_selection_definition (Union[Unset, LocalDataSelectionDefinition]): datasource selection definition. A
            selection is a "query" or data selection definition to run on the datasource
        min_contributors (Union[Unset, None, int]): minimum number of participants that contribute with their data
            required to run computations within this project
        network_id (Union[Unset, str]): id to uniquely identify the network
        policy (Union[Unset, ComputationPolicy]): policy to validate a specific computation
        computation_definition (Union[Unset, ComputationDefinition]): Generic computation.
        created_by_user (Union[Unset, str]): ID of user who created the project
        data_source_id (Union[Unset, None, str]): Unique identifier of a data source.
        dpia (Union[Unset, str]):
        shared (Union[Unset, bool]): True if the project has once been shared across the participants
        unique_id (Union[Unset, str]): Unique identifier of a project.
    """

    data_source_auto_match: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    query: Union[Unset, "DataSourceQuery"] = UNSET
    run_async: Union[Unset, bool] = UNSET
    topology: Union[Unset, Topology] = UNSET
    allow_clear_query: Union[Unset, bool] = UNSET
    workflow_json: Union[Unset, str] = UNSET
    query_timeout: Union[Unset, int] = 30
    authorization_status: Union[Unset, AuthorizationStatus] = UNSET
    compute_only: Union[Unset, bool] = UNSET
    created_with_client: Union[Unset, Client] = UNSET
    description: Union[Unset, None, str] = UNSET
    local: Union[Unset, None, bool] = UNSET
    created_by_node: Union[Unset, str] = UNSET
    workflow_type: Union[Unset, ProjectBaseWorkflowType] = UNSET
    authorized_users: Union[Unset, List[str]] = UNSET
    locked: Union[Unset, None, bool] = UNSET
    allow_shared_edit: Union[Unset, bool] = UNSET
    local_data_selection_definition: Union[Unset, "LocalDataSelectionDefinition"] = UNSET
    min_contributors: Union[Unset, None, int] = UNSET
    network_id: Union[Unset, str] = UNSET
    policy: Union[Unset, "ComputationPolicy"] = UNSET
    computation_definition: Union[Unset, "ComputationDefinition"] = UNSET
    created_by_user: Union[Unset, str] = UNSET
    data_source_id: Union[Unset, None, str] = UNSET
    dpia: Union[Unset, str] = UNSET
    shared: Union[Unset, bool] = UNSET
    unique_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data_source_auto_match = self.data_source_auto_match
        name = self.name
        query: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.query, Unset):
            query = self.query.to_dict()

        run_async = self.run_async
        topology: Union[Unset, str] = UNSET
        if not isinstance(self.topology, Unset):
            topology = self.topology.value

        allow_clear_query = self.allow_clear_query
        workflow_json = self.workflow_json
        query_timeout = self.query_timeout
        authorization_status: Union[Unset, str] = UNSET
        if not isinstance(self.authorization_status, Unset):
            authorization_status = self.authorization_status.value

        compute_only = self.compute_only
        created_with_client: Union[Unset, str] = UNSET
        if not isinstance(self.created_with_client, Unset):
            created_with_client = self.created_with_client.value

        description = self.description
        local = self.local
        created_by_node = self.created_by_node
        workflow_type: Union[Unset, str] = UNSET
        if not isinstance(self.workflow_type, Unset):
            workflow_type = self.workflow_type.value

        authorized_users: Union[Unset, List[str]] = UNSET
        if not isinstance(self.authorized_users, Unset):
            authorized_users = self.authorized_users

        locked = self.locked
        allow_shared_edit = self.allow_shared_edit
        local_data_selection_definition: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.local_data_selection_definition, Unset):
            local_data_selection_definition = self.local_data_selection_definition.to_dict()

        min_contributors = self.min_contributors
        network_id = self.network_id
        policy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.policy, Unset):
            policy = self.policy.to_dict()

        computation_definition: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.computation_definition, Unset):
            computation_definition = self.computation_definition.to_dict()

        created_by_user = self.created_by_user
        data_source_id = self.data_source_id
        dpia = self.dpia
        shared = self.shared
        unique_id = self.unique_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_source_auto_match is not UNSET:
            field_dict["dataSourceAutoMatch"] = data_source_auto_match
        if name is not UNSET:
            field_dict["name"] = name
        if query is not UNSET:
            field_dict["query"] = query
        if run_async is not UNSET:
            field_dict["runAsync"] = run_async
        if topology is not UNSET:
            field_dict["topology"] = topology
        if allow_clear_query is not UNSET:
            field_dict["allowClearQuery"] = allow_clear_query
        if workflow_json is not UNSET:
            field_dict["workflowJSON"] = workflow_json
        if query_timeout is not UNSET:
            field_dict["queryTimeout"] = query_timeout
        if authorization_status is not UNSET:
            field_dict["authorizationStatus"] = authorization_status
        if compute_only is not UNSET:
            field_dict["computeOnly"] = compute_only
        if created_with_client is not UNSET:
            field_dict["createdWithClient"] = created_with_client
        if description is not UNSET:
            field_dict["description"] = description
        if local is not UNSET:
            field_dict["local"] = local
        if created_by_node is not UNSET:
            field_dict["createdByNode"] = created_by_node
        if workflow_type is not UNSET:
            field_dict["workflowType"] = workflow_type
        if authorized_users is not UNSET:
            field_dict["authorizedUsers"] = authorized_users
        if locked is not UNSET:
            field_dict["locked"] = locked
        if allow_shared_edit is not UNSET:
            field_dict["allowSharedEdit"] = allow_shared_edit
        if local_data_selection_definition is not UNSET:
            field_dict["localDataSelectionDefinition"] = local_data_selection_definition
        if min_contributors is not UNSET:
            field_dict["minContributors"] = min_contributors
        if network_id is not UNSET:
            field_dict["networkId"] = network_id
        if policy is not UNSET:
            field_dict["policy"] = policy
        if computation_definition is not UNSET:
            field_dict["computationDefinition"] = computation_definition
        if created_by_user is not UNSET:
            field_dict["createdByUser"] = created_by_user
        if data_source_id is not UNSET:
            field_dict["dataSourceId"] = data_source_id
        if dpia is not UNSET:
            field_dict["dpia"] = dpia
        if shared is not UNSET:
            field_dict["shared"] = shared
        if unique_id is not UNSET:
            field_dict["uniqueId"] = unique_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.computation_definition import ComputationDefinition
        from ..models.computation_policy import ComputationPolicy
        from ..models.data_source_query import DataSourceQuery
        from ..models.local_data_selection_definition import LocalDataSelectionDefinition

        d = src_dict.copy()
        data_source_auto_match = d.pop("dataSourceAutoMatch", UNSET)

        name = d.pop("name", UNSET)

        _query = d.pop("query", UNSET)
        query: Union[Unset, DataSourceQuery]
        if isinstance(_query, Unset):
            query = UNSET
        else:
            query = DataSourceQuery.from_dict(_query)

        run_async = d.pop("runAsync", UNSET)

        _topology = d.pop("topology", UNSET)
        topology: Union[Unset, Topology]
        if isinstance(_topology, Unset):
            topology = UNSET
        else:
            topology = Topology(_topology)

        allow_clear_query = d.pop("allowClearQuery", UNSET)

        workflow_json = d.pop("workflowJSON", UNSET)

        query_timeout = d.pop("queryTimeout", UNSET)

        _authorization_status = d.pop("authorizationStatus", UNSET)
        authorization_status: Union[Unset, AuthorizationStatus]
        if isinstance(_authorization_status, Unset):
            authorization_status = UNSET
        else:
            authorization_status = AuthorizationStatus(_authorization_status)

        compute_only = d.pop("computeOnly", UNSET)

        _created_with_client = d.pop("createdWithClient", UNSET)
        created_with_client: Union[Unset, Client]
        if isinstance(_created_with_client, Unset):
            created_with_client = UNSET
        else:
            created_with_client = Client(_created_with_client)

        description = d.pop("description", UNSET)

        local = d.pop("local", UNSET)

        created_by_node = d.pop("createdByNode", UNSET)

        _workflow_type = d.pop("workflowType", UNSET)
        workflow_type: Union[Unset, ProjectBaseWorkflowType]
        if isinstance(_workflow_type, Unset):
            workflow_type = UNSET
        else:
            workflow_type = ProjectBaseWorkflowType(_workflow_type)

        authorized_users = cast(List[str], d.pop("authorizedUsers", UNSET))

        locked = d.pop("locked", UNSET)

        allow_shared_edit = d.pop("allowSharedEdit", UNSET)

        _local_data_selection_definition = d.pop("localDataSelectionDefinition", UNSET)
        local_data_selection_definition: Union[Unset, LocalDataSelectionDefinition]
        if isinstance(_local_data_selection_definition, Unset):
            local_data_selection_definition = UNSET
        else:
            local_data_selection_definition = LocalDataSelectionDefinition.from_dict(_local_data_selection_definition)

        min_contributors = d.pop("minContributors", UNSET)

        network_id = d.pop("networkId", UNSET)

        _policy = d.pop("policy", UNSET)
        policy: Union[Unset, ComputationPolicy]
        if isinstance(_policy, Unset):
            policy = UNSET
        else:
            policy = ComputationPolicy.from_dict(_policy)

        _computation_definition = d.pop("computationDefinition", UNSET)
        computation_definition: Union[Unset, ComputationDefinition]
        if isinstance(_computation_definition, Unset):
            computation_definition = UNSET
        else:
            computation_definition = ComputationDefinition.from_dict(_computation_definition)

        created_by_user = d.pop("createdByUser", UNSET)

        data_source_id = d.pop("dataSourceId", UNSET)

        dpia = d.pop("dpia", UNSET)

        shared = d.pop("shared", UNSET)

        unique_id = d.pop("uniqueId", UNSET)

        project_base = cls(
            data_source_auto_match=data_source_auto_match,
            name=name,
            query=query,
            run_async=run_async,
            topology=topology,
            allow_clear_query=allow_clear_query,
            workflow_json=workflow_json,
            query_timeout=query_timeout,
            authorization_status=authorization_status,
            compute_only=compute_only,
            created_with_client=created_with_client,
            description=description,
            local=local,
            created_by_node=created_by_node,
            workflow_type=workflow_type,
            authorized_users=authorized_users,
            locked=locked,
            allow_shared_edit=allow_shared_edit,
            local_data_selection_definition=local_data_selection_definition,
            min_contributors=min_contributors,
            network_id=network_id,
            policy=policy,
            computation_definition=computation_definition,
            created_by_user=created_by_user,
            data_source_id=data_source_id,
            dpia=dpia,
            shared=shared,
            unique_id=unique_id,
        )

        project_base.additional_properties = d
        return project_base

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
