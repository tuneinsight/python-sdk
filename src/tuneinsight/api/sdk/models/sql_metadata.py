from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SQLMetadata")


@attr.s(auto_attribs=True)
class SQLMetadata:
    """The metadata required to translate cross-standard queries to SQL for a datasource.

    Attributes:
        identifier (Union[Unset, str]): The name of the column in each table that uniquely identifies a person. This
            column is treated as
            a primary key in the database. It assumes that each series column uses a column with this name to
            link to the user (e.g., if this is called "PersonID", all tables must have a "PersonID" column).
        main_table (Union[Unset, str]): The name of the main table holding features for a person.
    """

    identifier: Union[Unset, str] = UNSET
    main_table: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        identifier = self.identifier
        main_table = self.main_table

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if main_table is not UNSET:
            field_dict["mainTable"] = main_table

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        identifier = d.pop("identifier", UNSET)

        main_table = d.pop("mainTable", UNSET)

        sql_metadata = cls(
            identifier=identifier,
            main_table=main_table,
        )

        sql_metadata.additional_properties = d
        return sql_metadata

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
