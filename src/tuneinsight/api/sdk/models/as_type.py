from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.preprocessing_operation_type import PreprocessingOperationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.as_type_type_map import AsTypeTypeMap


T = TypeVar("T", bound="AsType")


@attr.s(auto_attribs=True)
class AsType:
    """
    Attributes:
        type (PreprocessingOperationType): type of preprocessing operation
        type_map (AsTypeTypeMap): map from column name to destination type
        errors (Union[Unset, bool]): If true, an exception is raised on invalid data for provided dtype.
    """

    type: PreprocessingOperationType
    type_map: "AsTypeTypeMap"
    errors: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        type_map = self.type_map.to_dict()

        errors = self.errors

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "type_map": type_map,
            }
        )
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.as_type_type_map import AsTypeTypeMap

        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        type_map = AsTypeTypeMap.from_dict(d.pop("type_map"))

        errors = d.pop("errors", UNSET)

        as_type = cls(
            type=type,
            type_map=type_map,
            errors=errors,
        )

        as_type.additional_properties = d
        return as_type

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
