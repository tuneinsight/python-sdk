from typing import Any, Dict, List, Type, TypeVar, cast

import attr

from ..models.preprocessing_operation_type import PreprocessingOperationType

T = TypeVar("T", bound="MultiplyColumns")


@attr.s(auto_attribs=True)
class MultiplyColumns:
    """
    Attributes:
        type (PreprocessingOperationType): type of preprocessing operation
        input_columns (List[str]): the names of columns to multiply together
        output_column (str): column to use as output
    """

    type: PreprocessingOperationType
    input_columns: List[str]
    output_column: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        input_columns = self.input_columns

        output_column = self.output_column

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "inputColumns": input_columns,
                "outputColumn": output_column,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        input_columns = cast(List[str], d.pop("inputColumns"))

        output_column = d.pop("outputColumn")

        multiply_columns = cls(
            type=type,
            input_columns=input_columns,
            output_column=output_column,
        )

        multiply_columns.additional_properties = d
        return multiply_columns

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
