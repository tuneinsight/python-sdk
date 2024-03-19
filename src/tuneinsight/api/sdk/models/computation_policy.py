from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.computation_type import ComputationType
from ..models.preprocessing_operation_type import PreprocessingOperationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.computation_definition import ComputationDefinition
    from ..models.dp_policy import DPPolicy


T = TypeVar("T", bound="ComputationPolicy")


@attr.s(auto_attribs=True)
class ComputationPolicy:
    """policy to validate a specific computation

    Attributes:
        authorized_computation_types (Union[Unset, List[ComputationType]]): list of authorized computation types
        authorized_data_source_queries (Union[Unset, List[str]]): list of authorized datasource queries when
            restrictDataSourceQueries is set to true
        authorized_preprocessing_operations (Union[Unset, List[PreprocessingOperationType]]): list of authorized
            preprocessing operations types when restrictPreprocessingOperations is set to true
        flexible_parameters (Union[Unset, List[str]]): when validateParameters is enabled, specifies the set of
            parameters for which to ignore validation
        restrict_data_source_queries (Union[Unset, bool]): whether or not datasource queries should be restricted
        restrict_preprocessing_operations (Union[Unset, bool]): whether or not datasource queries should be restricted
        validate_parameters (Union[Unset, bool]): whether or not to validate the parameters with the ones from the
            template
        dp_policy (Union[Unset, DPPolicy]): represents the disclosure prevention policy that enables toggling various
            disclosure prevention mechanisms
        fixed_parameters (Union[Unset, List[str]]): when validateParameters is enabled, specifies the set of parameters
            that cannot be changed if empty, then all parameters are validated
        template (Union[Unset, ComputationDefinition]): Generic computation.
    """

    authorized_computation_types: Union[Unset, List[ComputationType]] = UNSET
    authorized_data_source_queries: Union[Unset, List[str]] = UNSET
    authorized_preprocessing_operations: Union[Unset, List[PreprocessingOperationType]] = UNSET
    flexible_parameters: Union[Unset, List[str]] = UNSET
    restrict_data_source_queries: Union[Unset, bool] = UNSET
    restrict_preprocessing_operations: Union[Unset, bool] = UNSET
    validate_parameters: Union[Unset, bool] = UNSET
    dp_policy: Union[Unset, "DPPolicy"] = UNSET
    fixed_parameters: Union[Unset, List[str]] = UNSET
    template: Union[Unset, "ComputationDefinition"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        authorized_computation_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.authorized_computation_types, Unset):
            authorized_computation_types = []
            for authorized_computation_types_item_data in self.authorized_computation_types:
                authorized_computation_types_item = authorized_computation_types_item_data.value

                authorized_computation_types.append(authorized_computation_types_item)

        authorized_data_source_queries: Union[Unset, List[str]] = UNSET
        if not isinstance(self.authorized_data_source_queries, Unset):
            authorized_data_source_queries = self.authorized_data_source_queries

        authorized_preprocessing_operations: Union[Unset, List[str]] = UNSET
        if not isinstance(self.authorized_preprocessing_operations, Unset):
            authorized_preprocessing_operations = []
            for authorized_preprocessing_operations_item_data in self.authorized_preprocessing_operations:
                authorized_preprocessing_operations_item = authorized_preprocessing_operations_item_data.value

                authorized_preprocessing_operations.append(authorized_preprocessing_operations_item)

        flexible_parameters: Union[Unset, List[str]] = UNSET
        if not isinstance(self.flexible_parameters, Unset):
            flexible_parameters = self.flexible_parameters

        restrict_data_source_queries = self.restrict_data_source_queries
        restrict_preprocessing_operations = self.restrict_preprocessing_operations
        validate_parameters = self.validate_parameters
        dp_policy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dp_policy, Unset):
            dp_policy = self.dp_policy.to_dict()

        fixed_parameters: Union[Unset, List[str]] = UNSET
        if not isinstance(self.fixed_parameters, Unset):
            fixed_parameters = self.fixed_parameters

        template: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authorized_computation_types is not UNSET:
            field_dict["authorizedComputationTypes"] = authorized_computation_types
        if authorized_data_source_queries is not UNSET:
            field_dict["authorizedDataSourceQueries"] = authorized_data_source_queries
        if authorized_preprocessing_operations is not UNSET:
            field_dict["authorizedPreprocessingOperations"] = authorized_preprocessing_operations
        if flexible_parameters is not UNSET:
            field_dict["flexibleParameters"] = flexible_parameters
        if restrict_data_source_queries is not UNSET:
            field_dict["restrictDataSourceQueries"] = restrict_data_source_queries
        if restrict_preprocessing_operations is not UNSET:
            field_dict["restrictPreprocessingOperations"] = restrict_preprocessing_operations
        if validate_parameters is not UNSET:
            field_dict["validateParameters"] = validate_parameters
        if dp_policy is not UNSET:
            field_dict["DPPolicy"] = dp_policy
        if fixed_parameters is not UNSET:
            field_dict["fixedParameters"] = fixed_parameters
        if template is not UNSET:
            field_dict["template"] = template

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.computation_definition import ComputationDefinition
        from ..models.dp_policy import DPPolicy

        d = src_dict.copy()
        authorized_computation_types = []
        _authorized_computation_types = d.pop("authorizedComputationTypes", UNSET)
        for authorized_computation_types_item_data in _authorized_computation_types or []:
            authorized_computation_types_item = ComputationType(authorized_computation_types_item_data)

            authorized_computation_types.append(authorized_computation_types_item)

        authorized_data_source_queries = cast(List[str], d.pop("authorizedDataSourceQueries", UNSET))

        authorized_preprocessing_operations = []
        _authorized_preprocessing_operations = d.pop("authorizedPreprocessingOperations", UNSET)
        for authorized_preprocessing_operations_item_data in _authorized_preprocessing_operations or []:
            authorized_preprocessing_operations_item = PreprocessingOperationType(
                authorized_preprocessing_operations_item_data
            )

            authorized_preprocessing_operations.append(authorized_preprocessing_operations_item)

        flexible_parameters = cast(List[str], d.pop("flexibleParameters", UNSET))

        restrict_data_source_queries = d.pop("restrictDataSourceQueries", UNSET)

        restrict_preprocessing_operations = d.pop("restrictPreprocessingOperations", UNSET)

        validate_parameters = d.pop("validateParameters", UNSET)

        _dp_policy = d.pop("DPPolicy", UNSET)
        dp_policy: Union[Unset, DPPolicy]
        if isinstance(_dp_policy, Unset):
            dp_policy = UNSET
        else:
            dp_policy = DPPolicy.from_dict(_dp_policy)

        fixed_parameters = cast(List[str], d.pop("fixedParameters", UNSET))

        _template = d.pop("template", UNSET)
        template: Union[Unset, ComputationDefinition]
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = ComputationDefinition.from_dict(_template)

        computation_policy = cls(
            authorized_computation_types=authorized_computation_types,
            authorized_data_source_queries=authorized_data_source_queries,
            authorized_preprocessing_operations=authorized_preprocessing_operations,
            flexible_parameters=flexible_parameters,
            restrict_data_source_queries=restrict_data_source_queries,
            restrict_preprocessing_operations=restrict_preprocessing_operations,
            validate_parameters=validate_parameters,
            dp_policy=dp_policy,
            fixed_parameters=fixed_parameters,
            template=template,
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
