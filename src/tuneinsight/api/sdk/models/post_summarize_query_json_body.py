from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.post_summarize_query_json_body_payload import PostSummarizeQueryJsonBodyPayload


T = TypeVar("T", bound="PostSummarizeQueryJsonBody")


@attr.s(auto_attribs=True)
class PostSummarizeQueryJsonBody:
    """
    Attributes:
        payload (PostSummarizeQueryJsonBodyPayload): UI state to summarize
    """

    payload: "PostSummarizeQueryJsonBodyPayload"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        payload = self.payload.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "payload": payload,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_summarize_query_json_body_payload import PostSummarizeQueryJsonBodyPayload

        d = src_dict.copy()
        payload = PostSummarizeQueryJsonBodyPayload.from_dict(d.pop("payload"))

        post_summarize_query_json_body = cls(
            payload=payload,
        )

        post_summarize_query_json_body.additional_properties = d
        return post_summarize_query_json_body

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
