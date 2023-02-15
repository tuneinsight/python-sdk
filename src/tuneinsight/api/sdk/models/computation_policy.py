from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.computation_definition import ComputationDefinition
    from ..models.differential_privacy_parameters import DifferentialPrivacyParameters


T = TypeVar("T", bound="ComputationPolicy")


@attr.s(auto_attribs=True)
class ComputationPolicy:
    """policy to validate a specific computation

    Attributes:
        differential_privacy_parameters (Union[Unset, DifferentialPrivacyParameters]): parameters for adding
            differential privacy noise to the computation's encrypted output
        fixed_parameters (Union[Unset, List[str]]): when validateParameters is enabled, specifies the set of parameters
            that cannot be changed if empty, then all parameters are validated
        flexible_parameters (Union[Unset, List[str]]): when validateParameters is enabled, specifies the set of
            parameters for which to ignore validation
        template (Union[Unset, ComputationDefinition]): Generic computation.
        validate_parameters (Union[Unset, bool]): whether or not to validate the parameters with the ones from the
            template
    """

    differential_privacy_parameters: Union[Unset, "DifferentialPrivacyParameters"] = UNSET
    fixed_parameters: Union[Unset, List[str]] = UNSET
    flexible_parameters: Union[Unset, List[str]] = UNSET
    template: Union[Unset, "ComputationDefinition"] = UNSET
    validate_parameters: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        differential_privacy_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.differential_privacy_parameters, Unset):
            differential_privacy_parameters = self.differential_privacy_parameters.to_dict()

        fixed_parameters: Union[Unset, List[str]] = UNSET
        if not isinstance(self.fixed_parameters, Unset):
            fixed_parameters = self.fixed_parameters

        flexible_parameters: Union[Unset, List[str]] = UNSET
        if not isinstance(self.flexible_parameters, Unset):
            flexible_parameters = self.flexible_parameters

        template: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.to_dict()

        validate_parameters = self.validate_parameters

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if differential_privacy_parameters is not UNSET:
            field_dict["differentialPrivacyParameters"] = differential_privacy_parameters
        if fixed_parameters is not UNSET:
            field_dict["fixedParameters"] = fixed_parameters
        if flexible_parameters is not UNSET:
            field_dict["flexibleParameters"] = flexible_parameters
        if template is not UNSET:
            field_dict["template"] = template
        if validate_parameters is not UNSET:
            field_dict["validateParameters"] = validate_parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.computation_definition import ComputationDefinition
        from ..models.differential_privacy_parameters import DifferentialPrivacyParameters

        d = src_dict.copy()
        _differential_privacy_parameters = d.pop("differentialPrivacyParameters", UNSET)
        differential_privacy_parameters: Union[Unset, DifferentialPrivacyParameters]
        if isinstance(_differential_privacy_parameters, Unset):
            differential_privacy_parameters = UNSET
        else:
            differential_privacy_parameters = DifferentialPrivacyParameters.from_dict(_differential_privacy_parameters)

        fixed_parameters = cast(List[str], d.pop("fixedParameters", UNSET))

        flexible_parameters = cast(List[str], d.pop("flexibleParameters", UNSET))

        _template = d.pop("template", UNSET)
        template: Union[Unset, ComputationDefinition]
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = ComputationDefinition.from_dict(_template)

        validate_parameters = d.pop("validateParameters", UNSET)

        computation_policy = cls(
            differential_privacy_parameters=differential_privacy_parameters,
            fixed_parameters=fixed_parameters,
            flexible_parameters=flexible_parameters,
            template=template,
            validate_parameters=validate_parameters,
        )

        computation_policy.additional_properties = d
        return computation_policy

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
