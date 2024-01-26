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
        unique_id (Union[Unset, str]): Unique identifier of a project.
        unrestricted_access (Union[Unset, None, bool]): when set to true, then all users from the same organization are
            authorized to access the project (view / edit depends on the roles)
        authorized_users (Union[Unset, List[str]]): The IDs of the users who can run the project
        name (Union[Unset, str]):
        allow_shared_edit (Union[Unset, bool]): True if this project can be modified after being shared. Modifications
            of a shared project will be broadcasted to the network
        local_data_selection_definition (Union[Unset, LocalDataSelectionDefinition]): datasource selection definition. A
            selection is a "query" or data selection definition to run on the datasource
        created_by_node (Union[Unset, str]): ID of node where the project was first created
        data_source_auto_match (Union[Unset, bool]): whether or not to automatically assign the first matching
            datasource when the project is shared with other nodes
        min_contributors (Union[Unset, None, int]): minimum number of participants that contribute with their data
            required to run computations within this project
        network_id (Union[Unset, str]): id to uniquely identify the network
        allow_clear_query (Union[Unset, bool]): [Dangerous, can lead to cross code data share] True if it is allowed for
            a client to query the data source all participants of the project and return the clear text result
        authorization_status (Union[Unset, AuthorizationStatus]): Authorization status of the project
        query_timeout (Union[Unset, int]): Timeout for the data source queries Default: 30.
        end_to_end_encrypted (Union[Unset, None, bool]): whether results are always end to end encrypted and decrypted
            on the client side
        workflow_json (Union[Unset, str]): JSON representation of the workflow UI in the frontend
        computation_definition (Union[Unset, ComputationDefinition]): Generic computation.
        data_source_id (Union[Unset, None, str]): Unique identifier of a data source.
        locked (Union[Unset, None, bool]): True if the project is read-only (likely because it has already been shared)
        non_contributor (Union[Unset, None, bool]): indicates that the current project participant takes part in the
            distributed computations but does not have any input data.
            By default this field is set according to the instance's configuration.
        dpia (Union[Unset, str]):
        run_async (Union[Unset, bool]): flag indicating if computation should be run asynchronously
        shared (Union[Unset, bool]): True if the project has once been shared across the participants
        topology (Union[Unset, Topology]): Network Topologies. 'star' or 'tree'. In star topology all nodes are
            connected to a central node. In tree topology all nodes are connected and aware of each other.
        created_by_user (Union[Unset, str]): ID of user who created the project
        description (Union[Unset, None, str]):
        local (Union[Unset, None, bool]): True if the project's computation should run only with local data (not
            configured the network)
        policy (Union[Unset, ComputationPolicy]): policy to validate a specific computation
        query (Union[Unset, DataSourceQuery]): schema used for the query
        workflow_type (Union[Unset, ProjectBaseWorkflowType]): type of the workflow UI in the frontend
        created_with_client (Union[Unset, Client]): Type of client that communicates with the agent API
        hide_leaf_participants (Union[Unset, None, bool]): whether leaf project participants are not shown to other leaf
            participants when the project is in a star topology.
    """

    unique_id: Union[Unset, str] = UNSET
    unrestricted_access: Union[Unset, None, bool] = UNSET
    authorized_users: Union[Unset, List[str]] = UNSET
    name: Union[Unset, str] = UNSET
    allow_shared_edit: Union[Unset, bool] = UNSET
    local_data_selection_definition: Union[Unset, "LocalDataSelectionDefinition"] = UNSET
    created_by_node: Union[Unset, str] = UNSET
    data_source_auto_match: Union[Unset, bool] = UNSET
    min_contributors: Union[Unset, None, int] = UNSET
    network_id: Union[Unset, str] = UNSET
    allow_clear_query: Union[Unset, bool] = UNSET
    authorization_status: Union[Unset, AuthorizationStatus] = UNSET
    query_timeout: Union[Unset, int] = 30
    end_to_end_encrypted: Union[Unset, None, bool] = UNSET
    workflow_json: Union[Unset, str] = UNSET
    computation_definition: Union[Unset, "ComputationDefinition"] = UNSET
    data_source_id: Union[Unset, None, str] = UNSET
    locked: Union[Unset, None, bool] = UNSET
    non_contributor: Union[Unset, None, bool] = UNSET
    dpia: Union[Unset, str] = UNSET
    run_async: Union[Unset, bool] = UNSET
    shared: Union[Unset, bool] = UNSET
    topology: Union[Unset, Topology] = UNSET
    created_by_user: Union[Unset, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    local: Union[Unset, None, bool] = UNSET
    policy: Union[Unset, "ComputationPolicy"] = UNSET
    query: Union[Unset, "DataSourceQuery"] = UNSET
    workflow_type: Union[Unset, ProjectBaseWorkflowType] = UNSET
    created_with_client: Union[Unset, Client] = UNSET
    hide_leaf_participants: Union[Unset, None, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unique_id = self.unique_id
        unrestricted_access = self.unrestricted_access
        authorized_users: Union[Unset, List[str]] = UNSET
        if not isinstance(self.authorized_users, Unset):
            authorized_users = self.authorized_users

        name = self.name
        allow_shared_edit = self.allow_shared_edit
        local_data_selection_definition: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.local_data_selection_definition, Unset):
            local_data_selection_definition = self.local_data_selection_definition.to_dict()

        created_by_node = self.created_by_node
        data_source_auto_match = self.data_source_auto_match
        min_contributors = self.min_contributors
        network_id = self.network_id
        allow_clear_query = self.allow_clear_query
        authorization_status: Union[Unset, str] = UNSET
        if not isinstance(self.authorization_status, Unset):
            authorization_status = self.authorization_status.value

        query_timeout = self.query_timeout
        end_to_end_encrypted = self.end_to_end_encrypted
        workflow_json = self.workflow_json
        computation_definition: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.computation_definition, Unset):
            computation_definition = self.computation_definition.to_dict()

        data_source_id = self.data_source_id
        locked = self.locked
        non_contributor = self.non_contributor
        dpia = self.dpia
        run_async = self.run_async
        shared = self.shared
        topology: Union[Unset, str] = UNSET
        if not isinstance(self.topology, Unset):
            topology = self.topology.value

        created_by_user = self.created_by_user
        description = self.description
        local = self.local
        policy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.policy, Unset):
            policy = self.policy.to_dict()

        query: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.query, Unset):
            query = self.query.to_dict()

        workflow_type: Union[Unset, str] = UNSET
        if not isinstance(self.workflow_type, Unset):
            workflow_type = self.workflow_type.value

        created_with_client: Union[Unset, str] = UNSET
        if not isinstance(self.created_with_client, Unset):
            created_with_client = self.created_with_client.value

        hide_leaf_participants = self.hide_leaf_participants

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unique_id is not UNSET:
            field_dict["uniqueId"] = unique_id
        if unrestricted_access is not UNSET:
            field_dict["unrestrictedAccess"] = unrestricted_access
        if authorized_users is not UNSET:
            field_dict["authorizedUsers"] = authorized_users
        if name is not UNSET:
            field_dict["name"] = name
        if allow_shared_edit is not UNSET:
            field_dict["allowSharedEdit"] = allow_shared_edit
        if local_data_selection_definition is not UNSET:
            field_dict["localDataSelectionDefinition"] = local_data_selection_definition
        if created_by_node is not UNSET:
            field_dict["createdByNode"] = created_by_node
        if data_source_auto_match is not UNSET:
            field_dict["dataSourceAutoMatch"] = data_source_auto_match
        if min_contributors is not UNSET:
            field_dict["minContributors"] = min_contributors
        if network_id is not UNSET:
            field_dict["networkId"] = network_id
        if allow_clear_query is not UNSET:
            field_dict["allowClearQuery"] = allow_clear_query
        if authorization_status is not UNSET:
            field_dict["authorizationStatus"] = authorization_status
        if query_timeout is not UNSET:
            field_dict["queryTimeout"] = query_timeout
        if end_to_end_encrypted is not UNSET:
            field_dict["endToEndEncrypted"] = end_to_end_encrypted
        if workflow_json is not UNSET:
            field_dict["workflowJSON"] = workflow_json
        if computation_definition is not UNSET:
            field_dict["computationDefinition"] = computation_definition
        if data_source_id is not UNSET:
            field_dict["dataSourceId"] = data_source_id
        if locked is not UNSET:
            field_dict["locked"] = locked
        if non_contributor is not UNSET:
            field_dict["nonContributor"] = non_contributor
        if dpia is not UNSET:
            field_dict["dpia"] = dpia
        if run_async is not UNSET:
            field_dict["runAsync"] = run_async
        if shared is not UNSET:
            field_dict["shared"] = shared
        if topology is not UNSET:
            field_dict["topology"] = topology
        if created_by_user is not UNSET:
            field_dict["createdByUser"] = created_by_user
        if description is not UNSET:
            field_dict["description"] = description
        if local is not UNSET:
            field_dict["local"] = local
        if policy is not UNSET:
            field_dict["policy"] = policy
        if query is not UNSET:
            field_dict["query"] = query
        if workflow_type is not UNSET:
            field_dict["workflowType"] = workflow_type
        if created_with_client is not UNSET:
            field_dict["createdWithClient"] = created_with_client
        if hide_leaf_participants is not UNSET:
            field_dict["hideLeafParticipants"] = hide_leaf_participants

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.computation_definition import ComputationDefinition
        from ..models.computation_policy import ComputationPolicy
        from ..models.data_source_query import DataSourceQuery
        from ..models.local_data_selection_definition import LocalDataSelectionDefinition

        d = src_dict.copy()
        unique_id = d.pop("uniqueId", UNSET)

        unrestricted_access = d.pop("unrestrictedAccess", UNSET)

        authorized_users = cast(List[str], d.pop("authorizedUsers", UNSET))

        name = d.pop("name", UNSET)

        allow_shared_edit = d.pop("allowSharedEdit", UNSET)

        _local_data_selection_definition = d.pop("localDataSelectionDefinition", UNSET)
        local_data_selection_definition: Union[Unset, LocalDataSelectionDefinition]
        if isinstance(_local_data_selection_definition, Unset):
            local_data_selection_definition = UNSET
        else:
            local_data_selection_definition = LocalDataSelectionDefinition.from_dict(_local_data_selection_definition)

        created_by_node = d.pop("createdByNode", UNSET)

        data_source_auto_match = d.pop("dataSourceAutoMatch", UNSET)

        min_contributors = d.pop("minContributors", UNSET)

        network_id = d.pop("networkId", UNSET)

        allow_clear_query = d.pop("allowClearQuery", UNSET)

        _authorization_status = d.pop("authorizationStatus", UNSET)
        authorization_status: Union[Unset, AuthorizationStatus]
        if isinstance(_authorization_status, Unset):
            authorization_status = UNSET
        else:
            authorization_status = AuthorizationStatus(_authorization_status)

        query_timeout = d.pop("queryTimeout", UNSET)

        end_to_end_encrypted = d.pop("endToEndEncrypted", UNSET)

        workflow_json = d.pop("workflowJSON", UNSET)

        _computation_definition = d.pop("computationDefinition", UNSET)
        computation_definition: Union[Unset, ComputationDefinition]
        if isinstance(_computation_definition, Unset):
            computation_definition = UNSET
        else:
            computation_definition = ComputationDefinition.from_dict(_computation_definition)

        data_source_id = d.pop("dataSourceId", UNSET)

        locked = d.pop("locked", UNSET)

        non_contributor = d.pop("nonContributor", UNSET)

        dpia = d.pop("dpia", UNSET)

        run_async = d.pop("runAsync", UNSET)

        shared = d.pop("shared", UNSET)

        _topology = d.pop("topology", UNSET)
        topology: Union[Unset, Topology]
        if isinstance(_topology, Unset):
            topology = UNSET
        else:
            topology = Topology(_topology)

        created_by_user = d.pop("createdByUser", UNSET)

        description = d.pop("description", UNSET)

        local = d.pop("local", UNSET)

        _policy = d.pop("policy", UNSET)
        policy: Union[Unset, ComputationPolicy]
        if isinstance(_policy, Unset):
            policy = UNSET
        else:
            policy = ComputationPolicy.from_dict(_policy)

        _query = d.pop("query", UNSET)
        query: Union[Unset, DataSourceQuery]
        if isinstance(_query, Unset):
            query = UNSET
        else:
            query = DataSourceQuery.from_dict(_query)

        _workflow_type = d.pop("workflowType", UNSET)
        workflow_type: Union[Unset, ProjectBaseWorkflowType]
        if isinstance(_workflow_type, Unset):
            workflow_type = UNSET
        else:
            workflow_type = ProjectBaseWorkflowType(_workflow_type)

        _created_with_client = d.pop("createdWithClient", UNSET)
        created_with_client: Union[Unset, Client]
        if isinstance(_created_with_client, Unset):
            created_with_client = UNSET
        else:
            created_with_client = Client(_created_with_client)

        hide_leaf_participants = d.pop("hideLeafParticipants", UNSET)

        project_base = cls(
            unique_id=unique_id,
            unrestricted_access=unrestricted_access,
            authorized_users=authorized_users,
            name=name,
            allow_shared_edit=allow_shared_edit,
            local_data_selection_definition=local_data_selection_definition,
            created_by_node=created_by_node,
            data_source_auto_match=data_source_auto_match,
            min_contributors=min_contributors,
            network_id=network_id,
            allow_clear_query=allow_clear_query,
            authorization_status=authorization_status,
            query_timeout=query_timeout,
            end_to_end_encrypted=end_to_end_encrypted,
            workflow_json=workflow_json,
            computation_definition=computation_definition,
            data_source_id=data_source_id,
            locked=locked,
            non_contributor=non_contributor,
            dpia=dpia,
            run_async=run_async,
            shared=shared,
            topology=topology,
            created_by_user=created_by_user,
            description=description,
            local=local,
            policy=policy,
            query=query,
            workflow_type=workflow_type,
            created_with_client=created_with_client,
            hide_leaf_participants=hide_leaf_participants,
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
