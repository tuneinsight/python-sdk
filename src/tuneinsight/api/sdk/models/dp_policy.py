from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.authorized_column import AuthorizedColumn
    from ..models.execution_quota_parameters import ExecutionQuotaParameters
    from ..models.threshold import Threshold


T = TypeVar("T", bound="DPPolicy")


@attr.s(auto_attribs=True)
class DPPolicy:
    """represents the disclosure prevention policy that enables toggling various mechanisms that are executed whenever the
    workflow runs.

        Attributes:
            authorized_columns (Union[Unset, List['AuthorizedColumn']]): constraint on the set of variables that can be used
                as input, in order to prevent misuse of variables that are out of context of the project.
                if > 0 variables are defined here, then the dataset will automatically drop any variables that do not belong to
                this set.
                Warning: this mechanism is only effective when the data selection parameters (data source queries) are fixed,
                and therefore
                returned variables cannot be aliased (for example using aliases in SQL SELECT statements) to evade this trap.
            combine_local_results (Union[Unset, bool]): when enabled, local computation results are combined into a single
                collective results that includes a breakdown of all local results.
            execution_quota_parameters (Union[Unset, ExecutionQuotaParameters]): Execution quota settings.
                The unit of the execution quota depends on the computation and other policies.
                If differential privacy is applied, it is in terms of the the epsilon value (ϵ) of the privacy budget.
                If the computation is a private set intersection, each query consumes budget equal to the size of the querying
                set.
                Otherwise, a unit represents one computation.
            link_records (Union[Unset, bool]): whether to link the input tables from the participants using common
                identifiers.
            linkage_identifier (Union[Unset, str]): name of the column used as unique identifier for the record linkage
                (must be specified when align tables is set to true).
            max_column_count (Union[Unset, Threshold]): represents a threshold, which can be made relative of the dataset
                size
            min_dataset_size (Union[Unset, int]): minimum size of the dataset used as local input (checked both before and
                after the preprocessing operations are run)
            min_global_dataset_size (Union[Unset, int]): minimum size of the global / collective dataset. It is collectively
                computed using the encrypted aggregation
            noisy_global_size (Union[Unset, bool]): when computing the global size, whether noise is used or not. If so,
                each node adds discrete noise to its input to the encrypted aggregation
            restrict_columns (Union[Unset, None, bool]): this flag controls whether columns restrictions is in place or not.
            use_differential_privacy (Union[Unset, bool]): whether to use Differential Privacy to protect the privacy of the
                results.
    """

    authorized_columns: Union[Unset, List["AuthorizedColumn"]] = UNSET
    combine_local_results: Union[Unset, bool] = UNSET
    execution_quota_parameters: Union[Unset, "ExecutionQuotaParameters"] = UNSET
    link_records: Union[Unset, bool] = UNSET
    linkage_identifier: Union[Unset, str] = UNSET
    max_column_count: Union[Unset, "Threshold"] = UNSET
    min_dataset_size: Union[Unset, int] = UNSET
    min_global_dataset_size: Union[Unset, int] = UNSET
    noisy_global_size: Union[Unset, bool] = UNSET
    restrict_columns: Union[Unset, None, bool] = UNSET
    use_differential_privacy: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        authorized_columns: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.authorized_columns, Unset):
            authorized_columns = []
            for authorized_columns_item_data in self.authorized_columns:
                authorized_columns_item = authorized_columns_item_data.to_dict()

                authorized_columns.append(authorized_columns_item)

        combine_local_results = self.combine_local_results
        execution_quota_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.execution_quota_parameters, Unset):
            execution_quota_parameters = self.execution_quota_parameters.to_dict()

        link_records = self.link_records
        linkage_identifier = self.linkage_identifier
        max_column_count: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.max_column_count, Unset):
            max_column_count = self.max_column_count.to_dict()

        min_dataset_size = self.min_dataset_size
        min_global_dataset_size = self.min_global_dataset_size
        noisy_global_size = self.noisy_global_size
        restrict_columns = self.restrict_columns
        use_differential_privacy = self.use_differential_privacy

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authorized_columns is not UNSET:
            field_dict["authorizedColumns"] = authorized_columns
        if combine_local_results is not UNSET:
            field_dict["combineLocalResults"] = combine_local_results
        if execution_quota_parameters is not UNSET:
            field_dict["executionQuotaParameters"] = execution_quota_parameters
        if link_records is not UNSET:
            field_dict["linkRecords"] = link_records
        if linkage_identifier is not UNSET:
            field_dict["linkageIdentifier"] = linkage_identifier
        if max_column_count is not UNSET:
            field_dict["maxColumnCount"] = max_column_count
        if min_dataset_size is not UNSET:
            field_dict["minDatasetSize"] = min_dataset_size
        if min_global_dataset_size is not UNSET:
            field_dict["minGlobalDatasetSize"] = min_global_dataset_size
        if noisy_global_size is not UNSET:
            field_dict["noisyGlobalSize"] = noisy_global_size
        if restrict_columns is not UNSET:
            field_dict["restrictColumns"] = restrict_columns
        if use_differential_privacy is not UNSET:
            field_dict["useDifferentialPrivacy"] = use_differential_privacy

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.authorized_column import AuthorizedColumn
        from ..models.execution_quota_parameters import ExecutionQuotaParameters
        from ..models.threshold import Threshold

        d = src_dict.copy()
        authorized_columns = []
        _authorized_columns = d.pop("authorizedColumns", UNSET)
        for authorized_columns_item_data in _authorized_columns or []:
            authorized_columns_item = AuthorizedColumn.from_dict(authorized_columns_item_data)

            authorized_columns.append(authorized_columns_item)

        combine_local_results = d.pop("combineLocalResults", UNSET)

        _execution_quota_parameters = d.pop("executionQuotaParameters", UNSET)
        execution_quota_parameters: Union[Unset, ExecutionQuotaParameters]
        if isinstance(_execution_quota_parameters, Unset):
            execution_quota_parameters = UNSET
        else:
            execution_quota_parameters = ExecutionQuotaParameters.from_dict(_execution_quota_parameters)

        link_records = d.pop("linkRecords", UNSET)

        linkage_identifier = d.pop("linkageIdentifier", UNSET)

        _max_column_count = d.pop("maxColumnCount", UNSET)
        max_column_count: Union[Unset, Threshold]
        if isinstance(_max_column_count, Unset):
            max_column_count = UNSET
        else:
            max_column_count = Threshold.from_dict(_max_column_count)

        min_dataset_size = d.pop("minDatasetSize", UNSET)

        min_global_dataset_size = d.pop("minGlobalDatasetSize", UNSET)

        noisy_global_size = d.pop("noisyGlobalSize", UNSET)

        restrict_columns = d.pop("restrictColumns", UNSET)

        use_differential_privacy = d.pop("useDifferentialPrivacy", UNSET)

        dp_policy = cls(
            authorized_columns=authorized_columns,
            combine_local_results=combine_local_results,
            execution_quota_parameters=execution_quota_parameters,
            link_records=link_records,
            linkage_identifier=linkage_identifier,
            max_column_count=max_column_count,
            min_dataset_size=min_dataset_size,
            min_global_dataset_size=min_global_dataset_size,
            noisy_global_size=noisy_global_size,
            restrict_columns=restrict_columns,
            use_differential_privacy=use_differential_privacy,
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
