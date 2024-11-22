from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.access_scope import AccessScope
from ..models.data_source_type import DataSourceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_source_query import DataSourceQuery


T = TypeVar("T", bound="QueryBookmarkDefinition")


@attr.s(auto_attribs=True)
class QueryBookmarkDefinition:
    """editable fields of a query bookmark

    Attributes:
        data_source_type (Union[Unset, DataSourceType]):
        description (Union[Unset, str]): optional description for the bookmark
        name (Union[Unset, str]): name of the bookmark
        query (Union[Unset, DataSourceQuery]): schema used for the query
        visibility_scope (Union[Unset, AccessScope]): defines the scope of access given to a resource
    """

    data_source_type: Union[Unset, DataSourceType] = UNSET
    description: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    query: Union[Unset, "DataSourceQuery"] = UNSET
    visibility_scope: Union[Unset, AccessScope] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data_source_type: Union[Unset, str] = UNSET
        if not isinstance(self.data_source_type, Unset):
            data_source_type = self.data_source_type.value

        description = self.description
        name = self.name
        query: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.query, Unset):
            query = self.query.to_dict()

        visibility_scope: Union[Unset, str] = UNSET
        if not isinstance(self.visibility_scope, Unset):
            visibility_scope = self.visibility_scope.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_source_type is not UNSET:
            field_dict["dataSourceType"] = data_source_type
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if query is not UNSET:
            field_dict["query"] = query
        if visibility_scope is not UNSET:
            field_dict["visibilityScope"] = visibility_scope

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_source_query import DataSourceQuery

        d = src_dict.copy()
        _data_source_type = d.pop("dataSourceType", UNSET)
        data_source_type: Union[Unset, DataSourceType]
        if isinstance(_data_source_type, Unset):
            data_source_type = UNSET
        else:
            data_source_type = DataSourceType(_data_source_type)

        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        _query = d.pop("query", UNSET)
        query: Union[Unset, DataSourceQuery]
        if isinstance(_query, Unset):
            query = UNSET
        else:
            query = DataSourceQuery.from_dict(_query)

        _visibility_scope = d.pop("visibilityScope", UNSET)
        visibility_scope: Union[Unset, AccessScope]
        if isinstance(_visibility_scope, Unset):
            visibility_scope = UNSET
        else:
            visibility_scope = AccessScope(_visibility_scope)

        query_bookmark_definition = cls(
            data_source_type=data_source_type,
            description=description,
            name=name,
            query=query,
            visibility_scope=visibility_scope,
        )

        query_bookmark_definition.additional_properties = d
        return query_bookmark_definition

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
