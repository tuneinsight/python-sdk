from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.data_source_query import DataSourceQuery


T = TypeVar("T", bound="DataSourceCompoundQuery")


@attr.s(auto_attribs=True)
class DataSourceCompoundQuery:
    """definition of datasource queries for each node in the computation"""

    additional_properties: Dict[str, "DataSourceQuery"] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pass

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_source_query import DataSourceQuery

        d = src_dict.copy()
        data_source_compound_query = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = DataSourceQuery.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        data_source_compound_query.additional_properties = additional_properties
        return data_source_compound_query

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "DataSourceQuery":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "DataSourceQuery") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
