from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.exported_key_bundle import ExportedKeyBundle


T = TypeVar("T", bound="ImportKeysDefinition")


@attr.s(auto_attribs=True)
class ImportKeysDefinition:
    """parameters for importing keys

    Attributes:
        force_update (Union[Unset, bool]): whether to overwrite keys that already exist in the storage when importing
        imported_key_bundle (Union[Unset, ExportedKeyBundle]): encrypted KEK (key encryption key) bundle exported with a
            password.
        password (Union[Unset, str]): password protecting the imported keys
    """

    force_update: Union[Unset, bool] = False
    imported_key_bundle: Union[Unset, "ExportedKeyBundle"] = UNSET
    password: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        force_update = self.force_update
        imported_key_bundle: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.imported_key_bundle, Unset):
            imported_key_bundle = self.imported_key_bundle.to_dict()

        password = self.password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if force_update is not UNSET:
            field_dict["forceUpdate"] = force_update
        if imported_key_bundle is not UNSET:
            field_dict["importedKeyBundle"] = imported_key_bundle
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.exported_key_bundle import ExportedKeyBundle

        d = src_dict.copy()
        force_update = d.pop("forceUpdate", UNSET)

        _imported_key_bundle = d.pop("importedKeyBundle", UNSET)
        imported_key_bundle: Union[Unset, ExportedKeyBundle]
        if isinstance(_imported_key_bundle, Unset):
            imported_key_bundle = UNSET
        else:
            imported_key_bundle = ExportedKeyBundle.from_dict(_imported_key_bundle)

        password = d.pop("password", UNSET)

        import_keys_definition = cls(
            force_update=force_update,
            imported_key_bundle=imported_key_bundle,
            password=password,
        )

        import_keys_definition.additional_properties = d
        return import_keys_definition

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
