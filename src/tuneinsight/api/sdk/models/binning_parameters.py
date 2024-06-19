from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.binning_parameters_method import BinningParametersMethod
from ..types import UNSET, Unset

T = TypeVar("T", bound="BinningParameters")


@attr.s(auto_attribs=True)
class BinningParameters:
    """parameters used to bin data

    Attributes:
        bin_size (Union[Unset, float]): size of bins
        bin_size_precision (Union[Unset, None, int]): number of decimals for generated range categories
        categories (Union[Unset, List[str]]): specified categories when method is specifiedCategories
        default_category (Union[Unset, str]): category to assign when an item does not fall in a specific category
            Default: 'other'.
        method (Union[Unset, BinningParametersMethod]): describes whether binning is done automatically or by specified
            values. Possible values: - "automatic" binning is done directly on the existing values, for all possible values
            found, a category is created - "rangeBins" binning is done according to provided range parameters -
            "specifiedCategories" binning is done on specified categories, values that do not fall in provided categories
            are tagged as 'other'
    """

    bin_size: Union[Unset, float] = UNSET
    bin_size_precision: Union[Unset, None, int] = 0
    categories: Union[Unset, List[str]] = UNSET
    default_category: Union[Unset, str] = "other"
    method: Union[Unset, BinningParametersMethod] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bin_size = self.bin_size
        bin_size_precision = self.bin_size_precision
        categories: Union[Unset, List[str]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories

        default_category = self.default_category
        method: Union[Unset, str] = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bin_size is not UNSET:
            field_dict["binSize"] = bin_size
        if bin_size_precision is not UNSET:
            field_dict["binSizePrecision"] = bin_size_precision
        if categories is not UNSET:
            field_dict["categories"] = categories
        if default_category is not UNSET:
            field_dict["defaultCategory"] = default_category
        if method is not UNSET:
            field_dict["method"] = method

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        bin_size = d.pop("binSize", UNSET)

        bin_size_precision = d.pop("binSizePrecision", UNSET)

        categories = cast(List[str], d.pop("categories", UNSET))

        default_category = d.pop("defaultCategory", UNSET)

        _method = d.pop("method", UNSET)
        method: Union[Unset, BinningParametersMethod]
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = BinningParametersMethod(_method)

        binning_parameters = cls(
            bin_size=bin_size,
            bin_size_precision=bin_size_precision,
            categories=categories,
            default_category=default_category,
            method=method,
        )

        binning_parameters.additional_properties = d
        return binning_parameters

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
