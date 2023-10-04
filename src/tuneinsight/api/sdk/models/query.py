from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.query_status import QueryStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_results import QueryResults


T = TypeVar("T", bound="Query")


@attr.s(auto_attribs=True)
class Query:
    """Data source query

    Attributes:
        results (Union[Unset, QueryResults]): result dataobject IDs
        updated_at (Union[Unset, str]):
        created_at (Union[Unset, str]):
        created_by_user (Union[Unset, str]): ID of user who created the project
        error (Union[Unset, str]): Error message, in case status of the query is error.
        project_id (Union[Unset, str]): Unique identifier of a project.
        id (Union[Unset, str]):
        query_string (Union[Unset, str]): String of the query e.g. SQL or JSON
        status (Union[Unset, QueryStatus]):
    """

    results: Union[Unset, "QueryResults"] = UNSET
    updated_at: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by_user: Union[Unset, str] = UNSET
    error: Union[Unset, str] = UNSET
    project_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    query_string: Union[Unset, str] = UNSET
    status: Union[Unset, QueryStatus] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        results: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.results, Unset):
            results = self.results.to_dict()

        updated_at = self.updated_at
        created_at = self.created_at
        created_by_user = self.created_by_user
        error = self.error
        project_id = self.project_id
        id = self.id
        query_string = self.query_string
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if results is not UNSET:
            field_dict["results"] = results
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by_user is not UNSET:
            field_dict["createdByUser"] = created_by_user
        if error is not UNSET:
            field_dict["error"] = error
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if id is not UNSET:
            field_dict["id"] = id
        if query_string is not UNSET:
            field_dict["queryString"] = query_string
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.query_results import QueryResults

        d = src_dict.copy()
        _results = d.pop("results", UNSET)
        results: Union[Unset, QueryResults]
        if isinstance(_results, Unset):
            results = UNSET
        else:
            results = QueryResults.from_dict(_results)

        updated_at = d.pop("updatedAt", UNSET)

        created_at = d.pop("createdAt", UNSET)

        created_by_user = d.pop("createdByUser", UNSET)

        error = d.pop("error", UNSET)

        project_id = d.pop("projectId", UNSET)

        id = d.pop("id", UNSET)

        query_string = d.pop("queryString", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, QueryStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = QueryStatus(_status)

        query = cls(
            results=results,
            updated_at=updated_at,
            created_at=created_at,
            created_by_user=created_by_user,
            error=error,
            project_id=project_id,
            id=id,
            query_string=query_string,
            status=status,
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
