from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.computation_type import ComputationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.computation_data_source_parameters import ComputationDataSourceParameters
    from ..models.computation_preprocessing_parameters import ComputationPreprocessingParameters
    from ..models.dp_policy import DPPolicy
    from ..models.local_input import LocalInput
    from ..models.rot_key_gen_rotations_item import RotKeyGenRotationsItem


T = TypeVar("T", bound="RotKeyGen")


@attr.s(auto_attribs=True)
class RotKeyGen:
    """
    Attributes:
        type (ComputationType): Type of the computation.
        local_input (Union[Unset, LocalInput]): If a local input is provided, the node initiating the computation will
            use it instead of querying the datasource. This data is *not* shared to other nodes, only used for the duration
            of the computation. The local input columns/values must be in the form {<column1>: [<value1>, <value2>, ...],
            ...}
        preprocessing_parameters (Union[Unset, ComputationPreprocessingParameters]): dataframe pre-processing parameters
            applied to the input retrieved from the datasource, if applicable
        timeout (Union[Unset, int]): The maximum amount of time in seconds the computation is allowed to run.
        local_input_id (Union[Unset, str]): Unique identifier of a data object.
        release_results (Union[Unset, bool]): flag to set to true if the computation should directly release the output
            results.
            If set, then encrypted results are automatically key switched and decrypted
            and a Result entity is saved
        wait (Union[Unset, bool]): Whether to wait synchronously for the computation result.
        dp_policy (Union[Unset, DPPolicy]): represents the disclosure prevention policy that enables toggling various
            disclosure prevention mechanisms
        data_source_parameters (Union[Unset, ComputationDataSourceParameters]): Parameters used to query the datasource
            from each node before the computation
        encrypted (Union[Unset, bool]): True if computation result should be encrypted with the collective public key.
        local (Union[Unset, bool]): True if the project's computation should run only with local data (not configured
            the network)
        join_id (Union[Unset, str]): Unique identifier of a data object.
        cohort_id (Union[Unset, str]): Unique identifier of a data object.
        input_data_object (Union[Unset, str]): Shared identifier of a data object.
        owner (Union[Unset, str]): The username of the user who started the computation.
        project_id (Union[Unset, str]): Unique identifier of a project.
        rotations (Union[Unset, List['RotKeyGenRotationsItem']]):
    """

    type: ComputationType
    local_input: Union[Unset, "LocalInput"] = UNSET
    preprocessing_parameters: Union[Unset, "ComputationPreprocessingParameters"] = UNSET
    timeout: Union[Unset, int] = UNSET
    local_input_id: Union[Unset, str] = UNSET
    release_results: Union[Unset, bool] = UNSET
    wait: Union[Unset, bool] = UNSET
    dp_policy: Union[Unset, "DPPolicy"] = UNSET
    data_source_parameters: Union[Unset, "ComputationDataSourceParameters"] = UNSET
    encrypted: Union[Unset, bool] = UNSET
    local: Union[Unset, bool] = UNSET
    join_id: Union[Unset, str] = UNSET
    cohort_id: Union[Unset, str] = UNSET
    input_data_object: Union[Unset, str] = UNSET
    owner: Union[Unset, str] = UNSET
    project_id: Union[Unset, str] = UNSET
    rotations: Union[Unset, List["RotKeyGenRotationsItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        local_input: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.local_input, Unset):
            local_input = self.local_input.to_dict()

        preprocessing_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.preprocessing_parameters, Unset):
            preprocessing_parameters = self.preprocessing_parameters.to_dict()

        timeout = self.timeout
        local_input_id = self.local_input_id
        release_results = self.release_results
        wait = self.wait
        dp_policy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dp_policy, Unset):
            dp_policy = self.dp_policy.to_dict()

        data_source_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data_source_parameters, Unset):
            data_source_parameters = self.data_source_parameters.to_dict()

        encrypted = self.encrypted
        local = self.local
        join_id = self.join_id
        cohort_id = self.cohort_id
        input_data_object = self.input_data_object
        owner = self.owner
        project_id = self.project_id
        rotations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rotations, Unset):
            rotations = []
            for rotations_item_data in self.rotations:
                rotations_item = rotations_item_data.to_dict()

                rotations.append(rotations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if local_input is not UNSET:
            field_dict["localInput"] = local_input
        if preprocessing_parameters is not UNSET:
            field_dict["preprocessingParameters"] = preprocessing_parameters
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if local_input_id is not UNSET:
            field_dict["localInputID"] = local_input_id
        if release_results is not UNSET:
            field_dict["releaseResults"] = release_results
        if wait is not UNSET:
            field_dict["wait"] = wait
        if dp_policy is not UNSET:
            field_dict["DPPolicy"] = dp_policy
        if data_source_parameters is not UNSET:
            field_dict["dataSourceParameters"] = data_source_parameters
        if encrypted is not UNSET:
            field_dict["encrypted"] = encrypted
        if local is not UNSET:
            field_dict["local"] = local
        if join_id is not UNSET:
            field_dict["joinId"] = join_id
        if cohort_id is not UNSET:
            field_dict["cohortId"] = cohort_id
        if input_data_object is not UNSET:
            field_dict["inputDataObject"] = input_data_object
        if owner is not UNSET:
            field_dict["owner"] = owner
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if rotations is not UNSET:
            field_dict["rotations"] = rotations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.computation_data_source_parameters import ComputationDataSourceParameters
        from ..models.computation_preprocessing_parameters import ComputationPreprocessingParameters
        from ..models.dp_policy import DPPolicy
        from ..models.local_input import LocalInput
        from ..models.rot_key_gen_rotations_item import RotKeyGenRotationsItem

        d = src_dict.copy()
        type = ComputationType(d.pop("type"))

        _local_input = d.pop("localInput", UNSET)
        local_input: Union[Unset, LocalInput]
        if isinstance(_local_input, Unset):
            local_input = UNSET
        else:
            local_input = LocalInput.from_dict(_local_input)

        _preprocessing_parameters = d.pop("preprocessingParameters", UNSET)
        preprocessing_parameters: Union[Unset, ComputationPreprocessingParameters]
        if isinstance(_preprocessing_parameters, Unset):
            preprocessing_parameters = UNSET
        else:
            preprocessing_parameters = ComputationPreprocessingParameters.from_dict(_preprocessing_parameters)

        timeout = d.pop("timeout", UNSET)

        local_input_id = d.pop("localInputID", UNSET)

        release_results = d.pop("releaseResults", UNSET)

        wait = d.pop("wait", UNSET)

        _dp_policy = d.pop("DPPolicy", UNSET)
        dp_policy: Union[Unset, DPPolicy]
        if isinstance(_dp_policy, Unset):
            dp_policy = UNSET
        else:
            dp_policy = DPPolicy.from_dict(_dp_policy)

        _data_source_parameters = d.pop("dataSourceParameters", UNSET)
        data_source_parameters: Union[Unset, ComputationDataSourceParameters]
        if isinstance(_data_source_parameters, Unset):
            data_source_parameters = UNSET
        else:
            data_source_parameters = ComputationDataSourceParameters.from_dict(_data_source_parameters)

        encrypted = d.pop("encrypted", UNSET)

        local = d.pop("local", UNSET)

        join_id = d.pop("joinId", UNSET)

        cohort_id = d.pop("cohortId", UNSET)

        input_data_object = d.pop("inputDataObject", UNSET)

        owner = d.pop("owner", UNSET)

        project_id = d.pop("projectId", UNSET)

        rotations = []
        _rotations = d.pop("rotations", UNSET)
        for rotations_item_data in _rotations or []:
            rotations_item = RotKeyGenRotationsItem.from_dict(rotations_item_data)

            rotations.append(rotations_item)

        rot_key_gen = cls(
            type=type,
            local_input=local_input,
            preprocessing_parameters=preprocessing_parameters,
            timeout=timeout,
            local_input_id=local_input_id,
            release_results=release_results,
            wait=wait,
            dp_policy=dp_policy,
            data_source_parameters=data_source_parameters,
            encrypted=encrypted,
            local=local,
            join_id=join_id,
            cohort_id=cohort_id,
            input_data_object=input_data_object,
            owner=owner,
            project_id=project_id,
            rotations=rotations,
        )

        rot_key_gen.additional_properties = d
        return rot_key_gen

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
