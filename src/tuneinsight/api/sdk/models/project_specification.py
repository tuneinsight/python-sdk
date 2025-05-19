from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.computation_type import ComputationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.computation_definition import ComputationDefinition
    from ..models.computation_policy import ComputationPolicy
    from ..models.computation_preprocessing_parameters import ComputationPreprocessingParameters
    from ..models.filter_ import Filter


T = TypeVar("T", bound="ProjectSpecification")


@attr.s(auto_attribs=True)
class ProjectSpecification:
    """Specifies parts of a project (called "checked project").

    Attributes:
        computation_definition (Union[Unset, ComputationDefinition]): Generic computation.
        computation_type (Union[Unset, ComputationType]): Type of the computation.
        match_only_computation_type (Union[Unset, bool]): If true, only the computation type (and not the parameters) is
            checked when testing this specification.
            This is deprecated and will be removed in v1.1.
        min_contributors (Union[Unset, None, float]): If defined, the minimum number of contributors of the checked
            project must be at least this value, or left
            undefined (in which case all participants are required to contribute).
        name (Union[Unset, str]): optional name describing what this specification intends to check.
        parameter_filters (Union[Unset, List['Filter']]): If defined, the computation parameters of the checked project
            must satisfy all these filters.
            To impose filters on more complex values, start the Value field of the filter with "json:" and use a JSON
            description of the entry.
        policy (Union[Unset, ComputationPolicy]): policy to validate a specific computation
        preprocessing (Union[Unset, ComputationPreprocessingParameters]): dataframe pre-processing parameters applied to
            the input retrieved from the datasource, if applicable
    """

    computation_definition: Union[Unset, "ComputationDefinition"] = UNSET
    computation_type: Union[Unset, ComputationType] = UNSET
    match_only_computation_type: Union[Unset, bool] = UNSET
    min_contributors: Union[Unset, None, float] = UNSET
    name: Union[Unset, str] = UNSET
    parameter_filters: Union[Unset, List["Filter"]] = UNSET
    policy: Union[Unset, "ComputationPolicy"] = UNSET
    preprocessing: Union[Unset, "ComputationPreprocessingParameters"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        computation_definition: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.computation_definition, Unset):
            computation_definition = self.computation_definition.to_dict()

        computation_type: Union[Unset, str] = UNSET
        if not isinstance(self.computation_type, Unset):
            computation_type = self.computation_type.value

        match_only_computation_type = self.match_only_computation_type
        min_contributors = self.min_contributors
        name = self.name
        parameter_filters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.parameter_filters, Unset):
            parameter_filters = []
            for parameter_filters_item_data in self.parameter_filters:
                parameter_filters_item = parameter_filters_item_data.to_dict()

                parameter_filters.append(parameter_filters_item)

        policy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.policy, Unset):
            policy = self.policy.to_dict()

        preprocessing: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.preprocessing, Unset):
            preprocessing = self.preprocessing.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if computation_definition is not UNSET:
            field_dict["computationDefinition"] = computation_definition
        if computation_type is not UNSET:
            field_dict["computationType"] = computation_type
        if match_only_computation_type is not UNSET:
            field_dict["matchOnlyComputationType"] = match_only_computation_type
        if min_contributors is not UNSET:
            field_dict["minContributors"] = min_contributors
        if name is not UNSET:
            field_dict["name"] = name
        if parameter_filters is not UNSET:
            field_dict["parameterFilters"] = parameter_filters
        if policy is not UNSET:
            field_dict["policy"] = policy
        if preprocessing is not UNSET:
            field_dict["preprocessing"] = preprocessing

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.computation_definition import ComputationDefinition
        from ..models.computation_policy import ComputationPolicy
        from ..models.computation_preprocessing_parameters import ComputationPreprocessingParameters
        from ..models.filter_ import Filter

        d = src_dict.copy()
        _computation_definition = d.pop("computationDefinition", UNSET)
        computation_definition: Union[Unset, ComputationDefinition]
        if isinstance(_computation_definition, Unset):
            computation_definition = UNSET
        else:
            computation_definition = ComputationDefinition.from_dict(_computation_definition)

        _computation_type = d.pop("computationType", UNSET)
        computation_type: Union[Unset, ComputationType]
        if isinstance(_computation_type, Unset):
            computation_type = UNSET
        else:
            computation_type = ComputationType(_computation_type)

        match_only_computation_type = d.pop("matchOnlyComputationType", UNSET)

        min_contributors = d.pop("minContributors", UNSET)

        name = d.pop("name", UNSET)

        parameter_filters = []
        _parameter_filters = d.pop("parameterFilters", UNSET)
        for parameter_filters_item_data in _parameter_filters or []:
            parameter_filters_item = Filter.from_dict(parameter_filters_item_data)

            parameter_filters.append(parameter_filters_item)

        _policy = d.pop("policy", UNSET)
        policy: Union[Unset, ComputationPolicy]
        if isinstance(_policy, Unset):
            policy = UNSET
        else:
            policy = ComputationPolicy.from_dict(_policy)

        _preprocessing = d.pop("preprocessing", UNSET)
        preprocessing: Union[Unset, ComputationPreprocessingParameters]
        if isinstance(_preprocessing, Unset):
            preprocessing = UNSET
        else:
            preprocessing = ComputationPreprocessingParameters.from_dict(_preprocessing)

        project_specification = cls(
            computation_definition=computation_definition,
            computation_type=computation_type,
            match_only_computation_type=match_only_computation_type,
            min_contributors=min_contributors,
            name=name,
            parameter_filters=parameter_filters,
            policy=policy,
            preprocessing=preprocessing,
        )

        project_specification.additional_properties = d
        return project_specification

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
