from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_type import APIType
from ..models.database_type import DatabaseType
from ..models.local_data_source_type import LocalDataSourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DataSourceConfig")


@attr.s(auto_attribs=True)
class DataSourceConfig:
    """data source configuration

    Attributes:
        with_auth (Union[Unset, bool]): Whether the API requires authentication
        cert (Union[Unset, str]): If applicable, name of the certificate to access the datasource. Certificate should be
            in '/usr/local/share/datasource-certificates/<cert>.{crt/key}'
        database (Union[Unset, str]): Name of the database
        host (Union[Unset, str]): Hostname of the database
        local_type (Union[Unset, LocalDataSourceType]):
        insecure_skip_verify_tls (Union[Unset, bool]): This flag enables skipping TLS verification when connecting to
            the remote API data source. WARNING: this should not be used in production
        port (Union[Unset, str]): Port number of the database
        suricata_path (Union[Unset, str]): the path to the suricata JSON file.
        api_type (Union[Unset, APIType]):
        csv_path (Union[Unset, str]): the path to the CSV file.
        api_url (Union[Unset, str]): URL of the API
        database_type (Union[Unset, DatabaseType]): Type of the database
    """

    with_auth: Union[Unset, bool] = UNSET
    cert: Union[Unset, str] = UNSET
    database: Union[Unset, str] = UNSET
    host: Union[Unset, str] = UNSET
    local_type: Union[Unset, LocalDataSourceType] = UNSET
    insecure_skip_verify_tls: Union[Unset, bool] = UNSET
    port: Union[Unset, str] = UNSET
    suricata_path: Union[Unset, str] = UNSET
    api_type: Union[Unset, APIType] = UNSET
    csv_path: Union[Unset, str] = UNSET
    api_url: Union[Unset, str] = UNSET
    database_type: Union[Unset, DatabaseType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        with_auth = self.with_auth
        cert = self.cert
        database = self.database
        host = self.host
        local_type: Union[Unset, str] = UNSET
        if not isinstance(self.local_type, Unset):
            local_type = self.local_type.value

        insecure_skip_verify_tls = self.insecure_skip_verify_tls
        port = self.port
        suricata_path = self.suricata_path
        api_type: Union[Unset, str] = UNSET
        if not isinstance(self.api_type, Unset):
            api_type = self.api_type.value

        csv_path = self.csv_path
        api_url = self.api_url
        database_type: Union[Unset, str] = UNSET
        if not isinstance(self.database_type, Unset):
            database_type = self.database_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if with_auth is not UNSET:
            field_dict["withAuth"] = with_auth
        if cert is not UNSET:
            field_dict["cert"] = cert
        if database is not UNSET:
            field_dict["database"] = database
        if host is not UNSET:
            field_dict["host"] = host
        if local_type is not UNSET:
            field_dict["localType"] = local_type
        if insecure_skip_verify_tls is not UNSET:
            field_dict["insecureSkipVerifyTLS"] = insecure_skip_verify_tls
        if port is not UNSET:
            field_dict["port"] = port
        if suricata_path is not UNSET:
            field_dict["suricataPath"] = suricata_path
        if api_type is not UNSET:
            field_dict["APIType"] = api_type
        if csv_path is not UNSET:
            field_dict["CSVPath"] = csv_path
        if api_url is not UNSET:
            field_dict["api-url"] = api_url
        if database_type is not UNSET:
            field_dict["databaseType"] = database_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        with_auth = d.pop("withAuth", UNSET)

        cert = d.pop("cert", UNSET)

        database = d.pop("database", UNSET)

        host = d.pop("host", UNSET)

        _local_type = d.pop("localType", UNSET)
        local_type: Union[Unset, LocalDataSourceType]
        if isinstance(_local_type, Unset):
            local_type = UNSET
        else:
            local_type = LocalDataSourceType(_local_type)

        insecure_skip_verify_tls = d.pop("insecureSkipVerifyTLS", UNSET)

        port = d.pop("port", UNSET)

        suricata_path = d.pop("suricataPath", UNSET)

        _api_type = d.pop("APIType", UNSET)
        api_type: Union[Unset, APIType]
        if isinstance(_api_type, Unset):
            api_type = UNSET
        else:
            api_type = APIType(_api_type)

        csv_path = d.pop("CSVPath", UNSET)

        api_url = d.pop("api-url", UNSET)

        _database_type = d.pop("databaseType", UNSET)
        database_type: Union[Unset, DatabaseType]
        if isinstance(_database_type, Unset):
            database_type = UNSET
        else:
            database_type = DatabaseType(_database_type)

        data_source_config = cls(
            with_auth=with_auth,
            cert=cert,
            database=database,
            host=host,
            local_type=local_type,
            insecure_skip_verify_tls=insecure_skip_verify_tls,
            port=port,
            suricata_path=suricata_path,
            api_type=api_type,
            csv_path=csv_path,
            api_url=api_url,
            database_type=database_type,
        )

        data_source_config.additional_properties = d
        return data_source_config

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
