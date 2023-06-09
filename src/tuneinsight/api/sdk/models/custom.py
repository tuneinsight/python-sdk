from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.preprocessing_operation_type import PreprocessingOperationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Custom")


@attr.s(auto_attribs=True)
class Custom:
    """
    Attributes:
        type (PreprocessingOperationType): type of preprocessing operation
        description (Union[Unset, str]): description given to the operation, for documentation purposes.
        function (Union[Unset, str]): function definition which must respect the following format:
            `def <custom_function_name>(df: pd.DataFrame) -> pd.DataFrame
                 <your code here>
                 return df`
        name (Union[Unset, str]): name given to the operation. The name has no impact on the operation
            and the name given to the function
    """

    type: PreprocessingOperationType
    description: Union[Unset, str] = UNSET
    function: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        description = self.description
        function = self.function
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if function is not UNSET:
            field_dict["function"] = function
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        description = d.pop("description", UNSET)

        function = d.pop("function", UNSET)

        name = d.pop("name", UNSET)

        custom = cls(
            type=type,
            description=description,
            function=function,
            name=name,
        )

        custom.additional_properties = d
        return custom

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
