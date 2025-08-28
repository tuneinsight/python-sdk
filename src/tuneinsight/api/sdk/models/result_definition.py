from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.visualization_type import VisualizationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ResultDefinition")


@attr.s(auto_attribs=True)
class ResultDefinition:
    """user-defined computation result fields

    Attributes:
        display_breakdown (Union[Unset, None, bool]): frontend flag used to toggle the display of the local breakdown
            when available.
        display_confidence_intervals (Union[Unset, None, bool]): frontend flag used to toggle the display of the
            confidence intervals in differentially private results.
        display_local (Union[Unset, None, bool]): frontend flag used to toggle the display of the local result when the
            result has both a collective and local output.
        display_raw_results (Union[Unset, None, bool]): frontend flag used to choose whether to display raw or post-
            processed results in the case of inconsistencies created by noise.
        is_large (Union[Unset, None, bool]): frontend flag describing whether this result should be displayed large.
        shared (Union[Unset, None, bool]): if set to true, the result is shared with users from the same project in the
            same organization.
        tags (Union[Unset, List[str]]): user-defined values describing tags attached to this result.
        title (Union[Unset, str]): title given to the result (mostly for the frontend)
        visualization_type (Union[Unset, VisualizationType]): represents the appropriate visualization type for a
            result.
    """

    display_breakdown: Union[Unset, None, bool] = UNSET
    display_confidence_intervals: Union[Unset, None, bool] = UNSET
    display_local: Union[Unset, None, bool] = UNSET
    display_raw_results: Union[Unset, None, bool] = UNSET
    is_large: Union[Unset, None, bool] = UNSET
    shared: Union[Unset, None, bool] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    title: Union[Unset, str] = UNSET
    visualization_type: Union[Unset, VisualizationType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_breakdown = self.display_breakdown
        display_confidence_intervals = self.display_confidence_intervals
        display_local = self.display_local
        display_raw_results = self.display_raw_results
        is_large = self.is_large
        shared = self.shared
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        title = self.title
        visualization_type: Union[Unset, str] = UNSET
        if not isinstance(self.visualization_type, Unset):
            visualization_type = self.visualization_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_breakdown is not UNSET:
            field_dict["displayBreakdown"] = display_breakdown
        if display_confidence_intervals is not UNSET:
            field_dict["displayConfidenceIntervals"] = display_confidence_intervals
        if display_local is not UNSET:
            field_dict["displayLocal"] = display_local
        if display_raw_results is not UNSET:
            field_dict["displayRawResults"] = display_raw_results
        if is_large is not UNSET:
            field_dict["isLarge"] = is_large
        if shared is not UNSET:
            field_dict["shared"] = shared
        if tags is not UNSET:
            field_dict["tags"] = tags
        if title is not UNSET:
            field_dict["title"] = title
        if visualization_type is not UNSET:
            field_dict["visualizationType"] = visualization_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        display_breakdown = d.pop("displayBreakdown", UNSET)

        display_confidence_intervals = d.pop("displayConfidenceIntervals", UNSET)

        display_local = d.pop("displayLocal", UNSET)

        display_raw_results = d.pop("displayRawResults", UNSET)

        is_large = d.pop("isLarge", UNSET)

        shared = d.pop("shared", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        title = d.pop("title", UNSET)

        _visualization_type = d.pop("visualizationType", UNSET)
        visualization_type: Union[Unset, VisualizationType]
        if isinstance(_visualization_type, Unset):
            visualization_type = UNSET
        else:
            visualization_type = VisualizationType(_visualization_type)

        result_definition = cls(
            display_breakdown=display_breakdown,
            display_confidence_intervals=display_confidence_intervals,
            display_local=display_local,
            display_raw_results=display_raw_results,
            is_large=is_large,
            shared=shared,
            tags=tags,
            title=title,
            visualization_type=visualization_type,
        )

        result_definition.additional_properties = d
        return result_definition

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
