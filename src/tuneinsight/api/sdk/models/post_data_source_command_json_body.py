from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_data_source_command_json_body_parameters import PostDataSourceCommandJsonBodyParameters


T = TypeVar("T", bound="PostDataSourceCommandJsonBody")


@attr.s(auto_attribs=True)
class PostDataSourceCommandJsonBody:
    """
    Attributes:
        command (Union[Unset, str]): Command identifier.
        parameters (Union[Unset, PostDataSourceCommandJsonBodyParameters]): Command's parameters.
    """

    command: Union[Unset, str] = UNSET
    parameters: Union[Unset, "PostDataSourceCommandJsonBodyParameters"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        command = self.command
        parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if command is not UNSET:
            field_dict["command"] = command
        if parameters is not UNSET:
            field_dict["parameters"] = parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_data_source_command_json_body_parameters import PostDataSourceCommandJsonBodyParameters

        d = src_dict.copy()
        command = d.pop("command", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: Union[Unset, PostDataSourceCommandJsonBodyParameters]
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = PostDataSourceCommandJsonBodyParameters.from_dict(_parameters)

        post_data_source_command_json_body = cls(
            command=command,
            parameters=parameters,
        )

        post_data_source_command_json_body.additional_properties = d
        return post_data_source_command_json_body

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
