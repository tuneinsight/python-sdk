from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.storage_operation import StorageOperation
from ..types import UNSET, Unset

T = TypeVar("T", bound="StorageDefinition")


@attr.s(auto_attribs=True)
class StorageDefinition:
    """specification of the storage operation

    Attributes:
        new_kek (Union[Unset, str]): new b64-formatted key to use on the storage, can be specified when running
            'encrypt' or 'rotate'
        operation (Union[Unset, StorageOperation]): operation to perform on the storage
    """

    new_kek: Union[Unset, str] = UNSET
    operation: Union[Unset, StorageOperation] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        new_kek = self.new_kek
        operation: Union[Unset, str] = UNSET
        if not isinstance(self.operation, Unset):
            operation = self.operation.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if new_kek is not UNSET:
            field_dict["newKEK"] = new_kek
        if operation is not UNSET:
            field_dict["operation"] = operation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        new_kek = d.pop("newKEK", UNSET)

        _operation = d.pop("operation", UNSET)
        operation: Union[Unset, StorageOperation]
        if isinstance(_operation, Unset):
            operation = UNSET
        else:
            operation = StorageOperation(_operation)

        storage_definition = cls(
            new_kek=new_kek,
            operation=operation,
        )

        storage_definition.additional_properties = d
        return storage_definition

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
