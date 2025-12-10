from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.fill_na_method import FillNAMethod
from ..models.preprocessing_operation_type import PreprocessingOperationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FillNA")


@attr.s(auto_attribs=True)
class FillNA:
    """
    Attributes:
        type (PreprocessingOperationType): type of preprocessing operation
        columns (Union[Unset, List[str]]): the columns where the missing values must be filled in. If not provided, all
            columns are used.
        method (Union[Unset, None, FillNAMethod]): the method to fill in missing values. This can be:
             - value: a static value is used to fill in all missing entries.
             - local-mean/local-median: the mean or median of each column is computed locally and used as value (numerical
            only).
             - local-mode: the most frequent value of each column is computed locally and used as value. In case of a tie,
            the lowest value (numerical or alphabetical) is used.
             - ffill/bfill: the column is forward- or backward-filled, using the previous or next non-empty value (see
            pandas.DataFrame.fillna for details).
             - interpolate: the missing values in the column are interpolated (using
            pandas.DataFrame.interpolate(method="linear")) (numerical only).
        value (Union[Unset, None, str]): the value to use to replace missing values if method==value.
    """

    type: PreprocessingOperationType
    columns: Union[Unset, List[str]] = UNSET
    method: Union[Unset, None, FillNAMethod] = UNSET
    value: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        columns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.columns, Unset):
            columns = self.columns

        method: Union[Unset, None, str] = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value if self.method else None

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if columns is not UNSET:
            field_dict["columns"] = columns
        if method is not UNSET:
            field_dict["method"] = method
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        columns = cast(List[str], d.pop("columns", UNSET))

        _method = d.pop("method", UNSET)
        method: Union[Unset, None, FillNAMethod]
        if _method is None:
            method = None
        elif isinstance(_method, Unset):
            method = UNSET
        else:
            method = FillNAMethod(_method)

        value = d.pop("value", UNSET)

        fill_na = cls(
            type=type,
            columns=columns,
            method=method,
            value=value,
        )

        fill_na.additional_properties = d
        return fill_na

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
