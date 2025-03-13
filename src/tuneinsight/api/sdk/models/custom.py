from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.preprocessing_operation_type import PreprocessingOperationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Custom")


@attr.s(auto_attribs=True)
class Custom:
    """
    Attributes:
        type (PreprocessingOperationType): type of preprocessing operation
        compatible_with_differential_privacy (Union[Unset, bool]): Whether this preprocessing operation is compatible
            with differential privacy. For this to be the case,
            it needs to be stable (each input record creates at most one output record) and have a statically
            determined (data-indenpendent) set of columns. Contact the Tune Insight team for more details on DP
            compatibility.
        description (Union[Unset, str]): description given to the operation, for documentation purposes.
        function (Union[Unset, str]): function definition which must respect the following format:
            `def <custom_function_name>(df: pd.DataFrame) -> pd.DataFrame
                 <your code here>
                 return df`
        name (Union[Unset, str]): name given to the operation. The name has no impact on the operation
            and the name given to the function
        output_columns (Union[Unset, List[str]]): If defined, the list of all columns that could be  _added_ by this
            function to the dataframe. If provided, the output
            columns are checked against this value.  This is required under differential privacy, and is recommended even
            when
            not using DP, as it enables column selections in the frontend (from dry-runs). If the custom operation modifies
            other columns in the datasets, it is recommended to follow this operation with a select.
    """

    type: PreprocessingOperationType
    compatible_with_differential_privacy: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    function: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    output_columns: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        compatible_with_differential_privacy = self.compatible_with_differential_privacy
        description = self.description
        function = self.function
        name = self.name
        output_columns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.output_columns, Unset):
            output_columns = self.output_columns

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if compatible_with_differential_privacy is not UNSET:
            field_dict["compatibleWithDifferentialPrivacy"] = compatible_with_differential_privacy
        if description is not UNSET:
            field_dict["description"] = description
        if function is not UNSET:
            field_dict["function"] = function
        if name is not UNSET:
            field_dict["name"] = name
        if output_columns is not UNSET:
            field_dict["outputColumns"] = output_columns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        compatible_with_differential_privacy = d.pop("compatibleWithDifferentialPrivacy", UNSET)

        description = d.pop("description", UNSET)

        function = d.pop("function", UNSET)

        name = d.pop("name", UNSET)

        output_columns = cast(List[str], d.pop("outputColumns", UNSET))

        custom = cls(
            type=type,
            compatible_with_differential_privacy=compatible_with_differential_privacy,
            description=description,
            function=function,
            name=name,
            output_columns=output_columns,
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
