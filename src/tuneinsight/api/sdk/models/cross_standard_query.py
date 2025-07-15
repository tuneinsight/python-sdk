from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advanced_filter import AdvancedFilter


T = TypeVar("T", bound="CrossStandardQuery")


@attr.s(auto_attribs=True)
class CrossStandardQuery:
    """A Cross-Standard Feasibility Query (TIQL). This structure represents feasibility queries
    independently of the underlying data structure, and can be used to define workflows at a
    higher level of abstraction. In order to perform the query on a datasource, it will first
    be converted to the appropriate query language by the backend.
    Performing a query results in a cohort, a table containing a fixed set of variables for a
    subset of the records in the data. As such, the query defines two operations: a filtering
    operation that selects which records to extract data from, and a variable extraction that
    defines what values are computed for each extracted record.

        Attributes:
            filter_ (Union[Unset, AdvancedFilter]): Abstract subclass of a filter for cross-standard queries.
            variables (Union[Unset, List[str]]): The variables to be extracted from the cohort. Each variable should either
                be the name
                of a feature (directly attached to a record), or a unique identifier defined in a filter
                for series variables (variables attached to a record that contain a list of values).
    """

    filter_: Union[Unset, "AdvancedFilter"] = UNSET
    variables: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        filter_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        variables: Union[Unset, List[str]] = UNSET
        if not isinstance(self.variables, Unset):
            variables = self.variables

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if variables is not UNSET:
            field_dict["variables"] = variables

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.advanced_filter import AdvancedFilter

        d = src_dict.copy()
        _filter_ = d.pop("filter", UNSET)
        filter_: Union[Unset, AdvancedFilter]
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = AdvancedFilter.from_dict(_filter_)

        variables = cast(List[str], d.pop("variables", UNSET))

        cross_standard_query = cls(
            filter_=filter_,
            variables=variables,
        )

        cross_standard_query.additional_properties = d
        return cross_standard_query

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
