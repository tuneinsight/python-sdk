from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.regression_type import RegressionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.approximation_params import ApproximationParams


T = TypeVar("T", bound="PredictionParams")


@attr.s(auto_attribs=True)
class PredictionParams:
    """subset of parameters required for only the prediction

    Attributes:
        approximation_params (Union[Unset, ApproximationParams]): parameters for polynomial approximation
        regression_type (Union[Unset, RegressionType]): type of the regression
    """

    approximation_params: Union[Unset, "ApproximationParams"] = UNSET
    regression_type: Union[Unset, RegressionType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        approximation_params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.approximation_params, Unset):
            approximation_params = self.approximation_params.to_dict()

        regression_type: Union[Unset, str] = UNSET
        if not isinstance(self.regression_type, Unset):
            regression_type = self.regression_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if approximation_params is not UNSET:
            field_dict["approximationParams"] = approximation_params
        if regression_type is not UNSET:
            field_dict["regressionType"] = regression_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.approximation_params import ApproximationParams

        d = src_dict.copy()
        _approximation_params = d.pop("approximationParams", UNSET)
        approximation_params: Union[Unset, ApproximationParams]
        if isinstance(_approximation_params, Unset):
            approximation_params = UNSET
        else:
            approximation_params = ApproximationParams.from_dict(_approximation_params)

        _regression_type = d.pop("regressionType", UNSET)
        regression_type: Union[Unset, RegressionType]
        if isinstance(_regression_type, Unset):
            regression_type = UNSET
        else:
            regression_type = RegressionType(_regression_type)

        prediction_params = cls(
            approximation_params=approximation_params,
            regression_type=regression_type,
        )

        prediction_params.additional_properties = d
        return prediction_params

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
