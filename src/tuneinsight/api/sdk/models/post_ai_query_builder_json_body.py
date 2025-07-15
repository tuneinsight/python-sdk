from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_builder_prompt_definition import AIBuilderPromptDefinition
    from ..models.post_ai_query_builder_json_body_data_model_template import PostAIQueryBuilderJsonBodyDataModelTemplate


T = TypeVar("T", bound="PostAIQueryBuilderJsonBody")


@attr.s(auto_attribs=True)
class PostAIQueryBuilderJsonBody:
    """
    Attributes:
        data_model (str):
        data_model_template (PostAIQueryBuilderJsonBodyDataModelTemplate):
        prompt (AIBuilderPromptDefinition): definition of a prompt for the AI query builder
        model_name (Union[Unset, str]):
        prompt_id (Union[Unset, str]):
    """

    data_model: str
    data_model_template: "PostAIQueryBuilderJsonBodyDataModelTemplate"
    prompt: "AIBuilderPromptDefinition"
    model_name: Union[Unset, str] = UNSET
    prompt_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data_model = self.data_model
        data_model_template = self.data_model_template.to_dict()

        prompt = self.prompt.to_dict()

        model_name = self.model_name
        prompt_id = self.prompt_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data_model": data_model,
                "data_model_template": data_model_template,
                "prompt": prompt,
            }
        )
        if model_name is not UNSET:
            field_dict["model_name"] = model_name
        if prompt_id is not UNSET:
            field_dict["promptId"] = prompt_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ai_builder_prompt_definition import AIBuilderPromptDefinition
        from ..models.post_ai_query_builder_json_body_data_model_template import (
            PostAIQueryBuilderJsonBodyDataModelTemplate,
        )

        d = src_dict.copy()
        data_model = d.pop("data_model")

        data_model_template = PostAIQueryBuilderJsonBodyDataModelTemplate.from_dict(d.pop("data_model_template"))

        prompt = AIBuilderPromptDefinition.from_dict(d.pop("prompt"))

        model_name = d.pop("model_name", UNSET)

        prompt_id = d.pop("promptId", UNSET)

        post_ai_query_builder_json_body = cls(
            data_model=data_model,
            data_model_template=data_model_template,
            prompt=prompt,
            model_name=model_name,
            prompt_id=prompt_id,
        )

        post_ai_query_builder_json_body.additional_properties = d
        return post_ai_query_builder_json_body

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
