"""Log-in configuration for Tune Insight clients."""

import os
import json
from dotenv import load_dotenv
import yaml


def _bool(string: str) -> bool:
    """Interprets a user-provided string to boolean, using common defaults (true / yes / y / 1)."""
    if string.lower() in ["1", "true", "yes", "y"]:
        return True
    return False


def _to_dict(obj):
    if not hasattr(obj, "__dict__"):
        return obj
    result = {}
    for key, val in obj.__dict__.items():
        if key.startswith("_"):
            continue
        element = []
        if isinstance(val, list):
            for item in val:
                element.append(_to_dict(item))
        else:
            element = _to_dict(val)
        result[key] = element
    return result


class OIDCConfiguration:
    """OIDC parameters to log in to Keycloak."""

    oidc_client_id: str
    oidc_client_secret: str
    oidc_url: str
    oidc_realm: str

    def __init__(
        self,
        oidc_client_id: str,
        oidc_client_secret: str,
        oidc_url: str,
        oidc_realm: str,
    ):
        self.oidc_client_id = oidc_client_id or "python-sdk"
        self.oidc_client_secret = oidc_client_secret or ""
        self.oidc_url = oidc_url or "https://auth.tuneinsight.com/auth/"
        self.oidc_realm = oidc_realm or "ti-realm"

    @staticmethod
    def from_json(json_dct):
        return OIDCConfiguration(
            json_dct.get("oidc_client_id"),
            json_dct.get("oidc_client_secret"),
            json_dct.get("oidc_url"),
            json_dct.get("oidc_realm"),
        )


class SecurityConfiguration:
    """Configuration of the security for a client connection."""

    static_token: str
    username: str
    password: str
    verify_ssl: bool
    oidc_config: OIDCConfiguration

    def __init__(
        self,
        oidc_config: OIDCConfiguration,
        static_token: str,
        username: str,
        password: str,
        verify_ssl: bool,
    ):
        self.oidc_config = oidc_config
        self.static_token = static_token or ""
        self.username = username or ""
        self.password = password or ""
        self.verify_ssl = True if verify_ssl is None else verify_ssl

    @staticmethod
    def from_json(json_dct):
        oidc_config = OIDCConfiguration.from_json(json_dct.get("oidc_config"))
        return SecurityConfiguration(
            oidc_config,
            json_dct.get("static_token"),
            json_dct.get("username"),
            json_dct.get("password"),
            json_dct.get("verify_ssl"),
        )


class ClientConfiguration:
    """URL and security parameters of a client."""

    url: str
    security: SecurityConfiguration
    http_proxy: str
    https_proxy: str

    def __init__(
        self,
        url: str,
        security: SecurityConfiguration,
        http_proxy: str = None,
        https_proxy: str = None,
        strict: bool = False,
    ):
        """
        Initializes a client configuration.

        Args:
            url (str): The URL of the Tune Insight API.
            security (SecurityConfiguration): The security settings of the configuration.
            http_proxy (str, optional): The HTTP proxy to be used. Defaults to None.
            https_proxy (str, optional): The HTTPS proxy to be used. Defaults to None.
            strict (boolean, default False): if true, the exact url is used. If False, this
                attempts to append "/api" to the url (as it's the most common case).
        """
        self.url = url
        # Allow users to make a mistake and forget the /api (except when running locally where the path might not be needed).
        if (
            not strict
            and not url.startswith("http://localhost")
            and not url.endswith("/api")
        ):
            if not url.endswith("/"):
                self.url += "/"
            self.url += "api"
        self.security = security
        self.http_proxy = http_proxy
        self.https_proxy = https_proxy

    def save(self, filepath: str):
        """Saves this configuration to a file."""
        with open(filepath, "w", encoding="utf-8") as f:
            res = _to_dict(self)
            yaml.safe_dump(res, f)

    @staticmethod
    def from_json(json_dct):
        """
        Creates a Client configuration from a JSON dictionary.

        Args:
            json_dct (dict): The JSON dictionary containing the client configuration.

        """
        security = SecurityConfiguration.from_json(json_dct.get("security"))
        strict = json_dct.get("strict", False)
        client = ClientConfiguration(json_dct.get("url"), security, strict=strict)
        client.http_proxy = json_dct.get("http_proxy") or client.http_proxy
        client.https_proxy = json_dct.get("https_proxy") or client.https_proxy
        return client

    @staticmethod
    def from_path(filepath: str):
        """
        Creates a Client configuration from a file.

        Args:
            filepath: the path to the file to load from, a text file with a
                configuration in JSON (as produced by ClientConfiguration.save).
        """
        with open(filepath, encoding="utf-8") as f:
            dm = yaml.safe_load(f)
            dumped = json.dumps(dm)
            client = ClientConfiguration.from_json(json.loads(dumped))
            return client

    @staticmethod
    def from_env(envpath: str = None):
        """
        Creates a Client configuration from environment variables.

        Args:
            envpath (optional): path to a file containing environment variables
                to use instead.
        """
        if envpath is not None:
            # Verify that the file exists
            if not os.path.exists(envpath):
                raise LookupError(".env file does not exist.")

            found = load_dotenv(dotenv_path=envpath)
            if not found:
                raise LookupError("No environment variable found.")

        # Verify that the environment variables are set
        if os.getenv("NODE_URL") is None:
            raise LookupError("Missing environments: NODE_URL is not set.")
        if (
            os.getenv("TI_USERNAME") is None
            and os.getenv("TI_PASSWORD") is None
            and os.getenv("TI_STATIC_TOKEN") is None
        ):
            raise LookupError(
                "Missing environments: need to set either TI_USERNAME and TI_PASSWORD or TI_STATIC_TOKEN."
            )

        oidc_config = OIDCConfiguration(
            oidc_url=os.getenv("OIDC_URL"),
            oidc_realm=os.getenv("OIDC_REALM"),
            oidc_client_id=os.getenv("OIDC_CLIENT_ID"),
            oidc_client_secret=os.getenv("OIDC_CLIENT_SECRET"),
        )

        security_config = SecurityConfiguration(
            username=os.getenv("TI_USERNAME"),
            password=os.getenv("TI_PASSWORD"),
            static_token=os.getenv("TI_STATIC_TOKEN"),
            verify_ssl=_bool(os.getenv("TI_VERIFY_SSL")),
            oidc_config=oidc_config,
        )
        client = ClientConfiguration(
            url=os.getenv("NODE_URL"),
            security=security_config,
            strict=os.getenv("URL_STRICT") or False,
        )

        client.http_proxy = os.getenv("HTTP_PROXY") or client.http_proxy
        client.https_proxy = os.getenv("HTTPS_PROXY") or client.https_proxy

        return client
