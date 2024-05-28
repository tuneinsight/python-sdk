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
        gt (Union[Unset, Any]): verifies that all values are greater than this value.
        isin (Union[Unset, List[Any]]):
        notin (Union[Unset, List[Any]]):
        ge (Union[Unset, Any]): verifies that all values are greater than or equal to this value.
        in_range (Union[Unset, ColumnSchemaChecksInRange]):
        le (Union[Unset, Any]): verifies that all values are less than or equal to this value.
        lt (Union[Unset, Any]): verifies that all values are less than this value.
        str_startswith (Union[Unset, str]):
        eq (Union[Unset, Any]): verifies that all values are equal to this value.
    """

    gt: Union[Unset, Any] = UNSET
    isin: Union[Unset, List[Any]] = UNSET
    notin: Union[Unset, List[Any]] = UNSET
    ge: Union[Unset, Any] = UNSET
    in_range: Union[Unset, "ColumnSchemaChecksInRange"] = UNSET
    le: Union[Unset, Any] = UNSET
    lt: Union[Unset, Any] = UNSET
    str_startswith: Union[Unset, str] = UNSET
    eq: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        gt = self.gt
        isin: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.isin, Unset):
            isin = self.isin

        notin: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.notin, Unset):
            notin = self.notin

        ge = self.ge
        in_range: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.in_range, Unset):
            in_range = self.in_range.to_dict()

        le = self.le
        lt = self.lt
        str_startswith = self.str_startswith
        eq = self.eq

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gt is not UNSET:
            field_dict["gt"] = gt
        if isin is not UNSET:
            field_dict["isin"] = isin
        if notin is not UNSET:
            field_dict["notin"] = notin
        if ge is not UNSET:
            field_dict["ge"] = ge
        if in_range is not UNSET:
            field_dict["in_range"] = in_range
        if le is not UNSET:
            field_dict["le"] = le
        if lt is not UNSET:
            field_dict["lt"] = lt
        if str_startswith is not UNSET:
            field_dict["str_startswith"] = str_startswith
        if eq is not UNSET:
            field_dict["eq"] = eq

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.column_schema_checks_in_range import ColumnSchemaChecksInRange

        d = src_dict.copy()
        gt = d.pop("gt", UNSET)

        isin = cast(List[Any], d.pop("isin", UNSET))

        notin = cast(List[Any], d.pop("notin", UNSET))

        ge = d.pop("ge", UNSET)

        _in_range = d.pop("in_range", UNSET)
        in_range: Union[Unset, ColumnSchemaChecksInRange]
        if isinstance(_in_range, Unset):
            in_range = UNSET
        else:
            in_range = ColumnSchemaChecksInRange.from_dict(_in_range)

        le = d.pop("le", UNSET)

        lt = d.pop("lt", UNSET)

        str_startswith = d.pop("str_startswith", UNSET)

        eq = d.pop("eq", UNSET)

        column_schema_checks = cls(
            gt=gt,
            isin=isin,
            notin=notin,
            ge=ge,
            in_range=in_range,
            le=le,
            lt=lt,
            str_startswith=str_startswith,
            eq=eq,
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
