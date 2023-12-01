from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="S3Parameters")


@attr.s(auto_attribs=True)
class S3Parameters:
    """parameters for the remote s3-compatible storage

    Attributes:
        access_key_id (Union[Unset, str]): s3 access key id
        bucket (Union[Unset, str]): s3 bucket
        region (Union[Unset, str]): s3 region
        secret_access_key (Union[Unset, str]): s3 secret access key
        url (Union[Unset, str]): s3 endpoint
    """

    access_key_id: Union[Unset, str] = UNSET
    bucket: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    secret_access_key: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access_key_id = self.access_key_id
        bucket = self.bucket
        region = self.region
        secret_access_key = self.secret_access_key
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_key_id is not UNSET:
            field_dict["accessKeyID"] = access_key_id
        if bucket is not UNSET:
            field_dict["bucket"] = bucket
        if region is not UNSET:
            field_dict["region"] = region
        if secret_access_key is not UNSET:
            field_dict["secretAccessKey"] = secret_access_key
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        access_key_id = d.pop("accessKeyID", UNSET)

        bucket = d.pop("bucket", UNSET)

        region = d.pop("region", UNSET)

        secret_access_key = d.pop("secretAccessKey", UNSET)

        url = d.pop("url", UNSET)

        s3_parameters = cls(
            access_key_id=access_key_id,
            bucket=bucket,
            region=region,
            secret_access_key=secret_access_key,
            url=url,
        )

        s3_parameters.additional_properties = d
        return s3_parameters

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
