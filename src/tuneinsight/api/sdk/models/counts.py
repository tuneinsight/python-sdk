from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.preprocessing_operation_type import PreprocessingOperationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Counts")


@attr.s(auto_attribs=True)
class Counts:
    """
    Attributes:
        type (PreprocessingOperationType): type of preprocessing operation
        output_col (Union[Unset, str]): name of the column to store the counts. If not specified, the name 'count' will
            be used. Default: 'count'.
    """

    type: PreprocessingOperationType
    output_col: Union[Unset, str] = "count"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        output_col = self.output_col

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if output_col is not UNSET:
            field_dict["outputCol"] = output_col

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        output_col = d.pop("outputCol", UNSET)

        counts = cls(
            type=type,
            output_col=output_col,
        )

        counts.additional_properties = d
        return counts

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
