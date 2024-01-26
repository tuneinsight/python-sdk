from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_ import Filter


T = TypeVar("T", bound="StatisticResult")


@attr.s(auto_attribs=True)
class StatisticResult:
    """
    Attributes:
        filter_ (Union[Unset, Filter]):
        name (Union[Unset, str]): given name of the statistic
        variable (Union[Unset, str]): target variable in the dataset from the which the statistic is computed
        min_ (Union[Unset, None, float]):
        quantiles (Union[Unset, List[float]]):
        variance (Union[Unset, None, float]):
        iqr (Union[Unset, None, float]):
        max_ (Union[Unset, None, float]):
        mean (Union[Unset, None, float]):
        median (Union[Unset, None, float]):
    """

    filter_: Union[Unset, "Filter"] = UNSET
    name: Union[Unset, str] = UNSET
    variable: Union[Unset, str] = UNSET
    min_: Union[Unset, None, float] = UNSET
    quantiles: Union[Unset, List[float]] = UNSET
    variance: Union[Unset, None, float] = UNSET
    iqr: Union[Unset, None, float] = UNSET
    max_: Union[Unset, None, float] = UNSET
    mean: Union[Unset, None, float] = UNSET
    median: Union[Unset, None, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        filter_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        name = self.name
        variable = self.variable
        min_ = self.min_
        quantiles: Union[Unset, List[float]] = UNSET
        if not isinstance(self.quantiles, Unset):
            quantiles = self.quantiles

        variance = self.variance
        iqr = self.iqr
        max_ = self.max_
        mean = self.mean
        median = self.median

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if name is not UNSET:
            field_dict["name"] = name
        if variable is not UNSET:
            field_dict["variable"] = variable
        if min_ is not UNSET:
            field_dict["min"] = min_
        if quantiles is not UNSET:
            field_dict["quantiles"] = quantiles
        if variance is not UNSET:
            field_dict["variance"] = variance
        if iqr is not UNSET:
            field_dict["IQR"] = iqr
        if max_ is not UNSET:
            field_dict["max"] = max_
        if mean is not UNSET:
            field_dict["mean"] = mean
        if median is not UNSET:
            field_dict["median"] = median

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.filter_ import Filter

        d = src_dict.copy()
        _filter_ = d.pop("filter", UNSET)
        filter_: Union[Unset, Filter]
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = Filter.from_dict(_filter_)

        name = d.pop("name", UNSET)

        variable = d.pop("variable", UNSET)

        min_ = d.pop("min", UNSET)

        quantiles = cast(List[float], d.pop("quantiles", UNSET))

        variance = d.pop("variance", UNSET)

        iqr = d.pop("IQR", UNSET)

        max_ = d.pop("max", UNSET)

        mean = d.pop("mean", UNSET)

        median = d.pop("median", UNSET)

        statistic_result = cls(
            filter_=filter_,
            name=name,
            variable=variable,
            min_=min_,
            quantiles=quantiles,
            variance=variance,
            iqr=iqr,
            max_=max_,
            mean=mean,
            median=median,
        )

        statistic_result.additional_properties = d
        return statistic_result

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
