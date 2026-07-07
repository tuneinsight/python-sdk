from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.preprocessing_operation_type import PreprocessingOperationType

T = TypeVar("T", bound="DivideColumns")


@attr.s(auto_attribs=True)
class DivideColumns:
    """
    Attributes:
        type (PreprocessingOperationType): type of preprocessing operation
        denominator_column (str): the name of the column to use as denominator.
        numerator_column (str): the name of the column to use as numerator.
        output_column (str): column to use as output
    """

    type: PreprocessingOperationType
    denominator_column: str
    numerator_column: str
    output_column: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        denominator_column = self.denominator_column
        numerator_column = self.numerator_column
        output_column = self.output_column

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "denominatorColumn": denominator_column,
                "numeratorColumn": numerator_column,
                "outputColumn": output_column,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        denominator_column = d.pop("denominatorColumn")

        numerator_column = d.pop("numeratorColumn")

        output_column = d.pop("outputColumn")

        divide_columns = cls(
            type=type,
            denominator_column=denominator_column,
            numerator_column=numerator_column,
            output_column=output_column,
        )

        divide_columns.additional_properties = d
        return divide_columns

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
