from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PrivateSearchDatabase")


@attr.s(auto_attribs=True)
class PrivateSearchDatabase:
    """Database used by private search

    Attributes:
        cryptosystem_params (Union[Unset, str]): cryptosystem parameters (b64-encoded)
        database_id (Union[Unset, str]): Unique identifier of a private search database.
        database_index (Union[Unset, str]): private search database hash index (b64-encoded)
        database_params (Union[Unset, str]): private search database parameters (b64-encoded), returned on GET /private-
            search-databases/<id>
    """

    cryptosystem_params: Union[Unset, str] = UNSET
    database_id: Union[Unset, str] = UNSET
    database_index: Union[Unset, str] = UNSET
    database_params: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cryptosystem_params = self.cryptosystem_params
        database_id = self.database_id
        database_index = self.database_index
        database_params = self.database_params

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cryptosystem_params is not UNSET:
            field_dict["cryptosystemParams"] = cryptosystem_params
        if database_id is not UNSET:
            field_dict["databaseID"] = database_id
        if database_index is not UNSET:
            field_dict["databaseIndex"] = database_index
        if database_params is not UNSET:
            field_dict["databaseParams"] = database_params

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cryptosystem_params = d.pop("cryptosystemParams", UNSET)

        database_id = d.pop("databaseID", UNSET)

        database_index = d.pop("databaseIndex", UNSET)

        database_params = d.pop("databaseParams", UNSET)

        private_search_database = cls(
            cryptosystem_params=cryptosystem_params,
            database_id=database_id,
            database_index=database_index,
            database_params=database_params,
        )

        private_search_database.additional_properties = d
        return private_search_database

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
