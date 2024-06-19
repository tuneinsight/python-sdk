from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.statistical_quantity import StatisticalQuantity
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_ import Filter


T = TypeVar("T", bound="StatisticDefinition")


@attr.s(auto_attribs=True)
class StatisticDefinition:
    """
    Attributes:
        error_on_na_n (Union[Unset, bool]): whether to raise an error if a NaN value is present in the dataset for this
            variable.
        filter_ (Union[Unset, Filter]):
        name (Union[Unset, str]): given name of the statistic
        variable (Union[Unset, str]): target variable in the dataset from the which the statistic is computed
        max_bound (Union[Unset, float]): specified maximum bound on the variable for sorting Default: 1.0.
        min_bound (Union[Unset, float]): specified minimum bound on the variable for sorting
        quantiles_k_value (Union[Unset, int]): k value used to determine the number of quantiles that are returned
        quantities (Union[Unset, List[StatisticalQuantity]]): if specified only compute the quantities given in this
            list if not specified all relevant statistics are computed
    """

    error_on_na_n: Union[Unset, bool] = UNSET
    filter_: Union[Unset, "Filter"] = UNSET
    name: Union[Unset, str] = UNSET
    variable: Union[Unset, str] = UNSET
    max_bound: Union[Unset, float] = 1.0
    min_bound: Union[Unset, float] = 0.0
    quantiles_k_value: Union[Unset, int] = UNSET
    quantities: Union[Unset, List[StatisticalQuantity]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error_on_na_n = self.error_on_na_n
        filter_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        name = self.name
        variable = self.variable
        max_bound = self.max_bound
        min_bound = self.min_bound
        quantiles_k_value = self.quantiles_k_value
        quantities: Union[Unset, List[str]] = UNSET
        if not isinstance(self.quantities, Unset):
            quantities = []
            for quantities_item_data in self.quantities:
                quantities_item = quantities_item_data.value

                quantities.append(quantities_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_on_na_n is not UNSET:
            field_dict["errorOnNaN"] = error_on_na_n
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if name is not UNSET:
            field_dict["name"] = name
        if variable is not UNSET:
            field_dict["variable"] = variable
        if max_bound is not UNSET:
            field_dict["maxBound"] = max_bound
        if min_bound is not UNSET:
            field_dict["minBound"] = min_bound
        if quantiles_k_value is not UNSET:
            field_dict["quantilesKValue"] = quantiles_k_value
        if quantities is not UNSET:
            field_dict["quantities"] = quantities

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.filter_ import Filter

        d = src_dict.copy()
        error_on_na_n = d.pop("errorOnNaN", UNSET)

        _filter_ = d.pop("filter", UNSET)
        filter_: Union[Unset, Filter]
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = Filter.from_dict(_filter_)

        name = d.pop("name", UNSET)

        variable = d.pop("variable", UNSET)

        max_bound = d.pop("maxBound", UNSET)

        min_bound = d.pop("minBound", UNSET)

        quantiles_k_value = d.pop("quantilesKValue", UNSET)

        quantities = []
        _quantities = d.pop("quantities", UNSET)
        for quantities_item_data in _quantities or []:
            quantities_item = StatisticalQuantity(quantities_item_data)

            quantities.append(quantities_item)

        statistic_definition = cls(
            error_on_na_n=error_on_na_n,
            filter_=filter_,
            name=name,
            variable=variable,
            max_bound=max_bound,
            min_bound=min_bound,
            quantiles_k_value=quantiles_k_value,
            quantities=quantities,
        )

        statistic_definition.additional_properties = d
        return statistic_definition

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
