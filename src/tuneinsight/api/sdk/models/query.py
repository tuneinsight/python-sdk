from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.query_status import QueryStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Query")


@attr.s(auto_attribs=True)
class Query:
    """Data source query

    Attributes:
        created_at (Union[Unset, str]):
        created_by_user (Union[Unset, str]): ID of user who created the project
        error (Union[Unset, str]): Error message, in case status of the query is error.
        id (Union[Unset, str]):
        project_id (Union[Unset, str]): Unique identifier of a project.
        query_string (Union[Unset, str]): String of the query e.g. SQL or JSON
        results (Union[Unset, str]): result dataobject IDs
        status (Union[Unset, QueryStatus]):
        updated_at (Union[Unset, str]):
    """

    created_at: Union[Unset, str] = UNSET
    created_by_user: Union[Unset, str] = UNSET
    error: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    project_id: Union[Unset, str] = UNSET
    query_string: Union[Unset, str] = UNSET
    results: Union[Unset, str] = UNSET
    status: Union[Unset, QueryStatus] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at
        created_by_user = self.created_by_user
        error = self.error
        id = self.id
        project_id = self.project_id
        query_string = self.query_string
        results = self.results
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by_user is not UNSET:
            field_dict["createdByUser"] = created_by_user
        if error is not UNSET:
            field_dict["error"] = error
        if id is not UNSET:
            field_dict["id"] = id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if query_string is not UNSET:
            field_dict["queryString"] = query_string
        if results is not UNSET:
            field_dict["results"] = results
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = d.pop("createdAt", UNSET)

        created_by_user = d.pop("createdByUser", UNSET)

        error = d.pop("error", UNSET)

        id = d.pop("id", UNSET)

        project_id = d.pop("projectId", UNSET)

        query_string = d.pop("queryString", UNSET)

        results = d.pop("results", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, QueryStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = QueryStatus(_status)

        updated_at = d.pop("updatedAt", UNSET)

        query = cls(
            created_at=created_at,
            created_by_user=created_by_user,
            error=error,
            id=id,
            project_id=project_id,
            query_string=query_string,
            results=results,
            status=status,
            updated_at=updated_at,
        )

        query.additional_properties = d
        return query

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
