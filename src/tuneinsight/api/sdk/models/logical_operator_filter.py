from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.advanced_filter_type import AdvancedFilterType
from ..models.logical_operator import LogicalOperator
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advanced_filter import AdvancedFilter


T = TypeVar("T", bound="LogicalOperatorFilter")


@attr.s(auto_attribs=True)
class LogicalOperatorFilter:
    """This filter aggregates the result of multiple filters using a logical operator.
    This either performs a conjunction (OR, ANY) or a disjunction (AND, ALL) of the filter results.

        Attributes:
            type (AdvancedFilterType): A type of filter for cross-standard queries.
            filters (Union[Unset, List['AdvancedFilter']]): A list of filters to apply, which are then combined using the
                logical operator.
            operator (Union[Unset, LogicalOperator]): A logical operator to "aggregate" multiple boolean values.
    """

    type: AdvancedFilterType
    filters: Union[Unset, List["AdvancedFilter"]] = UNSET
    operator: Union[Unset, LogicalOperator] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        filters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.filters, Unset):
            filters = []
            for filters_item_data in self.filters:
                filters_item = filters_item_data.to_dict()

                filters.append(filters_item)

        operator: Union[Unset, str] = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if filters is not UNSET:
            field_dict["filters"] = filters
        if operator is not UNSET:
            field_dict["operator"] = operator

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.advanced_filter import AdvancedFilter

        d = src_dict.copy()
        type = AdvancedFilterType(d.pop("type"))

        filters = []
        _filters = d.pop("filters", UNSET)
        for filters_item_data in _filters or []:
            filters_item = AdvancedFilter.from_dict(filters_item_data)

            filters.append(filters_item)

        _operator = d.pop("operator", UNSET)
        operator: Union[Unset, LogicalOperator]
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = LogicalOperator(_operator)

        logical_operator_filter = cls(
            type=type,
            filters=filters,
            operator=operator,
        )

        logical_operator_filter.additional_properties = d
        return logical_operator_filter

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
