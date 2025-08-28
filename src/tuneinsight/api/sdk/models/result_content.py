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
        breakdown_content (Union[Unset, Content]): Content that can be retrieved and displayed for the user
        computation (Union[Unset, Computation]): Metadata of a computation.
        content (Union[Unset, Content]): Content that can be retrieved and displayed for the user
        local_content (Union[Unset, Content]): Content that can be retrieved and displayed for the user
        result (Union[Unset, Result]):
    """

    breakdown_content: Union[Unset, "Content"] = UNSET
    computation: Union[Unset, "Computation"] = UNSET
    content: Union[Unset, "Content"] = UNSET
    local_content: Union[Unset, "Content"] = UNSET
    result: Union[Unset, "Result"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        breakdown_content: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.breakdown_content, Unset):
            breakdown_content = self.breakdown_content.to_dict()

        computation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.computation, Unset):
            computation = self.computation.to_dict()

        content: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_dict()

        local_content: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.local_content, Unset):
            local_content = self.local_content.to_dict()

        result: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if breakdown_content is not UNSET:
            field_dict["breakdownContent"] = breakdown_content
        if computation is not UNSET:
            field_dict["computation"] = computation
        if content is not UNSET:
            field_dict["content"] = content
        if local_content is not UNSET:
            field_dict["localContent"] = local_content
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.computation import Computation
        from ..models.content import Content
        from ..models.result import Result

        d = src_dict.copy()
        _breakdown_content = d.pop("breakdownContent", UNSET)
        breakdown_content: Union[Unset, Content]
        if isinstance(_breakdown_content, Unset):
            breakdown_content = UNSET
        else:
            breakdown_content = Content.from_dict(_breakdown_content)

        _computation = d.pop("computation", UNSET)
        computation: Union[Unset, Computation]
        if isinstance(_computation, Unset):
            computation = UNSET
        else:
            computation = Computation.from_dict(_computation)

        _content = d.pop("content", UNSET)
        content: Union[Unset, Content]
        if isinstance(_content, Unset):
            content = UNSET
        else:
            content = Content.from_dict(_content)

        _local_content = d.pop("localContent", UNSET)
        local_content: Union[Unset, Content]
        if isinstance(_local_content, Unset):
            local_content = UNSET
        else:
            local_content = Content.from_dict(_local_content)

        _result = d.pop("result", UNSET)
        result: Union[Unset, Result]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = Result.from_dict(_result)

        result_content = cls(
            breakdown_content=breakdown_content,
            computation=computation,
            content=content,
            local_content=local_content,
            result=result,
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
