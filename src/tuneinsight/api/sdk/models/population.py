from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advanced_filter import AdvancedFilter
    from ..models.population_database_query_builder import PopulationDatabaseQueryBuilder


T = TypeVar("T", bound="Population")


@attr.s(auto_attribs=True)
class Population:
    """Defines a population as a filter.
    Used as the core study population in a project's policy to restrict data source queries at computation time.

        Attributes:
            database_query_builder (Union[Unset, PopulationDatabaseQueryBuilder]): options for the database query builder
                used to define the study population.
            target_filter (Union[Unset, AdvancedFilter]): Abstract subclass of a filter for cross-standard queries.
    """

    database_query_builder: Union[Unset, "PopulationDatabaseQueryBuilder"] = UNSET
    target_filter: Union[Unset, "AdvancedFilter"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        database_query_builder: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.database_query_builder, Unset):
            database_query_builder = self.database_query_builder.to_dict()

        target_filter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.target_filter, Unset):
            target_filter = self.target_filter.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if database_query_builder is not UNSET:
            field_dict["databaseQueryBuilder"] = database_query_builder
        if target_filter is not UNSET:
            field_dict["targetFilter"] = target_filter

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.advanced_filter import AdvancedFilter
        from ..models.population_database_query_builder import PopulationDatabaseQueryBuilder

        d = src_dict.copy()
        _database_query_builder = d.pop("databaseQueryBuilder", UNSET)
        database_query_builder: Union[Unset, PopulationDatabaseQueryBuilder]
        if isinstance(_database_query_builder, Unset):
            database_query_builder = UNSET
        else:
            database_query_builder = PopulationDatabaseQueryBuilder.from_dict(_database_query_builder)

        _target_filter = d.pop("targetFilter", UNSET)
        target_filter: Union[Unset, AdvancedFilter]
        if isinstance(_target_filter, Unset):
            target_filter = UNSET
        else:
            target_filter = AdvancedFilter.from_dict(_target_filter)

        population = cls(
            database_query_builder=database_query_builder,
            target_filter=target_filter,
        )

        population.additional_properties = d
        return population

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
