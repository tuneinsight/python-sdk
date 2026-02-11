from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="StackFrame")


@attr.s(auto_attribs=True)
class StackFrame:
    """frame of the runtime stack.

    Attributes:
        function (Union[Unset, str]): name of the module and function from the frame.
        line (Union[Unset, int]): Line of code the frame is at.
    """

    function: Union[Unset, str] = UNSET
    line: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        function = self.function
        line = self.line

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if function is not UNSET:
            field_dict["function"] = function
        if line is not UNSET:
            field_dict["line"] = line

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        function = d.pop("function", UNSET)

        line = d.pop("line", UNSET)

        stack_frame = cls(
            function=function,
            line=line,
        )

        stack_frame.additional_properties = d
        return stack_frame

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
