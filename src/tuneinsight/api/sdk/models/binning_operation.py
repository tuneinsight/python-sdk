from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.group_by_type import GroupByType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.categorical_column import CategoricalColumn


T = TypeVar("T", bound="BinningOperation")


@attr.s(auto_attribs=True)
class BinningOperation:
    """Dataset binning operation definition

    Attributes:
        count_columns (Union[Unset, List['CategoricalColumn']]): list of categorical on which to count the number of
            records per bin per matching value
        group_by_type (Union[Unset, GroupByType]): type of the groupBy operation specified
        range_values (Union[Unset, List[float]]): list of cuts to use when groupByType is 'range' ([x,y] => creating 3
            bins [v < x, x <= v < y, y <= v])
        target_column (Union[Unset, str]): column targeted by the binning operation
        aggregated_columns (Union[Unset, List[str]]): list of numerical columns to aggregate per bin when binning is
            done, if unspecified binning only counts the number of rows
        categories (Union[Unset, List[str]]): list of categories when groupByType is 'category'
    """

    count_columns: Union[Unset, List["CategoricalColumn"]] = UNSET
    group_by_type: Union[Unset, GroupByType] = UNSET
    range_values: Union[Unset, List[float]] = UNSET
    target_column: Union[Unset, str] = UNSET
    aggregated_columns: Union[Unset, List[str]] = UNSET
    categories: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count_columns: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.count_columns, Unset):
            count_columns = []
            for count_columns_item_data in self.count_columns:
                count_columns_item = count_columns_item_data.to_dict()

                count_columns.append(count_columns_item)

        group_by_type: Union[Unset, str] = UNSET
        if not isinstance(self.group_by_type, Unset):
            group_by_type = self.group_by_type.value

        range_values: Union[Unset, List[float]] = UNSET
        if not isinstance(self.range_values, Unset):
            range_values = self.range_values

        target_column = self.target_column
        aggregated_columns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.aggregated_columns, Unset):
            aggregated_columns = self.aggregated_columns

        categories: Union[Unset, List[str]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count_columns is not UNSET:
            field_dict["countColumns"] = count_columns
        if group_by_type is not UNSET:
            field_dict["groupByType"] = group_by_type
        if range_values is not UNSET:
            field_dict["rangeValues"] = range_values
        if target_column is not UNSET:
            field_dict["targetColumn"] = target_column
        if aggregated_columns is not UNSET:
            field_dict["aggregatedColumns"] = aggregated_columns
        if categories is not UNSET:
            field_dict["categories"] = categories

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.categorical_column import CategoricalColumn

        d = src_dict.copy()
        count_columns = []
        _count_columns = d.pop("countColumns", UNSET)
        for count_columns_item_data in _count_columns or []:
            count_columns_item = CategoricalColumn.from_dict(count_columns_item_data)

            count_columns.append(count_columns_item)

        _group_by_type = d.pop("groupByType", UNSET)
        group_by_type: Union[Unset, GroupByType]
        if isinstance(_group_by_type, Unset):
            group_by_type = UNSET
        else:
            group_by_type = GroupByType(_group_by_type)

        range_values = cast(List[float], d.pop("rangeValues", UNSET))

        target_column = d.pop("targetColumn", UNSET)

        aggregated_columns = cast(List[str], d.pop("aggregatedColumns", UNSET))

        categories = cast(List[str], d.pop("categories", UNSET))

        binning_operation = cls(
            count_columns=count_columns,
            group_by_type=group_by_type,
            range_values=range_values,
            target_column=target_column,
            aggregated_columns=aggregated_columns,
            categories=categories,
        )

        binning_operation.additional_properties = d
        return binning_operation

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
