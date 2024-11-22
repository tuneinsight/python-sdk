from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.apply_reg_ex_regex_type import ApplyRegExRegexType
from ..models.preprocessing_operation_type import PreprocessingOperationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApplyRegEx")


@attr.s(auto_attribs=True)
class ApplyRegEx:
    """
    Attributes:
        type (PreprocessingOperationType): type of preprocessing operation
        regex (str): Regular expression to apply
        input_columns (Union[Unset, List[str]]): Columns to which the RegEx is applied
        output_columns (Union[Unset, List[str]]): If specified, names of the newly created columns (if not, no new
            columns are created, and the operation is in place).
        regex_type (Union[Unset, ApplyRegExRegexType]): Defines what is extracted from the regex (if not specified,
            match is used as default).
    """

    type: PreprocessingOperationType
    regex: str
    input_columns: Union[Unset, List[str]] = UNSET
    output_columns: Union[Unset, List[str]] = UNSET
    regex_type: Union[Unset, ApplyRegExRegexType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        regex = self.regex
        input_columns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.input_columns, Unset):
            input_columns = self.input_columns

        output_columns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.output_columns, Unset):
            output_columns = self.output_columns

        regex_type: Union[Unset, str] = UNSET
        if not isinstance(self.regex_type, Unset):
            regex_type = self.regex_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "regex": regex,
            }
        )
        if input_columns is not UNSET:
            field_dict["inputColumns"] = input_columns
        if output_columns is not UNSET:
            field_dict["outputColumns"] = output_columns
        if regex_type is not UNSET:
            field_dict["regexType"] = regex_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        regex = d.pop("regex")

        input_columns = cast(List[str], d.pop("inputColumns", UNSET))

        output_columns = cast(List[str], d.pop("outputColumns", UNSET))

        _regex_type = d.pop("regexType", UNSET)
        regex_type: Union[Unset, ApplyRegExRegexType]
        if isinstance(_regex_type, Unset):
            regex_type = UNSET
        else:
            regex_type = ApplyRegExRegexType(_regex_type)

        apply_reg_ex = cls(
            type=type,
            regex=regex,
            input_columns=input_columns,
            output_columns=output_columns,
            regex_type=regex_type,
        )

        apply_reg_ex.additional_properties = d
        return apply_reg_ex

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
