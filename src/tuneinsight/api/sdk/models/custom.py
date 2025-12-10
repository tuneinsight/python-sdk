from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.preprocessing_operation_type import PreprocessingOperationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_additional_inputs import CustomAdditionalInputs


T = TypeVar("T", bound="Custom")


@attr.s(auto_attribs=True)
class Custom:
    """
    Attributes:
        type (PreprocessingOperationType): type of preprocessing operation
        additional_inputs (Union[Unset, CustomAdditionalInputs]): Optional additional keyword arguments to pass to the
            custom function. Should contain simple values that can be marshalled
            to and from JSON (e.g., no custom classes).
        compatible_with_differential_privacy (Union[Unset, bool]): Whether this preprocessing operation is compatible
            with differential privacy. For this to be the case,
            it needs to be stable (each input record creates at most one output record) and have a statically
            determined (data-independent) set of columns. Contact the Tune Insight team for more details on DP
            compatibility.
        description (Union[Unset, str]): description given to the operation, for documentation purposes.
        function (Union[Unset, str]): function definition which must respect the following format (with optional
            additional_inputs keyword arguments):
            `def <custom_function_name>(df: pd.DataFrame, **additional_inputs) -> pd.DataFrame
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
        requires_full_table (Union[Unset, bool]): whether the function must be applied to all table rows at the same
            time for this custom operation to work correctly.
            When enabled, the preprocessing operations are applied on the full table instead of being applied in batches.
    """

    type: PreprocessingOperationType
    additional_inputs: Union[Unset, "CustomAdditionalInputs"] = UNSET
    compatible_with_differential_privacy: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    function: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    output_columns: Union[Unset, List[str]] = UNSET
    requires_full_table: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        additional_inputs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.additional_inputs, Unset):
            additional_inputs = self.additional_inputs.to_dict()

        compatible_with_differential_privacy = self.compatible_with_differential_privacy
        description = self.description
        function = self.function
        name = self.name
        output_columns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.output_columns, Unset):
            output_columns = self.output_columns

        requires_full_table = self.requires_full_table

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if additional_inputs is not UNSET:
            field_dict["additionalInputs"] = additional_inputs
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
        if requires_full_table is not UNSET:
            field_dict["requiresFullTable"] = requires_full_table

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.custom_additional_inputs import CustomAdditionalInputs

        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        _additional_inputs = d.pop("additionalInputs", UNSET)
        additional_inputs: Union[Unset, CustomAdditionalInputs]
        if isinstance(_additional_inputs, Unset):
            additional_inputs = UNSET
        else:
            additional_inputs = CustomAdditionalInputs.from_dict(_additional_inputs)

        compatible_with_differential_privacy = d.pop("compatibleWithDifferentialPrivacy", UNSET)

        description = d.pop("description", UNSET)

        function = d.pop("function", UNSET)

        name = d.pop("name", UNSET)

        output_columns = cast(List[str], d.pop("outputColumns", UNSET))

        requires_full_table = d.pop("requiresFullTable", UNSET)

        custom = cls(
            type=type,
            additional_inputs=additional_inputs,
            compatible_with_differential_privacy=compatible_with_differential_privacy,
            description=description,
            function=function,
            name=name,
            output_columns=output_columns,
            requires_full_table=requires_full_table,
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
