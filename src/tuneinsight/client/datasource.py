"""Classes to interact with datasources in a Tune Insight instance."""

from typing import Any
from io import StringIO
import pandas as pd

from tuneinsight.api.sdk.types import Response
from tuneinsight.api.sdk.types import File
from tuneinsight.api.sdk import Client
from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.api.api_datasource import post_data_source
from tuneinsight.api.sdk.api.api_datasource import put_data_source_data
from tuneinsight.api.sdk.api.api_datasource import delete_data_source
from tuneinsight.api.sdk.api.api_dataobject import post_data_object
from tuneinsight.client.validation import validate_response
from tuneinsight.client.dataobject import DataObject


class DataSource:
    """
    DataSource represents a datasource stored on a Tune Insight instance.

    The data used for computations in a Tune Insight instance is represented by
    a generic interface (datasource), which abstracts from how the data is
    actually stored and managed. Each datasource has a unique name.

    Class methods can be used to instantiate datasources of various types,
    including CSV files, PostgreS databases, APIs, and Pandas DataFrame.

    """

    model: models.DataSource = None
    client: Client = None

    def __init__(self, model: models.DataSource, client: Client):
        self.model = model
        self.client = client

    @classmethod
    def _from_definition(cls, client: Client, definition: models.DataSourceDefinition):
        """
        Creates a new datasource on the backend given the data source definition.

        Args:
            client (Client): the client to use to interact with the datasource
            definition (models.DataSourceDefinition): the definition of the datasource
        """
        response: Response[models.DataSource] = post_data_source.sync_detailed(
            client=client, json_body=definition
        )
        validate_response(response)
        return cls(model=response.parsed, client=client)

    @classmethod
    def local(cls, client: Client, name: str, clear_if_exists: bool = False):
        """
        Creates a new local datasource without any data.

        Args:
            client (Client): the client to use to interact with the datasource
            name (str): the name to give to the datasource.
            clear_if_exists (bool, optional): whether to replace an existing datasource with the same name.
        """
        definition = default_datasource_definition()
        definition.name = name
        definition.clear_if_exists = clear_if_exists
        ds_config_type = models.DataSourceConfigType.LOCALDATASOURCECONFIG
        ds_conf = models.LocalDataSourceConfig(type=ds_config_type)
        definition.config = ds_conf
        definition.type = "local"

        return cls._from_definition(client, definition=definition)

    @classmethod
    def database(
        cls,
        client: Client,
        config: models.DatabaseConnectionInfo,
        name: str,
        clear_if_exists: bool = False,
        secret_id: str = None,
    ):
        """
        Creates a new postgres database datasource.

        Args:
            client (Client): the client to use to interact with the datasource
            config (models.DatabaseConnectionInfo): the database configuration
            name (str, optional): the name to give to the datasource. Defaults to "".
            clear_if_exists (bool, optional): whether to try to clear any existing data source with the same name.
            secret_id (str, optional): secret id that stores the database credentials on the KMS connected to the instance.
        """
        definition = default_datasource_definition()
        definition.name = name
        definition.clear_if_exists = clear_if_exists
        definition.type = "database"
        ds_config_type = models.DataSourceConfigType.DATABASEDATASOURCECONFIG

        cred_id = "db-creds"
        if secret_id is None:
            credentials = models.Credentials(
                username=config.user, password=config.password, id=cred_id
            )
            credential_provider = models.LocalCredentialsProvider(
                type=models.CredentialsProviderType.LOCALCREDENTIALSPROVIDER,
                credentials=[credentials],
            )
        else:
            credentials = models.AzureKeyVaultCredentialsProviderMappingsItem(
                creds_id=cred_id, secret_id=secret_id
            )
            credential_provider = models.AzureKeyVaultCredentialsProvider(
                type=models.CredentialsProviderType.AZUREKEYVAULTCREDENTIALSPROVIDER,
                mappings=[credentials],
            )
        ds_config = models.DatabaseDataSourceConfig(
            type=ds_config_type, connection_info=config
        )
        definition.credentials_provider = credential_provider
        definition.config = ds_config

        return cls._from_definition(client, definition=definition)

    @classmethod
    def from_api(
        cls,
        client: Client,
        api_type: models.APIConnectionInfoType,
        api_url: str,
        api_token: str,
        name: str,
        clear_if_exists: bool = False,
        cert: str = "",
    ):
        """
        Creates a new API datasource.

        Args:
            client (Client): the client to use to interact with the datasource
            config (models.PostgresDatabaseConfig): the postgres configuration
            name (str): the name to give to the datasource.
            clear_if_exists (bool, optional): whether to replace an existing datasource with the same name.
            cert (str, optional): name of the certificate to use for this datasource
                (must be accessible in note at "/usr/local/share/datasource-certificates/{cert}.pem,.key").
        """
        definition = default_datasource_definition()
        definition.name = name
        definition.clear_if_exists = clear_if_exists
        definition.type = "api"

        ds_config = models.ApiDataSourceConfig(
            type=models.DataSourceConfigType.APIDATASOURCECONFIG
        )
        ds_config.connection_info = models.APIConnectionInfo(
            api_token=api_token, api_url=api_url, type=api_type, cert=cert
        )
        definition.config = ds_config

        return cls._from_definition(client, definition=definition)

    @classmethod
    def from_dataframe(
        cls,
        client: Client,
        dataframe: pd.DataFrame,
        name: str,
        clear_if_exists: bool = False,
    ):
        """
        Creates a new datasource from a Pandas DataFrame.

        Args:
            client (Client): the client to use to interact with the datasource
            dataframe (pd.DataFrame): the data to upload in the newly created datasource.
            name (str): the name to give to the datasource.
            clear_if_exists (bool, optional): whether to replace an existing datasource with the same name.
        """
        ds = cls.local(client, name, clear_if_exists)
        ds.load_dataframe(df=dataframe)
        return ds

    def __str__(self):
        model = self.model
        return f"id: {model.unique_id}, name: {model.name}, type: {model.type}, createdAt: {model.created_at}"

    def get_id(self) -> str:
        """
        Returns the unique id of this datasource.

        Returns:
            str: the id as a a string
        """
        return self.model.unique_id

    def adapt(
        self, do_type: models.DataObjectType, query: Any = "", json_path: str = ""
    ) -> DataObject:
        """
        Creates a dataobject from the data in this datasource (or the output of a query on it).

        Args:
            do_type (models.DataObjectType): the type of DataObject to create.
            query (str, optional): a query selecting a subset of the data. The default is "" for CSV datasource (all records),
                but note that this is an invalid query for database datasources.
            json_path (str, optional): JsonPath expression to retrieve data from within JSON-structured data. Defaults to "".

        Returns:
            DataObject: The newly created dataobject holding the data.
        """
        method = models.DataObjectCreationMethod.DATASOURCE
        definition = models.PostDataObjectJsonBody(
            method=method,
            data_source_id=self.get_id(),
            type=do_type,
            query=query,
            json_path=json_path,
        )
        response: Response[models.DataObject] = post_data_object.sync_detailed(
            client=self.client, json_body=definition
        )
        validate_response(response)
        return DataObject(model=response.parsed, client=self.client)

    def load_csv_data(self, path: str):
        """
        Loads the data in a CSV file (at "path") to this datasource.

        Args:
            path (str): path to the CSV file.
        """
        with open(path, mode="+rb") as f:
            file_type = File(payload=f, file_name="test")
            mpd = models.PutDataSourceDataMultipartData(
                data_source_request_data=file_type
            )
            response: Response[models.DataSource] = put_data_source_data.sync_detailed(
                client=self.client,
                data_source_id=self.model.unique_id,
                multipart_data=mpd,
            )
            f.close()
            validate_response(response)

    def load_dataframe(self, df: pd.DataFrame):
        """
        Uploads a dataframe to use as datasource content.

        Args:
            df (pd.DataFrame): the data to upload.
        """
        f = StringIO(initial_value="")
        df.to_csv(f, index=False)
        mpd = models.PutDataSourceDataMultipartData(
            data_source_request_data_raw=f.getvalue()
        )
        response: Response[models.DataSource] = put_data_source_data.sync_detailed(
            client=self.client, data_source_id=self.model.unique_id, multipart_data=mpd
        )
        validate_response(response)

    def get_dataframe(self, query: Any = "", json_path: str = "") -> pd.DataFrame:
        """
        Returns the data contained in the datasource as a pd.DataFrame.

        Args:
            query (str, optional): a query selecting a subset of the data. The default is "" for CSV datasource (all records),
                but note that this is an invalid query for database datasources.
            json_path (str, optional): JsonPath expression to retrieve data from within JSON-structured data. Defaults to "".

        Raises:
            AuthorizationError: if the client is not the owner of the datasource.
        """
        do = self.adapt(
            do_type=models.DataObjectType.TABLE, query=query, json_path=json_path
        )
        df = do.get_dataframe()
        do.delete()
        return df

    def delete(self):
        """
        Deletes this datasource.
        """
        response: Response[Any] = delete_data_source.sync_detailed(
            client=self.client, data_source_id=self.model.unique_id
        )
        validate_response(response)


## Internal methods to manipulate configurations.


def default_datasource_definition() -> models.DataSourceDefinition:
    """
    Returns a default-valued DataSourceDefinition.

    Returns:
        models.DataSourceDefinition: the definition with default values
    """
    return models.DataSourceDefinition(
        consent_type=models.DataSourceConsentType.UNKNOWN
    )


def new_postgres_config(
    host: str, port: str, name: str, user: str, password: str
) -> models.DatabaseConnectionInfo:
    """Convert a Postgres configuration to a models.DatabaseConnectionInfo."""
    return models.DatabaseConnectionInfo(
        type=models.DatabaseType.POSTGRES,
        host=host,
        port=port,
        database=name,
        user=user,
        password=password,
    )


def new_mariadb_config(
    host: str = "mariadb",
    port: str = "3306",
    name: str = "geco_0",
    user: str = "geco",
    password: str = "geco",
) -> models.DatabaseConnectionInfo:
    """Convert a MariaDB configuration to a models.DatabaseConnectionInfo."""
    return models.DatabaseConnectionInfo(
        type=models.DatabaseType.MYSQL,
        host=host,
        port=port,
        database=name,
        user=user,
        password=password,
    )
