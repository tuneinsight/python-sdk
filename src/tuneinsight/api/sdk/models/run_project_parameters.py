from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.run_mode import RunMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.computation_definition import ComputationDefinition


T = TypeVar("T", bound="RunProjectParameters")


@attr.s(auto_attribs=True)
class RunProjectParameters:
    """parameters used to launch the project with.

    Attributes:
        computation_definition (Union[Unset, ComputationDefinition]): Generic computation.
        computation_definition_base_64 (Union[Unset, str]): modified computation to run the project with.
            (base64-encoded)
        participants_from_computation (Union[Unset, str]): Identifier of a computation, unique across all computing
            nodes.
        requesting_instance_id (Union[Unset, str]): name of the instance that requested to run the project, when the
            project is being run from a leaf instance.
        run_mode (Union[Unset, RunMode]): Defines the mode in which to run a computation (local, collective, or both)
        wait (Union[Unset, None, bool]): whether to run the computation synchronously
    """

    computation_definition: Union[Unset, "ComputationDefinition"] = UNSET
    computation_definition_base_64: Union[Unset, str] = UNSET
    participants_from_computation: Union[Unset, str] = UNSET
    requesting_instance_id: Union[Unset, str] = UNSET
    run_mode: Union[Unset, RunMode] = UNSET
    wait: Union[Unset, None, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        computation_definition: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.computation_definition, Unset):
            computation_definition = self.computation_definition.to_dict()

        computation_definition_base_64 = self.computation_definition_base_64
        participants_from_computation = self.participants_from_computation
        requesting_instance_id = self.requesting_instance_id
        run_mode: Union[Unset, str] = UNSET
        if not isinstance(self.run_mode, Unset):
            run_mode = self.run_mode.value

        wait = self.wait

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if computation_definition is not UNSET:
            field_dict["computationDefinition"] = computation_definition
        if computation_definition_base_64 is not UNSET:
            field_dict["computationDefinitionBase64"] = computation_definition_base_64
        if participants_from_computation is not UNSET:
            field_dict["participantsFromComputation"] = participants_from_computation
        if requesting_instance_id is not UNSET:
            field_dict["requestingInstanceId"] = requesting_instance_id
        if run_mode is not UNSET:
            field_dict["runMode"] = run_mode
        if wait is not UNSET:
            field_dict["wait"] = wait

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.computation_definition import ComputationDefinition

        d = src_dict.copy()
        _computation_definition = d.pop("computationDefinition", UNSET)
        computation_definition: Union[Unset, ComputationDefinition]
        if isinstance(_computation_definition, Unset):
            computation_definition = UNSET
        else:
            computation_definition = ComputationDefinition.from_dict(_computation_definition)

        computation_definition_base_64 = d.pop("computationDefinitionBase64", UNSET)

        participants_from_computation = d.pop("participantsFromComputation", UNSET)

        requesting_instance_id = d.pop("requestingInstanceId", UNSET)

        _run_mode = d.pop("runMode", UNSET)
        run_mode: Union[Unset, RunMode]
        if isinstance(_run_mode, Unset):
            run_mode = UNSET
        else:
            run_mode = RunMode(_run_mode)

        wait = d.pop("wait", UNSET)

        run_project_parameters = cls(
            computation_definition=computation_definition,
            computation_definition_base_64=computation_definition_base_64,
            participants_from_computation=participants_from_computation,
            requesting_instance_id=requesting_instance_id,
            run_mode=run_mode,
            wait=wait,
        )

        run_project_parameters.additional_properties = d
        return run_project_parameters

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
