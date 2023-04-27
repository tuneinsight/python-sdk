from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, cast

import attr

if TYPE_CHECKING:
    from ..models.prediction_params import PredictionParams


T = TypeVar("T", bound="ModelDefinition")


@attr.s(auto_attribs=True)
class ModelDefinition:
    """Definition of a model to upload

    Attributes:
        name (str): common name to give to the model
        prediction_params (PredictionParams): subset of parameters required for only the prediction
        weights (List[List[float]]): Plaintext weights of the model as a float matrix
    """

    name: str
    prediction_params: "PredictionParams"
    weights: List[List[float]]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        prediction_params = self.prediction_params.to_dict()

        weights = []
        for weights_item_data in self.weights:
            weights_item = weights_item_data

            weights.append(weights_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "predictionParams": prediction_params,
                "weights": weights,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.prediction_params import PredictionParams

        d = src_dict.copy()
        name = d.pop("name")

        prediction_params = PredictionParams.from_dict(d.pop("predictionParams"))

        weights = []
        _weights = d.pop("weights")
        for weights_item_data in _weights:
            weights_item = cast(List[float], weights_item_data)

            weights.append(weights_item)

        model_definition = cls(
            name=name,
            prediction_params=prediction_params,
            weights=weights,
        )

        model_definition.additional_properties = d
        return model_definition

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
