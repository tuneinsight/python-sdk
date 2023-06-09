from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.private_search_database_database_hash_index import PrivateSearchDatabaseDatabaseHashIndex


T = TypeVar("T", bound="PrivateSearchDatabase")


@attr.s(auto_attribs=True)
class PrivateSearchDatabase:
    """Database used by private search

    Attributes:
        database_hash_index (Union[Unset, PrivateSearchDatabaseDatabaseHashIndex]): private search database hash index
            (in the form [<hash(string)>:<idx(int)>, ...]), returned on GET /private-search-databases/<id>
        database_id (Union[Unset, str]): Unique identifier of a private search database.
        database_params (Union[Unset, str]): private search database parameters (b64-encoded), returned on GET /private-
            search-databases/<id>
    """

    database_hash_index: Union[Unset, "PrivateSearchDatabaseDatabaseHashIndex"] = UNSET
    database_id: Union[Unset, str] = UNSET
    database_params: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        database_hash_index: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.database_hash_index, Unset):
            database_hash_index = self.database_hash_index.to_dict()

        database_id = self.database_id
        database_params = self.database_params

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if database_hash_index is not UNSET:
            field_dict["databaseHashIndex"] = database_hash_index
        if database_id is not UNSET:
            field_dict["databaseID"] = database_id
        if database_params is not UNSET:
            field_dict["databaseParams"] = database_params

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.private_search_database_database_hash_index import PrivateSearchDatabaseDatabaseHashIndex

        d = src_dict.copy()
        _database_hash_index = d.pop("databaseHashIndex", UNSET)
        database_hash_index: Union[Unset, PrivateSearchDatabaseDatabaseHashIndex]
        if isinstance(_database_hash_index, Unset):
            database_hash_index = UNSET
        else:
            database_hash_index = PrivateSearchDatabaseDatabaseHashIndex.from_dict(_database_hash_index)

        database_id = d.pop("databaseID", UNSET)

        database_params = d.pop("databaseParams", UNSET)

        private_search_database = cls(
            database_hash_index=database_hash_index,
            database_id=database_id,
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
