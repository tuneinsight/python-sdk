from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.logical_operator import LogicalOperator
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_ import Filter


T = TypeVar("T", bound="LogicalFormula")


@attr.s(auto_attribs=True)
class LogicalFormula:
    """logical formula composing filters

    Attributes:
        left_formula (Union[Unset, LogicalFormula]): logical formula composing filters
        operator (Union[Unset, LogicalOperator]): A logical operator to "aggregate" multiple boolean values.
        right_formula (Union[Unset, LogicalFormula]): logical formula composing filters
        single_filter (Union[Unset, Filter]):
    """

    left_formula: Union[Unset, "LogicalFormula"] = UNSET
    operator: Union[Unset, LogicalOperator] = UNSET
    right_formula: Union[Unset, "LogicalFormula"] = UNSET
    single_filter: Union[Unset, "Filter"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        left_formula: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.left_formula, Unset):
            left_formula = self.left_formula.to_dict()

        operator: Union[Unset, str] = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.value

        right_formula: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.right_formula, Unset):
            right_formula = self.right_formula.to_dict()

        single_filter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.single_filter, Unset):
            single_filter = self.single_filter.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if left_formula is not UNSET:
            field_dict["leftFormula"] = left_formula
        if operator is not UNSET:
            field_dict["operator"] = operator
        if right_formula is not UNSET:
            field_dict["rightFormula"] = right_formula
        if single_filter is not UNSET:
            field_dict["singleFilter"] = single_filter

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.filter_ import Filter

        d = src_dict.copy()
        _left_formula = d.pop("leftFormula", UNSET)
        left_formula: Union[Unset, LogicalFormula]
        if isinstance(_left_formula, Unset):
            left_formula = UNSET
        else:
            left_formula = LogicalFormula.from_dict(_left_formula)

        _operator = d.pop("operator", UNSET)
        operator: Union[Unset, LogicalOperator]
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = LogicalOperator(_operator)

        _right_formula = d.pop("rightFormula", UNSET)
        right_formula: Union[Unset, LogicalFormula]
        if isinstance(_right_formula, Unset):
            right_formula = UNSET
        else:
            right_formula = LogicalFormula.from_dict(_right_formula)

        _single_filter = d.pop("singleFilter", UNSET)
        single_filter: Union[Unset, Filter]
        if isinstance(_single_filter, Unset):
            single_filter = UNSET
        else:
            single_filter = Filter.from_dict(_single_filter)

        logical_formula = cls(
            left_formula=left_formula,
            operator=operator,
            right_formula=right_formula,
            single_filter=single_filter,
        )

        logical_formula.additional_properties = d
        return logical_formula

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
