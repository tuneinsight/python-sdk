from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.computation import Computation
    from ..models.content import Content
    from ..models.result import Result


T = TypeVar("T", bound="ResultContent")


@attr.s(auto_attribs=True)
class ResultContent:
    """result along with content and computation details

    Attributes:
        content (Union[Unset, Content]): Content that can be retrieved and displayed for the user
        result (Union[Unset, Result]):
        computation (Union[Unset, Computation]): Metadata of a computation.
    """

    content: Union[Unset, "Content"] = UNSET
    result: Union[Unset, "Result"] = UNSET
    computation: Union[Unset, "Computation"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_dict()

        result: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        computation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.computation, Unset):
            computation = self.computation.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if result is not UNSET:
            field_dict["result"] = result
        if computation is not UNSET:
            field_dict["computation"] = computation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.computation import Computation
        from ..models.content import Content
        from ..models.result import Result

        d = src_dict.copy()
        _content = d.pop("content", UNSET)
        content: Union[Unset, Content]
        if isinstance(_content, Unset):
            content = UNSET
        else:
            content = Content.from_dict(_content)

        _result = d.pop("result", UNSET)
        result: Union[Unset, Result]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = Result.from_dict(_result)

        _computation = d.pop("computation", UNSET)
        computation: Union[Unset, Computation]
        if isinstance(_computation, Unset):
            computation = UNSET
        else:
            computation = Computation.from_dict(_computation)

        result_content = cls(
            content=content,
            result=result,
            computation=computation,
        )

        result_content.additional_properties = d
        return result_content

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
