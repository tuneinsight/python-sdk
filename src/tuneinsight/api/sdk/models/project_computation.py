from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.computation import Computation
    from ..models.project import Project


T = TypeVar("T", bound="ProjectComputation")


@attr.s(auto_attribs=True)
class ProjectComputation:
    """
    Attributes:
        computation (Union[Unset, Computation]): Metadata of a computation.
        project (Union[Unset, Project]): Project entity definition.
    """

    computation: Union[Unset, "Computation"] = UNSET
    project: Union[Unset, "Project"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        computation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.computation, Unset):
            computation = self.computation.to_dict()

        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if computation is not UNSET:
            field_dict["computation"] = computation
        if project is not UNSET:
            field_dict["project"] = project

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.computation import Computation
        from ..models.project import Project

        d = src_dict.copy()
        _computation = d.pop("computation", UNSET)
        computation: Union[Unset, Computation]
        if isinstance(_computation, Unset):
            computation = UNSET
        else:
            computation = Computation.from_dict(_computation)

        _project = d.pop("project", UNSET)
        project: Union[Unset, Project]
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = Project.from_dict(_project)

        project_computation = cls(
            computation=computation,
            project=project,
        )

        project_computation.additional_properties = d
        return project_computation

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
