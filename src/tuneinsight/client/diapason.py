"""
`Diapason` defines the client used to interact with Tune Insight instances.
This client is initialized by connecting and authenticating to an instance.
The client serves as an entrypoint to the server, and can be used to interact
with all elements stored on the server side, such as dataobjects, datasources,
and projects.

"""

from contextlib import contextmanager
from typing import List, Union
import warnings
import webbrowser
import os
import attr
import pandas as pd

from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import UNSET, Response, is_unset
from tuneinsight.api.sdk import client as api_client
from tuneinsight.api.sdk.api.api_project import (
    post_project,
    get_project,
    get_project_list,
    post_project_join,
)
from tuneinsight.api.sdk.api.api_datasource import get_data_source_list
from tuneinsight.api.sdk.api.api_dataobject import get_data_object
from tuneinsight.api.sdk.api.api_infos import get_infos
from tuneinsight.api.sdk.api.health import get_health
from tuneinsight.api.sdk.api.api_users import get_user_info

from tuneinsight.client.dataobject import DataObject
from tuneinsight.client.datasource import DataSource
from tuneinsight.client.project import Project
from tuneinsight.client.validation import validate_response
from tuneinsight.client.auth import config
from tuneinsight.client.auth import auth
from tuneinsight.client.models import ModelManager
from tuneinsight.utils import time_tools


