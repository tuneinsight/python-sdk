from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.authorization_contract import AuthorizationContract
    from ..models.computation_definition import ComputationDefinition
    from ..models.datasource_policy import DatasourcePolicy


T = TypeVar("T", bound="ComputationPolicy")


@attr.s(auto_attribs=True)
class ComputationPolicy:
    """policy to validate a specific computation

    Attributes:
        authorization_contract (Union[Unset, AuthorizationContract]): describes what parts of the computation are
            allowed to change when a project is authorized
        data_policy (Union[Unset, DatasourcePolicy]): policy required by a datasource for the data to be used in a
            project.
        disabled (Union[Unset, None, bool]): when set to true, the policy is not enforced anymore.
            This field is useful when a project is being setup and workflows should be tested with or without policies.
        fixed_parameters (Union[Unset, List[str]]): when validateParameters is enabled, specifies the set of parameters
            that cannot be changed if empty, then all parameters are validated
        flexible_parameters (Union[Unset, List[str]]): when validateParameters is enabled, specifies the set of
            parameters for which to ignore validation
        template (Union[Unset, ComputationDefinition]): Generic computation.
        validate_parameters (Union[Unset, bool]): whether or not to validate the parameters with the ones from the
            template
    """

    authorization_contract: Union[Unset, "AuthorizationContract"] = UNSET
    data_policy: Union[Unset, "DatasourcePolicy"] = UNSET
    disabled: Union[Unset, None, bool] = UNSET
    fixed_parameters: Union[Unset, List[str]] = UNSET
    flexible_parameters: Union[Unset, List[str]] = UNSET
    template: Union[Unset, "ComputationDefinition"] = UNSET
    validate_parameters: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        authorization_contract: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.authorization_contract, Unset):
            authorization_contract = self.authorization_contract.to_dict()

        data_policy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data_policy, Unset):
            data_policy = self.data_policy.to_dict()

        disabled = self.disabled
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
        if authorization_contract is not UNSET:
            field_dict["authorizationContract"] = authorization_contract
        if data_policy is not UNSET:
            field_dict["dataPolicy"] = data_policy
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
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
        from ..models.authorization_contract import AuthorizationContract
        from ..models.computation_definition import ComputationDefinition
        from ..models.datasource_policy import DatasourcePolicy

        d = src_dict.copy()
        _authorization_contract = d.pop("authorizationContract", UNSET)
        authorization_contract: Union[Unset, AuthorizationContract]
        if isinstance(_authorization_contract, Unset):
            authorization_contract = UNSET
        else:
            authorization_contract = AuthorizationContract.from_dict(_authorization_contract)

        _data_policy = d.pop("dataPolicy", UNSET)
        data_policy: Union[Unset, DatasourcePolicy]
        if isinstance(_data_policy, Unset):
            data_policy = UNSET
        else:
            data_policy = DatasourcePolicy.from_dict(_data_policy)

        disabled = d.pop("disabled", UNSET)

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
            authorization_contract=authorization_contract,
            data_policy=data_policy,
            disabled=disabled,
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
