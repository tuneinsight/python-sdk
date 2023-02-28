from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.project_policy_computation_policies import ProjectPolicyComputationPolicies
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectPolicy")


@attr.s(auto_attribs=True)
class ProjectPolicy:
    """represents a policy used to validate requested computations in a collaboration

    Attributes:
        computation_policies (Union[Unset, ProjectPolicyComputationPolicies]): given policies for each computation type
    """

    computation_policies: Union[Unset, ProjectPolicyComputationPolicies] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        computation_policies: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.computation_policies, Unset):
            computation_policies = self.computation_policies.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if computation_policies is not UNSET:
            field_dict["computationPolicies"] = computation_policies

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _computation_policies = d.pop("computationPolicies", UNSET)
        computation_policies: Union[Unset, ProjectPolicyComputationPolicies]
        if isinstance(_computation_policies, Unset):
            computation_policies = UNSET
        else:
            computation_policies = ProjectPolicyComputationPolicies.from_dict(_computation_policies)

        project_policy = cls(
            computation_policies=computation_policies,
        )

        project_policy.additional_properties = d
        return project_policy

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
