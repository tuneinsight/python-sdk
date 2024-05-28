"""Module defining the Diapason class to interact with the Tune Insight instance."""

from contextlib import contextmanager
from typing import List, Union
import warnings
import webbrowser
import os

import attr
import pandas as pd

from tuneinsight.api.sdk.types import Response
from tuneinsight.api.sdk import client as api_client
from tuneinsight.api.sdk.api.api_project import post_project
from tuneinsight.api.sdk.api.api_project import get_project
from tuneinsight.api.sdk.api.api_project import get_project_list
from tuneinsight.api.sdk.api.api_datasource import get_data_source_list
from tuneinsight.api.sdk.api.api_dataobject import get_data_object
from tuneinsight.api.sdk.api.api_infos import get_infos
from tuneinsight.api.sdk.api.health import get_health
from tuneinsight.api.sdk import models
from tuneinsight.client.dataobject import DataObject

from tuneinsight.client.datasource import DataSource
from tuneinsight.client.project import Project
from tuneinsight.client.validation import validate_response
from tuneinsight.client import config
from tuneinsight.client import auth
from tuneinsight.api.sdk.types import UNSET
from tuneinsight.utils import time_tools


@attr.s(auto_attribs=True)
class Diapason:
    """
    Diapason is a client to interface with a Tune Insight instances.

    This class offers many useful utilities from other modules in the api, including
    authentication, datasource, dataobject, and project management.

    To create a Diapason client, it is recommended to use one of the from_... class
    methods to instantiate a client from a configuration.

    Args for __init__ (if doing so manually):
        conf (config.ClientConfiguration): URL and security configuration of the client.
        client (api.sdk.client.AuthenticatedClient): underlying client used to perform the requests.
        maas (client.models.ModelManager): model-as-a-service manager.
    """

    conf: config.ClientConfiguration
    client: api_client.Client = None
    maas: "ModelManager" = (
        None  # expected type ModelManager not included to avoid cryptolib dependency
    )
    # Whether the API versions of the SDK and server are compatible.
    # This is None until the test is performed (either manually or in new/get_project).
    _api_compatible: Union[bool, None] = None

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
                    "http": self.conf.http_proxy,
                    "https": self.conf.https_proxy,
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
    ):
        """
        Creates a client from the specified attributes.

        This is meant as a convenient way to define a client when default settings apply.
        Only the url endpoint and OIDC client ID need to be specified. Please use client.login()
        after creating this object to authenticate this client to Keycloak.

        Args:
            api_url (str): the URL of the API endpoint.
            oidc_client_id (str): the OIDC client ID of this user.
            oidc_realm (str): the OIDC realm (default ti-realm).
            oidc_url (str): where to find the OIDC auth server (default is the Tune Insight auth endpoint).
            http_proxy (str): the HTTP proxy to use (default is none).
            https_proxy (str): the HTTPS proxy to use (default is none).
            verify_ssl (bool): whether to verify SSL certificates (default is True).

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
        }
        conf = config.ClientConfiguration.from_json(conf)
        return cls(conf)

    # Model interface.

    def _get_client(self) -> api_client.AuthenticatedClient:
        """Returns the API client that this object wraps."""
        if self.client is None:
            raise AttributeError("client has not been created")
        return self.client

    def add_model_manager(self, model_manager):
        """Adds a ModelManager to this client."""
        self.maas = model_manager

    # User management.

    def login(self, open_page=True, blocking=True):
        """
        Provides users with a link to log in from a browser.

        Args:
            open_page (bool, True): whether to use the browser to open the login link.
            blocking (bool, True): whether to wait until the user has logged in.

        Returns:
            login_url (str): the URL to use to log in, or None if blocking is True.

        Raises:
            AttributeError: if the client is not a keycloak client.
        """
        if not isinstance(self.client, auth.KeycloakClient):
            raise AttributeError("client is not a KeycloakClient")

        device_resp = self.client.get_device_code()
        login_url = device_resp["verification_uri_complete"]
        # Sometimes, the login_url returned by keycloak is just the end of the query.
        # When that happens, complete the URL by adding the OIDC information.
        if not login_url.startswith("http") and isinstance(
            self.client, auth.KeycloakClient
        ):
            oidc_config = self.client.oidc_config  # pylint: disable=no-member
            oidc_url = oidc_config.oidc_url
            if not oidc_url.endswith("/"):
                oidc_url += "/"
            login_url = f"{oidc_url}realms/{oidc_config.oidc_realm}/device/{login_url}"
        print("Follow this link to login: " + login_url)
        if open_page:
            webbrowser.open(login_url)
        if blocking:
            self.wait_ready(sleep_seconds=1)
        return login_url

    def wait_ready(self, repeat: int = 50, sleep_seconds: int = 5):
        """Polls the API until it answers by using the healthcheck() endpoint.

        Args:
            repeat (int, optional): maximum number of requests sent to the API. Defaults to 50.
            sleep_seconds (int, optional): sleeping time between each request in seconds. Defaults to 5.

        Raises:
            TimeoutError: if the API has not answered.
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

        Use this as:
            with client.timeout(600) as c:
                [your code here using c as client]

        Args:
            timeout (int): the timeout in seconds

        Yields:
            Client: the client with updated timeout
        """
        old_timeout = self.client.timeout
        self.client.timeout = timeout
        yield self
        self.client.timeout = old_timeout

    # Datasource handlers.

    def new_datasource(
        self, dataframe: pd.DataFrame, name: str, clear_if_exists: bool = False
    ) -> DataSource:
        """
        Creates a new datasource from a dataframe. It uploads the dataframe to the created datasource.

        Args:
            dataframe (pd.DataFrame): dataframe to upload.
            name (str): name of the datasource to be created.
            clear_if_exists (str, optional): overwrite datasource if it already exists.

        Returns:
            DataSource: the newly created datasource.
        """
        return DataSource.from_dataframe(
            self._get_client(), dataframe, name, clear_if_exists
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
    ) -> DataSource:
        """
        Creates a new API datasource.

        Args:
            apiConfig (any): API configuration.
            name (str, required): name of the datasource to be created.
            clear_if_exists (str, optional): overwrite datasource if it already exists.
            cert (str, optional): name of the certificate to use for this datasource (must be accessible in note at "/usr/local/share/datasource-certificates/{cert}.pem,.key").

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
        )

    def new_csv_datasource(
        self, csv: str, name: str, clear_if_exists: bool = False
    ) -> DataSource:
        """
        Creates a new datasource and upload the given csv file to it.

        Args:
            csv (str): path to the csv file.
            name (str, required): name of the datasource to be created.
            clear_if_exists (str, optional): overwrite datasource if it already exists.
            cert (str, optional): name of the certificate to use for this datasource (must be accessible in note at "/usr/local/share/datasource-certificates/{cert}.pem,.key").

        Returns:
            DataSource: the newly created datasource
        """
        ds = DataSource.local(
            client=self._get_client(), name=name, clear_if_exists=clear_if_exists
        )
        ds.load_csv_data(path=csv)
        return ds

    def new_database(
        self,
        pg_config: models.DataSourceConfig,
        name: str,
        clear_if_exists: bool = False,
        credentials: models.Credentials = models.Credentials(),
    ) -> DataSource:
        """
        Creates a new Postgres datasource.

        Args:
            config (models.DataSourceConfig): Postgres configuration.
            name (str, required): name of the datasource to be created.
            clear_if_exists (str, optional): overwrite datasource if it already exists.
            credentials_id (models.Credential, optional): credentials / secret id that stores the database credentials on the KMS connected to the instance.

        Returns:
            DataSource: the newly created datasource
        """
        return DataSource.database(
            client=self._get_client(),
            config=pg_config,
            name=name,
            clear_if_exists=clear_if_exists,
            credentials=credentials,
        )

    def get_datasources(self, name: str = "") -> List[DataSource]:
        """Returns all the datasources of the instance.

        Args:
            name (str, optional): name of the datasource. If provided, it will be used to filter the datasources. Defaults to "".

        Returns:
            List[DataSource]: the datasources retrieved from the instance.
        """
        response: Response[List[models.DataSource]] = (
            get_data_source_list.sync_detailed(client=self.client, name=name)
        )
        validate_response(response)
        datasources = []
        for datasource in response.parsed:
            datasources.append(DataSource(model=datasource, client=self.client))
        return datasources

    def delete_datasource(self, ds: DataSource) -> List[DataSource]:
        """Deletes a datasource.

        Args:
            ds (DataSource): the datasource to delete

        Returns:
            List[DataSource]: updated list of datasources
        """
        ds.delete()  # Do we want to keep this method ?

    def get_datasource(self, ds_id: str = None, name: str = None) -> DataSource:
        """
        Returns a datasource by ID or name.

        Args:
            ds_id (str, optional): ID of the datasource.
            name (str, optional): name of the datasource. If ds_id is not provided, it will be used to find the datasource

        Returns:
            DataSource: the datasource
        """
        if ds_id is None:
            if name is None:
                raise ValueError("At least one of ds_id or name must be provided.")
            return self.get_datasources(name=name)[0]
        return DataSource.fetch_from_id(self.client, ds_id)

    # Dataobject management.

    def get_dataobject(self, do_id: str) -> DataObject:
        """Retrieves a dataobject, specified by ID.

        Args:
            do_id (str, optional): ID of the dataobject.

        Returns:
            DataObject: the dataobject.
        """
        do_response: Response[models.DataObject] = get_data_object.sync_detailed(
            client=self.client, data_object_id=do_id
        )
        validate_response(do_response)
        return DataObject(model=do_response.parsed, client=self.client)

    # Project management.

    def new_project(
        self,
        name: str,
        clear_if_exists: bool = False,
        topology: models.Topology = UNSET,
        authorized_users: list = None,
        participants: list = None,
        non_contributor: bool = False,
        run_async: bool = True,
        description: str = None,
    ) -> Project:
        """Creates a new project.

        Args:
            name (str): name of the project
            clear_if_exists (bool, optional): remove existing projects with the same name on this node before creating it. Defaults to False.
                Warning: this will cause issues when multiple nodes are involved in the project, as the same-named projects are
                not removed on other nodes. A warning will be raised explaining alternatives.
            topology (Union[Unset, Topology]): Network Topologies. 'star' or 'tree'. In star topology all nodes are
            connected to a central node. In tree topology all nodes are connected and aware of each other.
            authorized_users (Union[Unset, List[str]]): The IDs of the users who can run the project
            participants (Union[Unset, List[str]]): The IDs of the users who participate in the project.
            non_contributor (bool, default False): indicates that this participant participates in the computations but does not contribute any data.
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
                    """A project with the same name was removed on this node, but has not have been deleted on other nodes. \
