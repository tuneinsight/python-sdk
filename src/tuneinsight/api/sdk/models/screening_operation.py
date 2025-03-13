from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScreeningOperation")


@attr.s(auto_attribs=True)
class ScreeningOperation:
    """operation used to screen data.

    Attributes:
        auto_correct_dates (Union[Unset, bool]): when set to true, this operation will try to automatically detect the
            most common date format in the column
            and convert any other date in a different format.
        columns (Union[Unset, List[str]]): columns of the dataset on which this operation applies to.
        description (Union[Unset, str]): description given to the operation.
        enabled (Union[Unset, bool]): whether this operation will execute or not.
        filter_invalid_dates (Union[Unset, bool]): when set to true, any dates for which the format cannot be detected
            will be filtered out.
        name (Union[Unset, str]): name given to the operation.
        non_empty (Union[Unset, bool]): when set to true, then this operation filters any columns/rows that contain
            empty values.
        numeric (Union[Unset, bool]): when set to true, then this operation filters any values in the selected column
            that contain values
            that are not numeric.
        outlier_threshold (Union[Unset, None, float]): when `filterOutlier` is set to true, this threshold is used to
            determine by how much,
            in terms of standard deviations (threshold * STD)
            the numeric values are allowed to deviate from the mean of the data, to be considered as non-outliers.
        remove (Union[Unset, bool]): when set to true, then this operation removes the selected rows.
        replace_with (Union[Unset, None, str]): When specified alone, then all data from selected columns and rows is
            replaced with this value.
            If specified along with another validator operations (nonEmpty, numeric, etc), then any values
            that are invalidated by the operation are replaced with this value.
        rows (Union[Unset, List[int]]): row indices of the dataset on which this operation applies to.
        warnings (Union[Unset, List[str]]): warning returned by the backend if the operation is invalid with the current
            data.
    """

    auto_correct_dates: Union[Unset, bool] = UNSET
    columns: Union[Unset, List[str]] = UNSET
    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    filter_invalid_dates: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    non_empty: Union[Unset, bool] = UNSET
    numeric: Union[Unset, bool] = UNSET
    outlier_threshold: Union[Unset, None, float] = UNSET
    remove: Union[Unset, bool] = UNSET
    replace_with: Union[Unset, None, str] = UNSET
    rows: Union[Unset, List[int]] = UNSET
    warnings: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        auto_correct_dates = self.auto_correct_dates
        columns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.columns, Unset):
            columns = self.columns

        description = self.description
        enabled = self.enabled
        filter_invalid_dates = self.filter_invalid_dates
        name = self.name
        non_empty = self.non_empty
        numeric = self.numeric
        outlier_threshold = self.outlier_threshold
        remove = self.remove
        replace_with = self.replace_with
        rows: Union[Unset, List[int]] = UNSET
        if not isinstance(self.rows, Unset):
            rows = self.rows

        warnings: Union[Unset, List[str]] = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_correct_dates is not UNSET:
            field_dict["autoCorrectDates"] = auto_correct_dates
        if columns is not UNSET:
            field_dict["columns"] = columns
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if filter_invalid_dates is not UNSET:
            field_dict["filterInvalidDates"] = filter_invalid_dates
        if name is not UNSET:
            field_dict["name"] = name
        if non_empty is not UNSET:
            field_dict["nonEmpty"] = non_empty
        if numeric is not UNSET:
            field_dict["numeric"] = numeric
        if outlier_threshold is not UNSET:
            field_dict["outlierThreshold"] = outlier_threshold
        if remove is not UNSET:
            field_dict["remove"] = remove
        if replace_with is not UNSET:
            field_dict["replaceWith"] = replace_with
        if rows is not UNSET:
            field_dict["rows"] = rows
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        auto_correct_dates = d.pop("autoCorrectDates", UNSET)

        columns = cast(List[str], d.pop("columns", UNSET))

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        filter_invalid_dates = d.pop("filterInvalidDates", UNSET)

        name = d.pop("name", UNSET)

        non_empty = d.pop("nonEmpty", UNSET)

        numeric = d.pop("numeric", UNSET)

        outlier_threshold = d.pop("outlierThreshold", UNSET)

        remove = d.pop("remove", UNSET)

        replace_with = d.pop("replaceWith", UNSET)

        rows = cast(List[int], d.pop("rows", UNSET))

        warnings = cast(List[str], d.pop("warnings", UNSET))

        screening_operation = cls(
            auto_correct_dates=auto_correct_dates,
            columns=columns,
            description=description,
            enabled=enabled,
            filter_invalid_dates=filter_invalid_dates,
            name=name,
            non_empty=non_empty,
            numeric=numeric,
            outlier_threshold=outlier_threshold,
            remove=remove,
            replace_with=replace_with,
            rows=rows,
            warnings=warnings,
        )

        screening_operation.additional_properties = d
        return screening_operation

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
