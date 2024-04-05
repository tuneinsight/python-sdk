from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.column_schema_checks_in_range import ColumnSchemaChecksInRange


T = TypeVar("T", bound="ColumnSchemaChecks")


@attr.s(auto_attribs=True)
class ColumnSchemaChecks:
    """optional additional checks

    Attributes:
        eq (Union[Unset, Any]): verifies that all values are equal to this value.
        gt (Union[Unset, Any]): verifies that all values are greater than this value.
        in_range (Union[Unset, ColumnSchemaChecksInRange]):
        lt (Union[Unset, Any]): verifies that all values are less than this value.
        str_startswith (Union[Unset, str]):
        ge (Union[Unset, Any]): verifies that all values are greater than or equal to this value.
        isin (Union[Unset, List[Any]]):
        le (Union[Unset, Any]): verifies that all values are less than or equal to this value.
        notin (Union[Unset, List[Any]]):
    """

    eq: Union[Unset, Any] = UNSET
    gt: Union[Unset, Any] = UNSET
    in_range: Union[Unset, "ColumnSchemaChecksInRange"] = UNSET
    lt: Union[Unset, Any] = UNSET
    str_startswith: Union[Unset, str] = UNSET
    ge: Union[Unset, Any] = UNSET
    isin: Union[Unset, List[Any]] = UNSET
    le: Union[Unset, Any] = UNSET
    notin: Union[Unset, List[Any]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        eq = self.eq
        gt = self.gt
        in_range: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.in_range, Unset):
            in_range = self.in_range.to_dict()

        lt = self.lt
        str_startswith = self.str_startswith
        ge = self.ge
        isin: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.isin, Unset):
            isin = self.isin

        le = self.le
        notin: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.notin, Unset):
            notin = self.notin

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if eq is not UNSET:
            field_dict["eq"] = eq
        if gt is not UNSET:
            field_dict["gt"] = gt
        if in_range is not UNSET:
            field_dict["in_range"] = in_range
        if lt is not UNSET:
            field_dict["lt"] = lt
        if str_startswith is not UNSET:
            field_dict["str_startswith"] = str_startswith
        if ge is not UNSET:
            field_dict["ge"] = ge
        if isin is not UNSET:
            field_dict["isin"] = isin
        if le is not UNSET:
            field_dict["le"] = le
        if notin is not UNSET:
            field_dict["notin"] = notin

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.column_schema_checks_in_range import ColumnSchemaChecksInRange

        d = src_dict.copy()
        eq = d.pop("eq", UNSET)

        gt = d.pop("gt", UNSET)

        _in_range = d.pop("in_range", UNSET)
        in_range: Union[Unset, ColumnSchemaChecksInRange]
        if isinstance(_in_range, Unset):
            in_range = UNSET
        else:
            in_range = ColumnSchemaChecksInRange.from_dict(_in_range)

        lt = d.pop("lt", UNSET)

        str_startswith = d.pop("str_startswith", UNSET)

        ge = d.pop("ge", UNSET)

        isin = cast(List[Any], d.pop("isin", UNSET))

        le = d.pop("le", UNSET)

        notin = cast(List[Any], d.pop("notin", UNSET))

        column_schema_checks = cls(
            eq=eq,
            gt=gt,
            in_range=in_range,
            lt=lt,
            str_startswith=str_startswith,
            ge=ge,
            isin=isin,
            le=le,
            notin=notin,
        )

        column_schema_checks.additional_properties = d
        return column_schema_checks

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
