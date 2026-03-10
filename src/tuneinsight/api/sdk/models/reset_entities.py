from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResetEntities")


@attr.s(auto_attribs=True)
class ResetEntities:
    """which entities to/were reset

    Attributes:
        catalog (Union[Unset, bool]): If set to true, all catalog (of all data sources and any instance) occurrences are
            deleted.
        computations (Union[Unset, bool]): Delete all computations
        data_preparation_sessions (Union[Unset, bool]): Delete all data preparation sessions
        dataobjects (Union[Unset, bool]): Delete all data objects
        datasources (Union[Unset, bool]): Delete all data sources
        models (Union[Unset, bool]): Delete all data models
        networks (Union[Unset, bool]): Delete all networks from storage
        projects (Union[Unset, bool]): Delete all projects
        reload_terminologies (Union[Unset, bool]): If set to true, terminologies are reloaded from the bundled csv
            files.
        sessions (Union[Unset, bool]): Delete all sessions from storage
        settings (Union[Unset, bool]): Reset instance settings to default
    """

    catalog: Union[Unset, bool] = False
    computations: Union[Unset, bool] = False
    data_preparation_sessions: Union[Unset, bool] = False
    dataobjects: Union[Unset, bool] = False
    datasources: Union[Unset, bool] = False
    models: Union[Unset, bool] = False
    networks: Union[Unset, bool] = False
    projects: Union[Unset, bool] = False
    reload_terminologies: Union[Unset, bool] = False
    sessions: Union[Unset, bool] = False
    settings: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        catalog = self.catalog
        computations = self.computations
        data_preparation_sessions = self.data_preparation_sessions
        dataobjects = self.dataobjects
        datasources = self.datasources
        models = self.models
        networks = self.networks
        projects = self.projects
        reload_terminologies = self.reload_terminologies
        sessions = self.sessions
        settings = self.settings

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if catalog is not UNSET:
            field_dict["catalog"] = catalog
        if computations is not UNSET:
            field_dict["computations"] = computations
        if data_preparation_sessions is not UNSET:
            field_dict["dataPreparationSessions"] = data_preparation_sessions
        if dataobjects is not UNSET:
            field_dict["dataobjects"] = dataobjects
        if datasources is not UNSET:
            field_dict["datasources"] = datasources
        if models is not UNSET:
            field_dict["models"] = models
        if networks is not UNSET:
            field_dict["networks"] = networks
        if projects is not UNSET:
            field_dict["projects"] = projects
        if reload_terminologies is not UNSET:
            field_dict["reloadTerminologies"] = reload_terminologies
        if sessions is not UNSET:
            field_dict["sessions"] = sessions
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        catalog = d.pop("catalog", UNSET)

        computations = d.pop("computations", UNSET)

        data_preparation_sessions = d.pop("dataPreparationSessions", UNSET)

        dataobjects = d.pop("dataobjects", UNSET)

        datasources = d.pop("datasources", UNSET)

        models = d.pop("models", UNSET)

        networks = d.pop("networks", UNSET)

        projects = d.pop("projects", UNSET)

        reload_terminologies = d.pop("reloadTerminologies", UNSET)

        sessions = d.pop("sessions", UNSET)

        settings = d.pop("settings", UNSET)

        reset_entities = cls(
            catalog=catalog,
            computations=computations,
            data_preparation_sessions=data_preparation_sessions,
            dataobjects=dataobjects,
            datasources=datasources,
            models=models,
            networks=networks,
            projects=projects,
            reload_terminologies=reload_terminologies,
            sessions=sessions,
            settings=settings,
        )

        reset_entities.additional_properties = d
        return reset_entities

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
