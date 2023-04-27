from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.node_status import NodeStatus


T = TypeVar("T", bound="GetProjectNetworkStatusResponse200Item")


@attr.s(auto_attribs=True)
class GetProjectNetworkStatusResponse200Item:
    """
    Attributes:
        from_ (Union[Unset, str]):
        statuses (Union[Unset, List['NodeStatus']]):
    """

    from_: Union[Unset, str] = UNSET
    statuses: Union[Unset, List["NodeStatus"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from_ = self.from_
        statuses: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.statuses, Unset):
            statuses = []
            for statuses_item_data in self.statuses:
                statuses_item = statuses_item_data.to_dict()

                statuses.append(statuses_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_ is not UNSET:
            field_dict["from"] = from_
        if statuses is not UNSET:
            field_dict["statuses"] = statuses

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.node_status import NodeStatus

        d = src_dict.copy()
        from_ = d.pop("from", UNSET)

        statuses = []
        _statuses = d.pop("statuses", UNSET)
        for statuses_item_data in _statuses or []:
            statuses_item = NodeStatus.from_dict(statuses_item_data)

            statuses.append(statuses_item)

        get_project_network_status_response_200_item = cls(
            from_=from_,
            statuses=statuses,
        )

        get_project_network_status_response_200_item.additional_properties = d
        return get_project_network_status_response_200_item

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
