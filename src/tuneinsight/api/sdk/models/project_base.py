from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.client import Client
from ..models.participants_access_scope import ParticipantsAccessScope
from ..models.project_base_recurring_interval_unit import ProjectBaseRecurringIntervalUnit
from ..models.topology import Topology
from ..models.workflow_type import WorkflowType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.computation_definition import ComputationDefinition
    from ..models.computation_policy import ComputationPolicy


T = TypeVar("T", bound="ProjectBase")


@attr.s(auto_attribs=True)
class ProjectBase:
    """Common fields of a project (for get, patch and post)

    Attributes:
        allow_clear_query (Union[Unset, bool]): [Dangerous, can lead to cross code data share] True if it is allowed for
            a client to query the data source all participants of the project and return the clear text result
        allow_shared_edit (Union[Unset, bool]): True if this project can be modified after being shared. Modifications
            of a shared project will be broadcasted to the network
        authorized_instances (Union[Unset, List[str]]): list of instances that are allowed to request computations in
            the project.
            Can only be modified by project administrators from the instance that created this project.
        authorized_users (Union[Unset, List[str]]): list of users that are allowed to request computations in the
            project.
        computation_definition (Union[Unset, ComputationDefinition]): Generic computation.
        computation_definition_base_64 (Union[Unset, str]): base64-version of the computation definition
        created_by_node (Union[Unset, str]): ID (alias) of node where the project was first created
        created_by_user (Union[Unset, str]): ID of user who created the project
        created_with_client (Union[Unset, Client]): Type of client that communicates with the agent API
        data_source_auto_match (Union[Unset, bool]): whether or not to automatically assign the first matching
            datasource when the project is shared with other nodes
        data_source_id (Union[Unset, None, str]): Unique identifier of a data source.
        description (Union[Unset, None, str]):
        dpia (Union[Unset, str]):
        end_to_end_encrypted (Union[Unset, None, bool]): whether results are always end to end encrypted and decrypted
            on the client side
        hidden (Union[Unset, bool]): whether the project is hidden from the project list
        hide_leaf_participants (Union[Unset, None, bool]): whether leaf project participants are not shown to other leaf
            participants when the project is in a star topology.
        local (Union[Unset, None, bool]): True if the project's computation should run only with local data (not
            configured the network)
        min_contributors (Union[Unset, None, int]): minimum number of participants that contribute with their data
            required to run computations within this project
        name (Union[Unset, str]):
        network_id (Union[Unset, str]): id to uniquely identify the network
        network_name (Union[Unset, str]): name of the network from the list of existing networks to link the project to.
        non_contributor (Union[Unset, None, bool]): indicates that the current project participant takes part in the
            distributed computations but does not have any input data.
            By default this field is set according to the instance's configuration.
        output_data_source_id (Union[Unset, None, str]): Unique identifier of a data source.
        policy (Union[Unset, ComputationPolicy]): policy to validate a specific computation
        query_timeout (Union[Unset, int]): Timeout for the data source queries Default: 30.
        query_timeout_enabled (Union[Unset, None, bool]): whether to enable the query timeout or not
        recurring_end_time (Union[Unset, None, str]): ISO 8601 datetime when the repetition should stop. If not set, the
            project will run indefinitely
        recurring_interval (Union[Unset, None, int]): Interval between each repetition in minutes
        recurring_interval_unit (Union[Unset, ProjectBaseRecurringIntervalUnit]): Unit in which the recurring interval
            is given (minutes, hours, days, weeks, months, years) Default: ProjectBaseRecurringIntervalUnit.MINUTES.
        recurring_start_time (Union[Unset, None, str]): ISO 8601 datetime when the repetition should start
        restrict_instances (Union[Unset, None, bool]): (DEPRECATED: replace by using `specified` as the
            `runAccessScope`)
            whether to restrict which instances are allowed request computations in the project.
            Can only be modified by project administrators from the instance that created this project.
        run_access_scope (Union[Unset, ParticipantsAccessScope]): Generic access scope that enables configuring access
            to a specific action w.r.t participants of a project.
        run_async (Union[Unset, bool]): flag indicating if computation should be run asynchronously
        share_token (Union[Unset, str]): the sharing token
        shared (Union[Unset, bool]): True if the project has once been shared across the participants
        topology (Union[Unset, Topology]): Network Topologies. 'star' or 'tree'. In star topology all nodes are
            connected to a central node. In tree topology all nodes are connected and aware of each other.
        unique_id (Union[Unset, str]): Unique identifier of a project.
        unrestricted_access (Union[Unset, None, bool]): when set to true, then all users from the same organization are
            authorized to access the project (view / edit depends on the roles)
        workflow_json (Union[Unset, str]): JSON representation of the workflow UI in the frontend
        workflow_type (Union[Unset, WorkflowType]): type of the workflow UI in the frontend
    """

    allow_clear_query: Union[Unset, bool] = UNSET
    allow_shared_edit: Union[Unset, bool] = UNSET
    authorized_instances: Union[Unset, List[str]] = UNSET
    authorized_users: Union[Unset, List[str]] = UNSET
    computation_definition: Union[Unset, "ComputationDefinition"] = UNSET
    computation_definition_base_64: Union[Unset, str] = UNSET
    created_by_node: Union[Unset, str] = UNSET
    created_by_user: Union[Unset, str] = UNSET
    created_with_client: Union[Unset, Client] = UNSET
    data_source_auto_match: Union[Unset, bool] = UNSET
    data_source_id: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    dpia: Union[Unset, str] = UNSET
    end_to_end_encrypted: Union[Unset, None, bool] = UNSET
    hidden: Union[Unset, bool] = UNSET
    hide_leaf_participants: Union[Unset, None, bool] = UNSET
    local: Union[Unset, None, bool] = UNSET
    min_contributors: Union[Unset, None, int] = UNSET
    name: Union[Unset, str] = UNSET
    network_id: Union[Unset, str] = UNSET
    network_name: Union[Unset, str] = UNSET
    non_contributor: Union[Unset, None, bool] = UNSET
    output_data_source_id: Union[Unset, None, str] = UNSET
    policy: Union[Unset, "ComputationPolicy"] = UNSET
    query_timeout: Union[Unset, int] = 30
    query_timeout_enabled: Union[Unset, None, bool] = UNSET
    recurring_end_time: Union[Unset, None, str] = UNSET
    recurring_interval: Union[Unset, None, int] = UNSET
    recurring_interval_unit: Union[Unset, ProjectBaseRecurringIntervalUnit] = ProjectBaseRecurringIntervalUnit.MINUTES
    recurring_start_time: Union[Unset, None, str] = UNSET
    restrict_instances: Union[Unset, None, bool] = UNSET
    run_access_scope: Union[Unset, ParticipantsAccessScope] = UNSET
    run_async: Union[Unset, bool] = UNSET
    share_token: Union[Unset, str] = UNSET
    shared: Union[Unset, bool] = UNSET
    topology: Union[Unset, Topology] = UNSET
    unique_id: Union[Unset, str] = UNSET
    unrestricted_access: Union[Unset, None, bool] = UNSET
    workflow_json: Union[Unset, str] = UNSET
    workflow_type: Union[Unset, WorkflowType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allow_clear_query = self.allow_clear_query
        allow_shared_edit = self.allow_shared_edit
        authorized_instances: Union[Unset, List[str]] = UNSET
        if not isinstance(self.authorized_instances, Unset):
            authorized_instances = self.authorized_instances

        authorized_users: Union[Unset, List[str]] = UNSET
        if not isinstance(self.authorized_users, Unset):
            authorized_users = self.authorized_users

        computation_definition: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.computation_definition, Unset):
            computation_definition = self.computation_definition.to_dict()

        computation_definition_base_64 = self.computation_definition_base_64
        created_by_node = self.created_by_node
        created_by_user = self.created_by_user
        created_with_client: Union[Unset, str] = UNSET
        if not isinstance(self.created_with_client, Unset):
            created_with_client = self.created_with_client.value

        data_source_auto_match = self.data_source_auto_match
        data_source_id = self.data_source_id
        description = self.description
        dpia = self.dpia
        end_to_end_encrypted = self.end_to_end_encrypted
        hidden = self.hidden
        hide_leaf_participants = self.hide_leaf_participants
        local = self.local
        min_contributors = self.min_contributors
        name = self.name
        network_id = self.network_id
        network_name = self.network_name
        non_contributor = self.non_contributor
        output_data_source_id = self.output_data_source_id
        policy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.policy, Unset):
            policy = self.policy.to_dict()

        query_timeout = self.query_timeout
        query_timeout_enabled = self.query_timeout_enabled
        recurring_end_time = self.recurring_end_time
        recurring_interval = self.recurring_interval
        recurring_interval_unit: Union[Unset, str] = UNSET
        if not isinstance(self.recurring_interval_unit, Unset):
            recurring_interval_unit = self.recurring_interval_unit.value

        recurring_start_time = self.recurring_start_time
        restrict_instances = self.restrict_instances
        run_access_scope: Union[Unset, str] = UNSET
        if not isinstance(self.run_access_scope, Unset):
            run_access_scope = self.run_access_scope.value

        run_async = self.run_async
        share_token = self.share_token
        shared = self.shared
        topology: Union[Unset, str] = UNSET
        if not isinstance(self.topology, Unset):
            topology = self.topology.value

        unique_id = self.unique_id
        unrestricted_access = self.unrestricted_access
        workflow_json = self.workflow_json
        workflow_type: Union[Unset, str] = UNSET
        if not isinstance(self.workflow_type, Unset):
            workflow_type = self.workflow_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allow_clear_query is not UNSET:
            field_dict["allowClearQuery"] = allow_clear_query
        if allow_shared_edit is not UNSET:
            field_dict["allowSharedEdit"] = allow_shared_edit
        if authorized_instances is not UNSET:
            field_dict["authorizedInstances"] = authorized_instances
        if authorized_users is not UNSET:
            field_dict["authorizedUsers"] = authorized_users
        if computation_definition is not UNSET:
            field_dict["computationDefinition"] = computation_definition
        if computation_definition_base_64 is not UNSET:
            field_dict["computationDefinitionBase64"] = computation_definition_base_64
        if created_by_node is not UNSET:
            field_dict["createdByNode"] = created_by_node
        if created_by_user is not UNSET:
            field_dict["createdByUser"] = created_by_user
        if created_with_client is not UNSET:
            field_dict["createdWithClient"] = created_with_client
        if data_source_auto_match is not UNSET:
            field_dict["dataSourceAutoMatch"] = data_source_auto_match
        if data_source_id is not UNSET:
            field_dict["dataSourceId"] = data_source_id
        if description is not UNSET:
            field_dict["description"] = description
        if dpia is not UNSET:
            field_dict["dpia"] = dpia
        if end_to_end_encrypted is not UNSET:
            field_dict["endToEndEncrypted"] = end_to_end_encrypted
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if hide_leaf_participants is not UNSET:
            field_dict["hideLeafParticipants"] = hide_leaf_participants
        if local is not UNSET:
            field_dict["local"] = local
        if min_contributors is not UNSET:
            field_dict["minContributors"] = min_contributors
        if name is not UNSET:
            field_dict["name"] = name
        if network_id is not UNSET:
            field_dict["networkId"] = network_id
        if network_name is not UNSET:
            field_dict["networkName"] = network_name
        if non_contributor is not UNSET:
            field_dict["nonContributor"] = non_contributor
        if output_data_source_id is not UNSET:
            field_dict["outputDataSourceId"] = output_data_source_id
        if policy is not UNSET:
            field_dict["policy"] = policy
        if query_timeout is not UNSET:
            field_dict["queryTimeout"] = query_timeout
        if query_timeout_enabled is not UNSET:
            field_dict["queryTimeoutEnabled"] = query_timeout_enabled
        if recurring_end_time is not UNSET:
            field_dict["recurringEndTime"] = recurring_end_time
        if recurring_interval is not UNSET:
            field_dict["recurringInterval"] = recurring_interval
        if recurring_interval_unit is not UNSET:
            field_dict["recurringIntervalUnit"] = recurring_interval_unit
        if recurring_start_time is not UNSET:
            field_dict["recurringStartTime"] = recurring_start_time
        if restrict_instances is not UNSET:
            field_dict["restrictInstances"] = restrict_instances
        if run_access_scope is not UNSET:
            field_dict["runAccessScope"] = run_access_scope
        if run_async is not UNSET:
            field_dict["runAsync"] = run_async
        if share_token is not UNSET:
            field_dict["shareToken"] = share_token
        if shared is not UNSET:
            field_dict["shared"] = shared
        if topology is not UNSET:
            field_dict["topology"] = topology
        if unique_id is not UNSET:
            field_dict["uniqueId"] = unique_id
        if unrestricted_access is not UNSET:
            field_dict["unrestrictedAccess"] = unrestricted_access
        if workflow_json is not UNSET:
            field_dict["workflowJSON"] = workflow_json
        if workflow_type is not UNSET:
            field_dict["workflowType"] = workflow_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.computation_definition import ComputationDefinition
        from ..models.computation_policy import ComputationPolicy

        d = src_dict.copy()
        allow_clear_query = d.pop("allowClearQuery", UNSET)

        allow_shared_edit = d.pop("allowSharedEdit", UNSET)

        authorized_instances = cast(List[str], d.pop("authorizedInstances", UNSET))

        authorized_users = cast(List[str], d.pop("authorizedUsers", UNSET))

        _computation_definition = d.pop("computationDefinition", UNSET)
        computation_definition: Union[Unset, ComputationDefinition]
        if isinstance(_computation_definition, Unset):
            computation_definition = UNSET
        else:
            computation_definition = ComputationDefinition.from_dict(_computation_definition)

        computation_definition_base_64 = d.pop("computationDefinitionBase64", UNSET)

        created_by_node = d.pop("createdByNode", UNSET)

        created_by_user = d.pop("createdByUser", UNSET)

        _created_with_client = d.pop("createdWithClient", UNSET)
        created_with_client: Union[Unset, Client]
        if isinstance(_created_with_client, Unset):
            created_with_client = UNSET
        else:
            created_with_client = Client(_created_with_client)

        data_source_auto_match = d.pop("dataSourceAutoMatch", UNSET)

        data_source_id = d.pop("dataSourceId", UNSET)

        description = d.pop("description", UNSET)

        dpia = d.pop("dpia", UNSET)

        end_to_end_encrypted = d.pop("endToEndEncrypted", UNSET)

        hidden = d.pop("hidden", UNSET)

        hide_leaf_participants = d.pop("hideLeafParticipants", UNSET)

        local = d.pop("local", UNSET)

        min_contributors = d.pop("minContributors", UNSET)

        name = d.pop("name", UNSET)

        network_id = d.pop("networkId", UNSET)

        network_name = d.pop("networkName", UNSET)

        non_contributor = d.pop("nonContributor", UNSET)

        output_data_source_id = d.pop("outputDataSourceId", UNSET)

        _policy = d.pop("policy", UNSET)
        policy: Union[Unset, ComputationPolicy]
        if isinstance(_policy, Unset):
            policy = UNSET
        else:
            policy = ComputationPolicy.from_dict(_policy)

        query_timeout = d.pop("queryTimeout", UNSET)

        query_timeout_enabled = d.pop("queryTimeoutEnabled", UNSET)

        recurring_end_time = d.pop("recurringEndTime", UNSET)

        recurring_interval = d.pop("recurringInterval", UNSET)

        _recurring_interval_unit = d.pop("recurringIntervalUnit", UNSET)
        recurring_interval_unit: Union[Unset, ProjectBaseRecurringIntervalUnit]
        if isinstance(_recurring_interval_unit, Unset):
            recurring_interval_unit = UNSET
        else:
            recurring_interval_unit = ProjectBaseRecurringIntervalUnit(_recurring_interval_unit)

        recurring_start_time = d.pop("recurringStartTime", UNSET)

        restrict_instances = d.pop("restrictInstances", UNSET)

        _run_access_scope = d.pop("runAccessScope", UNSET)
        run_access_scope: Union[Unset, ParticipantsAccessScope]
        if isinstance(_run_access_scope, Unset):
            run_access_scope = UNSET
        else:
            run_access_scope = ParticipantsAccessScope(_run_access_scope)

        run_async = d.pop("runAsync", UNSET)

        share_token = d.pop("shareToken", UNSET)

        shared = d.pop("shared", UNSET)

        _topology = d.pop("topology", UNSET)
        topology: Union[Unset, Topology]
        if isinstance(_topology, Unset):
            topology = UNSET
        else:
            topology = Topology(_topology)

        unique_id = d.pop("uniqueId", UNSET)

        unrestricted_access = d.pop("unrestrictedAccess", UNSET)

        workflow_json = d.pop("workflowJSON", UNSET)

        _workflow_type = d.pop("workflowType", UNSET)
        workflow_type: Union[Unset, WorkflowType]
        if isinstance(_workflow_type, Unset):
            workflow_type = UNSET
        else:
            workflow_type = WorkflowType(_workflow_type)

        project_base = cls(
            allow_clear_query=allow_clear_query,
            allow_shared_edit=allow_shared_edit,
            authorized_instances=authorized_instances,
            authorized_users=authorized_users,
            computation_definition=computation_definition,
            computation_definition_base_64=computation_definition_base_64,
            created_by_node=created_by_node,
            created_by_user=created_by_user,
            created_with_client=created_with_client,
            data_source_auto_match=data_source_auto_match,
            data_source_id=data_source_id,
            description=description,
            dpia=dpia,
            end_to_end_encrypted=end_to_end_encrypted,
            hidden=hidden,
            hide_leaf_participants=hide_leaf_participants,
            local=local,
            min_contributors=min_contributors,
            name=name,
            network_id=network_id,
            network_name=network_name,
            non_contributor=non_contributor,
            output_data_source_id=output_data_source_id,
            policy=policy,
            query_timeout=query_timeout,
            query_timeout_enabled=query_timeout_enabled,
            recurring_end_time=recurring_end_time,
            recurring_interval=recurring_interval,
            recurring_interval_unit=recurring_interval_unit,
            recurring_start_time=recurring_start_time,
            restrict_instances=restrict_instances,
            run_access_scope=run_access_scope,
            run_async=run_async,
            share_token=share_token,
            shared=shared,
            topology=topology,
            unique_id=unique_id,
            unrestricted_access=unrestricted_access,
            workflow_json=workflow_json,
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
