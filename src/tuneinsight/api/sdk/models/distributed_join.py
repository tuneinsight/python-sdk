from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.computation_type import ComputationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.computation_data_source_parameters import ComputationDataSourceParameters
    from ..models.computation_preprocessing_parameters import ComputationPreprocessingParameters
    from ..models.dp_policy import DPPolicy
    from ..models.local_input import LocalInput


T = TypeVar("T", bound="DistributedJoin")


@attr.s(auto_attribs=True)
class DistributedJoin:
    """
    Attributes:
        type (ComputationType): Type of the computation.
        encrypted (Union[Unset, bool]): True if computation result should be encrypted with the collective public key.
        local_input_id (Union[Unset, str]): Unique identifier of a data object.
        project_id (Union[Unset, str]): Unique identifier of a project.
        dp_policy (Union[Unset, DPPolicy]): represents the disclosure prevention policy that enables toggling various
            disclosure prevention mechanisms
        cohort_id (Union[Unset, str]): Unique identifier of a data object.
        wait (Union[Unset, bool]): Whether to wait synchronously for the computation result.
        preprocessing_parameters (Union[Unset, ComputationPreprocessingParameters]): dataframe pre-processing parameters
            applied to the input retrieved from the datasource, if applicable
        timeout (Union[Unset, int]): The maximum amount of time in seconds the computation is allowed to run.
        owner (Union[Unset, str]): The username of the user who started the computation.
        data_source_parameters (Union[Unset, ComputationDataSourceParameters]): Parameters used to query the datasource
            from each node before the computation
        local (Union[Unset, bool]): True if the project's computation should run only with local data (not configured
            the network)
        local_input (Union[Unset, LocalInput]): If a local input is provided, the node initiating the computation will
            use it instead of querying the datasource. This data is *not* shared to other nodes, only used for the duration
            of the computation. The local input columns/values must be in the form {<column1>: [<value1>, <value2>, ...],
            ...}
        input_data_object (Union[Unset, str]): Shared identifier of a data object.
        join_id (Union[Unset, str]): Unique identifier of a data object.
        join_columns (Union[Unset, List[str]]):
        missing_patterns (Union[Unset, List[str]]):
        target_columns (Union[Unset, List[str]]):
    """

    type: ComputationType
    encrypted: Union[Unset, bool] = UNSET
    local_input_id: Union[Unset, str] = UNSET
    project_id: Union[Unset, str] = UNSET
    dp_policy: Union[Unset, "DPPolicy"] = UNSET
    cohort_id: Union[Unset, str] = UNSET
    wait: Union[Unset, bool] = UNSET
    preprocessing_parameters: Union[Unset, "ComputationPreprocessingParameters"] = UNSET
    timeout: Union[Unset, int] = UNSET
    owner: Union[Unset, str] = UNSET
    data_source_parameters: Union[Unset, "ComputationDataSourceParameters"] = UNSET
    local: Union[Unset, bool] = UNSET
    local_input: Union[Unset, "LocalInput"] = UNSET
    input_data_object: Union[Unset, str] = UNSET
    join_id: Union[Unset, str] = UNSET
    join_columns: Union[Unset, List[str]] = UNSET
    missing_patterns: Union[Unset, List[str]] = UNSET
    target_columns: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        encrypted = self.encrypted
        local_input_id = self.local_input_id
        project_id = self.project_id
        dp_policy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dp_policy, Unset):
            dp_policy = self.dp_policy.to_dict()

        cohort_id = self.cohort_id
        wait = self.wait
        preprocessing_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.preprocessing_parameters, Unset):
            preprocessing_parameters = self.preprocessing_parameters.to_dict()

        timeout = self.timeout
        owner = self.owner
        data_source_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data_source_parameters, Unset):
            data_source_parameters = self.data_source_parameters.to_dict()

        local = self.local
        local_input: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.local_input, Unset):
            local_input = self.local_input.to_dict()

        input_data_object = self.input_data_object
        join_id = self.join_id
        join_columns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.join_columns, Unset):
            join_columns = self.join_columns

        missing_patterns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.missing_patterns, Unset):
            missing_patterns = self.missing_patterns

        target_columns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.target_columns, Unset):
            target_columns = self.target_columns

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if encrypted is not UNSET:
            field_dict["encrypted"] = encrypted
        if local_input_id is not UNSET:
            field_dict["localInputID"] = local_input_id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if dp_policy is not UNSET:
            field_dict["DPPolicy"] = dp_policy
        if cohort_id is not UNSET:
            field_dict["cohortId"] = cohort_id
        if wait is not UNSET:
            field_dict["wait"] = wait
        if preprocessing_parameters is not UNSET:
            field_dict["preprocessingParameters"] = preprocessing_parameters
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if owner is not UNSET:
            field_dict["owner"] = owner
        if data_source_parameters is not UNSET:
            field_dict["dataSourceParameters"] = data_source_parameters
        if local is not UNSET:
            field_dict["local"] = local
        if local_input is not UNSET:
            field_dict["localInput"] = local_input
        if input_data_object is not UNSET:
            field_dict["inputDataObject"] = input_data_object
        if join_id is not UNSET:
            field_dict["joinId"] = join_id
        if join_columns is not UNSET:
            field_dict["joinColumns"] = join_columns
        if missing_patterns is not UNSET:
            field_dict["missingPatterns"] = missing_patterns
        if target_columns is not UNSET:
            field_dict["targetColumns"] = target_columns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.computation_data_source_parameters import ComputationDataSourceParameters
        from ..models.computation_preprocessing_parameters import ComputationPreprocessingParameters
        from ..models.dp_policy import DPPolicy
        from ..models.local_input import LocalInput

        d = src_dict.copy()
        type = ComputationType(d.pop("type"))

        encrypted = d.pop("encrypted", UNSET)

        local_input_id = d.pop("localInputID", UNSET)

        project_id = d.pop("projectId", UNSET)

        _dp_policy = d.pop("DPPolicy", UNSET)
        dp_policy: Union[Unset, DPPolicy]
        if isinstance(_dp_policy, Unset):
            dp_policy = UNSET
        else:
            dp_policy = DPPolicy.from_dict(_dp_policy)

        cohort_id = d.pop("cohortId", UNSET)

        wait = d.pop("wait", UNSET)

        _preprocessing_parameters = d.pop("preprocessingParameters", UNSET)
        preprocessing_parameters: Union[Unset, ComputationPreprocessingParameters]
        if isinstance(_preprocessing_parameters, Unset):
            preprocessing_parameters = UNSET
        else:
            preprocessing_parameters = ComputationPreprocessingParameters.from_dict(_preprocessing_parameters)

        timeout = d.pop("timeout", UNSET)

        owner = d.pop("owner", UNSET)

        _data_source_parameters = d.pop("dataSourceParameters", UNSET)
        data_source_parameters: Union[Unset, ComputationDataSourceParameters]
        if isinstance(_data_source_parameters, Unset):
            data_source_parameters = UNSET
        else:
            data_source_parameters = ComputationDataSourceParameters.from_dict(_data_source_parameters)

        local = d.pop("local", UNSET)

        _local_input = d.pop("localInput", UNSET)
        local_input: Union[Unset, LocalInput]
        if isinstance(_local_input, Unset):
            local_input = UNSET
        else:
            local_input = LocalInput.from_dict(_local_input)

        input_data_object = d.pop("inputDataObject", UNSET)

        join_id = d.pop("joinId", UNSET)

        join_columns = cast(List[str], d.pop("joinColumns", UNSET))

        missing_patterns = cast(List[str], d.pop("missingPatterns", UNSET))

        target_columns = cast(List[str], d.pop("targetColumns", UNSET))

        distributed_join = cls(
            type=type,
            encrypted=encrypted,
            local_input_id=local_input_id,
            project_id=project_id,
            dp_policy=dp_policy,
            cohort_id=cohort_id,
            wait=wait,
            preprocessing_parameters=preprocessing_parameters,
            timeout=timeout,
            owner=owner,
            data_source_parameters=data_source_parameters,
            local=local,
            local_input=local_input,
            input_data_object=input_data_object,
            join_id=join_id,
            join_columns=join_columns,
            missing_patterns=missing_patterns,
            target_columns=target_columns,
        )

        distributed_join.additional_properties = d
        return distributed_join

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
