from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_source_query import DataSourceQuery
    from ..models.screened_row import ScreenedRow
    from ..models.screening_metadata import ScreeningMetadata
    from ..models.screening_operation import ScreeningOperation


T = TypeVar("T", bound="ScreeningSession")


@attr.s(auto_attribs=True)
class ScreeningSession:
    """A screening session is used by users to retrieve, preprocess and validate data from a data source.
    This model contains information about the state of the session, including the data that was retrieved and
    the screening operations that were applied.

        Attributes:
            data_source_id (Union[Unset, None, str]): Unique identifier of a data source.
            name (Union[Unset, str]): name given to this session.
            operations (Union[Unset, List['ScreeningOperation']]): list of screening operations.
            query (Union[Unset, DataSourceQuery]): schema used for the query
            created_at (Union[Unset, str]): time at which the session was created (RFC 3339 format).
            created_by_user (Union[Unset, str]): name of the user that created this session.
            data (Union[Unset, List['ScreenedRow']]): the rows of the table that is being screened.
            data_object_id (Union[Unset, str]): Unique identifier of a data object.
            id (Union[Unset, str]): id of the screening session
            metadata (Union[Unset, ScreeningMetadata]): metadata of the dataset used in the screening process.
            updated_at (Union[Unset, str]): time at which the session was last updated (RFC 3339 format).
    """

    data_source_id: Union[Unset, None, str] = UNSET
    name: Union[Unset, str] = UNSET
    operations: Union[Unset, List["ScreeningOperation"]] = UNSET
    query: Union[Unset, "DataSourceQuery"] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by_user: Union[Unset, str] = UNSET
    data: Union[Unset, List["ScreenedRow"]] = UNSET
    data_object_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    metadata: Union[Unset, "ScreeningMetadata"] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data_source_id = self.data_source_id
        name = self.name
        operations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.operations, Unset):
            operations = []
            for operations_item_data in self.operations:
                operations_item = operations_item_data.to_dict()

                operations.append(operations_item)

        query: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.query, Unset):
            query = self.query.to_dict()

        created_at = self.created_at
        created_by_user = self.created_by_user
        data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()

                data.append(data_item)

        data_object_id = self.data_object_id
        id = self.id
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_source_id is not UNSET:
            field_dict["dataSourceId"] = data_source_id
        if name is not UNSET:
            field_dict["name"] = name
        if operations is not UNSET:
            field_dict["operations"] = operations
        if query is not UNSET:
            field_dict["query"] = query
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by_user is not UNSET:
            field_dict["createdByUser"] = created_by_user
        if data is not UNSET:
            field_dict["data"] = data
        if data_object_id is not UNSET:
            field_dict["dataObjectId"] = data_object_id
        if id is not UNSET:
            field_dict["id"] = id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_source_query import DataSourceQuery
        from ..models.screened_row import ScreenedRow
        from ..models.screening_metadata import ScreeningMetadata
        from ..models.screening_operation import ScreeningOperation

        d = src_dict.copy()
        data_source_id = d.pop("dataSourceId", UNSET)

        name = d.pop("name", UNSET)

        operations = []
        _operations = d.pop("operations", UNSET)
        for operations_item_data in _operations or []:
            operations_item = ScreeningOperation.from_dict(operations_item_data)

            operations.append(operations_item)

        _query = d.pop("query", UNSET)
        query: Union[Unset, DataSourceQuery]
        if isinstance(_query, Unset):
            query = UNSET
        else:
            query = DataSourceQuery.from_dict(_query)

        created_at = d.pop("createdAt", UNSET)

        created_by_user = d.pop("createdByUser", UNSET)

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = ScreenedRow.from_dict(data_item_data)

            data.append(data_item)

        data_object_id = d.pop("dataObjectId", UNSET)

        id = d.pop("id", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ScreeningMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ScreeningMetadata.from_dict(_metadata)

        updated_at = d.pop("updatedAt", UNSET)

        screening_session = cls(
            data_source_id=data_source_id,
            name=name,
            operations=operations,
            query=query,
            created_at=created_at,
            created_by_user=created_by_user,
            data=data,
            data_object_id=data_object_id,
            id=id,
            metadata=metadata,
            updated_at=updated_at,
        )

        screening_session.additional_properties = d
        return screening_session

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
