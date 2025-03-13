from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.comparison_type import ComparisonType
from ..models.preprocessing_operation_type import PreprocessingOperationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Filter")


@attr.s(auto_attribs=True)
class Filter:
    """
    Attributes:
        type (PreprocessingOperationType): type of preprocessing operation
        column (str): name of column to filter on
        value (str): value with which to compare
        comparator (Union[Unset, ComparisonType]): type of comparison
        numerical (Union[Unset, bool]): If true, data entries are converted to numerical values before doing the
            comparison.
        output_column (Union[Unset, str]): If provided, the data is not filtered, and instead a column is created with
            the filter values (true or false).
        value_metadata (Union[Unset, str]): metadata of the value (e.g. JSON for autocomplete)
        values (Union[Unset, List[str]]): list of values to pass in when the comparator is 'isin' (ignored otherwise)
    """

    type: PreprocessingOperationType
    column: str
    value: str
    comparator: Union[Unset, ComparisonType] = UNSET
    numerical: Union[Unset, bool] = UNSET
    output_column: Union[Unset, str] = UNSET
    value_metadata: Union[Unset, str] = UNSET
    values: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        column = self.column
        value = self.value
        comparator: Union[Unset, str] = UNSET
        if not isinstance(self.comparator, Unset):
            comparator = self.comparator.value

        numerical = self.numerical
        output_column = self.output_column
        value_metadata = self.value_metadata
        values: Union[Unset, List[str]] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "column": column,
                "value": value,
            }
        )
        if comparator is not UNSET:
            field_dict["comparator"] = comparator
        if numerical is not UNSET:
            field_dict["numerical"] = numerical
        if output_column is not UNSET:
            field_dict["outputColumn"] = output_column
        if value_metadata is not UNSET:
            field_dict["valueMetadata"] = value_metadata
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        column = d.pop("column")

        value = d.pop("value")

        _comparator = d.pop("comparator", UNSET)
        comparator: Union[Unset, ComparisonType]
        if isinstance(_comparator, Unset):
            comparator = UNSET
        else:
            comparator = ComparisonType(_comparator)

        numerical = d.pop("numerical", UNSET)

        output_column = d.pop("outputColumn", UNSET)

        value_metadata = d.pop("valueMetadata", UNSET)

        values = cast(List[str], d.pop("values", UNSET))

        filter_ = cls(
            type=type,
            column=column,
            value=value,
            comparator=comparator,
            numerical=numerical,
            output_column=output_column,
            value_metadata=value_metadata,
            values=values,
        )

        filter_.additional_properties = d
        return filter_

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
