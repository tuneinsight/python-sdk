from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.content_type import ContentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.result_contextual_info import ResultContextualInfo
    from ..models.statistic_result import StatisticResult


T = TypeVar("T", bound="Statistics")


@attr.s(auto_attribs=True)
class Statistics:
    """
    Attributes:
        type (ContentType): Type of the content
        results (List['StatisticResult']):
        contextual_info (Union[Unset, ResultContextualInfo]): contextual information about the content retrieved
    """

    type: ContentType
    results: List["StatisticResult"]
    contextual_info: Union[Unset, "ResultContextualInfo"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()

            results.append(results_item)

        contextual_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contextual_info, Unset):
            contextual_info = self.contextual_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "results": results,
            }
        )
        if contextual_info is not UNSET:
            field_dict["contextualInfo"] = contextual_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.result_contextual_info import ResultContextualInfo
        from ..models.statistic_result import StatisticResult

        d = src_dict.copy()
        type = ContentType(d.pop("type"))

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = StatisticResult.from_dict(results_item_data)

            results.append(results_item)

        _contextual_info = d.pop("contextualInfo", UNSET)
        contextual_info: Union[Unset, ResultContextualInfo]
        if isinstance(_contextual_info, Unset):
            contextual_info = UNSET
        else:
            contextual_info = ResultContextualInfo.from_dict(_contextual_info)

        statistics = cls(
            type=type,
            results=results,
            contextual_info=contextual_info,
        )

        statistics.additional_properties = d
        return statistics

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
