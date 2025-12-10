from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.preprocessing_operation_type import PreprocessingOperationType

T = TypeVar("T", bound="ComputeTimeSince")


@attr.s(auto_attribs=True)
class ComputeTimeSince:
    """
    Attributes:
        type (PreprocessingOperationType): type of preprocessing operation
        date_column (str): the name of the column containing the date (or date from which the time since is computed).
        output_column (str): the column where to save the time since in years (an integer).
    """

    type: PreprocessingOperationType
    date_column: str
    output_column: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        date_column = self.date_column
        output_column = self.output_column

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "dateColumn": date_column,
                "outputColumn": output_column,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        date_column = d.pop("dateColumn")

        output_column = d.pop("outputColumn")

        compute_time_since = cls(
            type=type,
            date_column=date_column,
            output_column=output_column,
        )

        compute_time_since.additional_properties = d
        return compute_time_since

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
