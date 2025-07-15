from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_type import APIType
from ..models.data_standard import DataStandard
from ..models.database_type import DatabaseType
from ..models.local_data_source_type import LocalDataSourceType
from ..models.mock_method import MockMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sql_metadata import SQLMetadata


T = TypeVar("T", bound="DataSourceConfig")


@attr.s(auto_attribs=True)
class DataSourceConfig:
    """data source configuration

    Attributes:
        api_type (Union[Unset, APIType]):
        csv_path (Union[Unset, str]): the path to the CSV file.
        sql_metadata (Union[Unset, SQLMetadata]): The metadata required to translate cross-standard queries to SQL for a
            datasource.
        api_url (Union[Unset, str]): URL of the API
        cert (Union[Unset, str]): If applicable, name of the certificate to access the datasource. Certificate should be
            in '/usr/local/share/datasource-certificates/<cert>.{crt/key}'
        data_standard (Union[Unset, DataStandard]):
        database (Union[Unset, str]): Name of the database
        database_type (Union[Unset, DatabaseType]): Type of the database
        generator_config (Union[Unset, str]): The configuration of the generator, encoded as a JSON string.
        generator_type (Union[Unset, MockMethod]): Method used to generate the mock data.
        host (Union[Unset, str]): Hostname of the database
        insecure_skip_verify_tls (Union[Unset, bool]): This flag enables skipping TLS verification when connecting to
            the remote API data source. WARNING: this should not be used in production
        local_type (Union[Unset, LocalDataSourceType]):
        port (Union[Unset, str]): Port number of the database
        s_3_bucket (Union[Unset, str]): Name of the S3 bucket
        s_3_default_object_key (Union[Unset, str]): Default object key to use when querying the S3 bucket
        s_3_region (Union[Unset, str]): Region of the S3 bucket
        s_3url (Union[Unset, str]): URL of the S3
        suricata_path (Union[Unset, str]): the path to the suricata JSON file.
        with_auth (Union[Unset, bool]): Whether the API requires authentication
    """

    api_type: Union[Unset, APIType] = UNSET
    csv_path: Union[Unset, str] = UNSET
    sql_metadata: Union[Unset, "SQLMetadata"] = UNSET
    api_url: Union[Unset, str] = UNSET
    cert: Union[Unset, str] = UNSET
    data_standard: Union[Unset, DataStandard] = UNSET
    database: Union[Unset, str] = UNSET
    database_type: Union[Unset, DatabaseType] = UNSET
    generator_config: Union[Unset, str] = UNSET
    generator_type: Union[Unset, MockMethod] = UNSET
    host: Union[Unset, str] = UNSET
    insecure_skip_verify_tls: Union[Unset, bool] = UNSET
    local_type: Union[Unset, LocalDataSourceType] = UNSET
    port: Union[Unset, str] = UNSET
    s_3_bucket: Union[Unset, str] = UNSET
    s_3_default_object_key: Union[Unset, str] = UNSET
    s_3_region: Union[Unset, str] = UNSET
    s_3url: Union[Unset, str] = UNSET
    suricata_path: Union[Unset, str] = UNSET
    with_auth: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        api_type: Union[Unset, str] = UNSET
        if not isinstance(self.api_type, Unset):
            api_type = self.api_type.value

        csv_path = self.csv_path
        sql_metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sql_metadata, Unset):
            sql_metadata = self.sql_metadata.to_dict()

        api_url = self.api_url
        cert = self.cert
        data_standard: Union[Unset, str] = UNSET
        if not isinstance(self.data_standard, Unset):
            data_standard = self.data_standard.value

        database = self.database
        database_type: Union[Unset, str] = UNSET
        if not isinstance(self.database_type, Unset):
            database_type = self.database_type.value

        generator_config = self.generator_config
        generator_type: Union[Unset, str] = UNSET
        if not isinstance(self.generator_type, Unset):
            generator_type = self.generator_type.value

        host = self.host
        insecure_skip_verify_tls = self.insecure_skip_verify_tls
        local_type: Union[Unset, str] = UNSET
        if not isinstance(self.local_type, Unset):
            local_type = self.local_type.value

        port = self.port
        s_3_bucket = self.s_3_bucket
        s_3_default_object_key = self.s_3_default_object_key
        s_3_region = self.s_3_region
        s_3url = self.s_3url
        suricata_path = self.suricata_path
        with_auth = self.with_auth

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_type is not UNSET:
            field_dict["APIType"] = api_type
        if csv_path is not UNSET:
            field_dict["CSVPath"] = csv_path
        if sql_metadata is not UNSET:
            field_dict["SQLMetadata"] = sql_metadata
        if api_url is not UNSET:
            field_dict["api-url"] = api_url
        if cert is not UNSET:
            field_dict["cert"] = cert
        if data_standard is not UNSET:
            field_dict["dataStandard"] = data_standard
        if database is not UNSET:
            field_dict["database"] = database
        if database_type is not UNSET:
            field_dict["databaseType"] = database_type
        if generator_config is not UNSET:
            field_dict["generatorConfig"] = generator_config
        if generator_type is not UNSET:
            field_dict["generatorType"] = generator_type
        if host is not UNSET:
            field_dict["host"] = host
        if insecure_skip_verify_tls is not UNSET:
            field_dict["insecureSkipVerifyTLS"] = insecure_skip_verify_tls
        if local_type is not UNSET:
            field_dict["localType"] = local_type
        if port is not UNSET:
            field_dict["port"] = port
        if s_3_bucket is not UNSET:
            field_dict["s3Bucket"] = s_3_bucket
        if s_3_default_object_key is not UNSET:
            field_dict["s3DefaultObjectKey"] = s_3_default_object_key
        if s_3_region is not UNSET:
            field_dict["s3Region"] = s_3_region
        if s_3url is not UNSET:
            field_dict["s3URL"] = s_3url
        if suricata_path is not UNSET:
            field_dict["suricataPath"] = suricata_path
        if with_auth is not UNSET:
            field_dict["withAuth"] = with_auth

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sql_metadata import SQLMetadata

        d = src_dict.copy()
        _api_type = d.pop("APIType", UNSET)
        api_type: Union[Unset, APIType]
        if isinstance(_api_type, Unset):
            api_type = UNSET
        else:
            api_type = APIType(_api_type)

        csv_path = d.pop("CSVPath", UNSET)

        _sql_metadata = d.pop("SQLMetadata", UNSET)
        sql_metadata: Union[Unset, SQLMetadata]
        if isinstance(_sql_metadata, Unset):
            sql_metadata = UNSET
        else:
            sql_metadata = SQLMetadata.from_dict(_sql_metadata)

        api_url = d.pop("api-url", UNSET)

        cert = d.pop("cert", UNSET)

        _data_standard = d.pop("dataStandard", UNSET)
        data_standard: Union[Unset, DataStandard]
        if isinstance(_data_standard, Unset):
            data_standard = UNSET
        else:
            data_standard = DataStandard(_data_standard)

        database = d.pop("database", UNSET)

        _database_type = d.pop("databaseType", UNSET)
        database_type: Union[Unset, DatabaseType]
        if isinstance(_database_type, Unset):
            database_type = UNSET
        else:
            database_type = DatabaseType(_database_type)

        generator_config = d.pop("generatorConfig", UNSET)

        _generator_type = d.pop("generatorType", UNSET)
        generator_type: Union[Unset, MockMethod]
        if isinstance(_generator_type, Unset):
            generator_type = UNSET
        else:
            generator_type = MockMethod(_generator_type)

        host = d.pop("host", UNSET)

        insecure_skip_verify_tls = d.pop("insecureSkipVerifyTLS", UNSET)

        _local_type = d.pop("localType", UNSET)
        local_type: Union[Unset, LocalDataSourceType]
        if isinstance(_local_type, Unset):
            local_type = UNSET
        else:
            local_type = LocalDataSourceType(_local_type)

        port = d.pop("port", UNSET)

        s_3_bucket = d.pop("s3Bucket", UNSET)

        s_3_default_object_key = d.pop("s3DefaultObjectKey", UNSET)

        s_3_region = d.pop("s3Region", UNSET)

        s_3url = d.pop("s3URL", UNSET)

        suricata_path = d.pop("suricataPath", UNSET)

        with_auth = d.pop("withAuth", UNSET)

        data_source_config = cls(
            api_type=api_type,
            csv_path=csv_path,
            sql_metadata=sql_metadata,
            api_url=api_url,
            cert=cert,
            data_standard=data_standard,
            database=database,
            database_type=database_type,
            generator_config=generator_config,
            generator_type=generator_type,
            host=host,
            insecure_skip_verify_tls=insecure_skip_verify_tls,
            local_type=local_type,
            port=port,
            s_3_bucket=s_3_bucket,
            s_3_default_object_key=s_3_default_object_key,
            s_3_region=s_3_region,
            s_3url=s_3url,
            suricata_path=suricata_path,
            with_auth=with_auth,
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
