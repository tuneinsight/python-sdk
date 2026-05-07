from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_summarize_query_agent_json_body_payload import PostSummarizeQueryAgentJsonBodyPayload


T = TypeVar("T", bound="PostSummarizeQueryAgentJsonBody")


@attr.s(auto_attribs=True)
class PostSummarizeQueryAgentJsonBody:
    """
    Attributes:
        language (str): Language code for the summary response
        payload (PostSummarizeQueryAgentJsonBodyPayload): UI state to summarize
        api_url (Union[Unset, str]): URL of the LLM API to use for the summarization
        auth_token (Union[Unset, str]): Authentication token for the LLM API
        model_name (Union[Unset, str]): Name of the model to use for the summarization
    """

    language: str
    payload: "PostSummarizeQueryAgentJsonBodyPayload"
    api_url: Union[Unset, str] = UNSET
    auth_token: Union[Unset, str] = UNSET
    model_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        language = self.language
        payload = self.payload.to_dict()

        api_url = self.api_url
        auth_token = self.auth_token
        model_name = self.model_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "language": language,
                "payload": payload,
            }
        )
        if api_url is not UNSET:
            field_dict["api_url"] = api_url
        if auth_token is not UNSET:
            field_dict["auth_token"] = auth_token
        if model_name is not UNSET:
            field_dict["model_name"] = model_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_summarize_query_agent_json_body_payload import PostSummarizeQueryAgentJsonBodyPayload

        d = src_dict.copy()
        language = d.pop("language")

        payload = PostSummarizeQueryAgentJsonBodyPayload.from_dict(d.pop("payload"))

        api_url = d.pop("api_url", UNSET)

        auth_token = d.pop("auth_token", UNSET)

        model_name = d.pop("model_name", UNSET)

        post_summarize_query_agent_json_body = cls(
            language=language,
            payload=payload,
            api_url=api_url,
            auth_token=auth_token,
            model_name=model_name,
        )

        post_summarize_query_agent_json_body.additional_properties = d
        return post_summarize_query_agent_json_body

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
