from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.content_type import ContentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.result_contextual_info import ResultContextualInfo


T = TypeVar("T", bound="Prediction")


@attr.s(auto_attribs=True)
class Prediction:
    """
    Attributes:
        type (ContentType): Type of the content
        labels (List[List[float]]): optional ground truth labels
        predictions (List[List[float]]): decrypted predicted values
        contextual_info (Union[Unset, ResultContextualInfo]): contextual information about the content retrieved
    """

    type: ContentType
    labels: List[List[float]]
    predictions: List[List[float]]
    contextual_info: Union[Unset, "ResultContextualInfo"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        labels = []
        for labels_item_data in self.labels:
            labels_item = labels_item_data

            labels.append(labels_item)

        predictions = []
        for predictions_item_data in self.predictions:
            predictions_item = predictions_item_data

            predictions.append(predictions_item)

        contextual_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contextual_info, Unset):
            contextual_info = self.contextual_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "labels": labels,
                "predictions": predictions,
            }
        )
        if contextual_info is not UNSET:
            field_dict["contextualInfo"] = contextual_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.result_contextual_info import ResultContextualInfo

        d = src_dict.copy()
        type = ContentType(d.pop("type"))

        labels = []
        _labels = d.pop("labels")
        for labels_item_data in _labels:
            labels_item = cast(List[float], labels_item_data)

            labels.append(labels_item)

        predictions = []
        _predictions = d.pop("predictions")
        for predictions_item_data in _predictions:
            predictions_item = cast(List[float], predictions_item_data)

            predictions.append(predictions_item)

        _contextual_info = d.pop("contextualInfo", UNSET)
        contextual_info: Union[Unset, ResultContextualInfo]
        if isinstance(_contextual_info, Unset):
            contextual_info = UNSET
        else:
            contextual_info = ResultContextualInfo.from_dict(_contextual_info)

        prediction = cls(
            type=type,
            labels=labels,
            predictions=predictions,
            contextual_info=contextual_info,
        )

        prediction.additional_properties = d
        return prediction

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
