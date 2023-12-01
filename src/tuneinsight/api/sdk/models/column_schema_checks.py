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
        lt (Union[Unset, Any]): verifies that all values are less than this value.
        str_startswith (Union[Unset, str]):
        gt (Union[Unset, Any]): verifies that all values are greater than this value.
        le (Union[Unset, Any]): verifies that all values are less than or equal to this value.
        in_range (Union[Unset, ColumnSchemaChecksInRange]):
        isin (Union[Unset, List[Any]]):
        notin (Union[Unset, List[Any]]):
        eq (Union[Unset, Any]): verifies that all values are equal to this value.
        ge (Union[Unset, Any]): verifies that all values are greater than or equal to this value.
    """

    lt: Union[Unset, Any] = UNSET
    str_startswith: Union[Unset, str] = UNSET
    gt: Union[Unset, Any] = UNSET
    le: Union[Unset, Any] = UNSET
    in_range: Union[Unset, "ColumnSchemaChecksInRange"] = UNSET
    isin: Union[Unset, List[Any]] = UNSET
    notin: Union[Unset, List[Any]] = UNSET
    eq: Union[Unset, Any] = UNSET
    ge: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        lt = self.lt
        str_startswith = self.str_startswith
        gt = self.gt
        le = self.le
        in_range: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.in_range, Unset):
            in_range = self.in_range.to_dict()

        isin: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.isin, Unset):
            isin = self.isin

        notin: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.notin, Unset):
            notin = self.notin

        eq = self.eq
        ge = self.ge

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lt is not UNSET:
            field_dict["lt"] = lt
        if str_startswith is not UNSET:
            field_dict["str_startswith"] = str_startswith
        if gt is not UNSET:
            field_dict["gt"] = gt
        if le is not UNSET:
            field_dict["le"] = le
        if in_range is not UNSET:
            field_dict["in_range"] = in_range
        if isin is not UNSET:
            field_dict["isin"] = isin
        if notin is not UNSET:
            field_dict["notin"] = notin
        if eq is not UNSET:
            field_dict["eq"] = eq
        if ge is not UNSET:
            field_dict["ge"] = ge

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.column_schema_checks_in_range import ColumnSchemaChecksInRange

        d = src_dict.copy()
        lt = d.pop("lt", UNSET)

        str_startswith = d.pop("str_startswith", UNSET)

        gt = d.pop("gt", UNSET)

        le = d.pop("le", UNSET)

        _in_range = d.pop("in_range", UNSET)
        in_range: Union[Unset, ColumnSchemaChecksInRange]
        if isinstance(_in_range, Unset):
            in_range = UNSET
        else:
            in_range = ColumnSchemaChecksInRange.from_dict(_in_range)

        isin = cast(List[Any], d.pop("isin", UNSET))

        notin = cast(List[Any], d.pop("notin", UNSET))

        eq = d.pop("eq", UNSET)

        ge = d.pop("ge", UNSET)

        column_schema_checks = cls(
            lt=lt,
            str_startswith=str_startswith,
            gt=gt,
            le=le,
            in_range=in_range,
            isin=isin,
            notin=notin,
            eq=eq,
            ge=ge,
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
