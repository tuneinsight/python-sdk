"""Classes to interact with datasources in a Tune Insight instance."""

import contextlib
from typing import Any, List
from io import StringIO
import pandas as pd

from tuneinsight.api.sdk.types import Response
from tuneinsight.api.sdk import Client
from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import Unset, UNSET, value_if_unset
from tuneinsight.api.sdk.api.api_datagen import post_synthetic_dataset
from tuneinsight.api.sdk.api.api_datasource import (
    post_data_source,
    patch_data_source_data,
    delete_data_source,
    get_data_source,
    patch_data_source,
)
from tuneinsight.api.sdk.api.api_dataobject import post_data_object

from tuneinsight.client.validation import validate_response
from tuneinsight.client.dataobject import DataObject
from tuneinsight.computations.policy import DataPolicy
from tuneinsight.utils.tracking import ProgressTracker, new_task_id
from tuneinsight.utils.io import generate_dataframe_chunks, generate_csv_records


class DataSource:
    """
    A `DataSource` represents a datasource stored on a Tune Insight instance.

    The data used for computations in a Tune Insight instance is represented by
    a generic interface (datasource), which abstracts from how the data is
    actually stored and managed. Each datasource has a unique name.

    Class methods can be used to instantiate datasources of various types,
    including CSV files, PostgreS databases, APIs, and Pandas DataFrame.

    Note that a `DataSource` object in the Python SDK does not contain any
    data. It only serves as a way to represent and interact with a datasource
    on the server side.

    See the https://dev.tuneinsight.com/docs/Usage/python-sdk/data-management/
    documentation page for details on datasources.

    """

    model: models.DataSource = None
    client: Client = None

    upload_chunk_size: int

    def __init__(self, model: models.DataSource, client: Client):
        self.model = model
        self.client = client
        self.local_query_parameters = None
        self.upload_chunk_size = 2048  # uploads 2048 records at each request.

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
    def local(
        cls,
        client: Client,
        name: str,
        clear_if_exists: bool = False,
        query_enabled: bool = False,
        access_scope: models.AccessScope = models.AccessScope.ORGANIZATION,
    ):
        """
        Creates a new local datasource without any data.

        Args:
            client (Client): the client to use to interact with the datasource
            name (str): the name to give to the datasource.
            clear_if_exists (bool, optional): whether to replace an existing datasource with the same name.
            query_enabled (bool, optional): whether to enable direct querying outside of computations on the datasource.
            access_scope (models.AccessScope, optional): scope of the datasource, limiting who can access it (organization by default).
        """
        definition = _default_datasource_definition()
        definition.name = name
        definition.clear_if_exists = clear_if_exists
        definition.type = models.DataSourceType.LOCAL
        definition.query_enabled = query_enabled
        definition.access_scope = access_scope
        return cls._from_definition(client, definition=definition)

    @classmethod
    def database(
        cls,
        client: Client,
        config: models.DataSourceConfig,
        credentials: models.Credentials,
        name: str,
        clear_if_exists: bool = False,
        access_scope: models.AccessScope = models.AccessScope.ORGANIZATION,
    ):
        """
        Creates a new database datasource.

        The Tune Insight instance will connect to the database described in `config`.
        Note that the database needs to be reachable for the instance for this to work.

        Args:
            client (Client): the client to use to interact with the datasource
            config (models.DataSourceConfig): the database configuration. Use the `new_postgres_config`
                and `new_mariadb_config` functions in this module to create the configuration.
            credentials (models.Credentials): the credentials needed to access this datasource from the server.
            name (str, optional): the name to give to the datasource. Defaults to "".
            clear_if_exists (bool, optional): whether to try to clear any existing data source with the same name.
            access_scope (models.AccessScope, optional): scope of the datasource, limiting who can access it (organization by default).
        """
        definition = _default_datasource_definition()
        definition.name = name
        definition.clear_if_exists = clear_if_exists
        definition.type = models.DataSourceType.DATABASE
        definition.configuration = config
        definition.credentials = credentials
        definition.access_scope = access_scope

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
        access_scope: models.AccessScope = models.AccessScope.ORGANIZATION,
    ):
        """
        Creates a new API datasource.

        When a computation is run using this datasource, the Tune Insight instance
        will pull data from the API configured by the parameters.

        Args:
            client (Client): the client to use to interact with the datasource
            api_type (models.APIType): The type of the API.
            api_url (str): the URL to access the API.
            api_token (str): the token needed to authenticate to the API.
            name (str): the name to give to the datasource.
            clear_if_exists (bool, optional): whether to replace an existing datasource with the same name.
            cert (str, optional): name of the certificate to use for this datasource
                (must be accessible in note at "/usr/local/share/datasource-certificates/{cert}.pem,.key").
            insecure_skip_verify_tls (bool, optional): Whether to skip TLS verification (⚠️ insecure). Defaults to False.
            access_scope (models.AccessScope, optional): scope of the datasource, limiting who can access it (organization by default).
        """
        definition = _default_datasource_definition()
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
        definition.access_scope = access_scope
        return cls._from_definition(client, definition=definition)

    @classmethod
    def from_dataframe(
        cls,
        client: Client,
        dataframe: pd.DataFrame,
        name: str,
        clear_if_exists: bool = False,
        query_enabled: bool = False,
        access_scope: models.AccessScope = models.AccessScope.ORGANIZATION,
    ):
        """
        Creates a new datasource from a `pandas.DataFrame`.

        The data contained in the `DataFrame` is uploaded to the Tune Insight instance.

        Args:
            client (Client): the client to use to interact with the datasource
            dataframe (pd.DataFrame): the data to upload in the newly created datasource.
            name (str): the name to give to the datasource.
            clear_if_exists (bool, optional): whether to replace an existing datasource with the same name.
            query_enabled (bool, optional): whether to enable direct querying outside of computations on the datasource.
            access_scope (models.AccessScope, optional): scope of the datasource, limiting who can access it (organization by default).
        """
        ds = cls.local(
            client, name, clear_if_exists, query_enabled, access_scope=access_scope
        )
        ds.upload_data(df=dataframe)
        return ds

    def __str__(self):
        model = self.model
        return f"id: {model.id}, name: {model.name}, type: {model.type}, createdAt: {model.created_at}"

    def get_id(self) -> str:
        """
        Returns the unique identifier of this datasource.

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

    def upload_data(
        self,
        df: pd.DataFrame = None,
        csv_path: str = None,
        table_name: str = "",
        replace: bool = False,
        verbose: bool = False,
        skip_invalid_rows: bool = False,
        delimiter: str = ",",
    ):
        """
        Uploads data to a data source. Data can be either appended or replaced.

        Args:
            df (pd.DataFrame, optional): dataframe to upload. Defaults to None.
            csv_path (str, optional): Path to the csv file containing the data to upload. Defaults to None.
            table_name (str, optional): name of the table to upload the data to. Required when the data source is a database. Defaults to "".
            replace (bool, optional): Whether to replace the existing data from the table. Defaults to False.
            verbose (bool, optional): When set to true, the upload progress is shown. Defaults to False.
            skip_invalid_rows (bool, optional): When set to true, then rows that are detected as invalid as they do not comply with the schema
                                                will no be inserted into the data source. Default to False.
            delimiter (str, optional): delimiter to use when parsing the csv data. Defaults to ",".

        Raises:
            ValueError: If no data is provided or the table name is missing when required.
        """
        if self.model.type not in [
            models.DataSourceType.DATABASE,
            models.DataSourceType.LOCAL,
        ]:
            raise ValueError(
                f"{self.model.type} data sources do not currently support data upload"
            )
        if self.model.type == models.DataSourceType.DATABASE and table_name == "":
            raise ValueError("table name must be provided")

        if df is not None:
            generator = generate_dataframe_chunks(df, self.upload_chunk_size)
        elif csv_path is not None:
            generator = generate_csv_records(csv_path, self.upload_chunk_size)
        else:
            raise ValueError("missing a datasource: specify either df or csv_path")

        first_chunk = True
        uploaded_records = 0
        for chunk_df in generator:
            self._upload_data_file(
                chunk_df,
                table_name=table_name,
                replace=first_chunk and replace,
                delimiter=delimiter,
                skip_invalid_rows=skip_invalid_rows,
            )
            uploaded_records += self.upload_chunk_size
            if verbose:
                print(f"uploaded {uploaded_records} records", end="\r")
            first_chunk = False
        if verbose:
            print()

    def _upload_data_file(
        self,
        df: pd.DataFrame,
        table_name: str = "",
        replace: bool = False,
        skip_invalid_rows: bool = False,
        delimiter: str = ",",
    ):
        f = StringIO(initial_value="")
        df.to_csv(f, index=False)
        self._upload_data(
            data=f.getvalue(),
            table_name=table_name,
            replace=replace,
            skip_invalid_rows=skip_invalid_rows,
            delimiter=delimiter,
        )

    def _upload_data(
        self,
        data: str,
        table_name: str = "",
        replace: bool = False,
        skip_invalid_rows: bool = False,
        delimiter: str = ",",
    ):
        response: Response[models.DataUploadResponse] = (
            patch_data_source_data.sync_detailed(
                client=self.client,
                data_source_id=self.model.id,
                json_body=models.DataUploadParams(
                    data=data,
                    replace=replace,
                    table_name=table_name,
                    delimiter=delimiter,
                    skip_invalid_rows=skip_invalid_rows,
                ),
            )
        )
        validate_response(response)

    def get_dataframe(self, query: Any = "", json_path: str = "") -> pd.DataFrame:
        """
        Returns the data contained in the datasource as a pd.DataFrame.

        🔥 Warning: this operation transfers (potentially private) data from the
        Tune Insight instance to the client. While the communication is encrypted,
        the data will be returned unencrypted in the memory of the Python process.

        ⚠️ Only the owner of the datasource is allowed to perform this operation.

        Args:
            query (str, optional): a query selecting a subset of the data. The default is "" for CSV datasource (all records),
                but note that this is an invalid query for database datasources.
            json_path (str, optional): JsonPath expression to retrieve data from within JSON-structured data. Defaults to "".

        Raises:
            AuthorizationError: if the client is not the owner of the datasource.
        """
        if not query and self.local_query_parameters is not None:
            query = self.local_query_parameters.database_query
        do = self.adapt(
            do_type=models.DataObjectType.TABLE, query=query, json_path=json_path
        )
        df = do.get_dataframe()
        do.delete()
        return df

    def delete(self):
        """
        Deletes this datasource.

        For most datasources, this does not delete the underlying data. For instance,
        deleting a database datasource only removes the connection and credentials,
        but the database remains unchanged.

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
        track_progress: bool = False,
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
            track_progress (bool, optional): whether to track the progress of the generation task.
        """
        # If no query is provided, but this datasource has a local query, use it.
        if query is None and self.local_query_parameters is not None:
            query = self.local_query_parameters.database_query
        # If the user specified neither the query nor the table name, use the datasource name as table.
        # This is a default case that will work for mock data.
        if isinstance(table, Unset) and isinstance(query, Unset):
            table = self.model.name
        task_id = new_task_id() if track_progress else None
        if track_progress:
            tracker = ProgressTracker(task_id)
            tracker.start_background(self.client)
        response = post_synthetic_dataset.sync_detailed(
            client=self.client,
            data_source_id=self.get_id(),
            num_rows=num_rows,
            table=table,
            query=query,
            table_name=name,
            dp_epsilon=epsilon,
            tracking_id=task_id,
        )
        validate_response(response)
        ds = DataSource(response.parsed, self.client)
        # For synthetic data, the table name is the same as the datasource name, so set the local query.
        if not isinstance(ds.model.name, Unset):
            ds.set_local_query(f"select * from {ds.model.name}")
        return ds

    ## Methods to interact with queries etc.
    def set_local_query(self, query: str):
        """
        Sets a default database query to use for this datasource.

        This default query will then be used when interacting with the datasource directly,
        e.g., to generate synthetic data. However, this query will not be used in projects.
        To set the database query to use in a project, use the local data selection with
        `project.get_local_data_selection()` or set the computation's query.

        Note that this is specific to the Diapason implementation, and the query is not
        persisted on the Tune Insight instance.

        Args
            query (str): the SQL query to use to fet the data from the datasource.
        """
        self.local_query_parameters = models.DataSourceQuery(database_query=query)

    ## Schema handling

    def get_schemas(self, name: str = None) -> List[models.DatasetSchema]:
        """Returns all dataset schemas that have been infered on this datasource.

        Args:
            name (str, optional): if provided, only return schemas with this name.

        Returns:
            List[models.DatasetSchema]: all schemas inferred from this datasource, or, if filtered
                by name, only the schemas with this name.
        """
        schemas = value_if_unset(self.model.inferred_schemas, [])
        if name is not None:

            def filter_by_name(schema: models.DatasetSchema):
                return schema.name == name

            return filter(filter_by_name, schemas)
        return schemas

    ## Methods to set the policies.

    def get_policy(self) -> DataPolicy:
        """Returns the data policy on this datasource."""
        return DataPolicy.from_model(self.model.policy)

    def set_policy(self, policy: DataPolicy):
        """Sets the data policy of this datasource."""
        self._patch(models.DataSourceDefinition(policy=policy))

    @contextlib.contextmanager
    def policy(self):
        """Context manager to handle policies on a datasource."""
        policy = self.get_policy()
        yield policy
        self.set_policy(policy)

    ## Methods to modify other parts of a datasource.

    def enable_cache(self, duration: int = 1):
        """Enables query results to be cached to speed up repeatedly querying the datasource.

        Args:
            duration (int, optional): duration in hours for which the cache is kept. Defaults to 1.
        """
        if duration <= 0:
            raise ValueError("duration must be a positive integer")
        self._patch(models.DataSourceDefinition(cache_duration=duration))

    def disable_cache(self):
        """Disables the caching of query results."""
        self._patch(models.DataSourceDefinition(cache_duration=0))

    def _patch(self, update: models.DataSourceDefinition):
        """Patches this datasource with the provided definition."""
        response = patch_data_source.sync_detailed(
            data_source_id=self.get_id(),
            client=self.client,
            json_body=update,
        )
        validate_response(response)


## Internal functions to manipulate configurations.


def _default_datasource_definition() -> models.DataSourceDefinition:
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
    """Converts a Postgres configuration to a models.DataSourceConfig."""
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


class RemoteDataSource:
    """
    Represents a DataSource hosted on another instance that is visible on the network.

    Some datasources can be marked as network visible, in which case other participants
    are able to learn of their existence. In cases where a participant is not a contributor,
    they can specify that this datasource should be used by the remote participant in a
    project.

    Note that only some metadata is available about remote data sources, and it is not
    possible to edit them in any way.
    """

    def __init__(self, model: models.DataSource):
        self.model = model

    def __repr__(self):
        return f"Remote Datasource {self.model.name} (type {self.model.type})."

    @property
    def auto_match(self) -> models.DataSourceDefinition:
        """
        Returns this data source as an auto-match criterion for use in a project.

        This is the mechanism used to specify that this datasource should be used in
        the project by the remote client. If auto-matched is enabled on the client side,
        the Tune Insight instance will automatically set the datasource of the project
        to match the type, and if possible the name of the auto-match criterion.
        """
        return models.DataSourceDefinition(name=self.model.name, type=self.model.type)
