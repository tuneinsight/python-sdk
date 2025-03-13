from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupingParameters")


@attr.s(auto_attribs=True)
class GroupingParameters:
    """provides flexible settings to define a grouping operation on the records.

    Attributes:
        bin_center (Union[Unset, float]): center around which the numerical bins are created. For example, if binSize=10
            and center=5,
            the bins will correspond to ..., [-15,-5), [-5,5), [5,15), ...
            This is ignored if either binMin or binMax is provided.
        bin_max (Union[Unset, None, float]): Upper bound on the data, and right bound of the last bin.
        bin_min (Union[Unset, None, float]): Lower bound on the data, and left bound of the first bin.
        bin_size (Union[Unset, float]): size of the bins.
        column (Union[Unset, str]): column from which the groups are created.
        cuts (Union[Unset, List[float]]): array of cuts to define variable-sized numerical bins. Each value defines the
            min and max bounds for the bins.
            For example: cuts = [-10,5,50] will create the following bins (,-10),[-10,5),[5,50),[50,).
        default_group (Union[Unset, str]): the default group to use for records that were not assigned a group.
        integer_bin_bounds (Union[Unset, bool]): whether integer bounds should be used for the numerical bins (only
            changes the bin labels, not binning procedure)
        numeric (Union[Unset, bool]): explicitly specifies the grouping to be done on numerical bins.
        possible_values (Union[Unset, List[str]]): list of accepted values for groups. if a record is not classified in
            this list, it is discarded unless a default group value is provided.
        strict (Union[Unset, bool]): if true, and `cuts` or `possibleValues` is used to define the groups, the returned
            values will only include
            the groups define inside the cuts (no "< min" or "> max" groups) or the possible values (no default group
            included).
    """

    bin_center: Union[Unset, float] = UNSET
    bin_max: Union[Unset, None, float] = UNSET
    bin_min: Union[Unset, None, float] = UNSET
    bin_size: Union[Unset, float] = UNSET
    column: Union[Unset, str] = UNSET
    cuts: Union[Unset, List[float]] = UNSET
    default_group: Union[Unset, str] = UNSET
    integer_bin_bounds: Union[Unset, bool] = UNSET
    numeric: Union[Unset, bool] = UNSET
    possible_values: Union[Unset, List[str]] = UNSET
    strict: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bin_center = self.bin_center
        bin_max = self.bin_max
        bin_min = self.bin_min
        bin_size = self.bin_size
        column = self.column
        cuts: Union[Unset, List[float]] = UNSET
        if not isinstance(self.cuts, Unset):
            cuts = self.cuts

        default_group = self.default_group
        integer_bin_bounds = self.integer_bin_bounds
        numeric = self.numeric
        possible_values: Union[Unset, List[str]] = UNSET
        if not isinstance(self.possible_values, Unset):
            possible_values = self.possible_values

        strict = self.strict

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bin_center is not UNSET:
            field_dict["binCenter"] = bin_center
        if bin_max is not UNSET:
            field_dict["binMax"] = bin_max
        if bin_min is not UNSET:
            field_dict["binMin"] = bin_min
        if bin_size is not UNSET:
            field_dict["binSize"] = bin_size
        if column is not UNSET:
            field_dict["column"] = column
        if cuts is not UNSET:
            field_dict["cuts"] = cuts
        if default_group is not UNSET:
            field_dict["defaultGroup"] = default_group
        if integer_bin_bounds is not UNSET:
            field_dict["integerBinBounds"] = integer_bin_bounds
        if numeric is not UNSET:
            field_dict["numeric"] = numeric
        if possible_values is not UNSET:
            field_dict["possibleValues"] = possible_values
        if strict is not UNSET:
            field_dict["strict"] = strict

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        bin_center = d.pop("binCenter", UNSET)

        bin_max = d.pop("binMax", UNSET)

        bin_min = d.pop("binMin", UNSET)

        bin_size = d.pop("binSize", UNSET)

        column = d.pop("column", UNSET)

        cuts = cast(List[float], d.pop("cuts", UNSET))

        default_group = d.pop("defaultGroup", UNSET)

        integer_bin_bounds = d.pop("integerBinBounds", UNSET)

        numeric = d.pop("numeric", UNSET)

        possible_values = cast(List[str], d.pop("possibleValues", UNSET))

        strict = d.pop("strict", UNSET)

        grouping_parameters = cls(
            bin_center=bin_center,
            bin_max=bin_max,
            bin_min=bin_min,
            bin_size=bin_size,
            column=column,
            cuts=cuts,
            default_group=default_group,
            integer_bin_bounds=integer_bin_bounds,
            numeric=numeric,
            possible_values=possible_values,
            strict=strict,
        )

        grouping_parameters.additional_properties = d
        return grouping_parameters

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
