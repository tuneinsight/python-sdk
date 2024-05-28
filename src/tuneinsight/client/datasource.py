"""Classes to interact with datasources in a Tune Insight instance."""

from typing import Any
from io import StringIO
import pandas as pd

from tuneinsight.api.sdk.types import Response
from tuneinsight.api.sdk.types import File
from tuneinsight.api.sdk import Client
from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import Unset, UNSET
from tuneinsight.api.sdk.api.api_datagen import post_synthetic_dataset
from tuneinsight.api.sdk.api.api_datasource import (
    post_data_source,
    put_data_source_data,
    delete_data_source,
    get_data_source,
)
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
        self.query_parameters = None

    ## Methods to create a datasource.

    @classmethod
    def fetch_from_id(cls, client: Client, datasource_id: str):
        """
        Creates a datasource object relating to a datasource in the backend.

        Args:
            client (Client): the client to use to interact with the datasource
            datasource_id (str): the unique identifier of the datasource.
        """
        ds_response: Response[models.DataSource] = get_data_source.sync_detailed(
            client=client, data_source_id=datasource_id
        )
        validate_response(ds_response)
        return cls(model=ds_response.parsed, client=client)

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
        definition.type = models.DataSourceType.LOCAL
        return cls._from_definition(client, definition=definition)

    @classmethod
    def database(
        cls,
        client: Client,
        config: models.DataSourceConfig,
        credentials: models.Credentials,
        name: str,
        clear_if_exists: bool = False,
    ):
        """
        Creates a new postgres database datasource.

        Args:
            client (Client): the client to use to interact with the datasource
            config (models.DataSourceConfig): the database configuration
            name (str, optional): the name to give to the datasource. Defaults to "".
            clear_if_exists (bool, optional): whether to try to clear any existing data source with the same name.
            credentials_id (str, optional): secret id that stores the database credentials on the KMS connected to the instance.
        """
        definition = default_datasource_definition()
        definition.name = name
        definition.clear_if_exists = clear_if_exists
        definition.type = models.DataSourceType.DATABASE
        definition.configuration = config
        definition.credentials = credentials

        return cls._from_definition(client, definition=definition)

    @classmethod
    def from_api(
        cls,
        client: Client,
        api_type: models.APIType,
        api_url: str,
        api_token: str,
        name: str,
        clear_if_exists: bool = False,
        cert: str = "",
        insecure_skip_verify_tls: bool = False,
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
        definition.type = models.DataSourceType.API
        definition.configuration = models.DataSourceConfig(
            api_url=api_url,
            api_type=api_type,
            cert=cert,
            insecure_skip_verify_tls=insecure_skip_verify_tls,
        )
        definition.credentials = models.Credentials(api_token=api_token)
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
        return f"id: {model.id}, name: {model.name}, type: {model.type}, createdAt: {model.created_at}"

    def get_id(self) -> str:
        """
        Returns the unique id of this datasource.

        Returns:
            str: the id as a a string
        """
        return self.model.id

    @property
    def is_mock(self) -> bool:
        """Whether this datasource contains mock/synthetic data, and should not be used in production."""
        return self.model.is_mock

    ## Methods to manipulate a datasource object.

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
                data_source_id=self.model.id,
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
            client=self.client, data_source_id=self.model.id, multipart_data=mpd
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
        if not query and self.query_parameters is not None:
            query = self.query_parameters.database_query
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
            client=self.client, data_source_id=self.model.id
        )
        validate_response(response)

    def synthesize(
        self,
        table: str = UNSET,
        query: str = UNSET,
        name: str = UNSET,
        num_rows: int = UNSET,
        epsilon: float = UNSET,
    ) -> "DataSource":
        """
        Generates a synthetic dataset that mimics this datasource.

        This creates a new database datasource that contains synthetic data
        with the same data structure (attributes and data types) as well as
        some statistical properties of the data.

        One of table or query must be specified to generate data from a
        database datasource. If neither are provided, the datasource name
        is used instead, but that can potentially cause issues.

        Args:
            table (str, optional): the table for which to generate synthetic data.
            query (str, optional): the data query to perform on the data to get
            name (str, optional): name of the synthetic datasource. If not provided,
                synthetic_{datasource_name} is used instead.
            num_rows (int, optional): number of rows to generate. If not provided,
                the synthetic dataset will have the same number of rows as this datasource.
            epsilon (float, optional): if set, use a differentially private generation
                method with this value of epsilon. The synthetic data produced by this
                method is guaranteed to be privacy-preserving, but will be less accurate.
                A good default value is epsilon=1. This will work better with large datasets.
        """
        # If no query is provided, but this datasource has a local query, use it.
        if query is None and self.query_parameters is not None:
            query = self.query_parameters.database_query
        # If the user specified neither the query nor the table name, use the datasource name as table.
        # This is a default case that will work for mock data.
        if isinstance(table, Unset) and isinstance(query, Unset):
            table = self.model.name
        response = post_synthetic_dataset.sync_detailed(
            client=self.client,
            data_source_id=self.get_id(),
            num_rows=num_rows,
            table=table,
            query=query,
            table_name=name,
            dp_epsilon=epsilon,
        )
        validate_response(response)
        ds = DataSource(response.parsed, self.client)
        # For synthetic data, the table name is the same as the datasource name, so set the local query.
        if not isinstance(ds.model.name, Unset):
            ds.set_query(f"select * from {ds.model.name}")
        return ds

    ## Methods to interact with queries etc.
    def set_query(self, query: str):
        """
        Sets the database query to use for this datasource.

        When this datasource is used in a project, its query will override the query defined
        in the local data selection of the project (if any), but not the query defined in the
        computation definition (which take precedence).

        Note that this is specific to the Diapason implementation, and the query is not
        persisted on the Tune Insight instance.

        Args
            query (str): the SQL query to use to fet the data from the datasource.
        """
        self.query_parameters = models.DataSourceQuery(database_query=query)


## Internal functions to manipulate configurations.


def default_datasource_definition() -> models.DataSourceDefinition:
    """
    Returns a default-valued DataSourceDefinition.

    Returns:
        models.DataSourceDefinition: the definition with default values
    """
    return models.DataSourceDefinition(
        consent_type=models.DataSourceConsentType.UNKNOWN
    )


def new_credentials(
    username: str = "", password: str = "", token: str = "", credentials_id: str = None
):
    """
    Creates a new credentials class with the correct credentials type.

    Args:
        username (str, optional): the username. Defaults to "".
        password (str, optional): the password. Defaults to "".
        token (str, optional): the API token. Defaults to "".
        credentials_id (str, optional): the secret ID to fetch the credentials remotely, if set, then the credentials type will be set to Azure Key Vault. Defaults to None.

    Returns:
        _type_: _description_
    """
    if credentials_id is None:
        return models.Credentials(username=username, password=password, api_token=token)
    return models.Credentials(
        credentials_id=credentials_id, type=models.CredentialsType.AZUREKEYVAULT
    )


def new_postgres_config(host: str, port: str, name: str) -> models.DataSourceConfig:
    """Convert a Postgres configuration to a models.DataSourceConfig."""
    return models.DataSourceConfig(
        database_type=models.DatabaseType.POSTGRES,
        host=host,
        port=port,
        database=name,
    )


def new_mariadb_config(
    host: str = "mariadb",
    port: str = "3306",
    name: str = "geco_0",
) -> models.DataSourceConfig:
    """Convert a MariaDB configuration to a models.DataSourceConfig."""
    return models.DataSourceConfig(
        database_type=models.DatabaseType.MYSQL,
        host=host,
        port=port,
        database=name,
    )
