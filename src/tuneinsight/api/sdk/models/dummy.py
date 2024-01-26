from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.computation_type import ComputationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.computation_data_source_parameters import ComputationDataSourceParameters
    from ..models.computation_preprocessing_parameters import ComputationPreprocessingParameters
    from ..models.dp_policy import DPPolicy
    from ..models.local_input import LocalInput


T = TypeVar("T", bound="Dummy")


@attr.s(auto_attribs=True)
class Dummy:
    """
    Attributes:
        type (ComputationType): Type of the computation.
        local (Union[Unset, bool]): True if the project's computation should run only with local data (not configured
            the network)
        local_input (Union[Unset, LocalInput]): If a local input is provided, the node initiating the computation will
            use it instead of querying the datasource. This data is *not* shared to other nodes, only used for the duration
            of the computation. The local input columns/values must be in the form {<column1>: [<value1>, <value2>, ...],
            ...}
        preprocessing_parameters (Union[Unset, ComputationPreprocessingParameters]): dataframe pre-processing parameters
            applied to the input retrieved from the datasource, if applicable
        cohort_id (Union[Unset, str]): Unique identifier of a data object.
        end_to_end_encrypted (Union[Unset, bool]): if the end to end encrypted mode is set to true,
            then when release results is set to true and the output
            is initially encrypted with a network collective key, then it is key switched to
            the initiating user's public key.
        local_input_id (Union[Unset, str]): Unique identifier of a data object.
        wait (Union[Unset, bool]): Whether to wait synchronously for the computation result.
        dp_policy (Union[Unset, DPPolicy]): represents the disclosure prevention policy that enables toggling various
            disclosure prevention mechanisms
        join_id (Union[Unset, str]): Unique identifier of a data object.
        timeout (Union[Unset, int]): The maximum amount of time in seconds the computation is allowed to run.
        encrypted (Union[Unset, bool]): True if computation result should be encrypted with the collective public key.
        owner (Union[Unset, str]): The username of the end user who requested the computation.
        project_id (Union[Unset, str]): Unique identifier of a project.
        release_results (Union[Unset, bool]): flag to set to true if the computation should directly release the output
            results.
            If set, then encrypted results are automatically key switched and decrypted
            and a Result entity is saved
        data_source_parameters (Union[Unset, ComputationDataSourceParameters]): Parameters used to query the datasource
            from each node before the computation
        input_data_object (Union[Unset, str]): Shared identifier of a data object.
        panic_in_constructor (Union[Unset, bool]):
        panic_in_start (Union[Unset, bool]):
        error_in_constructor (Union[Unset, bool]):
        error_in_start (Union[Unset, bool]):
    """

    type: ComputationType
    local: Union[Unset, bool] = UNSET
    local_input: Union[Unset, "LocalInput"] = UNSET
    preprocessing_parameters: Union[Unset, "ComputationPreprocessingParameters"] = UNSET
    cohort_id: Union[Unset, str] = UNSET
    end_to_end_encrypted: Union[Unset, bool] = UNSET
    local_input_id: Union[Unset, str] = UNSET
    wait: Union[Unset, bool] = UNSET
    dp_policy: Union[Unset, "DPPolicy"] = UNSET
    join_id: Union[Unset, str] = UNSET
    timeout: Union[Unset, int] = UNSET
    encrypted: Union[Unset, bool] = UNSET
    owner: Union[Unset, str] = UNSET
    project_id: Union[Unset, str] = UNSET
    release_results: Union[Unset, bool] = UNSET
    data_source_parameters: Union[Unset, "ComputationDataSourceParameters"] = UNSET
    input_data_object: Union[Unset, str] = UNSET
    panic_in_constructor: Union[Unset, bool] = UNSET
    panic_in_start: Union[Unset, bool] = UNSET
    error_in_constructor: Union[Unset, bool] = UNSET
    error_in_start: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        local = self.local
        local_input: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.local_input, Unset):
            local_input = self.local_input.to_dict()

        preprocessing_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.preprocessing_parameters, Unset):
            preprocessing_parameters = self.preprocessing_parameters.to_dict()

        cohort_id = self.cohort_id
        end_to_end_encrypted = self.end_to_end_encrypted
        local_input_id = self.local_input_id
        wait = self.wait
        dp_policy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dp_policy, Unset):
            dp_policy = self.dp_policy.to_dict()

        join_id = self.join_id
        timeout = self.timeout
        encrypted = self.encrypted
        owner = self.owner
        project_id = self.project_id
        release_results = self.release_results
        data_source_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data_source_parameters, Unset):
            data_source_parameters = self.data_source_parameters.to_dict()

        input_data_object = self.input_data_object
        panic_in_constructor = self.panic_in_constructor
        panic_in_start = self.panic_in_start
        error_in_constructor = self.error_in_constructor
        error_in_start = self.error_in_start

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if local is not UNSET:
            field_dict["local"] = local
        if local_input is not UNSET:
            field_dict["localInput"] = local_input
        if preprocessing_parameters is not UNSET:
            field_dict["preprocessingParameters"] = preprocessing_parameters
        if cohort_id is not UNSET:
            field_dict["cohortId"] = cohort_id
        if end_to_end_encrypted is not UNSET:
            field_dict["endToEndEncrypted"] = end_to_end_encrypted
        if local_input_id is not UNSET:
            field_dict["localInputID"] = local_input_id
        if wait is not UNSET:
            field_dict["wait"] = wait
        if dp_policy is not UNSET:
            field_dict["DPPolicy"] = dp_policy
        if join_id is not UNSET:
            field_dict["joinId"] = join_id
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if encrypted is not UNSET:
            field_dict["encrypted"] = encrypted
        if owner is not UNSET:
            field_dict["owner"] = owner
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if release_results is not UNSET:
            field_dict["releaseResults"] = release_results
        if data_source_parameters is not UNSET:
            field_dict["dataSourceParameters"] = data_source_parameters
        if input_data_object is not UNSET:
            field_dict["inputDataObject"] = input_data_object
        if panic_in_constructor is not UNSET:
            field_dict["panicInConstructor"] = panic_in_constructor
        if panic_in_start is not UNSET:
            field_dict["panicInStart"] = panic_in_start
        if error_in_constructor is not UNSET:
            field_dict["errorInConstructor"] = error_in_constructor
        if error_in_start is not UNSET:
            field_dict["errorInStart"] = error_in_start

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.computation_data_source_parameters import ComputationDataSourceParameters
        from ..models.computation_preprocessing_parameters import ComputationPreprocessingParameters
        from ..models.dp_policy import DPPolicy
        from ..models.local_input import LocalInput

        d = src_dict.copy()
        type = ComputationType(d.pop("type"))

        local = d.pop("local", UNSET)

        _local_input = d.pop("localInput", UNSET)
        local_input: Union[Unset, LocalInput]
        if isinstance(_local_input, Unset):
            local_input = UNSET
        else:
            local_input = LocalInput.from_dict(_local_input)

        _preprocessing_parameters = d.pop("preprocessingParameters", UNSET)
        preprocessing_parameters: Union[Unset, ComputationPreprocessingParameters]
        if isinstance(_preprocessing_parameters, Unset):
            preprocessing_parameters = UNSET
        else:
            preprocessing_parameters = ComputationPreprocessingParameters.from_dict(_preprocessing_parameters)

        cohort_id = d.pop("cohortId", UNSET)

        end_to_end_encrypted = d.pop("endToEndEncrypted", UNSET)

        local_input_id = d.pop("localInputID", UNSET)

        wait = d.pop("wait", UNSET)

        _dp_policy = d.pop("DPPolicy", UNSET)
        dp_policy: Union[Unset, DPPolicy]
        if isinstance(_dp_policy, Unset):
            dp_policy = UNSET
        else:
            dp_policy = DPPolicy.from_dict(_dp_policy)

        join_id = d.pop("joinId", UNSET)

        timeout = d.pop("timeout", UNSET)

        encrypted = d.pop("encrypted", UNSET)

        owner = d.pop("owner", UNSET)

        project_id = d.pop("projectId", UNSET)

        release_results = d.pop("releaseResults", UNSET)

        _data_source_parameters = d.pop("dataSourceParameters", UNSET)
        data_source_parameters: Union[Unset, ComputationDataSourceParameters]
        if isinstance(_data_source_parameters, Unset):
            data_source_parameters = UNSET
        else:
            data_source_parameters = ComputationDataSourceParameters.from_dict(_data_source_parameters)

        input_data_object = d.pop("inputDataObject", UNSET)

        panic_in_constructor = d.pop("panicInConstructor", UNSET)

        panic_in_start = d.pop("panicInStart", UNSET)

        error_in_constructor = d.pop("errorInConstructor", UNSET)

        error_in_start = d.pop("errorInStart", UNSET)

        dummy = cls(
            type=type,
            local=local,
            local_input=local_input,
            preprocessing_parameters=preprocessing_parameters,
            cohort_id=cohort_id,
            end_to_end_encrypted=end_to_end_encrypted,
            local_input_id=local_input_id,
            wait=wait,
            dp_policy=dp_policy,
            join_id=join_id,
            timeout=timeout,
            encrypted=encrypted,
            owner=owner,
            project_id=project_id,
            release_results=release_results,
            data_source_parameters=data_source_parameters,
            input_data_object=input_data_object,
            panic_in_constructor=panic_in_constructor,
            panic_in_start=panic_in_start,
            error_in_constructor=error_in_constructor,
            error_in_start=error_in_start,
        )

        dummy.additional_properties = d
        return dummy

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
