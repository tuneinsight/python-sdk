from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ApproximationParams")


@attr.s(auto_attribs=True)
class ApproximationParams:
    """parameters for polynomial approximation

    Attributes:
        approximation_degree (int): The degree for the sigmoid approximation. Default: 28.
        approximation_interval_max (float): The higher bound for the approximation. The features must respect it.
            Default: 8.0.
        approximation_interval_min (float): The lower bound for the approximation. The features must respect it.
            Default: -8.0.
    """

    approximation_degree: int = 28
    approximation_interval_max: float = 8.0
    approximation_interval_min: float = -8.0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        approximation_degree = self.approximation_degree
        approximation_interval_max = self.approximation_interval_max
        approximation_interval_min = self.approximation_interval_min

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "approximationDegree": approximation_degree,
                "approximationIntervalMax": approximation_interval_max,
                "approximationIntervalMin": approximation_interval_min,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        approximation_degree = d.pop("approximationDegree")

        approximation_interval_max = d.pop("approximationIntervalMax")

        approximation_interval_min = d.pop("approximationIntervalMin")

        approximation_params = cls(
            approximation_degree=approximation_degree,
            approximation_interval_max=approximation_interval_max,
            approximation_interval_min=approximation_interval_min,
        )

        approximation_params.additional_properties = d
        return approximation_params

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
