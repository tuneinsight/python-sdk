from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.duration import Duration
    from ..models.input_transformation import InputTransformation


T = TypeVar("T", bound="ConceptField")


@attr.s(auto_attribs=True)
class ConceptField:
    """A reference to a field in the TIQL data model. Used to specify what data is being accessed.

    Attributes:
        concept (Union[Unset, str]): The name of the concept whose entries are being accessed. If there is no ambiguity,
            i.e. the `conceptField` is used at a point
            in a TIQL query where it could refer to only one concept, then this field is optional.
        field (Union[Unset, str]): The name of the field to access on the concept.
        target_field (Union[Unset, str]): Optional target field through which the virtual join is added. When a concept
            has multiple fields that map to the same virtual source, this specifies which physical join path to use.
        time_offset (Union[Unset, Duration]): definition of a date-independent time interval
        transformation (Union[Unset, InputTransformation]): Transformation applied to a value extracted from the data as
            part of a TIQL query, before
            it is used in a filter.
    """

    concept: Union[Unset, str] = UNSET
    field: Union[Unset, str] = UNSET
    target_field: Union[Unset, str] = UNSET
    time_offset: Union[Unset, "Duration"] = UNSET
    transformation: Union[Unset, "InputTransformation"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        concept = self.concept
        field = self.field
        target_field = self.target_field
        time_offset: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.time_offset, Unset):
            time_offset = self.time_offset.to_dict()

        transformation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.transformation, Unset):
            transformation = self.transformation.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if concept is not UNSET:
            field_dict["concept"] = concept
        if field is not UNSET:
            field_dict["field"] = field
        if target_field is not UNSET:
            field_dict["targetField"] = target_field
        if time_offset is not UNSET:
            field_dict["timeOffset"] = time_offset
        if transformation is not UNSET:
            field_dict["transformation"] = transformation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.duration import Duration
        from ..models.input_transformation import InputTransformation

        d = src_dict.copy()
        concept = d.pop("concept", UNSET)

        field = d.pop("field", UNSET)

        target_field = d.pop("targetField", UNSET)

        _time_offset = d.pop("timeOffset", UNSET)
        time_offset: Union[Unset, Duration]
        if isinstance(_time_offset, Unset):
            time_offset = UNSET
        else:
            time_offset = Duration.from_dict(_time_offset)

        _transformation = d.pop("transformation", UNSET)
        transformation: Union[Unset, InputTransformation]
        if isinstance(_transformation, Unset):
            transformation = UNSET
        else:
            transformation = InputTransformation.from_dict(_transformation)

        concept_field = cls(
            concept=concept,
            field=field,
            target_field=target_field,
            time_offset=time_offset,
            transformation=transformation,
        )

        concept_field.additional_properties = d
        return concept_field

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
