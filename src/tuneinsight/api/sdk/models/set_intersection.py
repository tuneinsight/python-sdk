from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.computation_type import ComputationType
from ..models.run_mode import RunMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.computation_data_source_parameters import ComputationDataSourceParameters
    from ..models.computation_preprocessing_parameters import ComputationPreprocessingParameters
    from ..models.dp_policy import DPPolicy
    from ..models.fuzzy_matching_parameters import FuzzyMatchingParameters
    from ..models.local_input import LocalInput


T = TypeVar("T", bound="SetIntersection")


@attr.s(auto_attribs=True)
class SetIntersection:
    """
    Attributes:
        type (ComputationType): Type of the computation.
        dp_policy (Union[Unset, DPPolicy]): represents the disclosure prevention policy that enables toggling various
            disclosure prevention mechanisms
        cohort_id (Union[Unset, str]): Unique identifier of a data object.
        data_source_parameters (Union[Unset, ComputationDataSourceParameters]): Parameters used to query the datasource
            from each node before the computation
        dp_epsilon (Union[Unset, float]): If positive, the privacy budget used by this computation. Used only in DP
            mode. Default: -1.0.
        encrypted (Union[Unset, bool]): True if computation result should be encrypted with the collective public key.
        end_to_end_encrypted (Union[Unset, bool]): if the end to end encrypted mode is set to true,
            then when release results is set to true and the output
            is initially encrypted with a network collective key, then it is key switched to
            the initiating user's public key.
        ignore_boundary_checks (Union[Unset, bool]): when set to true, data boundary checks are disabled. (WARNING
            setting this to true can lead to erroneous results)
        input_data_object (Union[Unset, str]): Shared identifier of a data object.
        local (Union[Unset, bool]): True if the project's computation should run only with local data (not configured
            the network)
        local_input (Union[Unset, LocalInput]): If a local input is provided, the node initiating the computation will
            use it instead of querying the datasource. This data is *not* shared to other nodes, only used for the duration
            of the computation. The local input columns/values must be in the form {<column1>: [<value1>, <value2>, ...],
            ...}
        local_input_id (Union[Unset, str]): Unique identifier of a data object.
        owner (Union[Unset, str]): The username of the end user who requested the computation.
        precision (Union[Unset, None, int]): optional minimum required bit precision to guarantee when aggregating
            results.
            If the precision is set to `x`, then the user can expect the results error to be bounded by `2^(-x)`
            when comparing the decrypted results to the expected results.
            When encoding and encrypting data using FHE, the underlying scheme's parameterization offers a tradeoff between
            precision
            and input sizes. By default, the computation will choose parameters which allow for large values to be encoded
            but only offer 4 bits of precision.
            By default, the precision of results is set to 4 bits, which allows for large inputs.
            Note that only the following computations support this parameterization:
              - aggregation.
              - encrypted mean.
        preprocessing_parameters (Union[Unset, ComputationPreprocessingParameters]): dataframe pre-processing parameters
            applied to the input retrieved from the datasource, if applicable
        project_id (Union[Unset, str]): Unique identifier of a project.
        release_results (Union[Unset, bool]): flag to set to true if the computation should directly release the output
            results.
            If set, then encrypted results are automatically key switched and decrypted
            and a Result entity is saved
        run_mode (Union[Unset, RunMode]): Defines the mode in which to run a computation (local, collective, or both)
        timeout (Union[Unset, int]): The maximum amount of time in seconds the computation is allowed to run.
        wait (Union[Unset, bool]): Whether to wait synchronously for the computation result.
        encrypted_results (Union[Unset, bool]): if true, then the resulting matches are kept encrypted
        fuzzy_params (Union[Unset, FuzzyMatchingParameters]):
        hide_matching_origin (Union[Unset, bool]): if true, then the matches are aggregated before being decrypted,
            hiding the organizations with whom the items matched.
        matching_columns (Union[Unset, List[str]]): The columns on which the data should be matched
        max_chunk_size (Union[Unset, int]): the maximum chunk size the sender is willing to process at once
        share_results (Union[Unset, bool]): If true, then the intersection results decrypted on the initiating instance
            are shared to the other instances.
    """

    type: ComputationType
    dp_policy: Union[Unset, "DPPolicy"] = UNSET
    cohort_id: Union[Unset, str] = UNSET
    data_source_parameters: Union[Unset, "ComputationDataSourceParameters"] = UNSET
    dp_epsilon: Union[Unset, float] = -1.0
    encrypted: Union[Unset, bool] = UNSET
    end_to_end_encrypted: Union[Unset, bool] = UNSET
    ignore_boundary_checks: Union[Unset, bool] = UNSET
    input_data_object: Union[Unset, str] = UNSET
    local: Union[Unset, bool] = UNSET
    local_input: Union[Unset, "LocalInput"] = UNSET
    local_input_id: Union[Unset, str] = UNSET
    owner: Union[Unset, str] = UNSET
    precision: Union[Unset, None, int] = UNSET
    preprocessing_parameters: Union[Unset, "ComputationPreprocessingParameters"] = UNSET
    project_id: Union[Unset, str] = UNSET
    release_results: Union[Unset, bool] = UNSET
    run_mode: Union[Unset, RunMode] = UNSET
    timeout: Union[Unset, int] = UNSET
    wait: Union[Unset, bool] = UNSET
    encrypted_results: Union[Unset, bool] = UNSET
    fuzzy_params: Union[Unset, "FuzzyMatchingParameters"] = UNSET
    hide_matching_origin: Union[Unset, bool] = UNSET
    matching_columns: Union[Unset, List[str]] = UNSET
    max_chunk_size: Union[Unset, int] = UNSET
    share_results: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        dp_policy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dp_policy, Unset):
            dp_policy = self.dp_policy.to_dict()

        cohort_id = self.cohort_id
        data_source_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data_source_parameters, Unset):
            data_source_parameters = self.data_source_parameters.to_dict()

        dp_epsilon = self.dp_epsilon
        encrypted = self.encrypted
        end_to_end_encrypted = self.end_to_end_encrypted
        ignore_boundary_checks = self.ignore_boundary_checks
        input_data_object = self.input_data_object
        local = self.local
        local_input: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.local_input, Unset):
            local_input = self.local_input.to_dict()

        local_input_id = self.local_input_id
        owner = self.owner
        precision = self.precision
        preprocessing_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.preprocessing_parameters, Unset):
            preprocessing_parameters = self.preprocessing_parameters.to_dict()

        project_id = self.project_id
        release_results = self.release_results
        run_mode: Union[Unset, str] = UNSET
        if not isinstance(self.run_mode, Unset):
            run_mode = self.run_mode.value

        timeout = self.timeout
        wait = self.wait
        encrypted_results = self.encrypted_results
        fuzzy_params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fuzzy_params, Unset):
            fuzzy_params = self.fuzzy_params.to_dict()

        hide_matching_origin = self.hide_matching_origin
        matching_columns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.matching_columns, Unset):
            matching_columns = self.matching_columns

        max_chunk_size = self.max_chunk_size
        share_results = self.share_results

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if dp_policy is not UNSET:
            field_dict["DPPolicy"] = dp_policy
        if cohort_id is not UNSET:
            field_dict["cohortId"] = cohort_id
        if data_source_parameters is not UNSET:
            field_dict["dataSourceParameters"] = data_source_parameters
        if dp_epsilon is not UNSET:
            field_dict["dpEpsilon"] = dp_epsilon
        if encrypted is not UNSET:
            field_dict["encrypted"] = encrypted
        if end_to_end_encrypted is not UNSET:
            field_dict["endToEndEncrypted"] = end_to_end_encrypted
        if ignore_boundary_checks is not UNSET:
            field_dict["ignoreBoundaryChecks"] = ignore_boundary_checks
        if input_data_object is not UNSET:
            field_dict["inputDataObject"] = input_data_object
        if local is not UNSET:
            field_dict["local"] = local
        if local_input is not UNSET:
            field_dict["localInput"] = local_input
        if local_input_id is not UNSET:
            field_dict["localInputID"] = local_input_id
        if owner is not UNSET:
            field_dict["owner"] = owner
        if precision is not UNSET:
            field_dict["precision"] = precision
        if preprocessing_parameters is not UNSET:
            field_dict["preprocessingParameters"] = preprocessing_parameters
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if release_results is not UNSET:
            field_dict["releaseResults"] = release_results
        if run_mode is not UNSET:
            field_dict["runMode"] = run_mode
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if wait is not UNSET:
            field_dict["wait"] = wait
        if encrypted_results is not UNSET:
            field_dict["encryptedResults"] = encrypted_results
        if fuzzy_params is not UNSET:
            field_dict["fuzzyParams"] = fuzzy_params
        if hide_matching_origin is not UNSET:
            field_dict["hideMatchingOrigin"] = hide_matching_origin
        if matching_columns is not UNSET:
            field_dict["matchingColumns"] = matching_columns
        if max_chunk_size is not UNSET:
            field_dict["maxChunkSize"] = max_chunk_size
        if share_results is not UNSET:
            field_dict["shareResults"] = share_results

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.computation_data_source_parameters import ComputationDataSourceParameters
        from ..models.computation_preprocessing_parameters import ComputationPreprocessingParameters
        from ..models.dp_policy import DPPolicy
        from ..models.fuzzy_matching_parameters import FuzzyMatchingParameters
        from ..models.local_input import LocalInput

        d = src_dict.copy()
        type = ComputationType(d.pop("type"))

        _dp_policy = d.pop("DPPolicy", UNSET)
        dp_policy: Union[Unset, DPPolicy]
        if isinstance(_dp_policy, Unset):
            dp_policy = UNSET
        else:
            dp_policy = DPPolicy.from_dict(_dp_policy)

        cohort_id = d.pop("cohortId", UNSET)

        _data_source_parameters = d.pop("dataSourceParameters", UNSET)
        data_source_parameters: Union[Unset, ComputationDataSourceParameters]
        if isinstance(_data_source_parameters, Unset):
            data_source_parameters = UNSET
        else:
            data_source_parameters = ComputationDataSourceParameters.from_dict(_data_source_parameters)

        dp_epsilon = d.pop("dpEpsilon", UNSET)

        encrypted = d.pop("encrypted", UNSET)

        end_to_end_encrypted = d.pop("endToEndEncrypted", UNSET)

        ignore_boundary_checks = d.pop("ignoreBoundaryChecks", UNSET)

        input_data_object = d.pop("inputDataObject", UNSET)

        local = d.pop("local", UNSET)

        _local_input = d.pop("localInput", UNSET)
        local_input: Union[Unset, LocalInput]
        if isinstance(_local_input, Unset):
            local_input = UNSET
        else:
            local_input = LocalInput.from_dict(_local_input)

        local_input_id = d.pop("localInputID", UNSET)

        owner = d.pop("owner", UNSET)

        precision = d.pop("precision", UNSET)

        _preprocessing_parameters = d.pop("preprocessingParameters", UNSET)
        preprocessing_parameters: Union[Unset, ComputationPreprocessingParameters]
        if isinstance(_preprocessing_parameters, Unset):
            preprocessing_parameters = UNSET
        else:
            preprocessing_parameters = ComputationPreprocessingParameters.from_dict(_preprocessing_parameters)

        project_id = d.pop("projectId", UNSET)

        release_results = d.pop("releaseResults", UNSET)

        _run_mode = d.pop("runMode", UNSET)
        run_mode: Union[Unset, RunMode]
        if isinstance(_run_mode, Unset):
            run_mode = UNSET
        else:
            run_mode = RunMode(_run_mode)

        timeout = d.pop("timeout", UNSET)

        wait = d.pop("wait", UNSET)

        encrypted_results = d.pop("encryptedResults", UNSET)

        _fuzzy_params = d.pop("fuzzyParams", UNSET)
        fuzzy_params: Union[Unset, FuzzyMatchingParameters]
        if isinstance(_fuzzy_params, Unset):
            fuzzy_params = UNSET
        else:
            fuzzy_params = FuzzyMatchingParameters.from_dict(_fuzzy_params)

        hide_matching_origin = d.pop("hideMatchingOrigin", UNSET)

        matching_columns = cast(List[str], d.pop("matchingColumns", UNSET))

        max_chunk_size = d.pop("maxChunkSize", UNSET)

        share_results = d.pop("shareResults", UNSET)

        set_intersection = cls(
            type=type,
            dp_policy=dp_policy,
            cohort_id=cohort_id,
            data_source_parameters=data_source_parameters,
            dp_epsilon=dp_epsilon,
            encrypted=encrypted,
            end_to_end_encrypted=end_to_end_encrypted,
            ignore_boundary_checks=ignore_boundary_checks,
            input_data_object=input_data_object,
            local=local,
            local_input=local_input,
            local_input_id=local_input_id,
            owner=owner,
            precision=precision,
            preprocessing_parameters=preprocessing_parameters,
            project_id=project_id,
            release_results=release_results,
            run_mode=run_mode,
            timeout=timeout,
            wait=wait,
            encrypted_results=encrypted_results,
            fuzzy_params=fuzzy_params,
            hide_matching_origin=hide_matching_origin,
            matching_columns=matching_columns,
            max_chunk_size=max_chunk_size,
            share_results=share_results,
        )

        set_intersection.additional_properties = d
        return set_intersection

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
