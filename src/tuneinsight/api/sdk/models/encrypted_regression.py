from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.computation_type import ComputationType
from ..models.logical_operator import LogicalOperator
from ..models.run_mode import RunMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.computation_data_source_parameters import ComputationDataSourceParameters
    from ..models.computation_preprocessing_parameters import ComputationPreprocessingParameters
    from ..models.dp_policy import DPPolicy
    from ..models.encrypted_regression_params import EncryptedRegressionParams
    from ..models.local_input import LocalInput
    from ..models.unit_filter import UnitFilter


T = TypeVar("T", bound="EncryptedRegression")


@attr.s(auto_attribs=True)
class EncryptedRegression:
    """
    Attributes:
        type (ComputationType): Type of the computation.
        dp_policy (Union[Unset, DPPolicy]): represents the disclosure prevention policy that enables toggling various
            mechanisms that are executed whenever the workflow runs.
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
        linkage_operator (Union[Unset, LogicalOperator]): A logical operator to "aggregate" multiple boolean values.
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
        query_timeout (Union[Unset, int]): The maximum amount of time in seconds the data source query is allowed to
            run.
        record_deduplication (Union[Unset, bool]): controls whether records are deduplicated or not when performing
            record linkage.
        release_results (Union[Unset, bool]): flag to set to true if the computation should directly release the output
            results.
            If set, then encrypted results are automatically key switched and decrypted
            and a Result entity is saved
        run_mode (Union[Unset, RunMode]): Defines the mode in which to run a computation (local, collective, or both)
        timeout (Union[Unset, int]): The maximum amount of time in seconds the computation is allowed to run.
        units (Union[Unset, List['UnitFilter']]): unit requirements for the numerical values in the computation. Used to
            filter input records with mismatching units.
        wait (Union[Unset, bool]): Whether to wait synchronously for the computation result.
        feature_columns (Union[Unset, List[str]]): specified columns from the input dataset corresponding to the
            features
        l2clipping (Union[Unset, float]): clipping factor for data points (in L2 norm) when using differential privacy
            Default: 1.0.
        label_columns (Union[Unset, List[str]]): specified columns from the input dataset corresponding to the labels
        means (Union[Unset, List[float]]): Means to substract from each record as part of standardization. If not
            provided, the means
            are inferred from the data, except when differential privacy is used. It is recommended to
            set this value when using differential privacy (using a DP estimator for the means).
        params (Union[Unset, EncryptedRegressionParams]): Parameters for the encrypted regression.
        standard_deviations (Union[Unset, List[float]]): Standard deviations by which to divide each record as part of
            standardization. If not provided,
            the stddevs are inferred from the data, except when differential privacy is used. It is recommended
            to set this value when using differential privacy (using a DP estimator for the stddevs).
        target_model_name (Union[Unset, str]): common name to give to the output model
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
    linkage_operator: Union[Unset, LogicalOperator] = UNSET
    local: Union[Unset, bool] = UNSET
    local_input: Union[Unset, "LocalInput"] = UNSET
    local_input_id: Union[Unset, str] = UNSET
    owner: Union[Unset, str] = UNSET
    precision: Union[Unset, None, int] = UNSET
    preprocessing_parameters: Union[Unset, "ComputationPreprocessingParameters"] = UNSET
    project_id: Union[Unset, str] = UNSET
    query_timeout: Union[Unset, int] = UNSET
    record_deduplication: Union[Unset, bool] = UNSET
    release_results: Union[Unset, bool] = UNSET
    run_mode: Union[Unset, RunMode] = UNSET
    timeout: Union[Unset, int] = UNSET
    units: Union[Unset, List["UnitFilter"]] = UNSET
    wait: Union[Unset, bool] = UNSET
    feature_columns: Union[Unset, List[str]] = UNSET
    l2clipping: Union[Unset, float] = 1.0
    label_columns: Union[Unset, List[str]] = UNSET
    means: Union[Unset, List[float]] = UNSET
    params: Union[Unset, "EncryptedRegressionParams"] = UNSET
    standard_deviations: Union[Unset, List[float]] = UNSET
    target_model_name: Union[Unset, str] = UNSET
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
        linkage_operator: Union[Unset, str] = UNSET
        if not isinstance(self.linkage_operator, Unset):
            linkage_operator = self.linkage_operator.value

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
        query_timeout = self.query_timeout
        record_deduplication = self.record_deduplication
        release_results = self.release_results
        run_mode: Union[Unset, str] = UNSET
        if not isinstance(self.run_mode, Unset):
            run_mode = self.run_mode.value

        timeout = self.timeout
        units: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.units, Unset):
            units = []
            for units_item_data in self.units:
                units_item = units_item_data.to_dict()

                units.append(units_item)

        wait = self.wait
        feature_columns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.feature_columns, Unset):
            feature_columns = self.feature_columns

        l2clipping = self.l2clipping
        label_columns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.label_columns, Unset):
            label_columns = self.label_columns

        means: Union[Unset, List[float]] = UNSET
        if not isinstance(self.means, Unset):
            means = self.means

        params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        standard_deviations: Union[Unset, List[float]] = UNSET
        if not isinstance(self.standard_deviations, Unset):
            standard_deviations = self.standard_deviations

        target_model_name = self.target_model_name

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
        if linkage_operator is not UNSET:
            field_dict["linkageOperator"] = linkage_operator
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
        if query_timeout is not UNSET:
            field_dict["queryTimeout"] = query_timeout
        if record_deduplication is not UNSET:
            field_dict["recordDeduplication"] = record_deduplication
        if release_results is not UNSET:
            field_dict["releaseResults"] = release_results
        if run_mode is not UNSET:
            field_dict["runMode"] = run_mode
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if units is not UNSET:
            field_dict["units"] = units
        if wait is not UNSET:
            field_dict["wait"] = wait
        if feature_columns is not UNSET:
            field_dict["featureColumns"] = feature_columns
        if l2clipping is not UNSET:
            field_dict["l2clipping"] = l2clipping
        if label_columns is not UNSET:
            field_dict["labelColumns"] = label_columns
        if means is not UNSET:
            field_dict["means"] = means
        if params is not UNSET:
            field_dict["params"] = params
        if standard_deviations is not UNSET:
            field_dict["standardDeviations"] = standard_deviations
        if target_model_name is not UNSET:
            field_dict["targetModelName"] = target_model_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.computation_data_source_parameters import ComputationDataSourceParameters
        from ..models.computation_preprocessing_parameters import ComputationPreprocessingParameters
        from ..models.dp_policy import DPPolicy
        from ..models.encrypted_regression_params import EncryptedRegressionParams
        from ..models.local_input import LocalInput
        from ..models.unit_filter import UnitFilter

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

        _linkage_operator = d.pop("linkageOperator", UNSET)
        linkage_operator: Union[Unset, LogicalOperator]
        if isinstance(_linkage_operator, Unset):
            linkage_operator = UNSET
        else:
            linkage_operator = LogicalOperator(_linkage_operator)

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

        query_timeout = d.pop("queryTimeout", UNSET)

        record_deduplication = d.pop("recordDeduplication", UNSET)

        release_results = d.pop("releaseResults", UNSET)

        _run_mode = d.pop("runMode", UNSET)
        run_mode: Union[Unset, RunMode]
        if isinstance(_run_mode, Unset):
            run_mode = UNSET
        else:
            run_mode = RunMode(_run_mode)

        timeout = d.pop("timeout", UNSET)

        units = []
        _units = d.pop("units", UNSET)
        for units_item_data in _units or []:
            units_item = UnitFilter.from_dict(units_item_data)

            units.append(units_item)

        wait = d.pop("wait", UNSET)

        feature_columns = cast(List[str], d.pop("featureColumns", UNSET))

        l2clipping = d.pop("l2clipping", UNSET)

        label_columns = cast(List[str], d.pop("labelColumns", UNSET))

        means = cast(List[float], d.pop("means", UNSET))

        _params = d.pop("params", UNSET)
        params: Union[Unset, EncryptedRegressionParams]
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = EncryptedRegressionParams.from_dict(_params)

        standard_deviations = cast(List[float], d.pop("standardDeviations", UNSET))

        target_model_name = d.pop("targetModelName", UNSET)

        encrypted_regression = cls(
            type=type,
            dp_policy=dp_policy,
            cohort_id=cohort_id,
            data_source_parameters=data_source_parameters,
            dp_epsilon=dp_epsilon,
            encrypted=encrypted,
            end_to_end_encrypted=end_to_end_encrypted,
            ignore_boundary_checks=ignore_boundary_checks,
            input_data_object=input_data_object,
            linkage_operator=linkage_operator,
            local=local,
            local_input=local_input,
            local_input_id=local_input_id,
            owner=owner,
            precision=precision,
            preprocessing_parameters=preprocessing_parameters,
            project_id=project_id,
            query_timeout=query_timeout,
            record_deduplication=record_deduplication,
            release_results=release_results,
            run_mode=run_mode,
            timeout=timeout,
            units=units,
            wait=wait,
            feature_columns=feature_columns,
            l2clipping=l2clipping,
            label_columns=label_columns,
            means=means,
            params=params,
            standard_deviations=standard_deviations,
            target_model_name=target_model_name,
        )

        encrypted_regression.additional_properties = d
        return encrypted_regression

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
