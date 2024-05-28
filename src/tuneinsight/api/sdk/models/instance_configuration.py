from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="InstanceConfiguration")


@attr.s(auto_attribs=True)
class InstanceConfiguration:
    """contains information about the instance's current configuration

    Attributes:
        config_yaml (Union[Unset, str]): YAML-serialized configuration string.
        instance_name (Union[Unset, str]): name or alias of the instance
    """

    config_yaml: Union[Unset, str] = UNSET
    instance_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        config_yaml = self.config_yaml
        instance_name = self.instance_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config_yaml is not UNSET:
            field_dict["configYAML"] = config_yaml
        if instance_name is not UNSET:
            field_dict["instanceName"] = instance_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        config_yaml = d.pop("configYAML", UNSET)

        instance_name = d.pop("instanceName", UNSET)

        instance_configuration = cls(
            config_yaml=config_yaml,
            instance_name=instance_name,
        )

        instance_configuration.additional_properties = d
        return instance_configuration

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
