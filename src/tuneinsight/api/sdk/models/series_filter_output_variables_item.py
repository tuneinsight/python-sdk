from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.tiql_selection_criterion import TiqlSelectionCriterion
from ..types import UNSET, Unset

T = TypeVar("T", bound="SeriesFilterOutputVariablesItem")


@attr.s(auto_attribs=True)
class SeriesFilterOutputVariablesItem:
    """Defines how to select a value from a series that passes the filter. If a series passes the seriesFilter, then
    at least one of its entries passes the inner filter. The variable is extracted from one of the entries that
    pass this filter (according to entrySelectionCriterion), and from one of the features of the entry.

        Attributes:
            alias (Union[Unset, str]): Unique alias assigned to this variable that can be used in other parts of the query
                and as return value.
                In TIQL++, this property can be empty, in which case a unique identifier is defined by the transpiler.
            entry_selection_criterion (Union[Unset, TiqlSelectionCriterion]): Describes how to select, in a given series, an
                entry that passes the inner filter from which to select the
                variable value (since, in general, there will be multiple entries that pass). Only "first" is currently
                implemented, but this behavior is not enforced by most implementations for efficiency reasons.
            field (Union[Unset, str]): Name of the field to retrieve from the selected entry. The concept is implicitly
                described by the seriesFilter it is defined on.
            name (Union[Unset, str]): Deprecated. Use `alias` instead.
            source (Union[Unset, str]): Deprecated. Use `field` instead.
    """

    alias: Union[Unset, str] = UNSET
    entry_selection_criterion: Union[Unset, TiqlSelectionCriterion] = UNSET
    field: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alias = self.alias
        entry_selection_criterion: Union[Unset, str] = UNSET
        if not isinstance(self.entry_selection_criterion, Unset):
            entry_selection_criterion = self.entry_selection_criterion.value

        field = self.field
        name = self.name
        source = self.source

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alias is not UNSET:
            field_dict["alias"] = alias
        if entry_selection_criterion is not UNSET:
            field_dict["entrySelectionCriterion"] = entry_selection_criterion
        if field is not UNSET:
            field_dict["field"] = field
        if name is not UNSET:
            field_dict["name"] = name
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        alias = d.pop("alias", UNSET)

        _entry_selection_criterion = d.pop("entrySelectionCriterion", UNSET)
        entry_selection_criterion: Union[Unset, TiqlSelectionCriterion]
        if isinstance(_entry_selection_criterion, Unset):
            entry_selection_criterion = UNSET
        else:
            entry_selection_criterion = TiqlSelectionCriterion(_entry_selection_criterion)

        field = d.pop("field", UNSET)

        name = d.pop("name", UNSET)

        source = d.pop("source", UNSET)

        series_filter_output_variables_item = cls(
            alias=alias,
            entry_selection_criterion=entry_selection_criterion,
            field=field,
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
