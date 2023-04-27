import os
import json
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

class OIDCConfiguration:
    oidc_client_id: str
    oidc_client_secret: str
    oidc_url: str
    oidc_realm: str

    def __init__(self, oidc_client_id: str, oidc_client_secret: str, oidc_url: str, oidc_realm: str):
        self.oidc_client_id = "python-sdk" if oidc_client_id is None else oidc_client_id
        self.oidc_client_secret = "" if oidc_client_secret is None else oidc_client_secret
        self.oidc_url = "https://auth.tuneinsight.com/auth/" if oidc_url is None else oidc_url
        self.oidc_realm = "ti-realm" if oidc_realm is None else oidc_realm

    @staticmethod
    def from_json(json_dct):
        return OIDCConfiguration(json_dct.get('oidc_client_id'), json_dct.get('oidc_client_secret'), json_dct.get('oidc_url'), json_dct.get('oidc_realm'))


class Security:
    static_token: str
    username: str
    password: str
    verify_ssl: bool
    oidc_config: OIDCConfiguration

    def __init__(self, oidc_config: OIDCConfiguration, static_token: str, username: str, password: str, verify_ssl: bool):
        self.verify_ssl = True if verify_ssl is None else verify_ssl
        self.static_token = '' if static_token is None else static_token
        self.username = '' if username is None else username
        self.password = '' if password is None else password
        self.oidc_config = oidc_config

    @staticmethod
    def from_json(json_dct):
        oidc_config = OIDCConfiguration.from_json(json_dct.get('oidc_config'))
        return Security(oidc_config, json_dct.get('static_token'), json_dct.get('username'), json_dct.get('password'), json_dct.get('verify_ssl'))


class Client:
    url: str
    security: Security

    def __init__(self, url, security):
        self.url = url
        self.security = security

    def save(self,filepath: str):
        with open(filepath,"w",encoding='utf-8') as f:
            res = to_dict(self)
            yaml.safe_dump(res,f)

    @staticmethod
    def from_json(json_dct):
        security = Security.from_json(json_dct.get('security'))
        return Client(json_dct.get('url'), security)

def LoadClient(filepath: str) -> Client:
    with open(filepath,encoding='utf-8') as f:
        dm = yaml.safe_load(f)
        dumped = json.dumps(dm)
        client = Client.from_json(json.loads(dumped))
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

    oidc_config = OIDCConfiguration(
        oidc_url=os.getenv('OIDC_URL'),
        oidc_realm=os.getenv('OIDC_REALM'),
        oidc_client_id=os.getenv('OIDC_CLIENT_ID'),
        oidc_client_secret=os.getenv('OIDC_CLIENT_SECRET'),
    )

    security_config = Security(
        username=os.getenv('TI_USERNAME'),
        password=os.getenv('TI_PASSWORD'),
        static_token=os.getenv('TI_STATIC_TOKEN'),
        verify_ssl=literal_eval(os.getenv('TI_VERIFY_SSL')),
        oidc_config=oidc_config
    )
    client = Client(url=os.getenv('NODE_URL'), security=security_config)
    return client
