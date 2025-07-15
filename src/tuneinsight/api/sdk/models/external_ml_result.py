from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.content_type import ContentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.external_ml_history import ExternalMlHistory
    from ..models.result_contextual_info import ResultContextualInfo


T = TypeVar("T", bound="ExternalMlResult")


@attr.s(auto_attribs=True)
class ExternalMlResult:
    """
    Attributes:
        type (ContentType): Type of the content
        result_path (str): Path of the result shared model
        contextual_info (Union[Unset, ResultContextualInfo]): contextual information about the content retrieved
        coefficients (Union[Unset, List[float]]):
        history (Union[Unset, ExternalMlHistory]): Training history of external ML containing the evolution of the
            metrics during training
    """

    type: ContentType
    result_path: str
    contextual_info: Union[Unset, "ResultContextualInfo"] = UNSET
    coefficients: Union[Unset, List[float]] = UNSET
    history: Union[Unset, "ExternalMlHistory"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        result_path = self.result_path
        contextual_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contextual_info, Unset):
            contextual_info = self.contextual_info.to_dict()

        coefficients: Union[Unset, List[float]] = UNSET
        if not isinstance(self.coefficients, Unset):
            coefficients = self.coefficients

        history: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.history, Unset):
            history = self.history.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "resultPath": result_path,
            }
        )
        if contextual_info is not UNSET:
            field_dict["contextualInfo"] = contextual_info
        if coefficients is not UNSET:
            field_dict["coefficients"] = coefficients
        if history is not UNSET:
            field_dict["history"] = history

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.external_ml_history import ExternalMlHistory
        from ..models.result_contextual_info import ResultContextualInfo

        d = src_dict.copy()
        type = ContentType(d.pop("type"))

        result_path = d.pop("resultPath")

        _contextual_info = d.pop("contextualInfo", UNSET)
        contextual_info: Union[Unset, ResultContextualInfo]
        if isinstance(_contextual_info, Unset):
            contextual_info = UNSET
        else:
            contextual_info = ResultContextualInfo.from_dict(_contextual_info)

        coefficients = cast(List[float], d.pop("coefficients", UNSET))

        _history = d.pop("history", UNSET)
        history: Union[Unset, ExternalMlHistory]
        if isinstance(_history, Unset):
            history = UNSET
        else:
            history = ExternalMlHistory.from_dict(_history)

        external_ml_result = cls(
            type=type,
            result_path=result_path,
            contextual_info=contextual_info,
            coefficients=coefficients,
            history=history,
        )

        external_ml_result.additional_properties = d
        return external_ml_result

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
