from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.noise_parameters import NoiseParameters
    from ..models.privacy_budget_parameters import PrivacyBudgetParameters
    from ..models.threshold import Threshold


T = TypeVar("T", bound="DPPolicy")


@attr.s(auto_attribs=True)
class DPPolicy:
    """represents the disclosure prevention policy that enables toggling various disclosure prevention mechanisms

    Attributes:
        privacy_budget_parameters (Union[Unset, PrivacyBudgetParameters]): Differential privacy budget settings.
            The unit of the privacy budget is in terms of epsilon value (ϵ).
            More precisely, if a computation adds noise that is equivalent ϵ=0.1 then 0.1 of the privacy budget is used.
        min_frequencies (Union[Unset, Threshold]): represents a threshold, which can be made relative of the dataset
            size
        min_global_dataset_size (Union[Unset, int]): minimum size of the global / collective dataset. It is collectively
            computed using the encrypted aggregation
        noise_parameters (Union[Unset, NoiseParameters]): parameters for adding differential privacy noise to the
            computation's encrypted output
        noisy_global_size (Union[Unset, bool]): when computing the global size, whether noise is used or not. If so,
            each node adds discrete noise to its input to the encrypted aggregation
        authorized_variables (Union[Unset, List[str]]): constraint on the set of variables that can be used as input, in
            order to prevent misuse of variables that are out of context of the project.
            if > 0 variables are defined here, then the dataset will automatically drop any variables that do not belong to
            this set.
            Warning: this mechanism is only effective when the data selection parameters (data source queries) are fixed,
            and therefore
            returned variables cannot be aliased (for example using aliases in SQL SELECT statements) to evade this trap.
        max_column_count (Union[Unset, Threshold]): represents a threshold, which can be made relative of the dataset
            size
        max_factors (Union[Unset, Threshold]): represents a threshold, which can be made relative of the dataset size
        min_dataset_size (Union[Unset, int]): minimum size of the dataset used as local input (checked both before and
            after the preprocessing operations are run)
    """

    privacy_budget_parameters: Union[Unset, "PrivacyBudgetParameters"] = UNSET
    min_frequencies: Union[Unset, "Threshold"] = UNSET
    min_global_dataset_size: Union[Unset, int] = UNSET
    noise_parameters: Union[Unset, "NoiseParameters"] = UNSET
    noisy_global_size: Union[Unset, bool] = UNSET
    authorized_variables: Union[Unset, List[str]] = UNSET
    max_column_count: Union[Unset, "Threshold"] = UNSET
    max_factors: Union[Unset, "Threshold"] = UNSET
    min_dataset_size: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        privacy_budget_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.privacy_budget_parameters, Unset):
            privacy_budget_parameters = self.privacy_budget_parameters.to_dict()

        min_frequencies: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.min_frequencies, Unset):
            min_frequencies = self.min_frequencies.to_dict()

        min_global_dataset_size = self.min_global_dataset_size
        noise_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.noise_parameters, Unset):
            noise_parameters = self.noise_parameters.to_dict()

        noisy_global_size = self.noisy_global_size
        authorized_variables: Union[Unset, List[str]] = UNSET
        if not isinstance(self.authorized_variables, Unset):
            authorized_variables = self.authorized_variables

        max_column_count: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.max_column_count, Unset):
            max_column_count = self.max_column_count.to_dict()

        max_factors: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.max_factors, Unset):
            max_factors = self.max_factors.to_dict()

        min_dataset_size = self.min_dataset_size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if privacy_budget_parameters is not UNSET:
            field_dict["privacyBudgetParameters"] = privacy_budget_parameters
        if min_frequencies is not UNSET:
            field_dict["minFrequencies"] = min_frequencies
        if min_global_dataset_size is not UNSET:
            field_dict["minGlobalDatasetSize"] = min_global_dataset_size
        if noise_parameters is not UNSET:
            field_dict["noiseParameters"] = noise_parameters
        if noisy_global_size is not UNSET:
            field_dict["noisyGlobalSize"] = noisy_global_size
        if authorized_variables is not UNSET:
            field_dict["authorizedVariables"] = authorized_variables
        if max_column_count is not UNSET:
            field_dict["maxColumnCount"] = max_column_count
        if max_factors is not UNSET:
            field_dict["maxFactors"] = max_factors
        if min_dataset_size is not UNSET:
            field_dict["minDatasetSize"] = min_dataset_size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.noise_parameters import NoiseParameters
        from ..models.privacy_budget_parameters import PrivacyBudgetParameters
        from ..models.threshold import Threshold

        d = src_dict.copy()
        _privacy_budget_parameters = d.pop("privacyBudgetParameters", UNSET)
        privacy_budget_parameters: Union[Unset, PrivacyBudgetParameters]
        if isinstance(_privacy_budget_parameters, Unset):
            privacy_budget_parameters = UNSET
        else:
            privacy_budget_parameters = PrivacyBudgetParameters.from_dict(_privacy_budget_parameters)

        _min_frequencies = d.pop("minFrequencies", UNSET)
        min_frequencies: Union[Unset, Threshold]
        if isinstance(_min_frequencies, Unset):
            min_frequencies = UNSET
        else:
            min_frequencies = Threshold.from_dict(_min_frequencies)

        min_global_dataset_size = d.pop("minGlobalDatasetSize", UNSET)

        _noise_parameters = d.pop("noiseParameters", UNSET)
        noise_parameters: Union[Unset, NoiseParameters]
        if isinstance(_noise_parameters, Unset):
            noise_parameters = UNSET
        else:
            noise_parameters = NoiseParameters.from_dict(_noise_parameters)

        noisy_global_size = d.pop("noisyGlobalSize", UNSET)

        authorized_variables = cast(List[str], d.pop("authorizedVariables", UNSET))

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

        min_dataset_size = d.pop("minDatasetSize", UNSET)

        dp_policy = cls(
            privacy_budget_parameters=privacy_budget_parameters,
            min_frequencies=min_frequencies,
            min_global_dataset_size=min_global_dataset_size,
            noise_parameters=noise_parameters,
            noisy_global_size=noisy_global_size,
            authorized_variables=authorized_variables,
            max_column_count=max_column_count,
            max_factors=max_factors,
            min_dataset_size=min_dataset_size,
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
