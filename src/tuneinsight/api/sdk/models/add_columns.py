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
        input_columns (Union[Unset, List[str]]): the columns to add together
        numerical (Union[Unset, bool]): whether or not the added columns are numerical
        output_column (Union[Unset, str]): column to use as output
        sep (Union[Unset, str]): separator when the added columns are not numerical
    """

    type: PreprocessingOperationType
    input_columns: Union[Unset, List[str]] = UNSET
    numerical: Union[Unset, bool] = UNSET
    output_column: Union[Unset, str] = UNSET
    sep: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        input_columns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.input_columns, Unset):
            input_columns = self.input_columns

        numerical = self.numerical
        output_column = self.output_column
        sep = self.sep

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if input_columns is not UNSET:
            field_dict["inputColumns"] = input_columns
        if numerical is not UNSET:
            field_dict["numerical"] = numerical
        if output_column is not UNSET:
            field_dict["outputColumn"] = output_column
        if sep is not UNSET:
            field_dict["sep"] = sep

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        input_columns = cast(List[str], d.pop("inputColumns", UNSET))

        numerical = d.pop("numerical", UNSET)

        output_column = d.pop("outputColumn", UNSET)

        sep = d.pop("sep", UNSET)

        add_columns = cls(
            type=type,
            input_columns=input_columns,
            numerical=numerical,
            output_column=output_column,
            sep=sep,
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
