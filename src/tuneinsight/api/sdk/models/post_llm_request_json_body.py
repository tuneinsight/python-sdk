from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_llm_request_json_body_prompt_args import PostLlmRequestJsonBodyPromptArgs


T = TypeVar("T", bound="PostLlmRequestJsonBody")


@attr.s(auto_attribs=True)
class PostLlmRequestJsonBody:
    """Prompt parameters

    Attributes:
        prompt_args (PostLlmRequestJsonBodyPromptArgs): Parameters of the prompt as a dict
        api_url (Union[Unset, str]): URL of the LLM API to use for the prompt
        auth_token (Union[Unset, str]): Authentication token for the LLM API
        llm_model (Union[Unset, str]): LLM model name to get the prompt for
        prompt_only (Union[Unset, bool]): Set to True to get only the prompt to query the model afterwards
    """

    prompt_args: "PostLlmRequestJsonBodyPromptArgs"
    api_url: Union[Unset, str] = UNSET
    auth_token: Union[Unset, str] = UNSET
    llm_model: Union[Unset, str] = UNSET
    prompt_only: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        prompt_args = self.prompt_args.to_dict()

        api_url = self.api_url
        auth_token = self.auth_token
        llm_model = self.llm_model
        prompt_only = self.prompt_only

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "prompt_args": prompt_args,
            }
        )
        if api_url is not UNSET:
            field_dict["api_url"] = api_url
        if auth_token is not UNSET:
            field_dict["auth_token"] = auth_token
        if llm_model is not UNSET:
            field_dict["llm_model"] = llm_model
        if prompt_only is not UNSET:
            field_dict["prompt_only"] = prompt_only

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_llm_request_json_body_prompt_args import PostLlmRequestJsonBodyPromptArgs

        d = src_dict.copy()
        prompt_args = PostLlmRequestJsonBodyPromptArgs.from_dict(d.pop("prompt_args"))

        api_url = d.pop("api_url", UNSET)

        auth_token = d.pop("auth_token", UNSET)

        llm_model = d.pop("llm_model", UNSET)

        prompt_only = d.pop("prompt_only", UNSET)

        post_llm_request_json_body = cls(
            prompt_args=prompt_args,
            api_url=api_url,
            auth_token=auth_token,
            llm_model=llm_model,
            prompt_only=prompt_only,
        )

        post_llm_request_json_body.additional_properties = d
        return post_llm_request_json_body

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
