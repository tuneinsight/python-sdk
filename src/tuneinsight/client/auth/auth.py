"""Classes managing authentication to Keycloak."""

from typing import Dict


from time import time
from ast import literal_eval
from attr import define
from keycloak import KeycloakOpenID
from keycloak.exceptions import KeycloakError, raise_error_from_response

from tuneinsight.api.sdk import client
from tuneinsight.client.auth import config


@define(kw_only=True)
class KeycloakClient(client.AuthenticatedClient):
    """
    Client for Keycloak authentication.

    This class maintains and refreshes the tokens needed to authenticate to a
    Tune Insight instance. It is intended mostly for internal use: to connect
    to an instance, use `tuneinsight.client.Diapason` instead.

    """

    oidc_config: config.OIDCConfiguration
    username: str
    password: str
    device_code: str = ""
    tokens: dict = {}
    kc_open_id: KeycloakOpenID = None
    token_timeout: float = 0
    refresh_token_timeout: float = 0
    refresh_delay_seconds: float = 10
    verify_ssl: bool = True
    proxies: dict = {"http://": "", "https://": ""}

    def __attrs_post_init__(self):
        self.kc_open_id = KeycloakOpenID(
            server_url=self.oidc_config.oidc_url,
            client_id=self.oidc_config.oidc_client_id,
            client_secret_key=self.oidc_config.oidc_client_secret,
            realm_name=self.oidc_config.oidc_realm,
            verify=self.verify_ssl,
            proxies=self.proxies,
        )

    def update_tokens(self, tokens):
        self.tokens = tokens
        self.token_timeout = (
            time() + float(self.tokens["expires_in"]) - self.refresh_delay_seconds
        )
        self.refresh_token_timeout = (
            time()
            + float(self.tokens["refresh_expires_in"])
            - self.refresh_delay_seconds
        )

    def get_token(self) -> dict:
        # If a oidc_client_secret is provided, use client credentials flow for service accounts
        if self.oidc_config.oidc_client_secret != "":
            self.tokens = self.kc_open_id.token(
                self.username, grant_type="client_credentials"
            )
        # If a device_code is provided, use the device authorization grant flow
        elif self.device_code != "":
            self.tokens = self.kc_open_id.token(
                self.username,
                grant_type="urn:ietf:params:oauth:grant-type:device_code",
                device_code=self.device_code,
            )
        else:
            # Otherwise, use password flow for user accounts
            self.tokens = self.kc_open_id.token(self.username, self.password)
        self.update_tokens(self.tokens)

    def refresh_token(self) -> dict:
        self.update_tokens(self.kc_open_id.refresh_token(self.tokens["refresh_token"]))

    def get_device_code(self) -> dict:
        payload = {
            "client_id": self.kc_open_id.client_id,
        }

        url = (
            self.oidc_config.oidc_url
            + "realms/"
            + self.oidc_config.oidc_realm
            + "/protocol/openid-connect/auth/device"
        )

        resp = self.kc_open_id.connection.raw_post(url, payload)
        if resp.status_code in [200, 201, 204]:
            decoded_resp = literal_eval(resp.content.decode())
            self.device_code = decoded_resp["device_code"]
        # return literal_eval(resp.content.decode())
        return raise_error_from_response(resp, KeycloakError)

    def get_headers(self) -> Dict[str, str]:
        """Get headers to use in authenticated API endpoints."""
        if "access_token" not in self.tokens:
            self.get_token()
        if time() > self.token_timeout:
            if time() > self.refresh_token_timeout:
                self.get_token()
            elif "refresh_token" in self.tokens:
                self.refresh_token()
        if (
            "refresh_token" in self.tokens
            and self.refresh_token_timeout - time() < 10 * self.refresh_delay_seconds
        ):
            # Refresh token if we are approaching refresh_token_timeout
            self.refresh_token()
        return {
            "Authorization": f"Bearer {self.tokens['access_token']}",
            **self.headers,
        }
