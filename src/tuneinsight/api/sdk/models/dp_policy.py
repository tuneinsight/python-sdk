from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execution_quota_parameters import ExecutionQuotaParameters
    from ..models.threshold import Threshold


T = TypeVar("T", bound="DPPolicy")


@attr.s(auto_attribs=True)
class DPPolicy:
    """represents the disclosure prevention policy that enables toggling various disclosure prevention mechanisms

    Attributes:
        max_column_count (Union[Unset, Threshold]): represents a threshold, which can be made relative of the dataset
            size
        max_factors (Union[Unset, Threshold]): represents a threshold, which can be made relative of the dataset size
        noisy_global_size (Union[Unset, bool]): when computing the global size, whether noise is used or not. If so,
            each node adds discrete noise to its input to the encrypted aggregation
        use_differential_privacy (Union[Unset, bool]): whether to use Differential Privacy to protect the privacy of the
            results.
        execution_quota_parameters (Union[Unset, ExecutionQuotaParameters]): Execution quota settings.
            The unit of the execution quota depends on the computation and other policies.
            If differential privacy is applied, it is in terms of the the epsilon value (ϵ) of the privacy budget.
            If the computation is a private set intersection, each query consumes budget equal to the size of the querying
            set.
            Otherwise, a unit represents one computation.
        min_dataset_size (Union[Unset, int]): minimum size of the dataset used as local input (checked both before and
            after the preprocessing operations are run)
        min_frequencies (Union[Unset, Threshold]): represents a threshold, which can be made relative of the dataset
            size
        min_global_dataset_size (Union[Unset, int]): minimum size of the global / collective dataset. It is collectively
            computed using the encrypted aggregation
        authorized_variables (Union[Unset, List[str]]): constraint on the set of variables that can be used as input, in
            order to prevent misuse of variables that are out of context of the project.
            if > 0 variables are defined here, then the dataset will automatically drop any variables that do not belong to
            this set.
            Warning: this mechanism is only effective when the data selection parameters (data source queries) are fixed,
            and therefore
            returned variables cannot be aliased (for example using aliases in SQL SELECT statements) to evade this trap.
    """

    max_column_count: Union[Unset, "Threshold"] = UNSET
    max_factors: Union[Unset, "Threshold"] = UNSET
    noisy_global_size: Union[Unset, bool] = UNSET
    use_differential_privacy: Union[Unset, bool] = False
    execution_quota_parameters: Union[Unset, "ExecutionQuotaParameters"] = UNSET
    min_dataset_size: Union[Unset, int] = UNSET
    min_frequencies: Union[Unset, "Threshold"] = UNSET
    min_global_dataset_size: Union[Unset, int] = UNSET
    authorized_variables: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        max_column_count: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.max_column_count, Unset):
            max_column_count = self.max_column_count.to_dict()

        max_factors: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.max_factors, Unset):
            max_factors = self.max_factors.to_dict()

        noisy_global_size = self.noisy_global_size
        use_differential_privacy = self.use_differential_privacy
        execution_quota_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.execution_quota_parameters, Unset):
            execution_quota_parameters = self.execution_quota_parameters.to_dict()

        min_dataset_size = self.min_dataset_size
        min_frequencies: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.min_frequencies, Unset):
            min_frequencies = self.min_frequencies.to_dict()

        min_global_dataset_size = self.min_global_dataset_size
        authorized_variables: Union[Unset, List[str]] = UNSET
        if not isinstance(self.authorized_variables, Unset):
            authorized_variables = self.authorized_variables

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_column_count is not UNSET:
            field_dict["maxColumnCount"] = max_column_count
        if max_factors is not UNSET:
            field_dict["maxFactors"] = max_factors
        if noisy_global_size is not UNSET:
            field_dict["noisyGlobalSize"] = noisy_global_size
        if use_differential_privacy is not UNSET:
            field_dict["useDifferentialPrivacy"] = use_differential_privacy
        if execution_quota_parameters is not UNSET:
            field_dict["executionQuotaParameters"] = execution_quota_parameters
        if min_dataset_size is not UNSET:
            field_dict["minDatasetSize"] = min_dataset_size
        if min_frequencies is not UNSET:
            field_dict["minFrequencies"] = min_frequencies
        if min_global_dataset_size is not UNSET:
            field_dict["minGlobalDatasetSize"] = min_global_dataset_size
        if authorized_variables is not UNSET:
            field_dict["authorizedVariables"] = authorized_variables

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.execution_quota_parameters import ExecutionQuotaParameters
        from ..models.threshold import Threshold

        d = src_dict.copy()
        _max_column_count = d.pop("maxColumnCount", UNSET)
        max_column_count: Union[Unset, Threshold]
        if isinstance(_max_column_count, Unset):
            max_column_count = UNSET
        else:
            max_column_count = Threshold.from_dict(_max_column_count)

        _max_factors = d.pop("maxFactors", UNSET)
        max_factors: Union[Unset, Threshold]
        if isinstance(_max_factors, Unset):
            max_factors = UNSET
        else:
            max_factors = Threshold.from_dict(_max_factors)

        noisy_global_size = d.pop("noisyGlobalSize", UNSET)

        use_differential_privacy = d.pop("useDifferentialPrivacy", UNSET)

        _execution_quota_parameters = d.pop("executionQuotaParameters", UNSET)
        execution_quota_parameters: Union[Unset, ExecutionQuotaParameters]
        if isinstance(_execution_quota_parameters, Unset):
            execution_quota_parameters = UNSET
        else:
            execution_quota_parameters = ExecutionQuotaParameters.from_dict(_execution_quota_parameters)

        min_dataset_size = d.pop("minDatasetSize", UNSET)

        _min_frequencies = d.pop("minFrequencies", UNSET)
        min_frequencies: Union[Unset, Threshold]
        if isinstance(_min_frequencies, Unset):
            min_frequencies = UNSET
        else:
            min_frequencies = Threshold.from_dict(_min_frequencies)

        min_global_dataset_size = d.pop("minGlobalDatasetSize", UNSET)

        authorized_variables = cast(List[str], d.pop("authorizedVariables", UNSET))

        dp_policy = cls(
            max_column_count=max_column_count,
            max_factors=max_factors,
            noisy_global_size=noisy_global_size,
            use_differential_privacy=use_differential_privacy,
            execution_quota_parameters=execution_quota_parameters,
            min_dataset_size=min_dataset_size,
            min_frequencies=min_frequencies,
            min_global_dataset_size=min_global_dataset_size,
            authorized_variables=authorized_variables,
        )

        dp_policy.additional_properties = d
        return dp_policy

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
