from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

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
        raw_dp_results (Union[Unset, List[float]]): When using differential privacy, the output of the aggregation from
            which statistics are computed.
            This can be used to estimate confidence intervals for the values computed.
    """

    type: ContentType
    results: List["StatisticResult"]
    contextual_info: Union[Unset, "ResultContextualInfo"] = UNSET
    raw_dp_results: Union[Unset, List[float]] = UNSET
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

        raw_dp_results: Union[Unset, List[float]] = UNSET
        if not isinstance(self.raw_dp_results, Unset):
            raw_dp_results = self.raw_dp_results

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
        if raw_dp_results is not UNSET:
            field_dict["rawDPResults"] = raw_dp_results

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

        raw_dp_results = cast(List[float], d.pop("rawDPResults", UNSET))

        statistics = cls(
            type=type,
            results=results,
            contextual_info=contextual_info,
            raw_dp_results=raw_dp_results,
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
