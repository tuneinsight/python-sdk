from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.authorization_status import AuthorizationStatus
from ..models.client import Client
from ..models.participants_access_scope import ParticipantsAccessScope
from ..models.participation_status import ParticipationStatus
from ..models.project_status import ProjectStatus
from ..models.topology import Topology
from ..models.workflow_type import WorkflowType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.computation import Computation
    from ..models.computation_definition import ComputationDefinition
    from ..models.computation_policy import ComputationPolicy
    from ..models.network import Network
    from ..models.participant import Participant
    from ..models.privacy_summary import PrivacySummary
    from ..models.project_actions import ProjectActions


T = TypeVar("T", bound="Project")


@attr.s(auto_attribs=True)
class Project:
    """Project entity definition.

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
        policy (Union[Unset, ComputationPolicy]): policy to validate a specific computation
        query_timeout (Union[Unset, int]): Timeout for the data source queries Default: 30.
        recurring_end_time (Union[Unset, None, str]): ISO 8601 datetime when the repetition should stop. If not set, the
            project will run indefinitely
        recurring_interval (Union[Unset, None, int]): Interval between each repetition in minutes
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
        actions (Union[Unset, ProjectActions]): regroups availability statuses of relevant user actions on a project and
            remaining queries when running computations.
        authorization_status (Union[Unset, AuthorizationStatus]): Authorization status of the project
        computations (Union[Unset, List['Computation']]): List of computations of the project
        created_at (Union[Unset, str]):
        error (Union[Unset, str]): Description of a potential error that happened during the project lifespan
        network (Union[Unset, Network]): Network that represents a set of nodes
        num_contributors (Union[Unset, int]): counts the current number of contributors in this project.
        num_ready_contributors (Union[Unset, int]): counts the number of contributors in this project that are ready to
            run the project (connected data source + authorized the project).
        participants (Union[Unset, List['Participant']]): List of current participants from this instance of the
            project.
        participation_status (Union[Unset, ParticipationStatus]): participation state of a project's participant
        previous_participants (Union[Unset, List['Participant']]): List of participants that were previously set in the
            project.
        privacy_summary (Union[Unset, PrivacySummary]): Privacy summary for a project
        status (Union[Unset, ProjectStatus]): Stages of a project workflow
        updated_at (Union[Unset, str]):
        workflow_description (Union[Unset, str]): dynamically generated markdown description of the distributed workflow
            that is currently configured with the project.
            Not to be confused with the project description which is set by the user that has created the project for
            informative purposes.
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
    hide_leaf_participants: Union[Unset, None, bool] = UNSET
    local: Union[Unset, None, bool] = UNSET
    min_contributors: Union[Unset, None, int] = UNSET
    name: Union[Unset, str] = UNSET
    network_id: Union[Unset, str] = UNSET
    network_name: Union[Unset, str] = UNSET
    non_contributor: Union[Unset, None, bool] = UNSET
    policy: Union[Unset, "ComputationPolicy"] = UNSET
    query_timeout: Union[Unset, int] = 30
    recurring_end_time: Union[Unset, None, str] = UNSET
    recurring_interval: Union[Unset, None, int] = UNSET
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
    actions: Union[Unset, "ProjectActions"] = UNSET
    authorization_status: Union[Unset, AuthorizationStatus] = UNSET
    computations: Union[Unset, List["Computation"]] = UNSET
    created_at: Union[Unset, str] = UNSET
    error: Union[Unset, str] = UNSET
    network: Union[Unset, "Network"] = UNSET
    num_contributors: Union[Unset, int] = UNSET
    num_ready_contributors: Union[Unset, int] = UNSET
    participants: Union[Unset, List["Participant"]] = UNSET
    participation_status: Union[Unset, ParticipationStatus] = UNSET
    previous_participants: Union[Unset, List["Participant"]] = UNSET
    privacy_summary: Union[Unset, "PrivacySummary"] = UNSET
    status: Union[Unset, ProjectStatus] = UNSET
    updated_at: Union[Unset, str] = UNSET
    workflow_description: Union[Unset, str] = UNSET
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
        hide_leaf_participants = self.hide_leaf_participants
        local = self.local
        min_contributors = self.min_contributors
        name = self.name
        network_id = self.network_id
        network_name = self.network_name
        non_contributor = self.non_contributor
        policy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.policy, Unset):
            policy = self.policy.to_dict()

        query_timeout = self.query_timeout
        recurring_end_time = self.recurring_end_time
        recurring_interval = self.recurring_interval
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

        actions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.actions, Unset):
            actions = self.actions.to_dict()

        authorization_status: Union[Unset, str] = UNSET
        if not isinstance(self.authorization_status, Unset):
            authorization_status = self.authorization_status.value

        computations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.computations, Unset):
            computations = []
            for computations_item_data in self.computations:
                computations_item = computations_item_data.to_dict()

                computations.append(computations_item)

        created_at = self.created_at
        error = self.error
        network: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.network, Unset):
            network = self.network.to_dict()

        num_contributors = self.num_contributors
        num_ready_contributors = self.num_ready_contributors
        participants: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.participants, Unset):
            participants = []
            for participants_item_data in self.participants:
                participants_item = participants_item_data.to_dict()

                participants.append(participants_item)

        participation_status: Union[Unset, str] = UNSET
        if not isinstance(self.participation_status, Unset):
            participation_status = self.participation_status.value

        previous_participants: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.previous_participants, Unset):
            previous_participants = []
            for previous_participants_item_data in self.previous_participants:
                previous_participants_item = previous_participants_item_data.to_dict()

                previous_participants.append(previous_participants_item)

        privacy_summary: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.privacy_summary, Unset):
            privacy_summary = self.privacy_summary.to_dict()

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        updated_at = self.updated_at
        workflow_description = self.workflow_description

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
        if policy is not UNSET:
            field_dict["policy"] = policy
        if query_timeout is not UNSET:
            field_dict["queryTimeout"] = query_timeout
        if recurring_end_time is not UNSET:
            field_dict["recurringEndTime"] = recurring_end_time
        if recurring_interval is not UNSET:
            field_dict["recurringInterval"] = recurring_interval
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
        if actions is not UNSET:
            field_dict["actions"] = actions
        if authorization_status is not UNSET:
            field_dict["authorizationStatus"] = authorization_status
        if computations is not UNSET:
            field_dict["computations"] = computations
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if error is not UNSET:
            field_dict["error"] = error
        if network is not UNSET:
            field_dict["network"] = network
        if num_contributors is not UNSET:
            field_dict["numContributors"] = num_contributors
        if num_ready_contributors is not UNSET:
            field_dict["numReadyContributors"] = num_ready_contributors
        if participants is not UNSET:
            field_dict["participants"] = participants
        if participation_status is not UNSET:
            field_dict["participationStatus"] = participation_status
        if previous_participants is not UNSET:
            field_dict["previousParticipants"] = previous_participants
        if privacy_summary is not UNSET:
            field_dict["privacySummary"] = privacy_summary
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if workflow_description is not UNSET:
            field_dict["workflowDescription"] = workflow_description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.computation import Computation
        from ..models.computation_definition import ComputationDefinition
        from ..models.computation_policy import ComputationPolicy
        from ..models.network import Network
        from ..models.participant import Participant
        from ..models.privacy_summary import PrivacySummary
        from ..models.project_actions import ProjectActions

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

        hide_leaf_participants = d.pop("hideLeafParticipants", UNSET)

        local = d.pop("local", UNSET)

        min_contributors = d.pop("minContributors", UNSET)

        name = d.pop("name", UNSET)

        network_id = d.pop("networkId", UNSET)

        network_name = d.pop("networkName", UNSET)

        non_contributor = d.pop("nonContributor", UNSET)

        _policy = d.pop("policy", UNSET)
        policy: Union[Unset, ComputationPolicy]
        if isinstance(_policy, Unset):
            policy = UNSET
        else:
            policy = ComputationPolicy.from_dict(_policy)

        query_timeout = d.pop("queryTimeout", UNSET)

        recurring_end_time = d.pop("recurringEndTime", UNSET)

        recurring_interval = d.pop("recurringInterval", UNSET)

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

        _actions = d.pop("actions", UNSET)
        actions: Union[Unset, ProjectActions]
        if isinstance(_actions, Unset):
            actions = UNSET
        else:
            actions = ProjectActions.from_dict(_actions)

        _authorization_status = d.pop("authorizationStatus", UNSET)
        authorization_status: Union[Unset, AuthorizationStatus]
        if isinstance(_authorization_status, Unset):
            authorization_status = UNSET
        else:
            authorization_status = AuthorizationStatus(_authorization_status)

        computations = []
        _computations = d.pop("computations", UNSET)
        for computations_item_data in _computations or []:
            computations_item = Computation.from_dict(computations_item_data)

            computations.append(computations_item)

        created_at = d.pop("createdAt", UNSET)

        error = d.pop("error", UNSET)

        _network = d.pop("network", UNSET)
        network: Union[Unset, Network]
        if isinstance(_network, Unset):
            network = UNSET
        else:
            network = Network.from_dict(_network)

        num_contributors = d.pop("numContributors", UNSET)

        num_ready_contributors = d.pop("numReadyContributors", UNSET)

        participants = []
        _participants = d.pop("participants", UNSET)
        for participants_item_data in _participants or []:
            participants_item = Participant.from_dict(participants_item_data)

            participants.append(participants_item)

        _participation_status = d.pop("participationStatus", UNSET)
        participation_status: Union[Unset, ParticipationStatus]
        if isinstance(_participation_status, Unset):
            participation_status = UNSET
        else:
            participation_status = ParticipationStatus(_participation_status)

        previous_participants = []
        _previous_participants = d.pop("previousParticipants", UNSET)
        for previous_participants_item_data in _previous_participants or []:
            previous_participants_item = Participant.from_dict(previous_participants_item_data)

            previous_participants.append(previous_participants_item)

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

        project = cls(
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
            hide_leaf_participants=hide_leaf_participants,
            local=local,
            min_contributors=min_contributors,
            name=name,
            network_id=network_id,
            network_name=network_name,
            non_contributor=non_contributor,
            policy=policy,
            query_timeout=query_timeout,
            recurring_end_time=recurring_end_time,
            recurring_interval=recurring_interval,
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
            actions=actions,
            authorization_status=authorization_status,
            computations=computations,
            created_at=created_at,
            error=error,
            network=network,
            num_contributors=num_contributors,
            num_ready_contributors=num_ready_contributors,
            participants=participants,
            participation_status=participation_status,
            previous_participants=previous_participants,
            privacy_summary=privacy_summary,
            status=status,
            updated_at=updated_at,
            workflow_description=workflow_description,
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
