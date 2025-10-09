from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.data_source_command_type import DataSourceCommandType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.generic_command_parameters import GenericCommandParameters


T = TypeVar("T", bound="GenericCommand")


@attr.s(auto_attribs=True)
class GenericCommand:
    """A generic datasource command, identified by a name (command), and taking any number of
    named parameters. The names, arguments, and behavior expected are datasource specific.
    This API will be deprecated once the new datasource commands have been integrated fully.

        Attributes:
            type (DataSourceCommandType): List of datasource commands that can be performed.
            command (Union[Unset, str]): Command identifier.
            parameters (Union[Unset, GenericCommandParameters]): Command's parameters.
    """

    type: DataSourceCommandType
    command: Union[Unset, str] = UNSET
    parameters: Union[Unset, "GenericCommandParameters"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        command = self.command
        parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if command is not UNSET:
            field_dict["command"] = command
        if parameters is not UNSET:
            field_dict["parameters"] = parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.generic_command_parameters import GenericCommandParameters

        d = src_dict.copy()
        type = DataSourceCommandType(d.pop("type"))

        command = d.pop("command", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: Union[Unset, GenericCommandParameters]
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = GenericCommandParameters.from_dict(_parameters)

        generic_command = cls(
            type=type,
            command=command,
            parameters=parameters,
        )

        generic_command.additional_properties = d
        return generic_command

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
