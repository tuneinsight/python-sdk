from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.approximation_params import ApproximationParams
from ..models.encrypted_regression_params_linear import EncryptedRegressionParamsLinear
from ..models.regression_type import RegressionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="EncryptedRegressionParams")


@attr.s(auto_attribs=True)
class EncryptedRegressionParams:
    """Parameters for the encrypted regression.

    Attributes:
        approximation_params (Union[Unset, ApproximationParams]): parameters for polynomial approximation
        elastic_rate (Union[Unset, float]): The elastic rate of the regression. Default: 0.85.
        learning_rate (Union[Unset, float]): The learning rate of the regression. Default: 0.02.
        linear (Union[Unset, EncryptedRegressionParamsLinear]): Parameters specific for the linear regression.
        local_batch_size (Union[Unset, int]): The batch size in each local iteration. Default: 64.
        local_iteration_count (Union[Unset, int]): The maximum number of local iterations. Default: 1.
        momentum (Union[Unset, float]): The momentum rate of the regression. Default: 0.92.
        network_iteration_count (Union[Unset, int]): The global maximum number of iteration. Default: 1.
        seed (Union[Unset, float]): The seed to sample the initial weights.
        type (Union[Unset, RegressionType]): type of the regression
    """

    approximation_params: Union[Unset, ApproximationParams] = UNSET
    elastic_rate: Union[Unset, float] = 0.85
    learning_rate: Union[Unset, float] = 0.02
    linear: Union[Unset, EncryptedRegressionParamsLinear] = UNSET
    local_batch_size: Union[Unset, int] = 64
    local_iteration_count: Union[Unset, int] = 1
    momentum: Union[Unset, float] = 0.92
    network_iteration_count: Union[Unset, int] = 1
    seed: Union[Unset, float] = 0.0
    type: Union[Unset, RegressionType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        approximation_params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.approximation_params, Unset):
            approximation_params = self.approximation_params.to_dict()

        elastic_rate = self.elastic_rate
        learning_rate = self.learning_rate
        linear: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.linear, Unset):
            linear = self.linear.to_dict()

        local_batch_size = self.local_batch_size
        local_iteration_count = self.local_iteration_count
        momentum = self.momentum
        network_iteration_count = self.network_iteration_count
        seed = self.seed
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if approximation_params is not UNSET:
            field_dict["approximationParams"] = approximation_params
        if elastic_rate is not UNSET:
            field_dict["elasticRate"] = elastic_rate
        if learning_rate is not UNSET:
            field_dict["learningRate"] = learning_rate
        if linear is not UNSET:
            field_dict["linear"] = linear
        if local_batch_size is not UNSET:
            field_dict["localBatchSize"] = local_batch_size
        if local_iteration_count is not UNSET:
            field_dict["localIterationCount"] = local_iteration_count
        if momentum is not UNSET:
            field_dict["momentum"] = momentum
        if network_iteration_count is not UNSET:
            field_dict["networkIterationCount"] = network_iteration_count
        if seed is not UNSET:
            field_dict["seed"] = seed
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _approximation_params = d.pop("approximationParams", UNSET)
        approximation_params: Union[Unset, ApproximationParams]
        if isinstance(_approximation_params, Unset):
            approximation_params = UNSET
        else:
            approximation_params = ApproximationParams.from_dict(_approximation_params)

        elastic_rate = d.pop("elasticRate", UNSET)

        learning_rate = d.pop("learningRate", UNSET)

        _linear = d.pop("linear", UNSET)
        linear: Union[Unset, EncryptedRegressionParamsLinear]
        if isinstance(_linear, Unset):
            linear = UNSET
        else:
            linear = EncryptedRegressionParamsLinear.from_dict(_linear)

        local_batch_size = d.pop("localBatchSize", UNSET)

        local_iteration_count = d.pop("localIterationCount", UNSET)

        momentum = d.pop("momentum", UNSET)

        network_iteration_count = d.pop("networkIterationCount", UNSET)

        seed = d.pop("seed", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, RegressionType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = RegressionType(_type)

        encrypted_regression_params = cls(
            approximation_params=approximation_params,
            elastic_rate=elastic_rate,
            learning_rate=learning_rate,
            linear=linear,
            local_batch_size=local_batch_size,
            local_iteration_count=local_iteration_count,
            momentum=momentum,
            network_iteration_count=network_iteration_count,
            seed=seed,
            type=type,
        )

        encrypted_regression_params.additional_properties = d
        return encrypted_regression_params

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
