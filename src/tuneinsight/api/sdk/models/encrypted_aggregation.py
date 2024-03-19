from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.computation_definition_input_clipping_method import ComputationDefinitionInputClippingMethod
from ..models.computation_type import ComputationType
from ..models.run_mode import RunMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.computation_data_source_parameters import ComputationDataSourceParameters
    from ..models.computation_preprocessing_parameters import ComputationPreprocessingParameters
    from ..models.dp_policy import DPPolicy
    from ..models.local_input import LocalInput


T = TypeVar("T", bound="EncryptedAggregation")


@attr.s(auto_attribs=True)
class EncryptedAggregation:
    """
    Attributes:
        type (ComputationType): Type of the computation.
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
        preprocessing_parameters (Union[Unset, ComputationPreprocessingParameters]): dataframe pre-processing parameters
            applied to the input retrieved from the datasource, if applicable
        wait (Union[Unset, bool]): Whether to wait synchronously for the computation result.
        dp_policy (Union[Unset, DPPolicy]): represents the disclosure prevention policy that enables toggling various
            disclosure prevention mechanisms
        dp_epsilon (Union[Unset, float]): If positive, the privacy budget used by this computation. Used only in DP
            mode. Default: -1.0.
        join_id (Union[Unset, str]): Unique identifier of a data object.
        local_input_id (Union[Unset, str]): Unique identifier of a data object.
        maximum_aggregated_value (Union[Unset, None, float]): optional upper bound on the total expected value to be
            aggregated collectively. If provided, the computation will automatically deduce
            optimal cryptographic parameters in order to maximize precision while allowing encoding values up to this bound.
            If this parameter is not specified, then the default parameters will be used, which can accommodate total values
            up to 16 million.
            For example, when using default parameters and running an aggregation with 4 participants, local aggregated
            values cannot exceed 4 million.
        cohort_id (Union[Unset, str]): Unique identifier of a data object.
        local_input (Union[Unset, LocalInput]): If a local input is provided, the node initiating the computation will
            use it instead of querying the datasource. This data is *not* shared to other nodes, only used for the duration
            of the computation. The local input columns/values must be in the form {<column1>: [<value1>, <value2>, ...],
            ...}
        owner (Union[Unset, str]): The username of the end user who requested the computation.
        project_id (Union[Unset, str]): Unique identifier of a project.
        run_mode (Union[Unset, RunMode]): Defines the mode in which to run a computation (local, collective, or both)
        local (Union[Unset, bool]): True if the project's computation should run only with local data (not configured
            the network)
        encrypted (Union[Unset, bool]): True if computation result should be encrypted with the collective public key.
        end_to_end_encrypted (Union[Unset, bool]): if the end to end encrypted mode is set to true,
            then when release results is set to true and the output
            is initially encrypted with a network collective key, then it is key switched to
            the initiating user's public key.
        input_data_object (Union[Unset, str]): Shared identifier of a data object.
        release_results (Union[Unset, bool]): flag to set to true if the computation should directly release the output
            results.
            If set, then encrypted results are automatically key switched and decrypted
            and a Result entity is saved
        timeout (Union[Unset, int]): The maximum amount of time in seconds the computation is allowed to run.
        data_source_parameters (Union[Unset, ComputationDataSourceParameters]): Parameters used to query the datasource
            from each node before the computation
        count_column (Union[Unset, str]): The column, if any, that is a count column (of 1s). Used in DP mode to improve
            accuracy.
        features (Union[Unset, str]): Shared identifier of a data object.
        lower_bounds (Union[Unset, List[float]]): Lower bounds on the values in each column of the aggregation. Used in
            DP mode for clipping and sensitivity.
        nb_features (Union[Unset, int]): Number of columns of the dataset
        upper_bounds (Union[Unset, List[float]]): Upper bounds on the values in each column of the aggregation. Used in
            DP mode for clipping and sensitivity.
        aggregate_columns (Union[Unset, List[str]]): The columns on which the data should be aggregated
        aggregate_features (Union[Unset, bool]): If true, sum the columns together into one number
    """

    type: ComputationType
    input_clipping_method: Union[Unset, ComputationDefinitionInputClippingMethod] = (
        ComputationDefinitionInputClippingMethod.WARNING
    )
    preprocessing_parameters: Union[Unset, "ComputationPreprocessingParameters"] = UNSET
    wait: Union[Unset, bool] = UNSET
    dp_policy: Union[Unset, "DPPolicy"] = UNSET
    dp_epsilon: Union[Unset, float] = -1.0
    join_id: Union[Unset, str] = UNSET
    local_input_id: Union[Unset, str] = UNSET
    maximum_aggregated_value: Union[Unset, None, float] = UNSET
    cohort_id: Union[Unset, str] = UNSET
    local_input: Union[Unset, "LocalInput"] = UNSET
    owner: Union[Unset, str] = UNSET
    project_id: Union[Unset, str] = UNSET
    run_mode: Union[Unset, RunMode] = UNSET
    local: Union[Unset, bool] = UNSET
    encrypted: Union[Unset, bool] = UNSET
    end_to_end_encrypted: Union[Unset, bool] = UNSET
    input_data_object: Union[Unset, str] = UNSET
    release_results: Union[Unset, bool] = UNSET
    timeout: Union[Unset, int] = UNSET
    data_source_parameters: Union[Unset, "ComputationDataSourceParameters"] = UNSET
    count_column: Union[Unset, str] = UNSET
    features: Union[Unset, str] = UNSET
    lower_bounds: Union[Unset, List[float]] = UNSET
    nb_features: Union[Unset, int] = UNSET
    upper_bounds: Union[Unset, List[float]] = UNSET
    aggregate_columns: Union[Unset, List[str]] = UNSET
    aggregate_features: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        input_clipping_method: Union[Unset, str] = UNSET
        if not isinstance(self.input_clipping_method, Unset):
            input_clipping_method = self.input_clipping_method.value

        preprocessing_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.preprocessing_parameters, Unset):
            preprocessing_parameters = self.preprocessing_parameters.to_dict()

        wait = self.wait
        dp_policy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dp_policy, Unset):
            dp_policy = self.dp_policy.to_dict()

        dp_epsilon = self.dp_epsilon
        join_id = self.join_id
        local_input_id = self.local_input_id
        maximum_aggregated_value = self.maximum_aggregated_value
        cohort_id = self.cohort_id
        local_input: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.local_input, Unset):
            local_input = self.local_input.to_dict()

        owner = self.owner
        project_id = self.project_id
        run_mode: Union[Unset, str] = UNSET
        if not isinstance(self.run_mode, Unset):
            run_mode = self.run_mode.value

        local = self.local
        encrypted = self.encrypted
        end_to_end_encrypted = self.end_to_end_encrypted
        input_data_object = self.input_data_object
        release_results = self.release_results
        timeout = self.timeout
        data_source_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data_source_parameters, Unset):
            data_source_parameters = self.data_source_parameters.to_dict()

        count_column = self.count_column
        features = self.features
        lower_bounds: Union[Unset, List[float]] = UNSET
        if not isinstance(self.lower_bounds, Unset):
            lower_bounds = self.lower_bounds

        nb_features = self.nb_features
        upper_bounds: Union[Unset, List[float]] = UNSET
        if not isinstance(self.upper_bounds, Unset):
            upper_bounds = self.upper_bounds

        aggregate_columns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.aggregate_columns, Unset):
            aggregate_columns = self.aggregate_columns

        aggregate_features = self.aggregate_features

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if input_clipping_method is not UNSET:
            field_dict["inputClippingMethod"] = input_clipping_method
        if preprocessing_parameters is not UNSET:
            field_dict["preprocessingParameters"] = preprocessing_parameters
        if wait is not UNSET:
            field_dict["wait"] = wait
        if dp_policy is not UNSET:
            field_dict["DPPolicy"] = dp_policy
        if dp_epsilon is not UNSET:
            field_dict["dpEpsilon"] = dp_epsilon
        if join_id is not UNSET:
            field_dict["joinId"] = join_id
        if local_input_id is not UNSET:
            field_dict["localInputID"] = local_input_id
        if maximum_aggregated_value is not UNSET:
            field_dict["maximumAggregatedValue"] = maximum_aggregated_value
        if cohort_id is not UNSET:
            field_dict["cohortId"] = cohort_id
        if local_input is not UNSET:
            field_dict["localInput"] = local_input
        if owner is not UNSET:
            field_dict["owner"] = owner
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if run_mode is not UNSET:
            field_dict["runMode"] = run_mode
        if local is not UNSET:
            field_dict["local"] = local
        if encrypted is not UNSET:
            field_dict["encrypted"] = encrypted
        if end_to_end_encrypted is not UNSET:
            field_dict["endToEndEncrypted"] = end_to_end_encrypted
        if input_data_object is not UNSET:
            field_dict["inputDataObject"] = input_data_object
        if release_results is not UNSET:
            field_dict["releaseResults"] = release_results
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if data_source_parameters is not UNSET:
            field_dict["dataSourceParameters"] = data_source_parameters
        if count_column is not UNSET:
            field_dict["countColumn"] = count_column
        if features is not UNSET:
            field_dict["features"] = features
        if lower_bounds is not UNSET:
            field_dict["lowerBounds"] = lower_bounds
        if nb_features is not UNSET:
            field_dict["nbFeatures"] = nb_features
        if upper_bounds is not UNSET:
            field_dict["upperBounds"] = upper_bounds
        if aggregate_columns is not UNSET:
            field_dict["aggregateColumns"] = aggregate_columns
        if aggregate_features is not UNSET:
            field_dict["aggregateFeatures"] = aggregate_features

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.computation_data_source_parameters import ComputationDataSourceParameters
        from ..models.computation_preprocessing_parameters import ComputationPreprocessingParameters
        from ..models.dp_policy import DPPolicy
        from ..models.local_input import LocalInput

        d = src_dict.copy()
        type = ComputationType(d.pop("type"))

        _input_clipping_method = d.pop("inputClippingMethod", UNSET)
        input_clipping_method: Union[Unset, ComputationDefinitionInputClippingMethod]
        if isinstance(_input_clipping_method, Unset):
            input_clipping_method = UNSET
        else:
            input_clipping_method = ComputationDefinitionInputClippingMethod(_input_clipping_method)

        _preprocessing_parameters = d.pop("preprocessingParameters", UNSET)
        preprocessing_parameters: Union[Unset, ComputationPreprocessingParameters]
        if isinstance(_preprocessing_parameters, Unset):
            preprocessing_parameters = UNSET
        else:
            preprocessing_parameters = ComputationPreprocessingParameters.from_dict(_preprocessing_parameters)

        wait = d.pop("wait", UNSET)

        _dp_policy = d.pop("DPPolicy", UNSET)
        dp_policy: Union[Unset, DPPolicy]
        if isinstance(_dp_policy, Unset):
            dp_policy = UNSET
        else:
            dp_policy = DPPolicy.from_dict(_dp_policy)

        dp_epsilon = d.pop("dpEpsilon", UNSET)

        join_id = d.pop("joinId", UNSET)

        local_input_id = d.pop("localInputID", UNSET)

        maximum_aggregated_value = d.pop("maximumAggregatedValue", UNSET)

        cohort_id = d.pop("cohortId", UNSET)

        _local_input = d.pop("localInput", UNSET)
        local_input: Union[Unset, LocalInput]
        if isinstance(_local_input, Unset):
            local_input = UNSET
        else:
            local_input = LocalInput.from_dict(_local_input)

        owner = d.pop("owner", UNSET)

        project_id = d.pop("projectId", UNSET)

        _run_mode = d.pop("runMode", UNSET)
        run_mode: Union[Unset, RunMode]
        if isinstance(_run_mode, Unset):
            run_mode = UNSET
        else:
            run_mode = RunMode(_run_mode)

        local = d.pop("local", UNSET)

        encrypted = d.pop("encrypted", UNSET)

        end_to_end_encrypted = d.pop("endToEndEncrypted", UNSET)

        input_data_object = d.pop("inputDataObject", UNSET)

        release_results = d.pop("releaseResults", UNSET)

        timeout = d.pop("timeout", UNSET)

        _data_source_parameters = d.pop("dataSourceParameters", UNSET)
        data_source_parameters: Union[Unset, ComputationDataSourceParameters]
        if isinstance(_data_source_parameters, Unset):
            data_source_parameters = UNSET
        else:
            data_source_parameters = ComputationDataSourceParameters.from_dict(_data_source_parameters)

        count_column = d.pop("countColumn", UNSET)

        features = d.pop("features", UNSET)

        lower_bounds = cast(List[float], d.pop("lowerBounds", UNSET))

        nb_features = d.pop("nbFeatures", UNSET)

        upper_bounds = cast(List[float], d.pop("upperBounds", UNSET))

        aggregate_columns = cast(List[str], d.pop("aggregateColumns", UNSET))

        aggregate_features = d.pop("aggregateFeatures", UNSET)

        encrypted_aggregation = cls(
            type=type,
            input_clipping_method=input_clipping_method,
            preprocessing_parameters=preprocessing_parameters,
            wait=wait,
            dp_policy=dp_policy,
            dp_epsilon=dp_epsilon,
            join_id=join_id,
            local_input_id=local_input_id,
            maximum_aggregated_value=maximum_aggregated_value,
            cohort_id=cohort_id,
            local_input=local_input,
            owner=owner,
            project_id=project_id,
            run_mode=run_mode,
            local=local,
            encrypted=encrypted,
            end_to_end_encrypted=end_to_end_encrypted,
            input_data_object=input_data_object,
            release_results=release_results,
            timeout=timeout,
            data_source_parameters=data_source_parameters,
            count_column=count_column,
            features=features,
            lower_bounds=lower_bounds,
            nb_features=nb_features,
            upper_bounds=upper_bounds,
            aggregate_columns=aggregate_columns,
            aggregate_features=aggregate_features,
        )

        encrypted_aggregation.additional_properties = d
        return encrypted_aggregation

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
