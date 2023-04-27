from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.computation_definition import ComputationDefinition


T = TypeVar("T", bound="ProtocolDefinition")


@attr.s(auto_attribs=True)
class ProtocolDefinition:
    """A new protocol request definition

    Attributes:
        computation (Union[Unset, ComputationDefinition]): Generic computation.
        service_id (Union[Unset, str]): id of the protocol service
    """

    computation: Union[Unset, "ComputationDefinition"] = UNSET
    service_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        computation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.computation, Unset):
            computation = self.computation.to_dict()

        service_id = self.service_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if computation is not UNSET:
            field_dict["computation"] = computation
        if service_id is not UNSET:
            field_dict["serviceId"] = service_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.computation_definition import ComputationDefinition

        d = src_dict.copy()
        _computation = d.pop("computation", UNSET)
        computation: Union[Unset, ComputationDefinition]
        if isinstance(_computation, Unset):
            computation = UNSET
        else:
            computation = ComputationDefinition.from_dict(_computation)

        service_id = d.pop("serviceId", UNSET)

        protocol_definition = cls(
            computation=computation,
            service_id=service_id,
        )

        protocol_definition.additional_properties = d
        return protocol_definition

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
