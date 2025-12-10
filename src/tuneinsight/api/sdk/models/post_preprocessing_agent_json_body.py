from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_builder_prompt_definition import AIBuilderPromptDefinition


T = TypeVar("T", bound="PostPreprocessingAgentJsonBody")


@attr.s(auto_attribs=True)
class PostPreprocessingAgentJsonBody:
    """
    Attributes:
        available_columns (List[str]): List of available column names
        prompt (AIBuilderPromptDefinition): definition of a prompt for the AI query builder
        api_url (Union[Unset, str]): URL of the LLM API to use for the preprocessing
        auth_token (Union[Unset, str]): Authentication token for the LLM API
        model_name (Union[Unset, str]): Name of the model to use for the preprocessing
        prompt_id (Union[Unset, str]):
    """

    available_columns: List[str]
    prompt: "AIBuilderPromptDefinition"
    api_url: Union[Unset, str] = UNSET
    auth_token: Union[Unset, str] = UNSET
    model_name: Union[Unset, str] = UNSET
    prompt_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        available_columns = self.available_columns

        prompt = self.prompt.to_dict()

        api_url = self.api_url
        auth_token = self.auth_token
        model_name = self.model_name
        prompt_id = self.prompt_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "available_columns": available_columns,
                "prompt": prompt,
            }
        )
        if api_url is not UNSET:
            field_dict["api_url"] = api_url
        if auth_token is not UNSET:
            field_dict["auth_token"] = auth_token
        if model_name is not UNSET:
            field_dict["model_name"] = model_name
        if prompt_id is not UNSET:
            field_dict["promptId"] = prompt_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ai_builder_prompt_definition import AIBuilderPromptDefinition

        d = src_dict.copy()
        available_columns = cast(List[str], d.pop("available_columns"))

        prompt = AIBuilderPromptDefinition.from_dict(d.pop("prompt"))

        api_url = d.pop("api_url", UNSET)

        auth_token = d.pop("auth_token", UNSET)

        model_name = d.pop("model_name", UNSET)

        prompt_id = d.pop("promptId", UNSET)

        post_preprocessing_agent_json_body = cls(
            available_columns=available_columns,
            prompt=prompt,
            api_url=api_url,
            auth_token=auth_token,
            model_name=model_name,
            prompt_id=prompt_id,
        )

        post_preprocessing_agent_json_body.additional_properties = d
        return post_preprocessing_agent_json_body

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
