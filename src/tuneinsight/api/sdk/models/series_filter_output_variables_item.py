from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.series_filter_output_variables_item_entry_selection_criterion import (
    SeriesFilterOutputVariablesItemEntrySelectionCriterion,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SeriesFilterOutputVariablesItem")


@attr.s(auto_attribs=True)
class SeriesFilterOutputVariablesItem:
    """Defines how to select a value from a series that passes the filter. If a series passes the seriesFilter, then
    at least one of its entries passes the inner filter. The variable is extracted from one of the entries that
    pass this filter (according to entrySelectionCriterion), and from one of the features of the entry.

        Attributes:
            entry_selection_criterion (Union[Unset, SeriesFilterOutputVariablesItemEntrySelectionCriterion]): Describes how
                to select an entry in the series that passes the inner filter from which to select the
                variable value (since, in general, there will be multiple entries that pass). Only "first" is currently
                implemented, but this behavior is not enforced by most implementations for efficiency reasons.
            name (Union[Unset, str]): Unique name assigned to this variable that can be used in other parts of the query.
            source (Union[Unset, str]): Name of the feature to retrieve from the selected entry.
    """

    entry_selection_criterion: Union[Unset, SeriesFilterOutputVariablesItemEntrySelectionCriterion] = UNSET
    name: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entry_selection_criterion: Union[Unset, str] = UNSET
        if not isinstance(self.entry_selection_criterion, Unset):
            entry_selection_criterion = self.entry_selection_criterion.value

        name = self.name
        source = self.source

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entry_selection_criterion is not UNSET:
            field_dict["entrySelectionCriterion"] = entry_selection_criterion
        if name is not UNSET:
            field_dict["name"] = name
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _entry_selection_criterion = d.pop("entrySelectionCriterion", UNSET)
        entry_selection_criterion: Union[Unset, SeriesFilterOutputVariablesItemEntrySelectionCriterion]
        if isinstance(_entry_selection_criterion, Unset):
            entry_selection_criterion = UNSET
        else:
            entry_selection_criterion = SeriesFilterOutputVariablesItemEntrySelectionCriterion(
                _entry_selection_criterion
            )

        name = d.pop("name", UNSET)

        source = d.pop("source", UNSET)

        series_filter_output_variables_item = cls(
            entry_selection_criterion=entry_selection_criterion,
            name=name,
            source=source,
        )

        series_filter_output_variables_item.additional_properties = d
        return series_filter_output_variables_item

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
