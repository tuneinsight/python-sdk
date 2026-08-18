from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advanced_filter import AdvancedFilter
    from ..models.query_output_variable import QueryOutputVariable


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
            output_variables (Union[Unset, List['QueryOutputVariable']]): Additional variables to extract from each entity
                that passes the filter. These variables are
                extracted "context-free", i.e. they are not attached to a specific filter. Effectively, an
                entry of the corresponding series is selected, and its field is extracted as is. TIQL++ feature.
            tiql_core (Union[Unset, bool]): Whether this query is written in TIQL-core, a restrictive subset of TIQL. TIQL-
                Core is as expressive
                as TIQL (i.e. every TIQL query can be written in TIQL-Core) but has strict requirements on the query
                structure. This flag is intended to be set by the backend during transpiling and not set manually.
            unit (Union[Unset, str]): The unit of the feasibility query (i.e., what is a record -- should be "patient").
            variables (Union[Unset, List[str]]): Names of the variables to extract from each entity that passes the filter.
                These variables
                are created by passing SeriesFilters and uniquely identified by a name. The order of the variables
                in this list is the same as the column names in the output table.
    """

    filter_: Union[Unset, "AdvancedFilter"] = UNSET
    output_variables: Union[Unset, List["QueryOutputVariable"]] = UNSET
    tiql_core: Union[Unset, bool] = UNSET
    unit: Union[Unset, str] = UNSET
    variables: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        filter_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        output_variables: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.output_variables, Unset):
            output_variables = []
            for output_variables_item_data in self.output_variables:
                output_variables_item = output_variables_item_data.to_dict()

                output_variables.append(output_variables_item)

        tiql_core = self.tiql_core
        unit = self.unit
        variables: Union[Unset, List[str]] = UNSET
        if not isinstance(self.variables, Unset):
            variables = self.variables

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if output_variables is not UNSET:
            field_dict["outputVariables"] = output_variables
        if tiql_core is not UNSET:
            field_dict["tiqlCore"] = tiql_core
        if unit is not UNSET:
            field_dict["unit"] = unit
        if variables is not UNSET:
            field_dict["variables"] = variables

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.advanced_filter import AdvancedFilter
        from ..models.query_output_variable import QueryOutputVariable

        d = src_dict.copy()
        _filter_ = d.pop("filter", UNSET)
        filter_: Union[Unset, AdvancedFilter]
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = AdvancedFilter.from_dict(_filter_)

        output_variables = []
        _output_variables = d.pop("outputVariables", UNSET)
        for output_variables_item_data in _output_variables or []:
            output_variables_item = QueryOutputVariable.from_dict(output_variables_item_data)

            output_variables.append(output_variables_item)

        tiql_core = d.pop("tiqlCore", UNSET)

        unit = d.pop("unit", UNSET)

        variables = cast(List[str], d.pop("variables", UNSET))

        cross_standard_query = cls(
            filter_=filter_,
            output_variables=output_variables,
            tiql_core=tiql_core,
            unit=unit,
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
