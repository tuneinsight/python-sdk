from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.computation_type import ComputationType
from ..models.preprocessing_operation_type import PreprocessingOperationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dp_policy import DPPolicy
    from ..models.whitelisted_query import WhitelistedQuery


T = TypeVar("T", bound="DatasourcePolicy")


@attr.s(auto_attribs=True)
class DatasourcePolicy:
    """policy required by a datasource for the data to be used in a project.

    Attributes:
        dp_policy (Union[Unset, DPPolicy]): represents the disclosure prevention policy that enables toggling various
            mechanisms that are executed whenever the workflow runs.
        authorized_computation_types (Union[Unset, List[ComputationType]]): list of authorized computation types
        authorized_data_source_queries (Union[Unset, List['WhitelistedQuery']]): list of authorized datasource queries
            when restrictDataSourceQueries is set to true
        authorized_preprocessing_operations (Union[Unset, List[PreprocessingOperationType]]): list of authorized
            preprocessing operations types when restrictPreprocessingOperations is set to true
        restrict_data_source_queries (Union[Unset, bool]): whether or not datasource queries should be restricted
        restrict_preprocessing_operations (Union[Unset, bool]): whether or not datasource queries should be restricted
    """

    dp_policy: Union[Unset, "DPPolicy"] = UNSET
    authorized_computation_types: Union[Unset, List[ComputationType]] = UNSET
    authorized_data_source_queries: Union[Unset, List["WhitelistedQuery"]] = UNSET
    authorized_preprocessing_operations: Union[Unset, List[PreprocessingOperationType]] = UNSET
    restrict_data_source_queries: Union[Unset, bool] = UNSET
    restrict_preprocessing_operations: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dp_policy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dp_policy, Unset):
            dp_policy = self.dp_policy.to_dict()

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

        restrict_data_source_queries = self.restrict_data_source_queries
        restrict_preprocessing_operations = self.restrict_preprocessing_operations

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dp_policy is not UNSET:
            field_dict["DPPolicy"] = dp_policy
        if authorized_computation_types is not UNSET:
            field_dict["authorizedComputationTypes"] = authorized_computation_types
        if authorized_data_source_queries is not UNSET:
            field_dict["authorizedDataSourceQueries"] = authorized_data_source_queries
        if authorized_preprocessing_operations is not UNSET:
            field_dict["authorizedPreprocessingOperations"] = authorized_preprocessing_operations
        if restrict_data_source_queries is not UNSET:
            field_dict["restrictDataSourceQueries"] = restrict_data_source_queries
        if restrict_preprocessing_operations is not UNSET:
            field_dict["restrictPreprocessingOperations"] = restrict_preprocessing_operations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dp_policy import DPPolicy
        from ..models.whitelisted_query import WhitelistedQuery

        d = src_dict.copy()
        _dp_policy = d.pop("DPPolicy", UNSET)
        dp_policy: Union[Unset, DPPolicy]
        if isinstance(_dp_policy, Unset):
            dp_policy = UNSET
        else:
            dp_policy = DPPolicy.from_dict(_dp_policy)

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

        restrict_data_source_queries = d.pop("restrictDataSourceQueries", UNSET)

        restrict_preprocessing_operations = d.pop("restrictPreprocessingOperations", UNSET)

        datasource_policy = cls(
            dp_policy=dp_policy,
            authorized_computation_types=authorized_computation_types,
            authorized_data_source_queries=authorized_data_source_queries,
            authorized_preprocessing_operations=authorized_preprocessing_operations,
            restrict_data_source_queries=restrict_data_source_queries,
            restrict_preprocessing_operations=restrict_preprocessing_operations,
        )

        datasource_policy.additional_properties = d
        return datasource_policy

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
