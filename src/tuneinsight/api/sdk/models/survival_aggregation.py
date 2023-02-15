from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.computation_type import ComputationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.computation_data_source_parameters import ComputationDataSourceParameters
    from ..models.computation_preprocessing_parameters import ComputationPreprocessingParameters
    from ..models.differential_privacy_parameters import DifferentialPrivacyParameters
    from ..models.matching_column import MatchingColumn
    from ..models.survival import Survival
    from ..models.survival_aggregation_subgroups_item import SurvivalAggregationSubgroupsItem


T = TypeVar("T", bound="SurvivalAggregation")


@attr.s(auto_attribs=True)
class SurvivalAggregation:
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
        encrypted_matching (Union[Unset, bool]): if true, then the resulting matches are kept encrypted before
            aggregating the survival data (slower)
        matching_columns (Union[Unset, List['MatchingColumn']]): The columns on which the data should be matched
        matching_organization (Union[Unset, str]): when secure matching is enabled, the organization with whom to match
            records with
        secure_matching (Union[Unset, bool]): if true then a cohort is created by matching records with a specified
            organization
        subgroups (Union[Unset, List['SurvivalAggregationSubgroupsItem']]): list of filters to create survival subgroups
        survival_parameters (Union[Unset, Survival]):
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
    encrypted_matching: Union[Unset, bool] = UNSET
    matching_columns: Union[Unset, List["MatchingColumn"]] = UNSET
    matching_organization: Union[Unset, str] = UNSET
    secure_matching: Union[Unset, bool] = UNSET
    subgroups: Union[Unset, List["SurvivalAggregationSubgroupsItem"]] = UNSET
    survival_parameters: Union[Unset, "Survival"] = UNSET
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
        encrypted_matching = self.encrypted_matching
        matching_columns: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.matching_columns, Unset):
            matching_columns = []
            for matching_columns_item_data in self.matching_columns:
                matching_columns_item = matching_columns_item_data.to_dict()

                matching_columns.append(matching_columns_item)

        matching_organization = self.matching_organization
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
        if encrypted_matching is not UNSET:
            field_dict["encryptedMatching"] = encrypted_matching
        if matching_columns is not UNSET:
            field_dict["matchingColumns"] = matching_columns
        if matching_organization is not UNSET:
            field_dict["matchingOrganization"] = matching_organization
        if secure_matching is not UNSET:
            field_dict["secureMatching"] = secure_matching
        if subgroups is not UNSET:
            field_dict["subgroups"] = subgroups
        if survival_parameters is not UNSET:
            field_dict["survivalParameters"] = survival_parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.computation_data_source_parameters import ComputationDataSourceParameters
        from ..models.computation_preprocessing_parameters import ComputationPreprocessingParameters
        from ..models.differential_privacy_parameters import DifferentialPrivacyParameters
        from ..models.matching_column import MatchingColumn
        from ..models.survival import Survival
        from ..models.survival_aggregation_subgroups_item import SurvivalAggregationSubgroupsItem

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

        encrypted_matching = d.pop("encryptedMatching", UNSET)

        matching_columns = []
        _matching_columns = d.pop("matchingColumns", UNSET)
        for matching_columns_item_data in _matching_columns or []:
            matching_columns_item = MatchingColumn.from_dict(matching_columns_item_data)

            matching_columns.append(matching_columns_item)

        matching_organization = d.pop("matchingOrganization", UNSET)

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

        survival_aggregation = cls(
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
            encrypted_matching=encrypted_matching,
            matching_columns=matching_columns,
            matching_organization=matching_organization,
            secure_matching=secure_matching,
            subgroups=subgroups,
            survival_parameters=survival_parameters,
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
