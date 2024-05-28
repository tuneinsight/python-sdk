from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.computation_definition_input_clipping_method import ComputationDefinitionInputClippingMethod
from ..models.computation_type import ComputationType
from ..models.run_mode import RunMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.binning_operation import BinningOperation
    from ..models.computation_data_source_parameters import ComputationDataSourceParameters
    from ..models.computation_preprocessing_parameters import ComputationPreprocessingParameters
    from ..models.dp_policy import DPPolicy
    from ..models.local_input import LocalInput


T = TypeVar("T", bound="StatisticalAggregation")


@attr.s(auto_attribs=True)
class StatisticalAggregation:
    """
    Attributes:
        type (ComputationType): Type of the computation.
        release_results (Union[Unset, bool]): flag to set to true if the computation should directly release the output
            results.
            If set, then encrypted results are automatically key switched and decrypted
            and a Result entity is saved
        run_mode (Union[Unset, RunMode]): Defines the mode in which to run a computation (local, collective, or both)
        timeout (Union[Unset, int]): The maximum amount of time in seconds the computation is allowed to run.
        input_clipping_method (Union[Unset, ComputationDefinitionInputClippingMethod]): Optional method used for
            clipping before encrypting values when running aggregation-based workflows.
            The bounds are deduced based on the cryptographic parameters used for the aggregation.
            It can take the following values:
              - none: no clipping is applied and the output may contain overflowed values.
              - silent: automatic clipping is applied silently locally.
              - warning: automatic clipping is applied. If some values are clipped then a warning is issued (locally).
            (default)
              - error: if some values are out of bounds, then the computation is aborted.
             Default: ComputationDefinitionInputClippingMethod.WARNING.
        join_id (Union[Unset, str]): Unique identifier of a data object.
        maximum_aggregated_value (Union[Unset, None, float]): optional upper bound on the total expected value to be
            aggregated collectively. If provided, the computation will automatically deduce
            optimal cryptographic parameters in order to maximize precision while allowing encoding values up to this bound.
            If this parameter is not specified, then the default parameters will be used, which can accommodate total values
            up to 16 million.
            For example, when using default parameters and running an aggregation with 4 participants, local aggregated
            values cannot exceed 4 million.
        owner (Union[Unset, str]): The username of the end user who requested the computation.
        preprocessing_parameters (Union[Unset, ComputationPreprocessingParameters]): dataframe pre-processing parameters
            applied to the input retrieved from the datasource, if applicable
        project_id (Union[Unset, str]): Unique identifier of a project.
        dp_epsilon (Union[Unset, float]): If positive, the privacy budget used by this computation. Used only in DP
            mode. Default: -1.0.
        encrypted (Union[Unset, bool]): True if computation result should be encrypted with the collective public key.
        local (Union[Unset, bool]): True if the project's computation should run only with local data (not configured
            the network)
        local_input_id (Union[Unset, str]): Unique identifier of a data object.
        wait (Union[Unset, bool]): Whether to wait synchronously for the computation result.
        cohort_id (Union[Unset, str]): Unique identifier of a data object.
        data_source_parameters (Union[Unset, ComputationDataSourceParameters]): Parameters used to query the datasource
            from each node before the computation
        end_to_end_encrypted (Union[Unset, bool]): if the end to end encrypted mode is set to true,
            then when release results is set to true and the output
            is initially encrypted with a network collective key, then it is key switched to
            the initiating user's public key.
        input_data_object (Union[Unset, str]): Shared identifier of a data object.
        dp_policy (Union[Unset, DPPolicy]): represents the disclosure prevention policy that enables toggling various
            disclosure prevention mechanisms
        local_input (Union[Unset, LocalInput]): If a local input is provided, the node initiating the computation will
            use it instead of querying the datasource. This data is *not* shared to other nodes, only used for the duration
            of the computation. The local input columns/values must be in the form {<column1>: [<value1>, <value2>, ...],
            ...}
        aggregation_columns (Union[Unset, List[str]]): list of columns where all data is aggregated
        binning_operations (Union[Unset, List['BinningOperation']]): list of binning operations to apply before
            aggregating the results
        include_dataset_length (Union[Unset, bool]): whether or not to compute the total dataset length
    """

    type: ComputationType
    release_results: Union[Unset, bool] = UNSET
    run_mode: Union[Unset, RunMode] = UNSET
    timeout: Union[Unset, int] = UNSET
    input_clipping_method: Union[Unset, ComputationDefinitionInputClippingMethod] = (
        ComputationDefinitionInputClippingMethod.WARNING
    )
    join_id: Union[Unset, str] = UNSET
    maximum_aggregated_value: Union[Unset, None, float] = UNSET
    owner: Union[Unset, str] = UNSET
    preprocessing_parameters: Union[Unset, "ComputationPreprocessingParameters"] = UNSET
    project_id: Union[Unset, str] = UNSET
    dp_epsilon: Union[Unset, float] = -1.0
    encrypted: Union[Unset, bool] = UNSET
    local: Union[Unset, bool] = UNSET
    local_input_id: Union[Unset, str] = UNSET
    wait: Union[Unset, bool] = UNSET
    cohort_id: Union[Unset, str] = UNSET
    data_source_parameters: Union[Unset, "ComputationDataSourceParameters"] = UNSET
    end_to_end_encrypted: Union[Unset, bool] = UNSET
    input_data_object: Union[Unset, str] = UNSET
    dp_policy: Union[Unset, "DPPolicy"] = UNSET
    local_input: Union[Unset, "LocalInput"] = UNSET
    aggregation_columns: Union[Unset, List[str]] = UNSET
    binning_operations: Union[Unset, List["BinningOperation"]] = UNSET
    include_dataset_length: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        release_results = self.release_results
        run_mode: Union[Unset, str] = UNSET
        if not isinstance(self.run_mode, Unset):
            run_mode = self.run_mode.value

        timeout = self.timeout
        input_clipping_method: Union[Unset, str] = UNSET
        if not isinstance(self.input_clipping_method, Unset):
            input_clipping_method = self.input_clipping_method.value

        join_id = self.join_id
        maximum_aggregated_value = self.maximum_aggregated_value
        owner = self.owner
        preprocessing_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.preprocessing_parameters, Unset):
            preprocessing_parameters = self.preprocessing_parameters.to_dict()

        project_id = self.project_id
        dp_epsilon = self.dp_epsilon
        encrypted = self.encrypted
        local = self.local
        local_input_id = self.local_input_id
        wait = self.wait
        cohort_id = self.cohort_id
        data_source_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data_source_parameters, Unset):
            data_source_parameters = self.data_source_parameters.to_dict()

        end_to_end_encrypted = self.end_to_end_encrypted
        input_data_object = self.input_data_object
        dp_policy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dp_policy, Unset):
            dp_policy = self.dp_policy.to_dict()

        local_input: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.local_input, Unset):
            local_input = self.local_input.to_dict()

        aggregation_columns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.aggregation_columns, Unset):
            aggregation_columns = self.aggregation_columns

        binning_operations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.binning_operations, Unset):
            binning_operations = []
            for binning_operations_item_data in self.binning_operations:
                binning_operations_item = binning_operations_item_data.to_dict()

                binning_operations.append(binning_operations_item)

        include_dataset_length = self.include_dataset_length

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if release_results is not UNSET:
            field_dict["releaseResults"] = release_results
        if run_mode is not UNSET:
            field_dict["runMode"] = run_mode
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if input_clipping_method is not UNSET:
            field_dict["inputClippingMethod"] = input_clipping_method
        if join_id is not UNSET:
            field_dict["joinId"] = join_id
        if maximum_aggregated_value is not UNSET:
            field_dict["maximumAggregatedValue"] = maximum_aggregated_value
        if owner is not UNSET:
            field_dict["owner"] = owner
        if preprocessing_parameters is not UNSET:
            field_dict["preprocessingParameters"] = preprocessing_parameters
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if dp_epsilon is not UNSET:
            field_dict["dpEpsilon"] = dp_epsilon
        if encrypted is not UNSET:
            field_dict["encrypted"] = encrypted
        if local is not UNSET:
            field_dict["local"] = local
        if local_input_id is not UNSET:
            field_dict["localInputID"] = local_input_id
        if wait is not UNSET:
            field_dict["wait"] = wait
        if cohort_id is not UNSET:
            field_dict["cohortId"] = cohort_id
        if data_source_parameters is not UNSET:
            field_dict["dataSourceParameters"] = data_source_parameters
        if end_to_end_encrypted is not UNSET:
            field_dict["endToEndEncrypted"] = end_to_end_encrypted
        if input_data_object is not UNSET:
            field_dict["inputDataObject"] = input_data_object
        if dp_policy is not UNSET:
            field_dict["DPPolicy"] = dp_policy
        if local_input is not UNSET:
            field_dict["localInput"] = local_input
        if aggregation_columns is not UNSET:
            field_dict["aggregationColumns"] = aggregation_columns
        if binning_operations is not UNSET:
            field_dict["binningOperations"] = binning_operations
        if include_dataset_length is not UNSET:
            field_dict["includeDatasetLength"] = include_dataset_length

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.binning_operation import BinningOperation
        from ..models.computation_data_source_parameters import ComputationDataSourceParameters
        from ..models.computation_preprocessing_parameters import ComputationPreprocessingParameters
        from ..models.dp_policy import DPPolicy
        from ..models.local_input import LocalInput

        d = src_dict.copy()
        type = ComputationType(d.pop("type"))

        release_results = d.pop("releaseResults", UNSET)

        _run_mode = d.pop("runMode", UNSET)
        run_mode: Union[Unset, RunMode]
        if isinstance(_run_mode, Unset):
            run_mode = UNSET
        else:
            run_mode = RunMode(_run_mode)

        timeout = d.pop("timeout", UNSET)

        _input_clipping_method = d.pop("inputClippingMethod", UNSET)
        input_clipping_method: Union[Unset, ComputationDefinitionInputClippingMethod]
        if isinstance(_input_clipping_method, Unset):
            input_clipping_method = UNSET
        else:
            input_clipping_method = ComputationDefinitionInputClippingMethod(_input_clipping_method)

        join_id = d.pop("joinId", UNSET)

        maximum_aggregated_value = d.pop("maximumAggregatedValue", UNSET)

        owner = d.pop("owner", UNSET)

        _preprocessing_parameters = d.pop("preprocessingParameters", UNSET)
        preprocessing_parameters: Union[Unset, ComputationPreprocessingParameters]
        if isinstance(_preprocessing_parameters, Unset):
            preprocessing_parameters = UNSET
        else:
            preprocessing_parameters = ComputationPreprocessingParameters.from_dict(_preprocessing_parameters)

        project_id = d.pop("projectId", UNSET)

        dp_epsilon = d.pop("dpEpsilon", UNSET)

        encrypted = d.pop("encrypted", UNSET)

        local = d.pop("local", UNSET)

        local_input_id = d.pop("localInputID", UNSET)

        wait = d.pop("wait", UNSET)

        cohort_id = d.pop("cohortId", UNSET)

        _data_source_parameters = d.pop("dataSourceParameters", UNSET)
        data_source_parameters: Union[Unset, ComputationDataSourceParameters]
        if isinstance(_data_source_parameters, Unset):
            data_source_parameters = UNSET
        else:
            data_source_parameters = ComputationDataSourceParameters.from_dict(_data_source_parameters)

        end_to_end_encrypted = d.pop("endToEndEncrypted", UNSET)

        input_data_object = d.pop("inputDataObject", UNSET)

        _dp_policy = d.pop("DPPolicy", UNSET)
        dp_policy: Union[Unset, DPPolicy]
        if isinstance(_dp_policy, Unset):
            dp_policy = UNSET
        else:
            dp_policy = DPPolicy.from_dict(_dp_policy)

        _local_input = d.pop("localInput", UNSET)
        local_input: Union[Unset, LocalInput]
        if isinstance(_local_input, Unset):
            local_input = UNSET
        else:
            local_input = LocalInput.from_dict(_local_input)

        aggregation_columns = cast(List[str], d.pop("aggregationColumns", UNSET))

        binning_operations = []
        _binning_operations = d.pop("binningOperations", UNSET)
        for binning_operations_item_data in _binning_operations or []:
            binning_operations_item = BinningOperation.from_dict(binning_operations_item_data)

            binning_operations.append(binning_operations_item)

        include_dataset_length = d.pop("includeDatasetLength", UNSET)

        statistical_aggregation = cls(
            type=type,
            release_results=release_results,
            run_mode=run_mode,
            timeout=timeout,
            input_clipping_method=input_clipping_method,
            join_id=join_id,
            maximum_aggregated_value=maximum_aggregated_value,
            owner=owner,
            preprocessing_parameters=preprocessing_parameters,
            project_id=project_id,
            dp_epsilon=dp_epsilon,
            encrypted=encrypted,
            local=local,
            local_input_id=local_input_id,
            wait=wait,
            cohort_id=cohort_id,
            data_source_parameters=data_source_parameters,
            end_to_end_encrypted=end_to_end_encrypted,
            input_data_object=input_data_object,
            dp_policy=dp_policy,
            local_input=local_input,
            aggregation_columns=aggregation_columns,
            binning_operations=binning_operations,
            include_dataset_length=include_dataset_length,
        )

        statistical_aggregation.additional_properties = d
        return statistical_aggregation

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
