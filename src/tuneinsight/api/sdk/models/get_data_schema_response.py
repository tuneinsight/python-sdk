from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.query_builder_type import QueryBuilderType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_schema import DataSchema


T = TypeVar("T", bound="GetDataSchemaResponse")


@attr.s(auto_attribs=True)
class GetDataSchemaResponse:
    """regroups the data schema and query builder type that should be used.

    Attributes:
        query_builder_type (Union[Unset, QueryBuilderType]):
        schema (Union[Unset, DataSchema]): aims to provide a flexible definition of a data schema, which includes the
            tables and their relationships.
    """

    query_builder_type: Union[Unset, QueryBuilderType] = UNSET
    schema: Union[Unset, "DataSchema"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        query_builder_type: Union[Unset, str] = UNSET
        if not isinstance(self.query_builder_type, Unset):
            query_builder_type = self.query_builder_type.value

        schema: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.schema, Unset):
            schema = self.schema.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if query_builder_type is not UNSET:
            field_dict["queryBuilderType"] = query_builder_type
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_schema import DataSchema

        d = src_dict.copy()
        _query_builder_type = d.pop("queryBuilderType", UNSET)
        query_builder_type: Union[Unset, QueryBuilderType]
        if isinstance(_query_builder_type, Unset):
            query_builder_type = UNSET
        else:
            query_builder_type = QueryBuilderType(_query_builder_type)

        _schema = d.pop("schema", UNSET)
        schema: Union[Unset, DataSchema]
        if isinstance(_schema, Unset):
            schema = UNSET
        else:
            schema = DataSchema.from_dict(_schema)

        get_data_schema_response = cls(
            query_builder_type=query_builder_type,
            schema=schema,
        )

        get_data_schema_response.additional_properties = d
        return get_data_schema_response

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
