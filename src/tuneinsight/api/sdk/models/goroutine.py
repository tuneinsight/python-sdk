from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stack_frame import StackFrame


T = TypeVar("T", bound="Goroutine")


@attr.s(auto_attribs=True)
class Goroutine:
    """Information about a running goroutine.

    Attributes:
        function (Union[Unset, str]): function name of the lowest level stack frame.
        occurrences (Union[Unset, int]): number of occurrences of the same goroutine.
        stack (Union[Unset, List['StackFrame']]): the full call stack
    """

    function: Union[Unset, str] = UNSET
    occurrences: Union[Unset, int] = UNSET
    stack: Union[Unset, List["StackFrame"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        function = self.function
        occurrences = self.occurrences
        stack: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.stack, Unset):
            stack = []
            for stack_item_data in self.stack:
                stack_item = stack_item_data.to_dict()

                stack.append(stack_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if function is not UNSET:
            field_dict["function"] = function
        if occurrences is not UNSET:
            field_dict["occurrences"] = occurrences
        if stack is not UNSET:
            field_dict["stack"] = stack

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.stack_frame import StackFrame

        d = src_dict.copy()
        function = d.pop("function", UNSET)

        occurrences = d.pop("occurrences", UNSET)

        stack = []
        _stack = d.pop("stack", UNSET)
        for stack_item_data in _stack or []:
            stack_item = StackFrame.from_dict(stack_item_data)

            stack.append(stack_item)

        goroutine = cls(
            function=function,
            occurrences=occurrences,
            stack=stack,
        )

        goroutine.additional_properties = d
        return goroutine

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
