from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.model_type import ModelType
from ..models.training_algorithm import TrainingAlgorithm
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_object import DataObject
    from ..models.model_metadata import ModelMetadata
    from ..models.model_params import ModelParams


T = TypeVar("T", bound="Model")


@attr.s(auto_attribs=True)
class Model:
    """Machine learning model metadata definition

    Attributes:
        name (Union[Unset, str]): common name for the model
        updated_at (Union[Unset, str]):
        created_at (Union[Unset, str]):
        data_object (Union[Unset, DataObject]): A data object definition.
        model_id (Union[Unset, str]): Unique identifier of a model.
        model_params (Union[Unset, ModelParams]): detailed parameters about the model, only returned when getting
            specific model
        computation_id (Union[Unset, str]): Computation that created this model if collective model
        metadata (Union[Unset, ModelMetadata]): public metadata about the model
        training_algorithm (Union[Unset, TrainingAlgorithm]): the algorithm used to train the model
        type (Union[Unset, ModelType]): whether the model is local (plaintext) or collective (ciphertext)
    """

    name: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    data_object: Union[Unset, "DataObject"] = UNSET
    model_id: Union[Unset, str] = UNSET
    model_params: Union[Unset, "ModelParams"] = UNSET
    computation_id: Union[Unset, str] = UNSET
    metadata: Union[Unset, "ModelMetadata"] = UNSET
    training_algorithm: Union[Unset, TrainingAlgorithm] = UNSET
    type: Union[Unset, ModelType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        updated_at = self.updated_at
        created_at = self.created_at
        data_object: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data_object, Unset):
            data_object = self.data_object.to_dict()

        model_id = self.model_id
        model_params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.model_params, Unset):
            model_params = self.model_params.to_dict()

        computation_id = self.computation_id
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        training_algorithm: Union[Unset, str] = UNSET
        if not isinstance(self.training_algorithm, Unset):
            training_algorithm = self.training_algorithm.value

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if data_object is not UNSET:
            field_dict["dataObject"] = data_object
        if model_id is not UNSET:
            field_dict["modelID"] = model_id
        if model_params is not UNSET:
            field_dict["modelParams"] = model_params
        if computation_id is not UNSET:
            field_dict["computationId"] = computation_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if training_algorithm is not UNSET:
            field_dict["trainingAlgorithm"] = training_algorithm
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_object import DataObject
        from ..models.model_metadata import ModelMetadata
        from ..models.model_params import ModelParams

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        created_at = d.pop("createdAt", UNSET)

        _data_object = d.pop("dataObject", UNSET)
        data_object: Union[Unset, DataObject]
        if isinstance(_data_object, Unset):
            data_object = UNSET
        else:
            data_object = DataObject.from_dict(_data_object)

        model_id = d.pop("modelID", UNSET)

        _model_params = d.pop("modelParams", UNSET)
        model_params: Union[Unset, ModelParams]
        if isinstance(_model_params, Unset):
            model_params = UNSET
        else:
            model_params = ModelParams.from_dict(_model_params)

        computation_id = d.pop("computationId", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ModelMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ModelMetadata.from_dict(_metadata)

        _training_algorithm = d.pop("trainingAlgorithm", UNSET)
        training_algorithm: Union[Unset, TrainingAlgorithm]
        if isinstance(_training_algorithm, Unset):
            training_algorithm = UNSET
        else:
            training_algorithm = TrainingAlgorithm(_training_algorithm)

        _type = d.pop("type", UNSET)
        type: Union[Unset, ModelType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ModelType(_type)

        model = cls(
            name=name,
            updated_at=updated_at,
            created_at=created_at,
            data_object=data_object,
            model_id=model_id,
            model_params=model_params,
            computation_id=computation_id,
            metadata=metadata,
            training_algorithm=training_algorithm,
            type=type,
        )

        model.additional_properties = d
        return model

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
