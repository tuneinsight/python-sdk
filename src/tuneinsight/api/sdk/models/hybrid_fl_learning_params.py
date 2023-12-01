from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.aggregation_strategy import AggregationStrategy
from ..types import UNSET, Unset

T = TypeVar("T", bound="HybridFLLearningParams")


@attr.s(auto_attribs=True)
class HybridFLLearningParams:
    """Hyperparameters for the Hybrid Federated Learning

    Attributes:
        epsilon (Union[Unset, float]): Epsilon parameter of the differential privacy in HybridFL
        fl_rounds (Union[Unset, int]): Number of federated rounds of the Hybrid FL
        momentum (Union[Unset, float]): Momentum of the optimizer in the python-server
        strategy (Union[Unset, AggregationStrategy]): weighting aggregation strategy Default:
            AggregationStrategy.CONSTANT.
        use_clipping_factor (Union[Unset, bool]): If set to true, gradient clipping is adjusted specifically at each
            layer Default: True.
        batch_size (Union[Unset, int]): Batch size for the training in the python-server
        delta (Union[Unset, float]): Delta parameter of the differential privacy in HybridFL
        encrypt_aggregation (Union[Unset, bool]): Whether to to the aggregation encrypted or not in HybridFL Default:
            True.
        gradient_clipping (Union[Unset, float]): Gradient clipping to apply for the training and the noise computation
        learning_rate (Union[Unset, float]): Learning rate of the optimizer in the python-server
        local_epochs (Union[Unset, int]): Number of local epochs of the Hybrid FL between aggregations
        num_workers (Union[Unset, int]): Number of workers loading the data for training in the python-server
        add_noise (Union[Unset, bool]): Whether to add differential privacy or not to the HybridFL Default: True.
    """

    epsilon: Union[Unset, float] = UNSET
    fl_rounds: Union[Unset, int] = UNSET
    momentum: Union[Unset, float] = UNSET
    strategy: Union[Unset, AggregationStrategy] = AggregationStrategy.CONSTANT
    use_clipping_factor: Union[Unset, bool] = True
    batch_size: Union[Unset, int] = UNSET
    delta: Union[Unset, float] = UNSET
    encrypt_aggregation: Union[Unset, bool] = True
    gradient_clipping: Union[Unset, float] = UNSET
    learning_rate: Union[Unset, float] = UNSET
    local_epochs: Union[Unset, int] = UNSET
    num_workers: Union[Unset, int] = UNSET
    add_noise: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        epsilon = self.epsilon
        fl_rounds = self.fl_rounds
        momentum = self.momentum
        strategy: Union[Unset, str] = UNSET
        if not isinstance(self.strategy, Unset):
            strategy = self.strategy.value

        use_clipping_factor = self.use_clipping_factor
        batch_size = self.batch_size
        delta = self.delta
        encrypt_aggregation = self.encrypt_aggregation
        gradient_clipping = self.gradient_clipping
        learning_rate = self.learning_rate
        local_epochs = self.local_epochs
        num_workers = self.num_workers
        add_noise = self.add_noise

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if epsilon is not UNSET:
            field_dict["epsilon"] = epsilon
        if fl_rounds is not UNSET:
            field_dict["flRounds"] = fl_rounds
        if momentum is not UNSET:
            field_dict["momentum"] = momentum
        if strategy is not UNSET:
            field_dict["strategy"] = strategy
        if use_clipping_factor is not UNSET:
            field_dict["useClippingFactor"] = use_clipping_factor
        if batch_size is not UNSET:
            field_dict["batchSize"] = batch_size
        if delta is not UNSET:
            field_dict["delta"] = delta
        if encrypt_aggregation is not UNSET:
            field_dict["encryptAggregation"] = encrypt_aggregation
        if gradient_clipping is not UNSET:
            field_dict["gradientClipping"] = gradient_clipping
        if learning_rate is not UNSET:
            field_dict["learningRate"] = learning_rate
        if local_epochs is not UNSET:
            field_dict["localEpochs"] = local_epochs
        if num_workers is not UNSET:
            field_dict["numWorkers"] = num_workers
        if add_noise is not UNSET:
            field_dict["addNoise"] = add_noise

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        epsilon = d.pop("epsilon", UNSET)

        fl_rounds = d.pop("flRounds", UNSET)

        momentum = d.pop("momentum", UNSET)

        _strategy = d.pop("strategy", UNSET)
        strategy: Union[Unset, AggregationStrategy]
        if isinstance(_strategy, Unset):
            strategy = UNSET
        else:
            strategy = AggregationStrategy(_strategy)

        use_clipping_factor = d.pop("useClippingFactor", UNSET)

        batch_size = d.pop("batchSize", UNSET)

        delta = d.pop("delta", UNSET)

        encrypt_aggregation = d.pop("encryptAggregation", UNSET)

        gradient_clipping = d.pop("gradientClipping", UNSET)

        learning_rate = d.pop("learningRate", UNSET)

        local_epochs = d.pop("localEpochs", UNSET)

        num_workers = d.pop("numWorkers", UNSET)

        add_noise = d.pop("addNoise", UNSET)

        hybrid_fl_learning_params = cls(
            epsilon=epsilon,
            fl_rounds=fl_rounds,
            momentum=momentum,
            strategy=strategy,
            use_clipping_factor=use_clipping_factor,
            batch_size=batch_size,
            delta=delta,
            encrypt_aggregation=encrypt_aggregation,
            gradient_clipping=gradient_clipping,
            learning_rate=learning_rate,
            local_epochs=local_epochs,
            num_workers=num_workers,
            add_noise=add_noise,
        )

        hybrid_fl_learning_params.additional_properties = d
        return hybrid_fl_learning_params

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
