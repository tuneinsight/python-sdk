from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.computation_type import ComputationType
from ..models.preprocessing_operation_type import PreprocessingOperationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.authorization_contract import AuthorizationContract
    from ..models.computation_definition import ComputationDefinition
    from ..models.dp_policy import DPPolicy
    from ..models.whitelisted_query import WhitelistedQuery


T = TypeVar("T", bound="ComputationPolicy")


@attr.s(auto_attribs=True)
class ComputationPolicy:
    """policy to validate a specific computation

    Attributes:
        dp_policy (Union[Unset, DPPolicy]): represents the disclosure prevention policy that enables toggling various
            disclosure prevention mechanisms
        authorization_contract (Union[Unset, AuthorizationContract]): describes what parts of the computation are
            allowed to change when a project is authorized
        authorized_computation_types (Union[Unset, List[ComputationType]]): list of authorized computation types
        authorized_data_source_queries (Union[Unset, List['WhitelistedQuery']]): list of authorized datasource queries
            when restrictDataSourceQueries is set to true
        authorized_preprocessing_operations (Union[Unset, List[PreprocessingOperationType]]): list of authorized
            preprocessing operations types when restrictPreprocessingOperations is set to true
        disabled (Union[Unset, None, bool]): when set to true, the policy is not enforced anymore.
            This field is useful when a project is being setup and workflows should be tested with or without policies.
        fixed_parameters (Union[Unset, List[str]]): when validateParameters is enabled, specifies the set of parameters
            that cannot be changed if empty, then all parameters are validated
        flexible_parameters (Union[Unset, List[str]]): when validateParameters is enabled, specifies the set of
            parameters for which to ignore validation
        restrict_data_source_queries (Union[Unset, bool]): whether or not datasource queries should be restricted
        restrict_preprocessing_operations (Union[Unset, bool]): whether or not datasource queries should be restricted
        template (Union[Unset, ComputationDefinition]): Generic computation.
        validate_parameters (Union[Unset, bool]): whether or not to validate the parameters with the ones from the
            template
    """

    dp_policy: Union[Unset, "DPPolicy"] = UNSET
    authorization_contract: Union[Unset, "AuthorizationContract"] = UNSET
    authorized_computation_types: Union[Unset, List[ComputationType]] = UNSET
    authorized_data_source_queries: Union[Unset, List["WhitelistedQuery"]] = UNSET
    authorized_preprocessing_operations: Union[Unset, List[PreprocessingOperationType]] = UNSET
    disabled: Union[Unset, None, bool] = UNSET
    fixed_parameters: Union[Unset, List[str]] = UNSET
    flexible_parameters: Union[Unset, List[str]] = UNSET
    restrict_data_source_queries: Union[Unset, bool] = UNSET
    restrict_preprocessing_operations: Union[Unset, bool] = UNSET
    template: Union[Unset, "ComputationDefinition"] = UNSET
    validate_parameters: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dp_policy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dp_policy, Unset):
            dp_policy = self.dp_policy.to_dict()

        authorization_contract: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.authorization_contract, Unset):
            authorization_contract = self.authorization_contract.to_dict()

        authorized_computation_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.authorized_computation_types, Unset):
            authorized_computation_types = []
            for authorized_computation_types_item_data in self.authorized_computation_types:
                authorized_computation_types_item = authorized_computation_types_item_data.value

                authorized_computation_types.append(authorized_computation_types_item)

        authorized_data_source_queries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.authorized_data_source_queries, Unset):
            authorized_data_source_queries = []
            for authorized_data_source_queries_item_data in self.authorized_data_source_queries:
                authorized_data_source_queries_item = authorized_data_source_queries_item_data.to_dict()

                authorized_data_source_queries.append(authorized_data_source_queries_item)

        authorized_preprocessing_operations: Union[Unset, List[str]] = UNSET
        if not isinstance(self.authorized_preprocessing_operations, Unset):
            authorized_preprocessing_operations = []
            for authorized_preprocessing_operations_item_data in self.authorized_preprocessing_operations:
                authorized_preprocessing_operations_item = authorized_preprocessing_operations_item_data.value

                authorized_preprocessing_operations.append(authorized_preprocessing_operations_item)

        disabled = self.disabled
        fixed_parameters: Union[Unset, List[str]] = UNSET
        if not isinstance(self.fixed_parameters, Unset):
            fixed_parameters = self.fixed_parameters

        flexible_parameters: Union[Unset, List[str]] = UNSET
        if not isinstance(self.flexible_parameters, Unset):
            flexible_parameters = self.flexible_parameters

        restrict_data_source_queries = self.restrict_data_source_queries
        restrict_preprocessing_operations = self.restrict_preprocessing_operations
        template: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.to_dict()

        validate_parameters = self.validate_parameters

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dp_policy is not UNSET:
            field_dict["DPPolicy"] = dp_policy
        if authorization_contract is not UNSET:
            field_dict["authorizationContract"] = authorization_contract
        if authorized_computation_types is not UNSET:
            field_dict["authorizedComputationTypes"] = authorized_computation_types
        if authorized_data_source_queries is not UNSET:
            field_dict["authorizedDataSourceQueries"] = authorized_data_source_queries
        if authorized_preprocessing_operations is not UNSET:
            field_dict["authorizedPreprocessingOperations"] = authorized_preprocessing_operations
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if fixed_parameters is not UNSET:
            field_dict["fixedParameters"] = fixed_parameters
        if flexible_parameters is not UNSET:
            field_dict["flexibleParameters"] = flexible_parameters
        if restrict_data_source_queries is not UNSET:
            field_dict["restrictDataSourceQueries"] = restrict_data_source_queries
        if restrict_preprocessing_operations is not UNSET:
            field_dict["restrictPreprocessingOperations"] = restrict_preprocessing_operations
        if template is not UNSET:
            field_dict["template"] = template
        if validate_parameters is not UNSET:
            field_dict["validateParameters"] = validate_parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.authorization_contract import AuthorizationContract
        from ..models.computation_definition import ComputationDefinition
        from ..models.dp_policy import DPPolicy
        from ..models.whitelisted_query import WhitelistedQuery

        d = src_dict.copy()
        _dp_policy = d.pop("DPPolicy", UNSET)
        dp_policy: Union[Unset, DPPolicy]
        if isinstance(_dp_policy, Unset):
            dp_policy = UNSET
        else:
            dp_policy = DPPolicy.from_dict(_dp_policy)

        _authorization_contract = d.pop("authorizationContract", UNSET)
        authorization_contract: Union[Unset, AuthorizationContract]
        if isinstance(_authorization_contract, Unset):
            authorization_contract = UNSET
        else:
            authorization_contract = AuthorizationContract.from_dict(_authorization_contract)

        authorized_computation_types = []
        _authorized_computation_types = d.pop("authorizedComputationTypes", UNSET)
        for authorized_computation_types_item_data in _authorized_computation_types or []:
            authorized_computation_types_item = ComputationType(authorized_computation_types_item_data)

            authorized_computation_types.append(authorized_computation_types_item)

        authorized_data_source_queries = []
        _authorized_data_source_queries = d.pop("authorizedDataSourceQueries", UNSET)
        for authorized_data_source_queries_item_data in _authorized_data_source_queries or []:
            authorized_data_source_queries_item = WhitelistedQuery.from_dict(authorized_data_source_queries_item_data)

            authorized_data_source_queries.append(authorized_data_source_queries_item)

        authorized_preprocessing_operations = []
        _authorized_preprocessing_operations = d.pop("authorizedPreprocessingOperations", UNSET)
        for authorized_preprocessing_operations_item_data in _authorized_preprocessing_operations or []:
            authorized_preprocessing_operations_item = PreprocessingOperationType(
                authorized_preprocessing_operations_item_data
            )

            authorized_preprocessing_operations.append(authorized_preprocessing_operations_item)

        disabled = d.pop("disabled", UNSET)

        fixed_parameters = cast(List[str], d.pop("fixedParameters", UNSET))

        flexible_parameters = cast(List[str], d.pop("flexibleParameters", UNSET))

        restrict_data_source_queries = d.pop("restrictDataSourceQueries", UNSET)

        restrict_preprocessing_operations = d.pop("restrictPreprocessingOperations", UNSET)

        _template = d.pop("template", UNSET)
        template: Union[Unset, ComputationDefinition]
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = ComputationDefinition.from_dict(_template)

        validate_parameters = d.pop("validateParameters", UNSET)

        computation_policy = cls(
            dp_policy=dp_policy,
            authorization_contract=authorization_contract,
            authorized_computation_types=authorized_computation_types,
            authorized_data_source_queries=authorized_data_source_queries,
            authorized_preprocessing_operations=authorized_preprocessing_operations,
            disabled=disabled,
            fixed_parameters=fixed_parameters,
            flexible_parameters=flexible_parameters,
            restrict_data_source_queries=restrict_data_source_queries,
            restrict_preprocessing_operations=restrict_preprocessing_operations,
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
