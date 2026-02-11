from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.access_scope import AccessScope
from ..models.agent_type import AgentType
from ..models.data_source_type import DataSourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentPromptDefinition")


@attr.s(auto_attribs=True)
class AgentPromptDefinition:
    """definition of a prompt for the agent.

    Attributes:
        agent_type (Union[Unset, AgentType]): An agent is a contextual assistant that helps users interact more easily
            with existing system functionalities.
        data_source_type (Union[Unset, DataSourceType]):
        full_prompt (Union[Unset, str]): the actual prompt sent by the user to the agent.
        name (Union[Unset, str]): an AI-generated description of the prompt used to identify the full prompt in the
            frontend.
        visibility_scope (Union[Unset, AccessScope]): defines the scope of access given to a resource
    """

    agent_type: Union[Unset, AgentType] = UNSET
    data_source_type: Union[Unset, DataSourceType] = UNSET
    full_prompt: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    visibility_scope: Union[Unset, AccessScope] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        agent_type: Union[Unset, str] = UNSET
        if not isinstance(self.agent_type, Unset):
            agent_type = self.agent_type.value

        data_source_type: Union[Unset, str] = UNSET
        if not isinstance(self.data_source_type, Unset):
            data_source_type = self.data_source_type.value

        full_prompt = self.full_prompt
        name = self.name
        visibility_scope: Union[Unset, str] = UNSET
        if not isinstance(self.visibility_scope, Unset):
            visibility_scope = self.visibility_scope.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if agent_type is not UNSET:
            field_dict["agentType"] = agent_type
        if data_source_type is not UNSET:
            field_dict["dataSourceType"] = data_source_type
        if full_prompt is not UNSET:
            field_dict["fullPrompt"] = full_prompt
        if name is not UNSET:
            field_dict["name"] = name
        if visibility_scope is not UNSET:
            field_dict["visibilityScope"] = visibility_scope

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _agent_type = d.pop("agentType", UNSET)
        agent_type: Union[Unset, AgentType]
        if isinstance(_agent_type, Unset):
            agent_type = UNSET
        else:
            agent_type = AgentType(_agent_type)

        _data_source_type = d.pop("dataSourceType", UNSET)
        data_source_type: Union[Unset, DataSourceType]
        if isinstance(_data_source_type, Unset):
            data_source_type = UNSET
        else:
            data_source_type = DataSourceType(_data_source_type)

        full_prompt = d.pop("fullPrompt", UNSET)

        name = d.pop("name", UNSET)

        _visibility_scope = d.pop("visibilityScope", UNSET)
        visibility_scope: Union[Unset, AccessScope]
        if isinstance(_visibility_scope, Unset):
            visibility_scope = UNSET
        else:
            visibility_scope = AccessScope(_visibility_scope)

        agent_prompt_definition = cls(
            agent_type=agent_type,
            data_source_type=data_source_type,
            full_prompt=full_prompt,
            name=name,
            visibility_scope=visibility_scope,
        )

        agent_prompt_definition.additional_properties = d
        return agent_prompt_definition

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
