from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.preprocessing_operation_type import PreprocessingOperationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AddColumns")


@attr.s(auto_attribs=True)
class AddColumns:
    """
    Attributes:
        type (PreprocessingOperationType): type of preprocessing operation
        sep (Union[Unset, str]): separator when the added columns are not numerical
        input_columns (Union[Unset, List[str]]): the columns to add together
        numerical (Union[Unset, bool]): whether or not the output columns are numerical
        output (Union[Unset, str]): column to use as output
    """

    type: PreprocessingOperationType
    sep: Union[Unset, str] = UNSET
    input_columns: Union[Unset, List[str]] = UNSET
    numerical: Union[Unset, bool] = UNSET
    output: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        sep = self.sep
        input_columns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.input_columns, Unset):
            input_columns = self.input_columns

        numerical = self.numerical
        output = self.output

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if sep is not UNSET:
            field_dict["sep"] = sep
        if input_columns is not UNSET:
            field_dict["inputColumns"] = input_columns
        if numerical is not UNSET:
            field_dict["numerical"] = numerical
        if output is not UNSET:
            field_dict["output"] = output

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        sep = d.pop("sep", UNSET)

        input_columns = cast(List[str], d.pop("inputColumns", UNSET))

        numerical = d.pop("numerical", UNSET)

        output = d.pop("output", UNSET)

        add_columns = cls(
            type=type,
            sep=sep,
            input_columns=input_columns,
            numerical=numerical,
            output=output,
        )

        add_columns.additional_properties = d
        return add_columns

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
