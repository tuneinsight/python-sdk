from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_source_compound_query import DataSourceCompoundQuery
    from ..models.data_source_query import DataSourceQuery


T = TypeVar("T", bound="ComputationDataSourceParameters")


@attr.s(auto_attribs=True)
class ComputationDataSourceParameters:
    """Parameters used to query the datasource from each node before the computation

    Attributes:
        compound_disabled (Union[Unset, bool]): when true, then even if the compound query is specified, it is not taken
            into account (enables keeping previously defined queries)
        compound_query (Union[Unset, DataSourceCompoundQuery]): definition of datasource queries for each node in the
            computation
        data_source_query (Union[Unset, DataSourceQuery]): schema used for the query
        only_root_query (Union[Unset, bool]): Whether or not the query should only be executed at the root node of the
            computation
    """

    compound_disabled: Union[Unset, bool] = UNSET
    compound_query: Union[Unset, "DataSourceCompoundQuery"] = UNSET
    data_source_query: Union[Unset, "DataSourceQuery"] = UNSET
    only_root_query: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        compound_disabled = self.compound_disabled
        compound_query: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.compound_query, Unset):
            compound_query = self.compound_query.to_dict()

        data_source_query: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data_source_query, Unset):
            data_source_query = self.data_source_query.to_dict()

        only_root_query = self.only_root_query

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if compound_disabled is not UNSET:
            field_dict["compoundDisabled"] = compound_disabled
        if compound_query is not UNSET:
            field_dict["compoundQuery"] = compound_query
        if data_source_query is not UNSET:
            field_dict["dataSourceQuery"] = data_source_query
        if only_root_query is not UNSET:
            field_dict["onlyRootQuery"] = only_root_query

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_source_compound_query import DataSourceCompoundQuery
        from ..models.data_source_query import DataSourceQuery

        d = src_dict.copy()
        compound_disabled = d.pop("compoundDisabled", UNSET)

        _compound_query = d.pop("compoundQuery", UNSET)
        compound_query: Union[Unset, DataSourceCompoundQuery]
        if isinstance(_compound_query, Unset):
            compound_query = UNSET
        else:
            compound_query = DataSourceCompoundQuery.from_dict(_compound_query)

        _data_source_query = d.pop("dataSourceQuery", UNSET)
        data_source_query: Union[Unset, DataSourceQuery]
        if isinstance(_data_source_query, Unset):
            data_source_query = UNSET
        else:
            data_source_query = DataSourceQuery.from_dict(_data_source_query)

        only_root_query = d.pop("onlyRootQuery", UNSET)

        computation_data_source_parameters = cls(
            compound_disabled=compound_disabled,
            compound_query=compound_query,
            data_source_query=data_source_query,
            only_root_query=only_root_query,
        )

        computation_data_source_parameters.additional_properties = d
        return computation_data_source_parameters

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