@attr.s(auto_attribs=True)
class Diapason:
    """
    Diapason is the client that interfaces with a Tune Insight instance.

    This class offers many useful utilities from other modules in the api, including
    authentication, datasource, dataobject, and project management.

    To create a Diapason client, it is recommended to use one of the from_... class
    methods to instantiate a client from a configuration. In most cases, it is best to
    use Diapason.from_config with the instance URL and Client ID, then use .login to
    authenticate to the authentication provider. See the documentation at
    https://dev.tuneinsight.com/docs/Usage/python-sdk/client-configuration/ for more
    details, and other options

    Args for `__init__` (if doing so manually -- not recommended):
        `conf` (`config.ClientConfiguration`): URL and security configuration of the client.
        `client` (`api.sdk.client.AuthenticatedClient`): underlying client used to perform the requests.
        `maas` (`client.ModelManager`): model-as-a-service manager.
    """

    conf: config.ClientConfiguration
    client: api_client.Client = None
    maas: ModelManager = None
    # Whether this client uses end-to-end encryption.
    end_to_end_encrypted: bool = False
    # Whether the API versions of the SDK and server are compatible.
    # This is None until the test is performed (either manually or in new/get_project).
    _api_compatible: Union[bool, None] = None
    # The information about the user (capabilities etc.), stored to avoid re-requesting them.
    _user_info: models.UserInfo = None

    def __attrs_post_init__(self):
        if self.conf.security.static_token != "":
            self.client = api_client.AuthenticatedClient(
                base_url=self.conf.url,
                token=self.conf.security.static_token,
                verify_ssl=self.conf.security.verify_ssl,
            )
        else:
            self.client = auth.KeycloakClient(
                base_url=self.conf.url,
                token="",
                oidc_config=self.conf.security.oidc_config,
                username=self.conf.security.username,
                password=self.conf.security.password,
                verify_ssl=self.conf.security.verify_ssl,
                proxies={
                    "http://": self.conf.http_proxy,
                    "https://": self.conf.https_proxy,
                },
            )

    # Constructors.

    @classmethod
    def from_config_path(
        cls, path: str, url: str = None, username: str = None, password: str = None
    ):
        """
        Creates a client from a configuration file.

        Args:
            path (str): path to the yml configuration file.
            url (str, optional): if provided, URL to overwrite the URL in the config.
            username (str, optional): optional username to overwrite the configuration with. Defaults to None.
            password (str, optional): optional password to overwrite the configuration with. Defaults to None.

        Returns:
            Diapason: the configured diapason client.
        """
        conf = config.ClientConfiguration.from_path(path)
        if username is not None:
            conf.security.username = username
        if password is not None:
            conf.security.password = password
        if url is not None:
            conf.url = url
        return cls(conf=conf)

    @classmethod
    def from_env(cls, path: str = None):
        """
        Creates a client from the environment variables or a "dotenv" file.

        Args:
            path (str): path to the dotenv file. If None, it uses environment variables.

        Returns:
            Diapason: the configured diapason client.
        """
        conf = config.ClientConfiguration.from_env(path)
        return cls(conf=conf)

    @classmethod
    def from_config(
        cls,
        api_url: str,
        oidc_client_id: str,
        oidc_realm: str = "ti-realm",
        oidc_url: str = "https://auth.tuneinsight.com/auth/",
        http_proxy: str = "",
        https_proxy: str = "",
        verify_ssl: bool = True,
        strict: bool = False,
    ):
        """
        Creates a client from the specified attributes.

        This is meant as a convenient way to define a client when default settings apply.
        Only the url endpoint and OIDC client ID need to be specified. Please use client.login()
        after creating this object to authenticate this client to the authentication provider.

        Args:
            api_url (str): the URL of the API endpoint.
            oidc_client_id (str): the OIDC client ID of this user.
            oidc_realm (str): the OIDC realm (default ti-realm).
            oidc_url (str): where to find the OIDC auth server (default is the Tune Insight auth endpoint).
            http_proxy (str): the HTTP proxy to use (default is none).
            https_proxy (str): the HTTPS proxy to use (default is none).
            verify_ssl (bool): whether to verify SSL certificates (default is True).
            strict (bool): whether to use api_url as is (if True), or try and append /api if the url doesn't
                end in /api and strict = False. Set to true only if the API url does not end in /api.

        """
        conf = {
            "security": {
                "oidc_config": {
                    "oidc_client_id": oidc_client_id,
                    "oidc_realm": oidc_realm,
                    "oidc_url": oidc_url,
                },
                "verify_ssl": verify_ssl,
            },
            "url": api_url,
            "http_proxy": http_proxy,
            "https_proxy": https_proxy,
            "strict": strict,
        }
        conf = config.ClientConfiguration.from_json(conf)
        return cls(conf)

    @classmethod
    def with_service_account(
        cls,
        api_url: str,
        oidc_client_id: str,
        oidc_client_secret: str,
        oidc_url: str = "https://auth.tuneinsight.com/auth/",
        oidc_realm: str = "ti-realm",
        verify_ssl: bool = True,
        strict: bool = False,
    ) -> "Diapason":
        """
        Creates a client with service account credentials.

        Args:
            api_url (str): the URL of the API endpoint.
            oidc_client_id (str): the OIDC client ID of this user.
            oidc_client_secret (str): the OIDC client secret of this client.
            oidc_url (str): where to find the OIDC auth server (default is the Tune Insight auth endpoint).
            oidc_realm (str): the OIDC realm (default ti-realm).
            verify_ssl (bool): whether to verify SSL certificates (default is True).
            strict (bool): whether to use api_url as is (if True), or try and append /api if the url doesn't
                end in /api and strict = False. Set to true only if the API url does not end in /api.

        """
        conf = config.ClientConfiguration(
            api_url,
            config.SecurityConfiguration(
                config.OIDCConfiguration(
                    oidc_client_id=oidc_client_id,
                    oidc_client_secret=oidc_client_secret,
                    oidc_url=oidc_url,
                    oidc_realm=oidc_realm,
                ),
                "",
                "",
                "",
                verify_ssl,
            ),
            strict=strict,
        )
        return cls(conf)

    # Model interface.

    def _get_client(self) -> api_client.AuthenticatedClient:
        """
        Returns the API client that this object wraps.

        This is an internal method to use instead of self.client, as it throws
        more intelligible error messages.

        Raises:
            AttributeError: if no client has been initialized.
        """
        if self.client is None:
            raise AttributeError("The client has not been initialized.")
        return self.client

    def add_model_manager(self, model_manager: ModelManager):
        """
        Registers a `ModelManager` with this client to be used for model-as-a-service.

        This  is an 🧪 experimental feature, and is likely to change significantly.
        See `tuneinsight.computations.models.py` for more details.
        """
        self.maas = model_manager

    # User management.

    def login(self, open_page=True, blocking=True):
        """
        Provides users with a link to log in from a browser.

        By default, this opens the link a tab in the user's default browser, and waits
        until the user has successfully authenticated.

        Args:
            open_page (bool, True): whether to use the browser to open the login link.
            blocking (bool, True): whether to wait until the user has logged in.

        Returns:
            login_url (str): the URL to use to log in, or None if blocking is True.

        Raises:
            AttributeError: if the client is not an OIDC client.
        """
        client = self._get_client()
        if not isinstance(client, auth.KeycloakClient):
            raise AttributeError(
                ".login is only available for KeycloakClients. Use another authentication method."
            )

        device_resp = client.get_device_code()
        login_url = device_resp["verification_uri_complete"]
        # Sometimes, the login_url returned by the authentication provider is just the end of the query.
        # When that happens, complete the URL by adding the OIDC information.
        if not login_url.startswith("http") and isinstance(client, auth.KeycloakClient):
            oidc_config = client.oidc_config  # pylint: disable=no-member
            oidc_url = oidc_config.oidc_url
            if not oidc_url.endswith("/"):
                oidc_url += "/"
            login_url = f"{oidc_url}realms/{oidc_config.oidc_realm}/device/{login_url}"
        print("Follow this link to login: " + login_url)
        if open_page:
            webbrowser.open(login_url)
        if blocking:
            try:
                self.wait_ready(repeat=30, sleep_seconds=1)
            except TimeoutError:
                warnings.warn(
                    "The login attempt was likely successful, but the Tune Insight instance could "
                    "not be reached. Check that you have entered the correct URL and client ID, "
                    "and used appropriate proxy settings (if needed)."
                )
        return login_url

    def wait_ready(self, repeat: int = 50, sleep_seconds: int = 5):
        """
        Waits until the server is reachable and healthy.

        This polls the API until it answers by using the healthcheck() endpoint. Use this
        function in scripts that are launched when the instance or connection is not yet
        ready (e.g., at the startup of a system).

        Args:
            repeat (int, optional): maximum number of requests sent to the API. Defaults to 50.
            sleep_seconds (int, optional): sleeping time between each request in seconds. Defaults to 5.

        Raises:
            TimeoutError: if the API has not answered with `repeat * sleep_seconds = 250` seconds.
        """
        num_tries = repeat
        sleep_time = sleep_seconds * time_tools.SECOND
        # Disable API version checks while waiting for the server.
        with self._disabled_api_check():
            for i in range(num_tries):
                # At the last iteration, raise an error instead of silencing it.
                if self.healthcheck(warn=False, error=i == num_tries - 1):
                    return
                time_tools.sleep(sleep_time)

    @contextmanager
    def timeout(self, timeout: int):
        """
        Sets a custom timeout to the client temporarily to be used in a with statement.

        Some operations can take some time to complete (e.g., synthetic data generation).
        If this time exceeds the default timeout of 5 seconds, a `TimeoutError` will be
        raised, even if the operation eventually succeeds. This context manager changes
        this timeout to an arbitrary number of seconds within a `with` statement.

        Use this as:
            ```python
            with client.timeout(600):
                [your code here]
            ```

        Args:
            timeout (int): the timeout in seconds

        Yields:
            Client: the client with updated timeout
        """
        client = self._get_client()
        old_timeout = client.timeout
        client.timeout = timeout
        yield self
        client.timeout = old_timeout

    # Datasource handlers.

    def new_datasource(
        self,
        dataframe: pd.DataFrame,
        name: str,
        clear_if_exists: bool = False,
        query_enabled: bool = False,
        access_scope: models.AccessScope = models.AccessScope.ORGANIZATION,
    ) -> DataSource:
        """
        Creates a new datasource from a dataframe.

        The `pandas.DataFrame` provided as input is uploaded to the Tune Insight instance,
        where it is used to create a new "CSV" datasource.

        Args:
            dataframe (pd.DataFrame): dataframe to upload.
            name (str): name of the datasource to be created.
            clear_if_exists (str, optional): overwrite datasource if it already exists.
            query_enabled (bool, optional): whether to enable direct querying outside of computations on this datasource.
            access_scope (models.AccessScope, optional): scope of the datasource, limiting who can access it (organization by default).

        Returns:
            DataSource: the newly created datasource.
        """
        return DataSource.from_dataframe(
            self._get_client(),
            dataframe,
            name,
            clear_if_exists,
            query_enabled,
            access_scope,
        )

    def new_api_datasource(
        self,
        api_type: models.APIType,
        api_url: str,
        name: str,
        api_token: str = "",
        clear_if_exists: bool = False,
        cert: str = "",
        insecure_skip_verify_tls: bool = False,
        access_scope: models.AccessScope = models.AccessScope.ORGANIZATION,
    ) -> DataSource:
        """
        Creates a new API datasource.

        Args:
            api_type (models.APIType): the type of the API.
            api_url (str): the URL of the API to connect to.
            name (str, required): name of the datasource to be created.
            api_token (str): authentication token to connect to the API.
            clear_if_exists (str, optional): overwrite datasource if it already exists.
            cert (str, optional): name of the certificate to use for this datasource (must be accessible in note at "/usr/local/share/datasource-certificates/{cert}.pem,.key").
            insecure_skip_verify_tls (bool, False): whether to skip the TLS verification. WARNING: This is insecure, use only for tests.
            access_scope (models.AccessScope, optional): scope of the datasource, limiting who can access it (organization by default).

        Returns:
            DataSource: the newly created datasource
        """
        return DataSource.from_api(
            self._get_client(),
            api_type,
            api_url,
            api_token,
            name,
            clear_if_exists,
            cert,
            insecure_skip_verify_tls,
            access_scope,
        )

    def new_csv_datasource(
        self,
        csv: str,
        name: str,
        clear_if_exists: bool = False,
        access_scope: models.AccessScope = models.AccessScope.ORGANIZATION,
    ) -> DataSource:
        """
        Creates a new datasource and upload the given CSV file to it.

        Args:
            csv (str): path to the csv file.
            name (str, required): name of the datasource to be created.
            clear_if_exists (str, optional): overwrite datasource if it already exists.
            cert (str, optional): name of the certificate to use for this datasource (must be accessible in note at "/usr/local/share/datasource-certificates/{cert}.pem,.key").
            access_scope (models.AccessScope, optional): scope of the datasource, limiting who can access it (organization by default).

        Returns:
            DataSource: the newly created datasource
        """
        ds = DataSource.local(
            client=self._get_client(),
            name=name,
            clear_if_exists=clear_if_exists,
            access_scope=access_scope,
        )
        ds.upload_data(csv_path=csv)
        return ds

    def new_database(
        self,
        pg_config: models.DataSourceConfig,
        name: str,
        clear_if_exists: bool = False,
        credentials: models.Credentials = models.Credentials(),
        access_scope: models.AccessScope = models.AccessScope.ORGANIZATION,
    ) -> DataSource:
        """
        Creates a new database datasource, connecting to a Postgres database.

        Args:
            config (models.DataSourceConfig): Postgres configuration.
            name (str, required): name of the datasource to be created.
            clear_if_exists (str, optional): overwrite datasource if it already exists.
            credentials_id (models.Credential, optional): credentials / secret id that stores the database credentials on the KMS connected to the instance.
            access_scope (models.AccessScope, optional): scope of the datasource, limiting who can access it (organization by default).

        Returns:
            DataSource: the newly created datasource
        """
        return DataSource.database(
            client=self._get_client(),
            config=pg_config,
            name=name,
            clear_if_exists=clear_if_exists,
            credentials=credentials,
            access_scope=access_scope,
        )

    def get_datasources(self, name: str = "") -> List[DataSource]:
        """
        Returns all the datasources on the Tune Insight instance.

        Args:
            name (str, optional): name of the datasource. If provided, only the datasource
                with the given name is returned, if any is found. Otherwise, all datasources
                are returned.

        Returns:
            List[DataSource]: the datasources retrieved from the instance.
        """
        response: Response[List[models.DataSource]] = (
            get_data_source_list.sync_detailed(client=self._get_client(), name=name)
        )
        validate_response(response)
        datasources = []
        for datasource in response.parsed:
            datasources.append(DataSource(model=datasource, client=self._get_client()))
        return datasources

    def delete_datasource(self, ds: DataSource) -> List[DataSource]:
        """
        Deletes a datasource on the Tune Insight instance.

        For most datasources, this does not delete the underlying data. For instance,
        deleting a database datasource only removes the connection and credentials,
        but the database remains unchanged.

        Args:
            ds (DataSource): the datasource to delete

        Returns:
            List[DataSource]: updated list of datasources
        """
        ds.delete()  # Do we want to keep this method ?

    def get_datasource(self, datasource_id: str = None, name: str = None) -> DataSource:
        """
        Returns the datasource identified by the given unique identifier or name.

        This instantiates a new `DataSource` object that can be used to interact with
        the corresponding datasource on the Tune Insight instance. Importantly, no
        data is ever transferred in this process.

        Args:
            datasource_id (str, optional): unique identifier of the datasource.
            name (str, optional): name of the datasource. If ds_id is not provided, it will be used to find the datasource

        Returns:
            DataSource: the datasource
        """
        if datasource_id is None:
            if name is None:
                raise ValueError("At least one of id or name must be provided.")
            datasources = self.get_datasources(name=name)
            if not datasources:
                descriptor = (
                    f"name = {name}" if name is not None else f"ds_id = {datasource_id}"
                )
                raise ValueError(f"No datasource found with {descriptor}.")
            return datasources[0]
        return DataSource.fetch_from_id(self._get_client(), datasource_id)

    # Dataobject management.

    def get_dataobject(self, dataobject_id: str) -> DataObject:
        """
        Retrieves the dataobject with the given unique identifier.

        This instantiates a new DataObject object that can be used to interact with
        the corresponding dataobject on the Tune Insight instance. Importantly, no
        data is ever transferred in this process.

        Args:
            do_id (str, optional): ID of the dataobject.

        Returns:
            DataObject: the dataobject.
        """
        do_response: Response[models.DataObject] = get_data_object.sync_detailed(
            client=self._get_client(), data_object_id=dataobject_id
        )
        validate_response(do_response)
        return DataObject(model=do_response.parsed, client=self._get_client())

    # Project management.

    def new_project(
        self,
        name: str,
        clear_if_exists: bool = False,
        topology: models.Topology = UNSET,
        authorized_users: list = None,
        participants: list = None,
        non_contributor: bool = UNSET,
        min_contributors: int = UNSET,
        run_async: bool = True,
        description: str = None,
    ) -> Project:
        """
        Creates a new project on the Tune Insight instance.

        A project is a collaborative space within which computations are run on
        datasources, either locally or collectively. Projects exist on the Tune
        Insight instance, and can be shared with other instances.

        See https://dev.tuneinsight.com/docs/Usage/python-sdk/projects/ for the documentation.

        Args:
            name (str): name of the project
            clear_if_exists (bool, optional): remove existing projects with the same name on
                this node before creating it. Defaults to False.
                ⚠️ Warning: this will cause issues when multiple nodes are involved in the project, as the
                corresponding projects are not removed on other nodes. A warning will be raised explaining alternatives.
            topology (Union[Unset, Topology]): Network Topologies, either 'star' or 'tree'.
                In the star topology all nodes are connected to a central node.
                In the tree topology all nodes are connected and aware of each other.
            authorized_users (Union[Unset, List[str]]): The IDs of the users who can run the project. If left empty,
                only the user creating the project and administrators are authorized.
            participants (Union[Unset, List[str]]): The IDs of the users who participate in the project.
            non_contributor (bool, default UNSET): indicates that this participant participates in the
                computations but does not contribute any data. If left unchanged, this uses instance settings.
            min_contributors (int, default UNSET): if set, the minimum number of ready participants needed to run
                this project. If not set, all contributors must be ready to run the project.
            run_async (bool, default True): whether to run computations asynchronously.
            description (str,default None): optional description of the project. Defaults to None.

        Raises:
            Exception: in case the project already exists and clear_if_exists is False.
            Warning: in case the project already exists and clear_if_exists is True.

        Returns:
            Project: the newly created project
        """

        self.check_api_compatibility()

        if authorized_users is None:
            authorized_users = []

        if participants is None:
            participants = []

        if description is None:
            description = ""

        if name in [p.get_name() for p in self.get_projects()]:
            if clear_if_exists:
                warnings.warn(
                    "A project with the same name was removed on this node, but has not have been deleted on other nodes."
                    "This can cause an error when attempting to share the project, because of conflicting names."
                    "To avoid this, delete the project on other nodes, or create a project with a different name instead."
                )
                self.clear_project(name=name)
            else:
                raise ValueError(f"project {name} already exists.")

        proj_def = models.ProjectDefinition(
            name=name,
            local=True,
            allow_shared_edit=True,
            topology=topology,
            created_with_client=models.Client.DIAPASON_PY,
            authorized_users=authorized_users,
            participants=participants,
            non_contributor=non_contributor,
            min_contributors=min_contributors,
            run_async=run_async,
            description=description,
        )
        proj_response: Response[models.Project] = post_project.sync_detailed(
            client=self._get_client(), json_body=proj_def
        )
        validate_response(proj_response)
        p = Project(model=proj_response.parsed, diapason=self)
        return p

    def join_project_with_token(self, token: str) -> Project:
        """
        Joins a project using a sharing token.

        Args:
            token: the sharing token of the project, obtained from Project.get_sharing_token.

        Returns:
            Project: the project that was just joined.
        """
        resp = post_project_join.sync_detailed(client=self.client, token=token)
        validate_response(response=resp)
        return self.get_project(project_id=resp.parsed)

    def get_project(self, project_id: str = None, name: str = None) -> Project:
        """
        Returns the project identifier either by unique identifier or name.

        If no matching project is found, a LookupError is raised. Note that this
        can be because the project exists but the client does not have access to it.
        Contact your instance administrator if you think that is the case.

        Args:
            project_id (str, optional): id of the project. Has priority over name.
            name (str, optional): name of the project. If project_id is not provided, it will be used to find the project.

        Returns:
            Project: the project
        """
        self.check_api_compatibility()
        if project_id is not None:
            response: Response[models.Project] = get_project.sync_detailed(
                client=self._get_client(), project_id=project_id
            )
            validate_response(response)
            model = response.parsed

        elif name is not None:
            response: Response[List[models.Project]] = get_project_list.sync_detailed(
                client=self._get_client(), name=name
            )
            validate_response(response)
            if not response.parsed:
                raise LookupError(f"No project named {name} found.")
            model = response.parsed[0]

        else:
            raise ValueError("At least one of of project_id or name must be specified.")

        # Instantiate a project object from this model.
        return Project(model=model, diapason=self)

    def get_projects(self) -> List[Project]:
        """
        Returns all the projects available to the client.

        Returns:
            List[Project]: list of projects
        """
        self.check_api_compatibility()
        response: Response[List[models.Project]] = get_project_list.sync_detailed(
            client=self._get_client()
        )
        validate_response(response)
        projects = []
        for project in response.parsed:
            projects.append(Project(model=project, diapason=self))
        return projects

    def clear_project(self, project_id: str = None, name: str = None):
        """
        Deletes the project identified either by ID or name.

        This is equivalent to `self.get_project(...).delete()`.

        Args:
            project_id (str, optional): the unique identifier of the project.
            name (str, optional): name of the datasource. If provided, it will
                be used to filter the datasources. Defaults to "".
        """
        p = self.get_project(project_id=project_id, name=name)
        p.delete()

    def check_api_compatibility(self, hard=False) -> bool:
        """
        Checks that the server and client have the same API version.

        This is called automatically when creating or retrieving a project, and
        displays a user-friendly warning. If you see this warning, the version
        of the Python SDK that you are using may not be compatible with the Tune
        Insight instance you are connecting to: this can cause problems. Contact
        your administrator to get a compatible SDK version.

        Args
            hard (bool, default False): if true, this will raise an error if the
                connection fails or the API versions are found to be mismatching.
                Otherwise, this will raise a warning instead.
        """
        # This check is only performed once, for efficiency reasons.
        if self._api_compatible is not None:
            return self._api_compatible
        # Fetch the version of the server at /infos
        try:
            # Many exceptions can occur here: connection issues, server-side issues
            # (e.g. when running the server in different modes, or very ancient versions).
            # This general catch-all allows the compatibility check to remain optional.
            resp = get_infos.sync_detailed(client=self._get_client())
            validate_response(resp)
            api_checksum = resp.parsed.api_checksum
        except Exception as err:  # pylint: disable=broad-exception-caught
            if hard:
                raise err
            warnings.warn(
                f"An exception occured while checking API compatibility ({err})."
            )
            return False
        # Check that the version of this client from auto-generated file.
        with open(
            os.path.join(os.path.dirname(__file__), "..", "api", "api-checksum"),
            encoding="utf-8",
        ) as ff:
            this_checksum = ff.read().strip(" \n")
        if api_checksum != this_checksum:
            warnings.warn(
                "API version mismatch: the server and client use different versions "
                + "of the API. Some functionalities might not work as intended."
            )
        self._api_compatible = api_checksum == this_checksum
        return self._api_compatible

    @contextmanager
    def _disabled_api_check(self):
        """Temporarily disables API version checks within a with statement."""
        old_check = self._api_compatible
        self._api_compatible = True
        yield self
        self._api_compatible = old_check

    def healthcheck(self, warn: bool = True, error: bool = False) -> bool:
        """
        Checks that the client is set up properly and the instance is reachable.

        Args
            warn (bool, default True): whether to print a warning with the error
                message if the healthcheck fails.
            error (bool, default False): whether to raise an error if the healthcheck
                fails. This raises the error that made the it fail.

        """
        try:
            response = get_health.sync_detailed(client=self._get_client())
            validate_response(response)
            return True
        except Exception as err:  # pylint: disable=broad-exception-caught
            if error:
                raise err
            if warn:
                warnings.warn(f"Healthcheck error: {err} ({type(err)})")
            return False

    @property
    def user_infos(self) -> models.UserInfo:
        """Fetches information about this user from the connected instance."""
        if self._user_info is None:
            resp = get_user_info.sync_detailed(client=self.client)
            validate_response(resp)
            self._user_info = resp.parsed
        return self._user_info

    def can(self, capability: models.Capability):
        """Returns whether this user has the given capability (represented by its unique name)."""
        infos = self.user_infos
        if is_unset(infos.capabilities):
            return True
        return any(cap.name == capability for cap in infos.capabilities)
