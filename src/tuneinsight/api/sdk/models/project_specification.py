from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.computation_definition import ComputationDefinition
    from ..models.computation_policy import ComputationPolicy
    from ..models.computation_preprocessing_parameters import ComputationPreprocessingParameters


T = TypeVar("T", bound="ProjectSpecification")


@attr.s(auto_attribs=True)
class ProjectSpecification:
    """Specifies parts of a project (called "checked project").

    Attributes:
        computation_definition (Union[Unset, ComputationDefinition]): Generic computation.
        match_only_computation_type (Union[Unset, bool]): If true, only the computation type (and not the parameters) is
            checked when testing this specification.
        policy (Union[Unset, ComputationPolicy]): policy to validate a specific computation
        preprocessing (Union[Unset, ComputationPreprocessingParameters]): dataframe pre-processing parameters applied to
            the input retrieved from the datasource, if applicable
    """

    computation_definition: Union[Unset, "ComputationDefinition"] = UNSET
    match_only_computation_type: Union[Unset, bool] = UNSET
    policy: Union[Unset, "ComputationPolicy"] = UNSET
    preprocessing: Union[Unset, "ComputationPreprocessingParameters"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        computation_definition: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.computation_definition, Unset):
            computation_definition = self.computation_definition.to_dict()

        match_only_computation_type = self.match_only_computation_type
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
        if match_only_computation_type is not UNSET:
            field_dict["matchOnlyComputationType"] = match_only_computation_type
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

        d = src_dict.copy()
        _computation_definition = d.pop("computationDefinition", UNSET)
        computation_definition: Union[Unset, ComputationDefinition]
        if isinstance(_computation_definition, Unset):
            computation_definition = UNSET
        else:
            computation_definition = ComputationDefinition.from_dict(_computation_definition)

        match_only_computation_type = d.pop("matchOnlyComputationType", UNSET)

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
            match_only_computation_type=match_only_computation_type,
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
