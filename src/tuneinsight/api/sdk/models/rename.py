from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.preprocessing_operation_type import PreprocessingOperationType
from ..models.rename_axis import RenameAxis
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rename_mapper import RenameMapper


T = TypeVar("T", bound="Rename")


@attr.s(auto_attribs=True)
class Rename:
    """
    Attributes:
        type (PreprocessingOperationType): type of preprocessing operation
        mapper (RenameMapper): transformations to apply to that axis’ values
        copy (Union[Unset, bool]): whether to return a copy
        errors (Union[Unset, bool]): Control raising of exceptions on invalid data for provided dtype
        axis (Union[Unset, RenameAxis]): axis to target with mapper
    """

    type: PreprocessingOperationType
    mapper: "RenameMapper"
    copy: Union[Unset, bool] = UNSET
    errors: Union[Unset, bool] = UNSET
    axis: Union[Unset, RenameAxis] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        mapper = self.mapper.to_dict()

        copy = self.copy
        errors = self.errors
        axis: Union[Unset, str] = UNSET
        if not isinstance(self.axis, Unset):
            axis = self.axis.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "mapper": mapper,
            }
        )
        if copy is not UNSET:
            field_dict["copy"] = copy
        if errors is not UNSET:
            field_dict["errors"] = errors
        if axis is not UNSET:
            field_dict["axis"] = axis

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.rename_mapper import RenameMapper

        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        mapper = RenameMapper.from_dict(d.pop("mapper"))

        copy = d.pop("copy", UNSET)

        errors = d.pop("errors", UNSET)

        _axis = d.pop("axis", UNSET)
        axis: Union[Unset, RenameAxis]
        if isinstance(_axis, Unset):
            axis = UNSET
        else:
            axis = RenameAxis(_axis)

        rename = cls(
            type=type,
            mapper=mapper,
            copy=copy,
            errors=errors,
            axis=axis,
        )

        rename.additional_properties = d
        return rename

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
