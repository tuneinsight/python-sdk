from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.preprocessing_operation_type import PreprocessingOperationType

T = TypeVar("T", bound="ComputeBMI")


@attr.s(auto_attribs=True)
class ComputeBMI:
    """
    Attributes:
        type (PreprocessingOperationType): type of preprocessing operation
        height_column (str): the name of the column containing heights in m
        output_column (str): column to use as output
        weight_column (str): the name of the column containing weights in kg
    """

    type: PreprocessingOperationType
    height_column: str
    output_column: str
    weight_column: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        height_column = self.height_column
        output_column = self.output_column
        weight_column = self.weight_column

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "heightColumn": height_column,
                "outputColumn": output_column,
                "weightColumn": weight_column,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        height_column = d.pop("heightColumn")

        output_column = d.pop("outputColumn")

        weight_column = d.pop("weightColumn")

        compute_bmi = cls(
            type=type,
            height_column=height_column,
            output_column=output_column,
            weight_column=weight_column,
        )

        compute_bmi.additional_properties = d
        return compute_bmi

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
