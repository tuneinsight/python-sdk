from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.computation_type import ComputationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.computation_data_source_parameters import ComputationDataSourceParameters
    from ..models.computation_preprocessing_parameters import ComputationPreprocessingParameters
    from ..models.differential_privacy_parameters import DifferentialPrivacyParameters


T = TypeVar("T", bound="EncryptedAggregation")


@attr.s(auto_attribs=True)
class EncryptedAggregation:
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
        aggregate_columns (Union[Unset, List[str]]): The columns on which the data should be aggregated
        aggregate_features (Union[Unset, bool]): If true, sum the columns together into one number
        columns_auto_completion (Union[Unset, bool]): When true, before running the aggregation, the nodes unify their
            columns names sets and input zeroes for locally missing columns
        features (Union[Unset, str]): Shared identifier of a data object.
        nb_features (Union[Unset, int]): Number of columns of the dataset
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
    aggregate_columns: Union[Unset, List[str]] = UNSET
    aggregate_features: Union[Unset, bool] = UNSET
    columns_auto_completion: Union[Unset, bool] = UNSET
    features: Union[Unset, str] = UNSET
    nb_features: Union[Unset, int] = UNSET
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
        aggregate_columns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.aggregate_columns, Unset):
            aggregate_columns = self.aggregate_columns

        aggregate_features = self.aggregate_features
        columns_auto_completion = self.columns_auto_completion
        features = self.features
        nb_features = self.nb_features

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
        if aggregate_columns is not UNSET:
            field_dict["aggregateColumns"] = aggregate_columns
        if aggregate_features is not UNSET:
            field_dict["aggregateFeatures"] = aggregate_features
        if columns_auto_completion is not UNSET:
            field_dict["columnsAutoCompletion"] = columns_auto_completion
        if features is not UNSET:
            field_dict["features"] = features
        if nb_features is not UNSET:
            field_dict["nbFeatures"] = nb_features

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
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

        aggregate_columns = cast(List[str], d.pop("aggregateColumns", UNSET))

        aggregate_features = d.pop("aggregateFeatures", UNSET)

        columns_auto_completion = d.pop("columnsAutoCompletion", UNSET)

        features = d.pop("features", UNSET)

        nb_features = d.pop("nbFeatures", UNSET)

        encrypted_aggregation = cls(
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
            aggregate_columns=aggregate_columns,
            aggregate_features=aggregate_features,
            columns_auto_completion=columns_auto_completion,
            features=features,
            nb_features=nb_features,
        )

        encrypted_aggregation.additional_properties = d
        return encrypted_aggregation

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
