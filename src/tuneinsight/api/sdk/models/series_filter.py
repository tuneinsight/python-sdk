from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.advanced_filter_type import AdvancedFilterType
from ..models.boolean_aggregator import BooleanAggregator
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advanced_filter import AdvancedFilter
    from ..models.series_filter_output_variables_item import SeriesFilterOutputVariablesItem


T = TypeVar("T", bound="SeriesFilter")


@attr.s(auto_attribs=True)
class SeriesFilter:
    """A filter applied to a "series" feature, i.e., a feature that contains multiple entries for a single record.
    This filter consists of an "inner" filter that is applied to each entry in the series. Then, the results are
    aggregated through a logical operator (either AND or OR). A variable (single value) can be extracted upon
    successfully passing the filter by extracting a variable of an entry that passed the inner filter.

        Attributes:
            type (AdvancedFilterType): A type of filter for cross-standard queries.
            filter_ (Union[Unset, AdvancedFilter]): Abstract subclass of a filter for cross-standard queries.
            logical_aggregator (Union[Unset, BooleanAggregator]): A criterion to aggregate a series of boolean values as a
                single value.
            output_count_as_variable (Union[Unset, None, str]): If specified, the number of entries that pass the internal
                filter will be output as a variable with this name.
            output_variables (Union[Unset, List['SeriesFilterOutputVariablesItem']]):
            series (Union[Unset, str]): The name of the series feature to which the filter applies.
    """

    type: AdvancedFilterType
    filter_: Union[Unset, "AdvancedFilter"] = UNSET
    logical_aggregator: Union[Unset, BooleanAggregator] = UNSET
    output_count_as_variable: Union[Unset, None, str] = UNSET
    output_variables: Union[Unset, List["SeriesFilterOutputVariablesItem"]] = UNSET
    series: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        filter_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        logical_aggregator: Union[Unset, str] = UNSET
        if not isinstance(self.logical_aggregator, Unset):
            logical_aggregator = self.logical_aggregator.value

        output_count_as_variable = self.output_count_as_variable
        output_variables: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.output_variables, Unset):
            output_variables = []
            for output_variables_item_data in self.output_variables:
                output_variables_item = output_variables_item_data.to_dict()

                output_variables.append(output_variables_item)

        series = self.series

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if logical_aggregator is not UNSET:
            field_dict["logicalAggregator"] = logical_aggregator
        if output_count_as_variable is not UNSET:
            field_dict["outputCountAsVariable"] = output_count_as_variable
        if output_variables is not UNSET:
            field_dict["outputVariables"] = output_variables
        if series is not UNSET:
            field_dict["series"] = series

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.advanced_filter import AdvancedFilter
        from ..models.series_filter_output_variables_item import SeriesFilterOutputVariablesItem

        d = src_dict.copy()
        type = AdvancedFilterType(d.pop("type"))

        _filter_ = d.pop("filter", UNSET)
        filter_: Union[Unset, AdvancedFilter]
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = AdvancedFilter.from_dict(_filter_)

        _logical_aggregator = d.pop("logicalAggregator", UNSET)
        logical_aggregator: Union[Unset, BooleanAggregator]
        if isinstance(_logical_aggregator, Unset):
            logical_aggregator = UNSET
        else:
            logical_aggregator = BooleanAggregator(_logical_aggregator)

        output_count_as_variable = d.pop("outputCountAsVariable", UNSET)

        output_variables = []
        _output_variables = d.pop("outputVariables", UNSET)
        for output_variables_item_data in _output_variables or []:
            output_variables_item = SeriesFilterOutputVariablesItem.from_dict(output_variables_item_data)

            output_variables.append(output_variables_item)

        series = d.pop("series", UNSET)

        series_filter = cls(
            type=type,
            filter_=filter_,
            logical_aggregator=logical_aggregator,
            output_count_as_variable=output_count_as_variable,
            output_variables=output_variables,
            series=series,
        )

        series_filter.additional_properties = d
        return series_filter

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
