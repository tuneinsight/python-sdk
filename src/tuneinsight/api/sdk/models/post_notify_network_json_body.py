from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostNotifyNetworkJsonBody")


@attr.s(auto_attribs=True)
class PostNotifyNetworkJsonBody:
    """
    Attributes:
        network_changed (Union[Unset, bool]): Indicates that the network has changed and other nodes should re-
            synchronize their state with the portal.
    """

    network_changed: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        network_changed = self.network_changed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if network_changed is not UNSET:
            field_dict["networkChanged"] = network_changed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        network_changed = d.pop("networkChanged", UNSET)

        post_notify_network_json_body = cls(
            network_changed=network_changed,
        )

        post_notify_network_json_body.additional_properties = d
        return post_notify_network_json_body

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
