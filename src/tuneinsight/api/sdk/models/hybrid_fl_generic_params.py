from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.aggregation_strategy import AggregationStrategy
from ..types import UNSET, Unset

T = TypeVar("T", bound="HybridFLGenericParams")


@attr.s(auto_attribs=True)
class HybridFLGenericParams:
    """Parameters for the Hybrid Federated Learning

    Attributes:
        encrypt_aggregation (Union[Unset, bool]): Whether to to the aggregation encrypted or not in HybridFL Default:
            True.
        fl_rounds (Union[Unset, int]): Number of federated rounds of the Hybrid FL
        num_workers (Union[Unset, int]): Number of workers loading the data for training in the python-server
        strategy (Union[Unset, AggregationStrategy]): weighting aggregation strategy Default:
            AggregationStrategy.CONSTANT.
    """

    encrypt_aggregation: Union[Unset, bool] = True
    fl_rounds: Union[Unset, int] = UNSET
    num_workers: Union[Unset, int] = UNSET
    strategy: Union[Unset, AggregationStrategy] = AggregationStrategy.CONSTANT
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        encrypt_aggregation = self.encrypt_aggregation
        fl_rounds = self.fl_rounds
        num_workers = self.num_workers
        strategy: Union[Unset, str] = UNSET
        if not isinstance(self.strategy, Unset):
            strategy = self.strategy.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if encrypt_aggregation is not UNSET:
            field_dict["encryptAggregation"] = encrypt_aggregation
        if fl_rounds is not UNSET:
            field_dict["flRounds"] = fl_rounds
        if num_workers is not UNSET:
            field_dict["numWorkers"] = num_workers
        if strategy is not UNSET:
            field_dict["strategy"] = strategy

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        encrypt_aggregation = d.pop("encryptAggregation", UNSET)

        fl_rounds = d.pop("flRounds", UNSET)

        num_workers = d.pop("numWorkers", UNSET)

        _strategy = d.pop("strategy", UNSET)
        strategy: Union[Unset, AggregationStrategy]
        if isinstance(_strategy, Unset):
            strategy = UNSET
        else:
            strategy = AggregationStrategy(_strategy)

        hybrid_fl_generic_params = cls(
            encrypt_aggregation=encrypt_aggregation,
            fl_rounds=fl_rounds,
            num_workers=num_workers,
            strategy=strategy,
        )

        hybrid_fl_generic_params.additional_properties = d
        return hybrid_fl_generic_params

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
