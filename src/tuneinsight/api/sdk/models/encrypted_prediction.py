from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.computation_type import ComputationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.computation_data_source_parameters import ComputationDataSourceParameters
    from ..models.computation_preprocessing_parameters import ComputationPreprocessingParameters
    from ..models.dp_policy import DPPolicy
    from ..models.local_input import LocalInput


T = TypeVar("T", bound="EncryptedPrediction")


@attr.s(auto_attribs=True)
class EncryptedPrediction:
    """
    Attributes:
        type (ComputationType): Type of the computation.
        dp_policy (Union[Unset, DPPolicy]): represents the disclosure prevention policy that enables toggling various
            disclosure prevention mechanisms
        cohort_id (Union[Unset, str]): Unique identifier of a data object.
        data_source_parameters (Union[Unset, ComputationDataSourceParameters]): Parameters used to query the datasource
            from each node before the computation
        encrypted (Union[Unset, bool]): True if computation result should be encrypted with the collective public key.
        input_data_object (Union[Unset, str]): Shared identifier of a data object.
        join_id (Union[Unset, str]): Unique identifier of a data object.
        local (Union[Unset, bool]): True if the project's computation should run only with local data (not configured
            the network)
        local_input (Union[Unset, LocalInput]): If a local input is provided, the node initiating the computation will
            use it instead of querying the datasource. This data is *not* shared to other nodes, only used for the duration
            of the computation. The local input columns/values must be in the form {<column1>: [<value1>, <value2>, ...],
            ...}
        local_input_id (Union[Unset, str]): Unique identifier of a data object.
        owner (Union[Unset, str]): The username of the user who started the computation.
        preprocessing_parameters (Union[Unset, ComputationPreprocessingParameters]): dataframe pre-processing parameters
            applied to the input retrieved from the datasource, if applicable
        project_id (Union[Unset, str]): Unique identifier of a project.
        timeout (Union[Unset, int]): The maximum amount of time in seconds the computation is allowed to run.
        wait (Union[Unset, bool]): Whether to wait synchronously for the computation result.
        data (Union[Unset, str]): Unique identifier of a data object.
        feature_columns (Union[Unset, List[str]]): specified features columns, not required, if not specified, all
            columns from the input dataset are used
        include_ground_truth_labels (Union[Unset, bool]): if true, then the result should contain the associated ground
            truth labels
        label_columns (Union[Unset, List[str]]): specified label columns of the original dataset if the computation
            specifies to return the ground truth labels alongside
        model (Union[Unset, str]): Unique identifier of a data object.
        only_root_prediction (Union[Unset, bool]): if true and the computation is not local, then the prediction is only
            computed by the root node and the ct is broadcast to other nodes for later key switch
    """

    type: ComputationType
    dp_policy: Union[Unset, "DPPolicy"] = UNSET
    cohort_id: Union[Unset, str] = UNSET
    data_source_parameters: Union[Unset, "ComputationDataSourceParameters"] = UNSET
    encrypted: Union[Unset, bool] = UNSET
    input_data_object: Union[Unset, str] = UNSET
    join_id: Union[Unset, str] = UNSET
    local: Union[Unset, bool] = UNSET
    local_input: Union[Unset, "LocalInput"] = UNSET
    local_input_id: Union[Unset, str] = UNSET
    owner: Union[Unset, str] = UNSET
    preprocessing_parameters: Union[Unset, "ComputationPreprocessingParameters"] = UNSET
    project_id: Union[Unset, str] = UNSET
    timeout: Union[Unset, int] = UNSET
    wait: Union[Unset, bool] = UNSET
    data: Union[Unset, str] = UNSET
    feature_columns: Union[Unset, List[str]] = UNSET
    include_ground_truth_labels: Union[Unset, bool] = UNSET
    label_columns: Union[Unset, List[str]] = UNSET
    model: Union[Unset, str] = UNSET
    only_root_prediction: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        dp_policy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dp_policy, Unset):
            dp_policy = self.dp_policy.to_dict()

        cohort_id = self.cohort_id
        data_source_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data_source_parameters, Unset):
            data_source_parameters = self.data_source_parameters.to_dict()

        encrypted = self.encrypted
        input_data_object = self.input_data_object
        join_id = self.join_id
        local = self.local
        local_input: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.local_input, Unset):
            local_input = self.local_input.to_dict()

        local_input_id = self.local_input_id
        owner = self.owner
        preprocessing_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.preprocessing_parameters, Unset):
            preprocessing_parameters = self.preprocessing_parameters.to_dict()

        project_id = self.project_id
        timeout = self.timeout
        wait = self.wait
        data = self.data
        feature_columns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.feature_columns, Unset):
            feature_columns = self.feature_columns

        include_ground_truth_labels = self.include_ground_truth_labels
        label_columns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.label_columns, Unset):
            label_columns = self.label_columns

        model = self.model
        only_root_prediction = self.only_root_prediction

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if dp_policy is not UNSET:
            field_dict["DPPolicy"] = dp_policy
        if cohort_id is not UNSET:
            field_dict["cohortId"] = cohort_id
        if data_source_parameters is not UNSET:
            field_dict["dataSourceParameters"] = data_source_parameters
        if encrypted is not UNSET:
            field_dict["encrypted"] = encrypted
        if input_data_object is not UNSET:
            field_dict["inputDataObject"] = input_data_object
        if join_id is not UNSET:
            field_dict["joinId"] = join_id
        if local is not UNSET:
            field_dict["local"] = local
        if local_input is not UNSET:
            field_dict["localInput"] = local_input
        if local_input_id is not UNSET:
            field_dict["localInputID"] = local_input_id
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
        if data is not UNSET:
            field_dict["data"] = data
        if feature_columns is not UNSET:
            field_dict["featureColumns"] = feature_columns
        if include_ground_truth_labels is not UNSET:
            field_dict["includeGroundTruthLabels"] = include_ground_truth_labels
        if label_columns is not UNSET:
            field_dict["labelColumns"] = label_columns
        if model is not UNSET:
            field_dict["model"] = model
        if only_root_prediction is not UNSET:
            field_dict["onlyRootPrediction"] = only_root_prediction

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.computation_data_source_parameters import ComputationDataSourceParameters
        from ..models.computation_preprocessing_parameters import ComputationPreprocessingParameters
        from ..models.dp_policy import DPPolicy
        from ..models.local_input import LocalInput

        d = src_dict.copy()
        type = ComputationType(d.pop("type"))

        _dp_policy = d.pop("DPPolicy", UNSET)
        dp_policy: Union[Unset, DPPolicy]
        if isinstance(_dp_policy, Unset):
            dp_policy = UNSET
        else:
            dp_policy = DPPolicy.from_dict(_dp_policy)

        cohort_id = d.pop("cohortId", UNSET)

        _data_source_parameters = d.pop("dataSourceParameters", UNSET)
        data_source_parameters: Union[Unset, ComputationDataSourceParameters]
        if isinstance(_data_source_parameters, Unset):
            data_source_parameters = UNSET
        else:
            data_source_parameters = ComputationDataSourceParameters.from_dict(_data_source_parameters)

        encrypted = d.pop("encrypted", UNSET)

        input_data_object = d.pop("inputDataObject", UNSET)

        join_id = d.pop("joinId", UNSET)

        local = d.pop("local", UNSET)

        _local_input = d.pop("localInput", UNSET)
        local_input: Union[Unset, LocalInput]
        if isinstance(_local_input, Unset):
            local_input = UNSET
        else:
            local_input = LocalInput.from_dict(_local_input)

        local_input_id = d.pop("localInputID", UNSET)

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

        data = d.pop("data", UNSET)

        feature_columns = cast(List[str], d.pop("featureColumns", UNSET))

        include_ground_truth_labels = d.pop("includeGroundTruthLabels", UNSET)

        label_columns = cast(List[str], d.pop("labelColumns", UNSET))

        model = d.pop("model", UNSET)

        only_root_prediction = d.pop("onlyRootPrediction", UNSET)

        encrypted_prediction = cls(
            type=type,
            dp_policy=dp_policy,
            cohort_id=cohort_id,
            data_source_parameters=data_source_parameters,
            encrypted=encrypted,
            input_data_object=input_data_object,
            join_id=join_id,
            local=local,
            local_input=local_input,
            local_input_id=local_input_id,
            owner=owner,
            preprocessing_parameters=preprocessing_parameters,
            project_id=project_id,
            timeout=timeout,
            wait=wait,
            data=data,
            feature_columns=feature_columns,
            include_ground_truth_labels=include_ground_truth_labels,
            label_columns=label_columns,
            model=model,
            only_root_prediction=only_root_prediction,
        )

        encrypted_prediction.additional_properties = d
        return encrypted_prediction

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
