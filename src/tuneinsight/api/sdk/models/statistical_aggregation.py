from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.computation_type import ComputationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.binning_operation import BinningOperation
    from ..models.computation_data_source_parameters import ComputationDataSourceParameters
    from ..models.computation_preprocessing_parameters import ComputationPreprocessingParameters
    from ..models.differential_privacy_parameters import DifferentialPrivacyParameters


T = TypeVar("T", bound="StatisticalAggregation")


@attr.s(auto_attribs=True)
class StatisticalAggregation:
    """
    Attributes:
        type (ComputationType): Type of the computation.
        cohort_id (Union[Unset, str]): Unique identifier of a data object.
        data_source_parameters (Union[Unset, ComputationDataSourceParameters]): Parameters used to query the datasource
            from each node before the computation
        differential_privacy_parameters (Union[Unset, DifferentialPrivacyParameters]): parameters for adding
            differential privacy noise to the computation's encrypted output
        encrypted (Union[Unset, bool]): True if computation result should be encrypted with the collective public key.
        input_data_object (Union[Unset, str]): Shared identifier of a data object.
        join_id (Union[Unset, str]): Unique identifier of a data object.
        local (Union[Unset, bool]): True if the project's computation should run only with local data (not configured
            the network)
        owner (Union[Unset, str]): The username of the user who started the computation.
        preprocessing_parameters (Union[Unset, ComputationPreprocessingParameters]): dataframe pre-processing parameters
            applied to the input retrieved from the datasource, if applicable
        project_id (Union[Unset, str]): Unique identifier of a project.
        timeout (Union[Unset, int]): The maximum amount of time in seconds the computation is allowed to run.
        wait (Union[Unset, bool]): Whether to wait synchronously for the computation result.
        aggregation_columns (Union[Unset, List[str]]): list of columns where all data is aggregated
        binning_operations (Union[Unset, List['BinningOperation']]): list of binning operations to apply before
            aggregating the results
        include_dataset_length (Union[Unset, bool]): whether or not to compute the total dataset length
    """

    type: ComputationType
    cohort_id: Union[Unset, str] = UNSET
    data_source_parameters: Union[Unset, "ComputationDataSourceParameters"] = UNSET
    differential_privacy_parameters: Union[Unset, "DifferentialPrivacyParameters"] = UNSET
    encrypted: Union[Unset, bool] = UNSET
    input_data_object: Union[Unset, str] = UNSET
    join_id: Union[Unset, str] = UNSET
    local: Union[Unset, bool] = UNSET
    owner: Union[Unset, str] = UNSET
    preprocessing_parameters: Union[Unset, "ComputationPreprocessingParameters"] = UNSET
    project_id: Union[Unset, str] = UNSET
    timeout: Union[Unset, int] = UNSET
    wait: Union[Unset, bool] = UNSET
    aggregation_columns: Union[Unset, List[str]] = UNSET
    binning_operations: Union[Unset, List["BinningOperation"]] = UNSET
    include_dataset_length: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        cohort_id = self.cohort_id
        data_source_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data_source_parameters, Unset):
            data_source_parameters = self.data_source_parameters.to_dict()

        differential_privacy_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.differential_privacy_parameters, Unset):
            differential_privacy_parameters = self.differential_privacy_parameters.to_dict()

        encrypted = self.encrypted
        input_data_object = self.input_data_object
        join_id = self.join_id
        local = self.local
        owner = self.owner
        preprocessing_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.preprocessing_parameters, Unset):
            preprocessing_parameters = self.preprocessing_parameters.to_dict()

        project_id = self.project_id
        timeout = self.timeout
        wait = self.wait
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
        if cohort_id is not UNSET:
            field_dict["cohortId"] = cohort_id
        if data_source_parameters is not UNSET:
            field_dict["dataSourceParameters"] = data_source_parameters
        if differential_privacy_parameters is not UNSET:
            field_dict["differentialPrivacyParameters"] = differential_privacy_parameters
        if encrypted is not UNSET:
            field_dict["encrypted"] = encrypted
        if input_data_object is not UNSET:
            field_dict["inputDataObject"] = input_data_object
        if join_id is not UNSET:
            field_dict["joinId"] = join_id
        if local is not UNSET:
            field_dict["local"] = local
        if owner is not UNSET:
            field_dict["owner"] = owner
        if preprocessing_parameters is not UNSET:
            field_dict["preprocessingParameters"] = preprocessing_parameters
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if wait is not UNSET:
            field_dict["wait"] = wait
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
        from ..models.differential_privacy_parameters import DifferentialPrivacyParameters

        d = src_dict.copy()
        type = ComputationType(d.pop("type"))

        cohort_id = d.pop("cohortId", UNSET)

        _data_source_parameters = d.pop("dataSourceParameters", UNSET)
        data_source_parameters: Union[Unset, ComputationDataSourceParameters]
        if isinstance(_data_source_parameters, Unset):
            data_source_parameters = UNSET
        else:
            data_source_parameters = ComputationDataSourceParameters.from_dict(_data_source_parameters)

        _differential_privacy_parameters = d.pop("differentialPrivacyParameters", UNSET)
        differential_privacy_parameters: Union[Unset, DifferentialPrivacyParameters]
        if isinstance(_differential_privacy_parameters, Unset):
            differential_privacy_parameters = UNSET
        else:
            differential_privacy_parameters = DifferentialPrivacyParameters.from_dict(_differential_privacy_parameters)

        encrypted = d.pop("encrypted", UNSET)

        input_data_object = d.pop("inputDataObject", UNSET)

        join_id = d.pop("joinId", UNSET)

        local = d.pop("local", UNSET)

        owner = d.pop("owner", UNSET)

        _preprocessing_parameters = d.pop("preprocessingParameters", UNSET)
        preprocessing_parameters: Union[Unset, ComputationPreprocessingParameters]
        if isinstance(_preprocessing_parameters, Unset):
            preprocessing_parameters = UNSET
        else:
            preprocessing_parameters = ComputationPreprocessingParameters.from_dict(_preprocessing_parameters)

        project_id = d.pop("projectId", UNSET)

        timeout = d.pop("timeout", UNSET)

        wait = d.pop("wait", UNSET)

        aggregation_columns = cast(List[str], d.pop("aggregationColumns", UNSET))

        binning_operations = []
        _binning_operations = d.pop("binningOperations", UNSET)
        for binning_operations_item_data in _binning_operations or []:
            binning_operations_item = BinningOperation.from_dict(binning_operations_item_data)

            binning_operations.append(binning_operations_item)

        include_dataset_length = d.pop("includeDatasetLength", UNSET)

        statistical_aggregation = cls(
            type=type,
            cohort_id=cohort_id,
            data_source_parameters=data_source_parameters,
            differential_privacy_parameters=differential_privacy_parameters,
            encrypted=encrypted,
            input_data_object=input_data_object,
            join_id=join_id,
            local=local,
            owner=owner,
            preprocessing_parameters=preprocessing_parameters,
            project_id=project_id,
            timeout=timeout,
            wait=wait,
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
