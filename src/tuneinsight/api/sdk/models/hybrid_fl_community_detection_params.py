from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="HybridFLCommunityDetectionParams")


@attr.s(auto_attribs=True)
class HybridFLCommunityDetectionParams:
    """Hyperparameters for community detection protocols in the Hybrid FL

    Attributes:
        params_type (Union[Unset, str]): Type of the protocol to use
        num_communities (Union[Unset, int]): Number of communities to detect
        rho (Union[Unset, float]): Rho convergence parameter for the community detection
    """

    params_type: Union[Unset, str] = UNSET
    num_communities: Union[Unset, int] = UNSET
    rho: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        params_type = self.params_type
        num_communities = self.num_communities
        rho = self.rho

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if params_type is not UNSET:
            field_dict["paramsType"] = params_type
        if num_communities is not UNSET:
            field_dict["numCommunities"] = num_communities
        if rho is not UNSET:
            field_dict["rho"] = rho

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        params_type = d.pop("paramsType", UNSET)

        num_communities = d.pop("numCommunities", UNSET)

        rho = d.pop("rho", UNSET)

        hybrid_fl_community_detection_params = cls(
            params_type=params_type,
            num_communities=num_communities,
            rho=rho,
        )

        hybrid_fl_community_detection_params.additional_properties = d
        return hybrid_fl_community_detection_params

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
