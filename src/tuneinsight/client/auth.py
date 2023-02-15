from typing import Dict
from time import time
from attr import define
from keycloak import KeycloakOpenID

from tuneinsight.api.sdk import client
from tuneinsight.client import config


@define(kw_only=True)
class KeycloakClient(client.AuthenticatedClient):

    kc_config: config.KeycloakConfiguration
    username: str
    password: str
    tokens: dict = {}
    kc_open_id: KeycloakOpenID = None
    token_timeout: float = 0

    def __attrs_post_init__(self):
        self.kc_open_id = KeycloakOpenID(server_url=self.kc_config.keycloak_url,
                                client_id=self.kc_config.keycloak_client_id,
                                realm_name=self.kc_config.keycloak_realm)

    def getToken(self) -> dict:
        self.tokens = self.kc_open_id.token(self.username,self.password)
        self.token_timeout = time() + float(self.tokens['expires_in'])

    def refreshToken(self) -> dict:
        self.tokens = self.kc_open_id.refresh_token(self.tokens["refresh_token"])
        self.token_timeout = time() + float(self.tokens['expires_in'])

    def get_headers(self) -> Dict[str, str]:
        """Get headers to be used in authenticated endpoints"""
        if not "access_token" in self.tokens:
            self.getToken()
        if time() > self.token_timeout:
            self.refreshToken()

        return {"Authorization": f"Bearer {self.tokens['access_token']}", **self.headers}
