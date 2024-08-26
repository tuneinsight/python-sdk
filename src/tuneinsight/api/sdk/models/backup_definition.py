from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.backup_type import BackupType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.s3_parameters import S3Parameters


T = TypeVar("T", bound="BackupDefinition")


@attr.s(auto_attribs=True)
class BackupDefinition:
    """backup parameters

    Attributes:
        encrypt (Union[Unset, bool]): whether or not to encrypt the backup
        encryption_key (Union[Unset, str]): b64 encoded encryption in case the backup needs to be encrypted
        path (Union[Unset, str]): path to the local backup directory
        s_3_parameters (Union[Unset, S3Parameters]): parameters for the remote s3-compatible storage
        type (Union[Unset, BackupType]): enumeration of backup types
    """

    encrypt: Union[Unset, bool] = UNSET
    encryption_key: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    s_3_parameters: Union[Unset, "S3Parameters"] = UNSET
    type: Union[Unset, BackupType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        encrypt = self.encrypt
        encryption_key = self.encryption_key
        path = self.path
        s_3_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.s_3_parameters, Unset):
            s_3_parameters = self.s_3_parameters.to_dict()

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if encrypt is not UNSET:
            field_dict["encrypt"] = encrypt
        if encryption_key is not UNSET:
            field_dict["encryptionKey"] = encryption_key
        if path is not UNSET:
            field_dict["path"] = path
        if s_3_parameters is not UNSET:
            field_dict["s3Parameters"] = s_3_parameters
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.s3_parameters import S3Parameters

        d = src_dict.copy()
        encrypt = d.pop("encrypt", UNSET)

        encryption_key = d.pop("encryptionKey", UNSET)

        path = d.pop("path", UNSET)

        _s_3_parameters = d.pop("s3Parameters", UNSET)
        s_3_parameters: Union[Unset, S3Parameters]
        if isinstance(_s_3_parameters, Unset):
            s_3_parameters = UNSET
        else:
            s_3_parameters = S3Parameters.from_dict(_s_3_parameters)

        _type = d.pop("type", UNSET)
        type: Union[Unset, BackupType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = BackupType(_type)

        backup_definition = cls(
            encrypt=encrypt,
            encryption_key=encryption_key,
            path=path,
            s_3_parameters=s_3_parameters,
            type=type,
        )

        backup_definition.additional_properties = d
        return backup_definition

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
