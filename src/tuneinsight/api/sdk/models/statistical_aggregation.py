from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.computation_type import ComputationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.binning_operation import BinningOperation
    from ..models.computation_data_source_parameters import ComputationDataSourceParameters
    from ..models.computation_preprocessing_parameters import ComputationPreprocessingParameters
    from ..models.dp_policy import DPPolicy
    from ..models.local_input import LocalInput


T = TypeVar("T", bound="StatisticalAggregation")


@attr.s(auto_attribs=True)
class StatisticalAggregation:
    """
    Attributes:
        type (ComputationType): Type of the computation.
        encrypted (Union[Unset, bool]): True if computation result should be encrypted with the collective public key.
        local_input_id (Union[Unset, str]): Unique identifier of a data object.
        project_id (Union[Unset, str]): Unique identifier of a project.
        dp_policy (Union[Unset, DPPolicy]): represents the disclosure prevention policy that enables toggling various
            disclosure prevention mechanisms
        cohort_id (Union[Unset, str]): Unique identifier of a data object.
        wait (Union[Unset, bool]): Whether to wait synchronously for the computation result.
        preprocessing_parameters (Union[Unset, ComputationPreprocessingParameters]): dataframe pre-processing parameters
            applied to the input retrieved from the datasource, if applicable
        timeout (Union[Unset, int]): The maximum amount of time in seconds the computation is allowed to run.
        owner (Union[Unset, str]): The username of the user who started the computation.
        data_source_parameters (Union[Unset, ComputationDataSourceParameters]): Parameters used to query the datasource
            from each node before the computation
        local (Union[Unset, bool]): True if the project's computation should run only with local data (not configured
            the network)
        local_input (Union[Unset, LocalInput]): If a local input is provided, the node initiating the computation will
            use it instead of querying the datasource. This data is *not* shared to other nodes, only used for the duration
            of the computation. The local input columns/values must be in the form {<column1>: [<value1>, <value2>, ...],
            ...}
        input_data_object (Union[Unset, str]): Shared identifier of a data object.
        join_id (Union[Unset, str]): Unique identifier of a data object.
        aggregation_columns (Union[Unset, List[str]]): list of columns where all data is aggregated
        binning_operations (Union[Unset, List['BinningOperation']]): list of binning operations to apply before
            aggregating the results
        include_dataset_length (Union[Unset, bool]): whether or not to compute the total dataset length
    """

    type: ComputationType
    encrypted: Union[Unset, bool] = UNSET
    local_input_id: Union[Unset, str] = UNSET
    project_id: Union[Unset, str] = UNSET
    dp_policy: Union[Unset, "DPPolicy"] = UNSET
    cohort_id: Union[Unset, str] = UNSET
    wait: Union[Unset, bool] = UNSET
    preprocessing_parameters: Union[Unset, "ComputationPreprocessingParameters"] = UNSET
    timeout: Union[Unset, int] = UNSET
    owner: Union[Unset, str] = UNSET
    data_source_parameters: Union[Unset, "ComputationDataSourceParameters"] = UNSET
    local: Union[Unset, bool] = UNSET
    local_input: Union[Unset, "LocalInput"] = UNSET
    input_data_object: Union[Unset, str] = UNSET
    join_id: Union[Unset, str] = UNSET
    aggregation_columns: Union[Unset, List[str]] = UNSET
    binning_operations: Union[Unset, List["BinningOperation"]] = UNSET
    include_dataset_length: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        encrypted = self.encrypted
        local_input_id = self.local_input_id
        project_id = self.project_id
        dp_policy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dp_policy, Unset):
            dp_policy = self.dp_policy.to_dict()

        cohort_id = self.cohort_id
        wait = self.wait
        preprocessing_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.preprocessing_parameters, Unset):
            preprocessing_parameters = self.preprocessing_parameters.to_dict()

        timeout = self.timeout
        owner = self.owner
        data_source_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data_source_parameters, Unset):
            data_source_parameters = self.data_source_parameters.to_dict()

        local = self.local
        local_input: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.local_input, Unset):
            local_input = self.local_input.to_dict()

        input_data_object = self.input_data_object
        join_id = self.join_id
        aggregation_columns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.aggregation_columns, Unset):
            aggregation_columns = self.aggregation_columns

        binning_operations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.binning_operations, Unset):
            binning_operations = []
            for binning_operations_item_data in self.binning_operations:
                binning_operations_item = binning_operations_item_data.to_dict()

                binning_operations.append(binning_operations_item)

        include_dataset_length = self.include_dataset_length

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if encrypted is not UNSET:
            field_dict["encrypted"] = encrypted
        if local_input_id is not UNSET:
            field_dict["localInputID"] = local_input_id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if dp_policy is not UNSET:
            field_dict["DPPolicy"] = dp_policy
        if cohort_id is not UNSET:
            field_dict["cohortId"] = cohort_id
        if wait is not UNSET:
            field_dict["wait"] = wait
        if preprocessing_parameters is not UNSET:
            field_dict["preprocessingParameters"] = preprocessing_parameters
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if owner is not UNSET:
            field_dict["owner"] = owner
        if data_source_parameters is not UNSET:
            field_dict["dataSourceParameters"] = data_source_parameters
        if local is not UNSET:
            field_dict["local"] = local
        if local_input is not UNSET:
            field_dict["localInput"] = local_input
        if input_data_object is not UNSET:
            field_dict["inputDataObject"] = input_data_object
        if join_id is not UNSET:
            field_dict["joinId"] = join_id
        if aggregation_columns is not UNSET:
            field_dict["aggregationColumns"] = aggregation_columns
        if binning_operations is not UNSET:
            field_dict["binningOperations"] = binning_operations
        if include_dataset_length is not UNSET:
            field_dict["includeDatasetLength"] = include_dataset_length

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.binning_operation import BinningOperation
        from ..models.computation_data_source_parameters import ComputationDataSourceParameters
        from ..models.computation_preprocessing_parameters import ComputationPreprocessingParameters
        from ..models.dp_policy import DPPolicy
        from ..models.local_input import LocalInput

        d = src_dict.copy()
        type = ComputationType(d.pop("type"))

        encrypted = d.pop("encrypted", UNSET)

        local_input_id = d.pop("localInputID", UNSET)

        project_id = d.pop("projectId", UNSET)

        _dp_policy = d.pop("DPPolicy", UNSET)
        dp_policy: Union[Unset, DPPolicy]
        if isinstance(_dp_policy, Unset):
            dp_policy = UNSET
        else:
            dp_policy = DPPolicy.from_dict(_dp_policy)

        cohort_id = d.pop("cohortId", UNSET)

        wait = d.pop("wait", UNSET)

        _preprocessing_parameters = d.pop("preprocessingParameters", UNSET)
        preprocessing_parameters: Union[Unset, ComputationPreprocessingParameters]
        if isinstance(_preprocessing_parameters, Unset):
            preprocessing_parameters = UNSET
        else:
            preprocessing_parameters = ComputationPreprocessingParameters.from_dict(_preprocessing_parameters)

        timeout = d.pop("timeout", UNSET)

        owner = d.pop("owner", UNSET)

        _data_source_parameters = d.pop("dataSourceParameters", UNSET)
        data_source_parameters: Union[Unset, ComputationDataSourceParameters]
        if isinstance(_data_source_parameters, Unset):
            data_source_parameters = UNSET
        else:
            data_source_parameters = ComputationDataSourceParameters.from_dict(_data_source_parameters)

        local = d.pop("local", UNSET)

        _local_input = d.pop("localInput", UNSET)
        local_input: Union[Unset, LocalInput]
        if isinstance(_local_input, Unset):
            local_input = UNSET
        else:
            local_input = LocalInput.from_dict(_local_input)

        input_data_object = d.pop("inputDataObject", UNSET)

        join_id = d.pop("joinId", UNSET)

        aggregation_columns = cast(List[str], d.pop("aggregationColumns", UNSET))

        binning_operations = []
        _binning_operations = d.pop("binningOperations", UNSET)
        for binning_operations_item_data in _binning_operations or []:
            binning_operations_item = BinningOperation.from_dict(binning_operations_item_data)

            binning_operations.append(binning_operations_item)

        include_dataset_length = d.pop("includeDatasetLength", UNSET)

        statistical_aggregation = cls(
            type=type,
            encrypted=encrypted,
            local_input_id=local_input_id,
            project_id=project_id,
            dp_policy=dp_policy,
            cohort_id=cohort_id,
            wait=wait,
            preprocessing_parameters=preprocessing_parameters,
            timeout=timeout,
            owner=owner,
            data_source_parameters=data_source_parameters,
            local=local,
            local_input=local_input,
            input_data_object=input_data_object,
            join_id=join_id,
            aggregation_columns=aggregation_columns,
            binning_operations=binning_operations,
            include_dataset_length=include_dataset_length,
        )

        statistical_aggregation.additional_properties = d
        return statistical_aggregation

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
