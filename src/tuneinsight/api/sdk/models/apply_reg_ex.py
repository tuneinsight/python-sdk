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
        regex (str): regular expression to apply
        regex_type (Union[Unset, ApplyRegExRegexType]): defines what we want to retrieve from the regex
        cols (Union[Unset, List[str]]): cols from which to extract field
        names (Union[Unset, List[str]]): names of resulting columns (if none, no new columns are created)
    """

    type: PreprocessingOperationType
    regex: str
    regex_type: Union[Unset, ApplyRegExRegexType] = UNSET
    cols: Union[Unset, List[str]] = UNSET
    names: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        regex = self.regex
        regex_type: Union[Unset, str] = UNSET
        if not isinstance(self.regex_type, Unset):
            regex_type = self.regex_type.value

        cols: Union[Unset, List[str]] = UNSET
        if not isinstance(self.cols, Unset):
            cols = self.cols

        names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.names, Unset):
            names = self.names

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "regex": regex,
            }
        )
        if regex_type is not UNSET:
            field_dict["regex_type"] = regex_type
        if cols is not UNSET:
            field_dict["cols"] = cols
        if names is not UNSET:
            field_dict["names"] = names

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        regex = d.pop("regex")

        _regex_type = d.pop("regex_type", UNSET)
        regex_type: Union[Unset, ApplyRegExRegexType]
        if isinstance(_regex_type, Unset):
            regex_type = UNSET
        else:
            regex_type = ApplyRegExRegexType(_regex_type)

        cols = cast(List[str], d.pop("cols", UNSET))

        names = cast(List[str], d.pop("names", UNSET))

        apply_reg_ex = cls(
            type=type,
            regex=regex,
            regex_type=regex_type,
            cols=cols,
            names=names,
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
