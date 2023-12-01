from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.computation_type import ComputationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.computation_data_source_parameters import ComputationDataSourceParameters
    from ..models.computation_preprocessing_parameters import ComputationPreprocessingParameters
    from ..models.dp_policy import DPPolicy
    from ..models.local_input import LocalInput
    from ..models.matching_column import MatchingColumn
    from ..models.survival import Survival
    from ..models.survival_aggregation_subgroups_item import SurvivalAggregationSubgroupsItem


T = TypeVar("T", bound="SurvivalAggregation")


@attr.s(auto_attribs=True)
class SurvivalAggregation:
    """
    Attributes:
        type (ComputationType): Type of the computation.
        join_id (Union[Unset, str]): Unique identifier of a data object.
        local_input (Union[Unset, LocalInput]): If a local input is provided, the node initiating the computation will
            use it instead of querying the datasource. This data is *not* shared to other nodes, only used for the duration
            of the computation. The local input columns/values must be in the form {<column1>: [<value1>, <value2>, ...],
            ...}
        wait (Union[Unset, bool]): Whether to wait synchronously for the computation result.
        input_data_object (Union[Unset, str]): Shared identifier of a data object.
        cohort_id (Union[Unset, str]): Unique identifier of a data object.
        project_id (Union[Unset, str]): Unique identifier of a project.
        release_results (Union[Unset, bool]): flag to set to true if the computation should directly release the output
            results.
            If set, then encrypted results are automatically key switched and decrypted
            and a Result entity is saved
        dp_policy (Union[Unset, DPPolicy]): represents the disclosure prevention policy that enables toggling various
            disclosure prevention mechanisms
        encrypted (Union[Unset, bool]): True if computation result should be encrypted with the collective public key.
        local (Union[Unset, bool]): True if the project's computation should run only with local data (not configured
            the network)
        local_input_id (Union[Unset, str]): Unique identifier of a data object.
        owner (Union[Unset, str]): The username of the end user who requested the computation.
        preprocessing_parameters (Union[Unset, ComputationPreprocessingParameters]): dataframe pre-processing parameters
            applied to the input retrieved from the datasource, if applicable
        timeout (Union[Unset, int]): The maximum amount of time in seconds the computation is allowed to run.
        data_source_parameters (Union[Unset, ComputationDataSourceParameters]): Parameters used to query the datasource
            from each node before the computation
        secure_matching (Union[Unset, bool]): if true then a cohort is created by matching records with a specified
            organization
        subgroups (Union[Unset, List['SurvivalAggregationSubgroupsItem']]): list of filters to create survival subgroups
        survival_parameters (Union[Unset, Survival]):
        encrypted_matching (Union[Unset, bool]): if true, then the resulting matches are kept encrypted before
            aggregating the survival data (slower)
        matching_columns (Union[Unset, List['MatchingColumn']]): The columns on which the data should be matched
        matching_organization (Union[Unset, str]): when secure matching is enabled, the organization with whom to match
            records with
    """

    type: ComputationType
    join_id: Union[Unset, str] = UNSET
    local_input: Union[Unset, "LocalInput"] = UNSET
    wait: Union[Unset, bool] = UNSET
    input_data_object: Union[Unset, str] = UNSET
    cohort_id: Union[Unset, str] = UNSET
    project_id: Union[Unset, str] = UNSET
    release_results: Union[Unset, bool] = UNSET
    dp_policy: Union[Unset, "DPPolicy"] = UNSET
    encrypted: Union[Unset, bool] = UNSET
    local: Union[Unset, bool] = UNSET
    local_input_id: Union[Unset, str] = UNSET
    owner: Union[Unset, str] = UNSET
    preprocessing_parameters: Union[Unset, "ComputationPreprocessingParameters"] = UNSET
    timeout: Union[Unset, int] = UNSET
    data_source_parameters: Union[Unset, "ComputationDataSourceParameters"] = UNSET
    secure_matching: Union[Unset, bool] = UNSET
    subgroups: Union[Unset, List["SurvivalAggregationSubgroupsItem"]] = UNSET
    survival_parameters: Union[Unset, "Survival"] = UNSET
    encrypted_matching: Union[Unset, bool] = UNSET
    matching_columns: Union[Unset, List["MatchingColumn"]] = UNSET
    matching_organization: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        join_id = self.join_id
        local_input: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.local_input, Unset):
            local_input = self.local_input.to_dict()

        wait = self.wait
        input_data_object = self.input_data_object
        cohort_id = self.cohort_id
        project_id = self.project_id
        release_results = self.release_results
        dp_policy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dp_policy, Unset):
            dp_policy = self.dp_policy.to_dict()

        encrypted = self.encrypted
        local = self.local
        local_input_id = self.local_input_id
        owner = self.owner
        preprocessing_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.preprocessing_parameters, Unset):
            preprocessing_parameters = self.preprocessing_parameters.to_dict()

        timeout = self.timeout
        data_source_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data_source_parameters, Unset):
            data_source_parameters = self.data_source_parameters.to_dict()

        secure_matching = self.secure_matching
        subgroups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subgroups, Unset):
            subgroups = []
            for subgroups_item_data in self.subgroups:
                subgroups_item = subgroups_item_data.to_dict()

                subgroups.append(subgroups_item)

        survival_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.survival_parameters, Unset):
            survival_parameters = self.survival_parameters.to_dict()

        encrypted_matching = self.encrypted_matching
        matching_columns: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.matching_columns, Unset):
            matching_columns = []
            for matching_columns_item_data in self.matching_columns:
                matching_columns_item = matching_columns_item_data.to_dict()

                matching_columns.append(matching_columns_item)

        matching_organization = self.matching_organization

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if join_id is not UNSET:
            field_dict["joinId"] = join_id
        if local_input is not UNSET:
            field_dict["localInput"] = local_input
        if wait is not UNSET:
            field_dict["wait"] = wait
        if input_data_object is not UNSET:
            field_dict["inputDataObject"] = input_data_object
        if cohort_id is not UNSET:
            field_dict["cohortId"] = cohort_id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if release_results is not UNSET:
            field_dict["releaseResults"] = release_results
        if dp_policy is not UNSET:
            field_dict["DPPolicy"] = dp_policy
        if encrypted is not UNSET:
            field_dict["encrypted"] = encrypted
        if local is not UNSET:
            field_dict["local"] = local
        if local_input_id is not UNSET:
            field_dict["localInputID"] = local_input_id
        if owner is not UNSET:
            field_dict["owner"] = owner
        if preprocessing_parameters is not UNSET:
            field_dict["preprocessingParameters"] = preprocessing_parameters
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if data_source_parameters is not UNSET:
            field_dict["dataSourceParameters"] = data_source_parameters
        if secure_matching is not UNSET:
            field_dict["secureMatching"] = secure_matching
        if subgroups is not UNSET:
            field_dict["subgroups"] = subgroups
        if survival_parameters is not UNSET:
            field_dict["survivalParameters"] = survival_parameters
        if encrypted_matching is not UNSET:
            field_dict["encryptedMatching"] = encrypted_matching
        if matching_columns is not UNSET:
            field_dict["matchingColumns"] = matching_columns
        if matching_organization is not UNSET:
            field_dict["matchingOrganization"] = matching_organization

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.computation_data_source_parameters import ComputationDataSourceParameters
        from ..models.computation_preprocessing_parameters import ComputationPreprocessingParameters
        from ..models.dp_policy import DPPolicy
        from ..models.local_input import LocalInput
        from ..models.matching_column import MatchingColumn
        from ..models.survival import Survival
        from ..models.survival_aggregation_subgroups_item import SurvivalAggregationSubgroupsItem

        d = src_dict.copy()
        type = ComputationType(d.pop("type"))

        join_id = d.pop("joinId", UNSET)

        _local_input = d.pop("localInput", UNSET)
        local_input: Union[Unset, LocalInput]
        if isinstance(_local_input, Unset):
            local_input = UNSET
        else:
            local_input = LocalInput.from_dict(_local_input)

        wait = d.pop("wait", UNSET)

        input_data_object = d.pop("inputDataObject", UNSET)

        cohort_id = d.pop("cohortId", UNSET)

        project_id = d.pop("projectId", UNSET)

        release_results = d.pop("releaseResults", UNSET)

        _dp_policy = d.pop("DPPolicy", UNSET)
        dp_policy: Union[Unset, DPPolicy]
        if isinstance(_dp_policy, Unset):
            dp_policy = UNSET
        else:
            dp_policy = DPPolicy.from_dict(_dp_policy)

        encrypted = d.pop("encrypted", UNSET)

        local = d.pop("local", UNSET)

        local_input_id = d.pop("localInputID", UNSET)

        owner = d.pop("owner", UNSET)

        _preprocessing_parameters = d.pop("preprocessingParameters", UNSET)
        preprocessing_parameters: Union[Unset, ComputationPreprocessingParameters]
        if isinstance(_preprocessing_parameters, Unset):
            preprocessing_parameters = UNSET
        else:
            preprocessing_parameters = ComputationPreprocessingParameters.from_dict(_preprocessing_parameters)

        timeout = d.pop("timeout", UNSET)

        _data_source_parameters = d.pop("dataSourceParameters", UNSET)
        data_source_parameters: Union[Unset, ComputationDataSourceParameters]
        if isinstance(_data_source_parameters, Unset):
            data_source_parameters = UNSET
        else:
            data_source_parameters = ComputationDataSourceParameters.from_dict(_data_source_parameters)

        secure_matching = d.pop("secureMatching", UNSET)

        subgroups = []
        _subgroups = d.pop("subgroups", UNSET)
        for subgroups_item_data in _subgroups or []:
            subgroups_item = SurvivalAggregationSubgroupsItem.from_dict(subgroups_item_data)

            subgroups.append(subgroups_item)

        _survival_parameters = d.pop("survivalParameters", UNSET)
        survival_parameters: Union[Unset, Survival]
        if isinstance(_survival_parameters, Unset):
            survival_parameters = UNSET
        else:
            survival_parameters = Survival.from_dict(_survival_parameters)

        encrypted_matching = d.pop("encryptedMatching", UNSET)

        matching_columns = []
        _matching_columns = d.pop("matchingColumns", UNSET)
        for matching_columns_item_data in _matching_columns or []:
            matching_columns_item = MatchingColumn.from_dict(matching_columns_item_data)

            matching_columns.append(matching_columns_item)

        matching_organization = d.pop("matchingOrganization", UNSET)

        survival_aggregation = cls(
            type=type,
            join_id=join_id,
            local_input=local_input,
            wait=wait,
            input_data_object=input_data_object,
            cohort_id=cohort_id,
            project_id=project_id,
            release_results=release_results,
            dp_policy=dp_policy,
            encrypted=encrypted,
            local=local,
            local_input_id=local_input_id,
            owner=owner,
            preprocessing_parameters=preprocessing_parameters,
            timeout=timeout,
            data_source_parameters=data_source_parameters,
            secure_matching=secure_matching,
            subgroups=subgroups,
            survival_parameters=survival_parameters,
            encrypted_matching=encrypted_matching,
            matching_columns=matching_columns,
            matching_organization=matching_organization,
        )

        survival_aggregation.additional_properties = d
        return survival_aggregation

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
