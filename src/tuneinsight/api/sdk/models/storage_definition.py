from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.storage_operation import StorageOperation
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_definition import BackupDefinition


T = TypeVar("T", bound="StorageDefinition")


@attr.s(auto_attribs=True)
class StorageDefinition:
    """specification of the storage operation

    Attributes:
        backup_definition (Union[Unset, BackupDefinition]): backup parameters
        current_key (Union[Unset, str]): currently used b64-formatted encryption key, needs to be specified when running
            'decrypt' or 'rotate'
        encrypt_unencrypted (Union[Unset, bool]): when performing a rotation, if true, then unencrypted values get
            encrypted
        new_key (Union[Unset, str]): new b64-formatted key to use on the storage, needs to be specified when running
            'encrypt' or 'rotate'
        operation (Union[Unset, StorageOperation]): operation to perform on the storage
    """

    backup_definition: Union[Unset, "BackupDefinition"] = UNSET
    current_key: Union[Unset, str] = UNSET
    encrypt_unencrypted: Union[Unset, bool] = UNSET
    new_key: Union[Unset, str] = UNSET
    operation: Union[Unset, StorageOperation] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        backup_definition: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.backup_definition, Unset):
            backup_definition = self.backup_definition.to_dict()

        current_key = self.current_key
        encrypt_unencrypted = self.encrypt_unencrypted
        new_key = self.new_key
        operation: Union[Unset, str] = UNSET
        if not isinstance(self.operation, Unset):
            operation = self.operation.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backup_definition is not UNSET:
            field_dict["backupDefinition"] = backup_definition
        if current_key is not UNSET:
            field_dict["currentKey"] = current_key
        if encrypt_unencrypted is not UNSET:
            field_dict["encryptUnencrypted"] = encrypt_unencrypted
        if new_key is not UNSET:
            field_dict["newKey"] = new_key
        if operation is not UNSET:
            field_dict["operation"] = operation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.backup_definition import BackupDefinition

        d = src_dict.copy()
        _backup_definition = d.pop("backupDefinition", UNSET)
        backup_definition: Union[Unset, BackupDefinition]
        if isinstance(_backup_definition, Unset):
            backup_definition = UNSET
        else:
            backup_definition = BackupDefinition.from_dict(_backup_definition)

        current_key = d.pop("currentKey", UNSET)

        encrypt_unencrypted = d.pop("encryptUnencrypted", UNSET)

        new_key = d.pop("newKey", UNSET)

        _operation = d.pop("operation", UNSET)
        operation: Union[Unset, StorageOperation]
        if isinstance(_operation, Unset):
            operation = UNSET
        else:
            operation = StorageOperation(_operation)

        storage_definition = cls(
            backup_definition=backup_definition,
            current_key=current_key,
            encrypt_unencrypted=encrypt_unencrypted,
            new_key=new_key,
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
