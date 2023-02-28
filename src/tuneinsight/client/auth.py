from typing import Dict
from time import time
from attr import define
from keycloak import KeycloakOpenID

from tuneinsight.api.sdk import client
from tuneinsight.client import config


@define(kw_only=True)
class KeycloakClient(client.AuthenticatedClient):
    """Client for Keycloak authentication"""

    kc_config: config.KeycloakConfiguration
    username: str
    password: str
    tokens: dict = {}
    kc_open_id: KeycloakOpenID = None
    token_timeout: float = 0
    refresh_token_timeout: float = 0
    refresh_delay_seconds: float = 10

    def __attrs_post_init__(self):

        self.kc_open_id = KeycloakOpenID(server_url=self.kc_config.keycloak_url,
                                client_id=self.kc_config.keycloak_client_id,
                                client_secret_key=self.kc_config.keycloak_client_secret,
                                realm_name=self.kc_config.keycloak_realm)

    def update_tokens(self,tokens):
        self.tokens = tokens
        self.token_timeout = time() + float(self.tokens['expires_in']) - self.refresh_delay_seconds
        self.refresh_token_timeout = time() + float(self.tokens['refresh_expires_in']) - self.refresh_delay_seconds

    def get_token(self) -> dict:

        # If a keycloak_client_secret is provided, use client credentials flow for service accounts
        if self.kc_config.keycloak_client_secret != "":
            self.tokens = self.kc_open_id.token(
                self.username, grant_type="client_credentials")
        else:
            # Otherwise, use password flow for user accounts
            self.tokens = self.kc_open_id.token(self.username, self.password)
        self.update_tokens(self.tokens)

    def refresh_token(self) -> dict:
        self.update_tokens(self.kc_open_id.refresh_token(self.tokens["refresh_token"]))

    def get_headers(self) -> Dict[str, str]:
        """Get headers to be used in authenticated endpoints"""
        if "access_token" not in self.tokens:
            self.get_token()
        if time() > self.token_timeout:
            if time() > self.refresh_token_timeout:
                self.get_token()
            else:
                self.refresh_token()
        return {"Authorization": f"Bearer {self.tokens['access_token']}", **self.headers}
