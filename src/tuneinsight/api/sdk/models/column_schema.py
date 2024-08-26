from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.column_schema_checks import ColumnSchemaChecks


T = TypeVar("T", bound="ColumnSchema")


@attr.s(auto_attribs=True)
class ColumnSchema:
    """
    Attributes:
        checks (Union[Unset, ColumnSchemaChecks]): optional additional checks
        coerce (Union[Unset, bool]): if set to true, the validation will first coerce the column into the corresponding
            dtype
            before applying the validation.
        description (Union[Unset, str]): informative description for the column
        dtype (Union[Unset, str]): expected data type for the column
            supported types:
            https://pandera.readthedocs.io/en/stable/dtype_validation.html#supported-pandas-datatypes
        nullable (Union[Unset, bool]): whether the column is allowed to contain null values.
        required (Union[Unset, None, bool]): if set to false, the column will be considered as optional in the dataset.
        title (Union[Unset, str]): name given to the column for informative purposes
    """

    checks: Union[Unset, "ColumnSchemaChecks"] = UNSET
    coerce: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    dtype: Union[Unset, str] = UNSET
    nullable: Union[Unset, bool] = UNSET
    required: Union[Unset, None, bool] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        checks: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.checks, Unset):
            checks = self.checks.to_dict()

        coerce = self.coerce
        description = self.description
        dtype = self.dtype
        nullable = self.nullable
        required = self.required
        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if checks is not UNSET:
            field_dict["checks"] = checks
        if coerce is not UNSET:
            field_dict["coerce"] = coerce
        if description is not UNSET:
            field_dict["description"] = description
        if dtype is not UNSET:
            field_dict["dtype"] = dtype
        if nullable is not UNSET:
            field_dict["nullable"] = nullable
        if required is not UNSET:
            field_dict["required"] = required
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.column_schema_checks import ColumnSchemaChecks

        d = src_dict.copy()
        _checks = d.pop("checks", UNSET)
        checks: Union[Unset, ColumnSchemaChecks]
        if isinstance(_checks, Unset):
            checks = UNSET
        else:
            checks = ColumnSchemaChecks.from_dict(_checks)

        coerce = d.pop("coerce", UNSET)

        description = d.pop("description", UNSET)

        dtype = d.pop("dtype", UNSET)

        nullable = d.pop("nullable", UNSET)

        required = d.pop("required", UNSET)

        title = d.pop("title", UNSET)

        column_schema = cls(
            checks=checks,
            coerce=coerce,
            description=description,
            dtype=dtype,
            nullable=nullable,
            required=required,
            title=title,
        )

        column_schema.additional_properties = d
        return column_schema

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
