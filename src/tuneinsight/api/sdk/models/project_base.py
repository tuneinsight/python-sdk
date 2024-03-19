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
        local (Union[Unset, None, bool]): True if the project's computation should run only with local data (not
            configured the network)
        allow_shared_edit (Union[Unset, bool]): True if this project can be modified after being shared. Modifications
            of a shared project will be broadcasted to the network
        authorized_users (Union[Unset, List[str]]): The IDs of the users who can run the project
        end_to_end_encrypted (Union[Unset, None, bool]): whether results are always end to end encrypted and decrypted
            on the client side
        policy (Union[Unset, ComputationPolicy]): policy to validate a specific computation
        topology (Union[Unset, Topology]): Network Topologies. 'star' or 'tree'. In star topology all nodes are
            connected to a central node. In tree topology all nodes are connected and aware of each other.
        allow_clear_query (Union[Unset, bool]): [Dangerous, can lead to cross code data share] True if it is allowed for
            a client to query the data source all participants of the project and return the clear text result
        network_id (Union[Unset, str]): id to uniquely identify the network
        run_async (Union[Unset, bool]): flag indicating if computation should be run asynchronously
        shared (Union[Unset, bool]): True if the project has once been shared across the participants
        unrestricted_access (Union[Unset, None, bool]): when set to true, then all users from the same organization are
            authorized to access the project (view / edit depends on the roles)
        data_source_id (Union[Unset, None, str]): Unique identifier of a data source.
        hide_leaf_participants (Union[Unset, None, bool]): whether leaf project participants are not shown to other leaf
            participants when the project is in a star topology.
        query_timeout (Union[Unset, int]): Timeout for the data source queries Default: 30.
        created_with_client (Union[Unset, Client]): Type of client that communicates with the agent API
        data_source_auto_match (Union[Unset, bool]): whether or not to automatically assign the first matching
            datasource when the project is shared with other nodes
        min_contributors (Union[Unset, None, int]): minimum number of participants that contribute with their data
            required to run computations within this project
        non_contributor (Union[Unset, None, bool]): indicates that the current project participant takes part in the
            distributed computations but does not have any input data.
            By default this field is set according to the instance's configuration.
        query (Union[Unset, DataSourceQuery]): schema used for the query
        unique_id (Union[Unset, str]): Unique identifier of a project.
        workflow_json (Union[Unset, str]): JSON representation of the workflow UI in the frontend
        authorization_status (Union[Unset, AuthorizationStatus]): Authorization status of the project
        computation_definition (Union[Unset, ComputationDefinition]): Generic computation.
        dpia (Union[Unset, str]):
        local_data_selection_definition (Union[Unset, LocalDataSelectionDefinition]): datasource selection definition. A
            selection is a "query" or data selection definition to run on the datasource
        locked (Union[Unset, None, bool]): True if the project is read-only (likely because it has already been shared)
        name (Union[Unset, str]):
        created_by_node (Union[Unset, str]): ID of node where the project was first created
        created_by_user (Union[Unset, str]): ID of user who created the project
        description (Union[Unset, None, str]):
        workflow_type (Union[Unset, ProjectBaseWorkflowType]): type of the workflow UI in the frontend
    """

    local: Union[Unset, None, bool] = UNSET
    allow_shared_edit: Union[Unset, bool] = UNSET
    authorized_users: Union[Unset, List[str]] = UNSET
    end_to_end_encrypted: Union[Unset, None, bool] = UNSET
    policy: Union[Unset, "ComputationPolicy"] = UNSET
    topology: Union[Unset, Topology] = UNSET
    allow_clear_query: Union[Unset, bool] = UNSET
    network_id: Union[Unset, str] = UNSET
    run_async: Union[Unset, bool] = UNSET
    shared: Union[Unset, bool] = UNSET
    unrestricted_access: Union[Unset, None, bool] = UNSET
    data_source_id: Union[Unset, None, str] = UNSET
    hide_leaf_participants: Union[Unset, None, bool] = UNSET
    query_timeout: Union[Unset, int] = 30
    created_with_client: Union[Unset, Client] = UNSET
    data_source_auto_match: Union[Unset, bool] = UNSET
    min_contributors: Union[Unset, None, int] = UNSET
    non_contributor: Union[Unset, None, bool] = UNSET
    query: Union[Unset, "DataSourceQuery"] = UNSET
    unique_id: Union[Unset, str] = UNSET
    workflow_json: Union[Unset, str] = UNSET
    authorization_status: Union[Unset, AuthorizationStatus] = UNSET
    computation_definition: Union[Unset, "ComputationDefinition"] = UNSET
    dpia: Union[Unset, str] = UNSET
    local_data_selection_definition: Union[Unset, "LocalDataSelectionDefinition"] = UNSET
    locked: Union[Unset, None, bool] = UNSET
    name: Union[Unset, str] = UNSET
    created_by_node: Union[Unset, str] = UNSET
    created_by_user: Union[Unset, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    workflow_type: Union[Unset, ProjectBaseWorkflowType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        local = self.local
        allow_shared_edit = self.allow_shared_edit
        authorized_users: Union[Unset, List[str]] = UNSET
        if not isinstance(self.authorized_users, Unset):
            authorized_users = self.authorized_users

        end_to_end_encrypted = self.end_to_end_encrypted
        policy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.policy, Unset):
            policy = self.policy.to_dict()

        topology: Union[Unset, str] = UNSET
        if not isinstance(self.topology, Unset):
            topology = self.topology.value

        allow_clear_query = self.allow_clear_query
        network_id = self.network_id
        run_async = self.run_async
        shared = self.shared
        unrestricted_access = self.unrestricted_access
        data_source_id = self.data_source_id
        hide_leaf_participants = self.hide_leaf_participants
        query_timeout = self.query_timeout
        created_with_client: Union[Unset, str] = UNSET
        if not isinstance(self.created_with_client, Unset):
            created_with_client = self.created_with_client.value

        data_source_auto_match = self.data_source_auto_match
        min_contributors = self.min_contributors
        non_contributor = self.non_contributor
        query: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.query, Unset):
            query = self.query.to_dict()

        unique_id = self.unique_id
        workflow_json = self.workflow_json
        authorization_status: Union[Unset, str] = UNSET
        if not isinstance(self.authorization_status, Unset):
            authorization_status = self.authorization_status.value

        computation_definition: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.computation_definition, Unset):
            computation_definition = self.computation_definition.to_dict()

        dpia = self.dpia
        local_data_selection_definition: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.local_data_selection_definition, Unset):
            local_data_selection_definition = self.local_data_selection_definition.to_dict()

        locked = self.locked
        name = self.name
        created_by_node = self.created_by_node
        created_by_user = self.created_by_user
        description = self.description
        workflow_type: Union[Unset, str] = UNSET
        if not isinstance(self.workflow_type, Unset):
            workflow_type = self.workflow_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if local is not UNSET:
            field_dict["local"] = local
        if allow_shared_edit is not UNSET:
            field_dict["allowSharedEdit"] = allow_shared_edit
        if authorized_users is not UNSET:
            field_dict["authorizedUsers"] = authorized_users
        if end_to_end_encrypted is not UNSET:
            field_dict["endToEndEncrypted"] = end_to_end_encrypted
        if policy is not UNSET:
            field_dict["policy"] = policy
        if topology is not UNSET:
            field_dict["topology"] = topology
        if allow_clear_query is not UNSET:
            field_dict["allowClearQuery"] = allow_clear_query
        if network_id is not UNSET:
            field_dict["networkId"] = network_id
        if run_async is not UNSET:
            field_dict["runAsync"] = run_async
        if shared is not UNSET:
            field_dict["shared"] = shared
        if unrestricted_access is not UNSET:
            field_dict["unrestrictedAccess"] = unrestricted_access
        if data_source_id is not UNSET:
            field_dict["dataSourceId"] = data_source_id
        if hide_leaf_participants is not UNSET:
            field_dict["hideLeafParticipants"] = hide_leaf_participants
        if query_timeout is not UNSET:
            field_dict["queryTimeout"] = query_timeout
        if created_with_client is not UNSET:
            field_dict["createdWithClient"] = created_with_client
        if data_source_auto_match is not UNSET:
            field_dict["dataSourceAutoMatch"] = data_source_auto_match
        if min_contributors is not UNSET:
            field_dict["minContributors"] = min_contributors
        if non_contributor is not UNSET:
            field_dict["nonContributor"] = non_contributor
        if query is not UNSET:
            field_dict["query"] = query
        if unique_id is not UNSET:
            field_dict["uniqueId"] = unique_id
        if workflow_json is not UNSET:
            field_dict["workflowJSON"] = workflow_json
        if authorization_status is not UNSET:
            field_dict["authorizationStatus"] = authorization_status
        if computation_definition is not UNSET:
            field_dict["computationDefinition"] = computation_definition
        if dpia is not UNSET:
            field_dict["dpia"] = dpia
        if local_data_selection_definition is not UNSET:
            field_dict["localDataSelectionDefinition"] = local_data_selection_definition
        if locked is not UNSET:
            field_dict["locked"] = locked
        if name is not UNSET:
            field_dict["name"] = name
        if created_by_node is not UNSET:
            field_dict["createdByNode"] = created_by_node
        if created_by_user is not UNSET:
            field_dict["createdByUser"] = created_by_user
        if description is not UNSET:
            field_dict["description"] = description
        if workflow_type is not UNSET:
            field_dict["workflowType"] = workflow_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.computation_definition import ComputationDefinition
        from ..models.computation_policy import ComputationPolicy
        from ..models.data_source_query import DataSourceQuery
        from ..models.local_data_selection_definition import LocalDataSelectionDefinition

        d = src_dict.copy()
        local = d.pop("local", UNSET)

        allow_shared_edit = d.pop("allowSharedEdit", UNSET)

        authorized_users = cast(List[str], d.pop("authorizedUsers", UNSET))

        end_to_end_encrypted = d.pop("endToEndEncrypted", UNSET)

        _policy = d.pop("policy", UNSET)
        policy: Union[Unset, ComputationPolicy]
        if isinstance(_policy, Unset):
            policy = UNSET
        else:
            policy = ComputationPolicy.from_dict(_policy)

        _topology = d.pop("topology", UNSET)
        topology: Union[Unset, Topology]
        if isinstance(_topology, Unset):
            topology = UNSET
        else:
            topology = Topology(_topology)

        allow_clear_query = d.pop("allowClearQuery", UNSET)

        network_id = d.pop("networkId", UNSET)

        run_async = d.pop("runAsync", UNSET)

        shared = d.pop("shared", UNSET)

        unrestricted_access = d.pop("unrestrictedAccess", UNSET)

        data_source_id = d.pop("dataSourceId", UNSET)

        hide_leaf_participants = d.pop("hideLeafParticipants", UNSET)

        query_timeout = d.pop("queryTimeout", UNSET)

        _created_with_client = d.pop("createdWithClient", UNSET)
        created_with_client: Union[Unset, Client]
        if isinstance(_created_with_client, Unset):
            created_with_client = UNSET
        else:
            created_with_client = Client(_created_with_client)

        data_source_auto_match = d.pop("dataSourceAutoMatch", UNSET)

        min_contributors = d.pop("minContributors", UNSET)

        non_contributor = d.pop("nonContributor", UNSET)

        _query = d.pop("query", UNSET)
        query: Union[Unset, DataSourceQuery]
        if isinstance(_query, Unset):
            query = UNSET
        else:
            query = DataSourceQuery.from_dict(_query)

        unique_id = d.pop("uniqueId", UNSET)

        workflow_json = d.pop("workflowJSON", UNSET)

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

        dpia = d.pop("dpia", UNSET)

        _local_data_selection_definition = d.pop("localDataSelectionDefinition", UNSET)
        local_data_selection_definition: Union[Unset, LocalDataSelectionDefinition]
        if isinstance(_local_data_selection_definition, Unset):
            local_data_selection_definition = UNSET
        else:
            local_data_selection_definition = LocalDataSelectionDefinition.from_dict(_local_data_selection_definition)

        locked = d.pop("locked", UNSET)

        name = d.pop("name", UNSET)

        created_by_node = d.pop("createdByNode", UNSET)

        created_by_user = d.pop("createdByUser", UNSET)

        description = d.pop("description", UNSET)

        _workflow_type = d.pop("workflowType", UNSET)
        workflow_type: Union[Unset, ProjectBaseWorkflowType]
        if isinstance(_workflow_type, Unset):
            workflow_type = UNSET
        else:
            workflow_type = ProjectBaseWorkflowType(_workflow_type)

        project_base = cls(
            local=local,
            allow_shared_edit=allow_shared_edit,
            authorized_users=authorized_users,
            end_to_end_encrypted=end_to_end_encrypted,
            policy=policy,
            topology=topology,
            allow_clear_query=allow_clear_query,
            network_id=network_id,
            run_async=run_async,
            shared=shared,
            unrestricted_access=unrestricted_access,
            data_source_id=data_source_id,
            hide_leaf_participants=hide_leaf_participants,
            query_timeout=query_timeout,
            created_with_client=created_with_client,
            data_source_auto_match=data_source_auto_match,
            min_contributors=min_contributors,
            non_contributor=non_contributor,
            query=query,
            unique_id=unique_id,
            workflow_json=workflow_json,
            authorization_status=authorization_status,
            computation_definition=computation_definition,
            dpia=dpia,
            local_data_selection_definition=local_data_selection_definition,
            locked=locked,
            name=name,
            created_by_node=created_by_node,
            created_by_user=created_by_user,
            description=description,
            workflow_type=workflow_type,
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
