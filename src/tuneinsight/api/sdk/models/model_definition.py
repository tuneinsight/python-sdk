from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_metadata import ModelMetadata
    from ..models.prediction_params import PredictionParams


T = TypeVar("T", bound="ModelDefinition")


@attr.s(auto_attribs=True)
class ModelDefinition:
    """Definition of a model to upload

    Attributes:
        name (str): common name to give to the model
        prediction_params (PredictionParams): subset of parameters required for only the prediction
        weights (List[List[float]]): Plaintext weights of the model as a float matrix
        metadata (Union[Unset, ModelMetadata]): public metadata about the model
        project_id (Union[Unset, str]): Unique identifier of a project.
    """

    name: str
    prediction_params: "PredictionParams"
    weights: List[List[float]]
    metadata: Union[Unset, "ModelMetadata"] = UNSET
    project_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        prediction_params = self.prediction_params.to_dict()

        weights = []
        for weights_item_data in self.weights:
            weights_item = weights_item_data

            weights.append(weights_item)

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        project_id = self.project_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "predictionParams": prediction_params,
                "weights": weights,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if project_id is not UNSET:
            field_dict["projectId"] = project_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_metadata import ModelMetadata
        from ..models.prediction_params import PredictionParams

        d = src_dict.copy()
        name = d.pop("name")

        prediction_params = PredictionParams.from_dict(d.pop("predictionParams"))

        weights = []
        _weights = d.pop("weights")
        for weights_item_data in _weights:
            weights_item = cast(List[float], weights_item_data)

            weights.append(weights_item)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ModelMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ModelMetadata.from_dict(_metadata)

        project_id = d.pop("projectId", UNSET)

        model_definition = cls(
            name=name,
            prediction_params=prediction_params,
            weights=weights,
            metadata=metadata,
            project_id=project_id,
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