This can cause an error when attempting to share the project, because of conflicting names. \
To avoid this, delete the project on other nodes, or create a differently-named project instead."""
                )
                self.clear_project(name=name)
            else:
                raise ValueError(f"project {name} already exists")

        proj_def = models.ProjectDefinition(
            name=name,
            local=True,
            allow_shared_edit=True,
            topology=topology,
            created_with_client=models.Client.DIAPASON_PY,
            authorized_users=authorized_users,
            participants=participants,
            non_contributor=non_contributor,
            run_async=run_async,
            description=description,
        )
        # authorization_status = models.AuthorizationStatus.UNAUTHORIZED)
        proj_response: Response[models.Project] = post_project.sync_detailed(
            client=self.client, json_body=proj_def
        )
        validate_response(proj_response)
        p = Project(model=proj_response.parsed, client=self.client)
        return p

    def get_project(self, project_id: str = None, name: str = None) -> Project:
        """Returns a project, either by id or name.

        Args:
            project_id (str, optional): id of the project.
            name (str, optional): name of the project. If project_id is not provided, it will be used to find the project.

        Returns:
            Project: the project
        """
        self.check_api_compatibility()
        if project_id is None:
            if name is None:
                raise ValueError(
                    "At least one of of project_id or name must be specified."
                )
            return self.get_project_by_name(name=name)
        proj_response: Response[models.Project] = get_project.sync_detailed(
            client=self.client, project_id=project_id
        )
        validate_response(proj_response)
        return Project(model=proj_response.parsed, client=self.client)

    def get_projects(self) -> List[Project]:
        """
        Returns all the projects available to the client.

        Returns:
            List[Project]: list of projects
        """
        self.check_api_compatibility()
        response: Response[List[models.Project]] = get_project_list.sync_detailed(
            client=self.client
        )
        validate_response(response)
        projects = []
        for project in response.parsed:
            projects.append(Project(model=project, client=self.client))
        return projects

    def get_project_by_name(self, name: str) -> Project:
        """Returns a project by name.

        Args:
            name (str): name of the project

        Raises:
            LookupError: if the project is not found

        Returns:
            Project: the project
        """
        self.check_api_compatibility()
        response: Response[List[models.Project]] = get_project_list.sync_detailed(
            client=self.client, name=name
        )
        validate_response(response)
        if len(response.parsed):
            return Project(model=response.parsed[0], client=self.client)
        raise LookupError("project not found")

    def clear_project(self, project_id: str = None, name: str = None):
        """
        Deletes a project, retrieved either by ID or name.

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
            resp = get_infos.sync_detailed(client=self.client)
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
            response = get_health.sync_detailed(client=self.client)
            validate_response(response)
            return True
        except Exception as err:  # pylint: disable=broad-exception-caught
            if error:
                raise err
            if warn:
                warnings.warn(f"Healthcheck error: {err} ({type(err)})")
            return False
