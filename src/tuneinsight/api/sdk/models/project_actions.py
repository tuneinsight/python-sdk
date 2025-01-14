from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.run_mode import RunMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.availability_status import AvailabilityStatus


T = TypeVar("T", bound="ProjectActions")


@attr.s(auto_attribs=True)
class ProjectActions:
    """regroups availability statuses of relevant user actions on a project and remaining queries when running
    computations.

        Attributes:
            available_run_modes (Union[Unset, List[RunMode]]): list of run modes that are currently supported.
            edit_data_source (Union[Unset, AvailabilityStatus]): generic object that holds information about whether a
                resource or action is available to the user.
            edit_operation_params (Union[Unset, AvailabilityStatus]): generic object that holds information about whether a
                resource or action is available to the user.
            edit_operation_type (Union[Unset, AvailabilityStatus]): generic object that holds information about whether a
                resource or action is available to the user.
            edit_policy (Union[Unset, AvailabilityStatus]): generic object that holds information about whether a resource
                or action is available to the user.
            edit_preprocessing (Union[Unset, AvailabilityStatus]): generic object that holds information about whether a
                resource or action is available to the user.
            edit_query (Union[Unset, AvailabilityStatus]): generic object that holds information about whether a resource or
                action is available to the user.
            remaining_collective_runs (Union[Unset, None, int]): if an execution quota is setup with the project,
                this field returns the remaining number of collective computations that can be run with this project.
            remaining_local_runs (Union[Unset, None, int]): if an execution quota is setup with the project,
                this field returns the remaining number of local computations that can be run with this project.
            request_auth (Union[Unset, AvailabilityStatus]): generic object that holds information about whether a resource
                or action is available to the user.
            revoke_auth_request (Union[Unset, AvailabilityStatus]): generic object that holds information about whether a
                resource or action is available to the user.
            run_collective (Union[Unset, AvailabilityStatus]): generic object that holds information about whether a
                resource or action is available to the user.
            run_local (Union[Unset, AvailabilityStatus]): generic object that holds information about whether a resource or
                action is available to the user.
            share (Union[Unset, AvailabilityStatus]): generic object that holds information about whether a resource or
                action is available to the user.
    """

    available_run_modes: Union[Unset, List[RunMode]] = UNSET
    edit_data_source: Union[Unset, "AvailabilityStatus"] = UNSET
    edit_operation_params: Union[Unset, "AvailabilityStatus"] = UNSET
    edit_operation_type: Union[Unset, "AvailabilityStatus"] = UNSET
    edit_policy: Union[Unset, "AvailabilityStatus"] = UNSET
    edit_preprocessing: Union[Unset, "AvailabilityStatus"] = UNSET
    edit_query: Union[Unset, "AvailabilityStatus"] = UNSET
    remaining_collective_runs: Union[Unset, None, int] = UNSET
    remaining_local_runs: Union[Unset, None, int] = UNSET
    request_auth: Union[Unset, "AvailabilityStatus"] = UNSET
    revoke_auth_request: Union[Unset, "AvailabilityStatus"] = UNSET
    run_collective: Union[Unset, "AvailabilityStatus"] = UNSET
    run_local: Union[Unset, "AvailabilityStatus"] = UNSET
    share: Union[Unset, "AvailabilityStatus"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        available_run_modes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.available_run_modes, Unset):
            available_run_modes = []
            for available_run_modes_item_data in self.available_run_modes:
                available_run_modes_item = available_run_modes_item_data.value

                available_run_modes.append(available_run_modes_item)

        edit_data_source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.edit_data_source, Unset):
            edit_data_source = self.edit_data_source.to_dict()

        edit_operation_params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.edit_operation_params, Unset):
            edit_operation_params = self.edit_operation_params.to_dict()

        edit_operation_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.edit_operation_type, Unset):
            edit_operation_type = self.edit_operation_type.to_dict()

        edit_policy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.edit_policy, Unset):
            edit_policy = self.edit_policy.to_dict()

        edit_preprocessing: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.edit_preprocessing, Unset):
            edit_preprocessing = self.edit_preprocessing.to_dict()

        edit_query: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.edit_query, Unset):
            edit_query = self.edit_query.to_dict()

        remaining_collective_runs = self.remaining_collective_runs
        remaining_local_runs = self.remaining_local_runs
        request_auth: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.request_auth, Unset):
            request_auth = self.request_auth.to_dict()

        revoke_auth_request: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.revoke_auth_request, Unset):
            revoke_auth_request = self.revoke_auth_request.to_dict()

        run_collective: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.run_collective, Unset):
            run_collective = self.run_collective.to_dict()

        run_local: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.run_local, Unset):
            run_local = self.run_local.to_dict()

        share: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.share, Unset):
            share = self.share.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if available_run_modes is not UNSET:
            field_dict["availableRunModes"] = available_run_modes
        if edit_data_source is not UNSET:
            field_dict["editDataSource"] = edit_data_source
        if edit_operation_params is not UNSET:
            field_dict["editOperationParams"] = edit_operation_params
        if edit_operation_type is not UNSET:
            field_dict["editOperationType"] = edit_operation_type
        if edit_policy is not UNSET:
            field_dict["editPolicy"] = edit_policy
        if edit_preprocessing is not UNSET:
            field_dict["editPreprocessing"] = edit_preprocessing
        if edit_query is not UNSET:
            field_dict["editQuery"] = edit_query
        if remaining_collective_runs is not UNSET:
            field_dict["remainingCollectiveRuns"] = remaining_collective_runs
        if remaining_local_runs is not UNSET:
            field_dict["remainingLocalRuns"] = remaining_local_runs
        if request_auth is not UNSET:
            field_dict["requestAuth"] = request_auth
        if revoke_auth_request is not UNSET:
            field_dict["revokeAuthRequest"] = revoke_auth_request
        if run_collective is not UNSET:
            field_dict["runCollective"] = run_collective
        if run_local is not UNSET:
            field_dict["runLocal"] = run_local
        if share is not UNSET:
            field_dict["share"] = share

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.availability_status import AvailabilityStatus

        d = src_dict.copy()
        available_run_modes = []
        _available_run_modes = d.pop("availableRunModes", UNSET)
        for available_run_modes_item_data in _available_run_modes or []:
            available_run_modes_item = RunMode(available_run_modes_item_data)

            available_run_modes.append(available_run_modes_item)

        _edit_data_source = d.pop("editDataSource", UNSET)
        edit_data_source: Union[Unset, AvailabilityStatus]
        if isinstance(_edit_data_source, Unset):
            edit_data_source = UNSET
        else:
            edit_data_source = AvailabilityStatus.from_dict(_edit_data_source)

        _edit_operation_params = d.pop("editOperationParams", UNSET)
        edit_operation_params: Union[Unset, AvailabilityStatus]
        if isinstance(_edit_operation_params, Unset):
            edit_operation_params = UNSET
        else:
            edit_operation_params = AvailabilityStatus.from_dict(_edit_operation_params)

        _edit_operation_type = d.pop("editOperationType", UNSET)
        edit_operation_type: Union[Unset, AvailabilityStatus]
        if isinstance(_edit_operation_type, Unset):
            edit_operation_type = UNSET
        else:
            edit_operation_type = AvailabilityStatus.from_dict(_edit_operation_type)

        _edit_policy = d.pop("editPolicy", UNSET)
        edit_policy: Union[Unset, AvailabilityStatus]
        if isinstance(_edit_policy, Unset):
            edit_policy = UNSET
        else:
            edit_policy = AvailabilityStatus.from_dict(_edit_policy)

        _edit_preprocessing = d.pop("editPreprocessing", UNSET)
        edit_preprocessing: Union[Unset, AvailabilityStatus]
        if isinstance(_edit_preprocessing, Unset):
            edit_preprocessing = UNSET
        else:
            edit_preprocessing = AvailabilityStatus.from_dict(_edit_preprocessing)

        _edit_query = d.pop("editQuery", UNSET)
        edit_query: Union[Unset, AvailabilityStatus]
        if isinstance(_edit_query, Unset):
            edit_query = UNSET
        else:
            edit_query = AvailabilityStatus.from_dict(_edit_query)

        remaining_collective_runs = d.pop("remainingCollectiveRuns", UNSET)

        remaining_local_runs = d.pop("remainingLocalRuns", UNSET)

        _request_auth = d.pop("requestAuth", UNSET)
        request_auth: Union[Unset, AvailabilityStatus]
        if isinstance(_request_auth, Unset):
            request_auth = UNSET
        else:
            request_auth = AvailabilityStatus.from_dict(_request_auth)

        _revoke_auth_request = d.pop("revokeAuthRequest", UNSET)
        revoke_auth_request: Union[Unset, AvailabilityStatus]
        if isinstance(_revoke_auth_request, Unset):
            revoke_auth_request = UNSET
        else:
            revoke_auth_request = AvailabilityStatus.from_dict(_revoke_auth_request)

        _run_collective = d.pop("runCollective", UNSET)
        run_collective: Union[Unset, AvailabilityStatus]
        if isinstance(_run_collective, Unset):
            run_collective = UNSET
        else:
            run_collective = AvailabilityStatus.from_dict(_run_collective)

        _run_local = d.pop("runLocal", UNSET)
        run_local: Union[Unset, AvailabilityStatus]
        if isinstance(_run_local, Unset):
            run_local = UNSET
        else:
            run_local = AvailabilityStatus.from_dict(_run_local)

        _share = d.pop("share", UNSET)
        share: Union[Unset, AvailabilityStatus]
        if isinstance(_share, Unset):
            share = UNSET
        else:
            share = AvailabilityStatus.from_dict(_share)

        project_actions = cls(
            available_run_modes=available_run_modes,
            edit_data_source=edit_data_source,
            edit_operation_params=edit_operation_params,
            edit_operation_type=edit_operation_type,
            edit_policy=edit_policy,
            edit_preprocessing=edit_preprocessing,
            edit_query=edit_query,
            remaining_collective_runs=remaining_collective_runs,
            remaining_local_runs=remaining_local_runs,
            request_auth=request_auth,
            revoke_auth_request=revoke_auth_request,
            run_collective=run_collective,
            run_local=run_local,
            share=share,
        )

        project_actions.additional_properties = d
        return project_actions

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
