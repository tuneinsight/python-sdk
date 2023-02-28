import os
import json
from types import SimpleNamespace
from dataclasses import dataclass
from ast import literal_eval
from dotenv import load_dotenv
import yaml


def to_dict(obj):
    if not  hasattr(obj,"__dict__"):
        return obj
    result = {}
    for key, val in obj.__dict__.items():
        if key.startswith("_"):
            continue
        element = []
        if isinstance(val, list):
            for item in val:
                element.append(to_dict(item))
        else:
            element = to_dict(val)
        result[key] = element
    return result

@dataclass
class KeycloakConfiguration:
    keycloak_client_id: str
    keycloak_client_secret: str
    keycloak_url: str
    keycloak_realm: str

    def __init__(self, keycloak_client_id: str, keycloak_client_secret: str, keycloak_url: str, keycloak_realm: str):
        self.keycloak_client_id = "python-sdk" if keycloak_client_id is None else keycloak_client_id
        self.keycloak_client_secret = "" if keycloak_client_secret is None else keycloak_client_secret
        self.keycloak_url = "https://auth.tuneinsight.com/auth/" if keycloak_url is None else keycloak_url
        self.keycloak_realm = "ti-realm" if keycloak_realm is None else keycloak_realm


@dataclass
class Security:
    static_token: str
    username: str
    password: str
    verify_ssl: bool
    kc_config: KeycloakConfiguration

    def __init__(self, static_token: str, username: str, password: str, verify_ssl: bool, kc_config: KeycloakConfiguration):
        self.verify_ssl = True if verify_ssl is None else verify_ssl
        self.static_token = static_token
        self.username = username
        self.password = password
        self.kc_config = kc_config


@dataclass
class Client:
    url: str
    security: Security

    def save(self,filepath: str):
        with open(filepath,"w",encoding='utf-8') as f:
            res = to_dict(self)
            yaml.safe_dump(res,f)



def LoadClient(filepath: str) -> Client:
    with open(filepath,encoding='utf-8') as f:
        dm = yaml.safe_load(f)
        dumped = json.dumps(dm)
        client = json.loads(dumped,object_hook=lambda d: SimpleNamespace(**d))
        return client

def LoadEnvClient(envpath: str = None) -> Client:

    if envpath is not None:
        # Verify that the file exists
        if not os.path.exists(envpath):
            raise Exception("env file does not exist")

        found = load_dotenv(dotenv_path=envpath)
        if not found:
            raise Exception("No environment variable found")

    # Verify that the environment variables are set
    if os.getenv('NODE_URL') is None:
        raise Exception("Missing environments: NODE_URL is not set")
    if os.getenv('TI_USERNAME') is None and os.getenv('TI_PASSWORD') is None and os.getenv('TI_STATIC_TOKEN') is None:
        raise Exception("Missing environments: need to set either TI_USERNAME and TI_PASSWORD or TI_STATIC_TOKEN")

    kc_config = KeycloakConfiguration(
        keycloak_url=os.getenv('KEYCLOAK_URL'),
        keycloak_realm=os.getenv('KEYCLOAK_REALM'),
        keycloak_client_id=os.getenv('KEYCLOAK_CLIENT_ID'),
        keycloak_client_secret=os.getenv('KEYCLOAK_CLIENT_SECRET'),
    )

    security_config = Security(
        username=os.getenv('TI_USERNAME'),
        password=os.getenv('TI_PASSWORD'),
        static_token=os.getenv('TI_STATIC_TOKEN'),
        verify_ssl=literal_eval(os.getenv('TI_VERIFY_SSL')),
        kc_config=kc_config
    )
    client = Client(url=os.getenv('NODE_URL'), security=security_config)
    return client
