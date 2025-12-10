from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.preprocessing_operation_type import PreprocessingOperationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AppendS3PresignedURLs")


@attr.s(auto_attribs=True)
class AppendS3PresignedURLs:
    """
    Attributes:
        type (PreprocessingOperationType): type of preprocessing operation
        input_columns (List[str]): the names of columns which contain S3 URLs / paths
        presigned_url_expiration (Union[Unset, int]): expiration time in minutes for the presigned URL (default 60
            minutes) Default: 60.
    """

    type: PreprocessingOperationType
    input_columns: List[str]
    presigned_url_expiration: Union[Unset, int] = 60
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        input_columns = self.input_columns

        presigned_url_expiration = self.presigned_url_expiration

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "inputColumns": input_columns,
            }
        )
        if presigned_url_expiration is not UNSET:
            field_dict["presignedURLExpiration"] = presigned_url_expiration

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        input_columns = cast(List[str], d.pop("inputColumns"))

        presigned_url_expiration = d.pop("presignedURLExpiration", UNSET)

        append_s3_presigned_ur_ls = cls(
            type=type,
            input_columns=input_columns,
            presigned_url_expiration=presigned_url_expiration,
        )

        append_s3_presigned_ur_ls.additional_properties = d
        return append_s3_presigned_ur_ls

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
