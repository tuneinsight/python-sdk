from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="HybridFLMachineLearningParams")


@attr.s(auto_attribs=True)
class HybridFLMachineLearningParams:
    """Hyperparameters for machine learning protocols in the Hybrid FL

    Attributes:
        params_type (Union[Unset, str]): Type of the protocol to use
        batch_size (Union[Unset, int]): Batch size for the training in the python-server
        learning_rate (Union[Unset, float]): Learning rate of the optimizer in the python-server
        local_epochs (Union[Unset, int]): Number of local epochs of the Hybrid FL between aggregations
        momentum (Union[Unset, float]): Momentum of the optimizer in the python-server
    """

    params_type: Union[Unset, str] = UNSET
    batch_size: Union[Unset, int] = UNSET
    learning_rate: Union[Unset, float] = UNSET
    local_epochs: Union[Unset, int] = UNSET
    momentum: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        params_type = self.params_type
        batch_size = self.batch_size
        learning_rate = self.learning_rate
        local_epochs = self.local_epochs
        momentum = self.momentum

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if params_type is not UNSET:
            field_dict["paramsType"] = params_type
        if batch_size is not UNSET:
            field_dict["batchSize"] = batch_size
        if learning_rate is not UNSET:
            field_dict["learningRate"] = learning_rate
        if local_epochs is not UNSET:
            field_dict["localEpochs"] = local_epochs
        if momentum is not UNSET:
            field_dict["momentum"] = momentum

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        params_type = d.pop("paramsType", UNSET)

        batch_size = d.pop("batchSize", UNSET)

        learning_rate = d.pop("learningRate", UNSET)

        local_epochs = d.pop("localEpochs", UNSET)

        momentum = d.pop("momentum", UNSET)

        hybrid_fl_machine_learning_params = cls(
            params_type=params_type,
            batch_size=batch_size,
            learning_rate=learning_rate,
            local_epochs=local_epochs,
            momentum=momentum,
        )

        hybrid_fl_machine_learning_params.additional_properties = d
        return hybrid_fl_machine_learning_params

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
