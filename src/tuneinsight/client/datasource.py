from typing import Any
from io import StringIO
import pandas as pd
import attr

from tuneinsight.api.sdk.types import Response
from tuneinsight.api.sdk.types import File
from tuneinsight.api.sdk import Client
from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.api.api_datasource import post_data_source
from tuneinsight.api.sdk.api.api_datasource import put_data_source_data
from tuneinsight.api.sdk.api.api_datasource import delete_data_source
from tuneinsight.api.sdk.api.api_dataobject import post_data_object
from tuneinsight.client.validation import validate_response
from tuneinsight.client.dataobject import DataObject

@attr.define
class DataSource:
    """
    DataSource represents a datasource stored on geco
    """

    model: models.DataSource
    client: Client

    @classmethod
    def from_definition(cls,client: Client,definition: models.DataSourceDefinition):
        """
        from_definition creates a new datasource on the backend given the data source definition

        Args:
            client (Client): the client to use to interact with the datasource
            definition (models.DataSourceDefinition): the definition of the datasource
        """
        response: Response[models.DataSource] = post_data_source.sync_detailed(client=client,json_body=definition)
        validate_response(response)
        return cls(model=response.parsed,client=client)


    @classmethod
    def local(cls,client: Client, name: str, clear_if_exists: bool = False):
        """
        local creates a new local datasource without any data

        Args:
            client (Client): the client to use to interact with the datasource
            name (str, optional): the name to give to the datasource. Defaults to "".
        """
        definition = default_datasource_definition()
        definition.name = name
        definition.clear_if_exists = clear_if_exists
        ds_config_type = models.DataSourceConfigType.LOCALDATASOURCECONFIG
        ds_conf = models.LocalDataSourceConfig(type=ds_config_type)
        definition.config = ds_conf
        definition.type = "local"


        return cls.from_definition(client,definition=definition)

    @classmethod
    def postgres(cls,client: Client,config: models.DatabaseConnectionInfo, name: str, clear_if_exists: bool = False):
        """
        postgres creates a new postgres database datasource

        Args:
            client (Client): the client to use to interact with the datasource
            config (models.PostgresDatabaseConfig): the postgres configuration
            name (str, optional): the name to give to the datasource. Defaults to "".
        """
        definition = default_datasource_definition()
        definition.name = name
        definition.clear_if_exists = clear_if_exists
        definition.type = "database"
        ds_config_type = models.DataSourceConfigType.DATABASEDATASOURCECONFIG
        credentials = models.Credentials(username=config.user,password=config.password,id="db-creds")
        local_creds = models.LocalCredentialsProvider(type=models.CredentialsProviderType.LOCALCREDENTIALSPROVIDER,credentials=[credentials])
        ds_config = models.DatabaseDataSourceConfig(type=ds_config_type,connection_info=config)
        definition.credentials_provider = local_creds
        definition.config = ds_config

        return cls.from_definition(client,definition=definition)

    @classmethod
    def from_api(cls,client: Client, api_type: models.APIConnectionInfoType, api_url: str, api_token: str, name: str, clear_if_exists: bool = False, cert: str = ""):
        """
        from_api creates a new api datasource

        Args:
            client (Client): the client to use to interact with the datasource
            config (models.PostgresDatabaseConfig): the postgres configuration
            name (str, optional): the name to give to the datasource. Defaults to "".
            clear_if_exists (str, optional): overwrite datasource if it already exists.
            cert (str, optional): name of the certificate to use for this datasource (must be accessible in note at "/usr/local/share/datasource-certificates/{cert}.pem,.key").
        """
        definition = default_datasource_definition()
        definition.name = name
        definition.clear_if_exists = clear_if_exists
        definition.type = "api"

        ds_config = models.ApiDataSourceConfig(type=models.DataSourceConfigType.APIDATASOURCECONFIG)
        ds_config.connection_info = models.APIConnectionInfo(api_token=api_token, api_url=api_url, type=api_type, cert=cert)
        definition.config = ds_config

        return cls.from_definition(client,definition=definition)



    @classmethod
    def from_dataframe(cls,client: Client,dataframe: pd.DataFrame, name: str, clear_if_exists: bool = False):
        ds = cls.local(client, name, clear_if_exists)
        ds.load_dataframe(df=dataframe)
        return ds



    def __str__(self):
        model = self.model
        return f'id: {model.unique_id}, name: {model.name}, type: {model.type}, createdAt: {model.created_at}'


    def get_id(self) -> str:
        """
        get_id returns the id of the datasource

        Returns:
            str: the id as a a string
        """
        return self.model.unique_id


    def adapt(self,do_type: models.DataObjectType,query: Any = "",json_path: str = "") -> DataObject:
        """
        adapt adapts the data source into a dataobject

        Args:
            do_type (models.DataObjectType): _description_
            query (Any, optional): _description_. Defaults to "".

        Returns:
            DataObject: _description_
        """
        method = models.DataObjectCreationMethod.DATASOURCE
        definition = models.PostDataObjectJsonBody(method=method,data_source_id=self.get_id(),type=do_type,query=query,json_path=json_path)
        response: Response[models.DataObject] = post_data_object.sync_detailed(client=self.client,json_body=definition)
        validate_response(response)
        return DataObject(model=response.parsed,client=self.client)

    def load_csv_data(self,path: str):
        """
        loadData loads csv data stored in the file "path" to the datasources

        Args:
            path (_type_): path to the csv file
        """
        with open(path,mode='+rb') as f:
            fileType = File(payload=f,file_name="test")
            mpd = models.PutDataSourceDataMultipartData(data_source_request_data=fileType)
            response: Response[models.DataSource] = put_data_source_data.sync_detailed(client=self.client,data_source_id=self.model.unique_id,multipart_data=mpd)
            f.close()
            validate_response(response)


    def load_dataframe(self,df: pd.DataFrame):
        f = StringIO(initial_value="")
        df.to_csv(f,index=False)
        mpd = models.PutDataSourceDataMultipartData(data_source_request_data_raw=f.getvalue())
        response: Response[models.DataSource] = put_data_source_data.sync_detailed(client=self.client,data_source_id=self.model.unique_id,multipart_data=mpd)
        validate_response(response)


    def get_dataframe(self,query: Any = "",json_path: str = "") -> pd.DataFrame:
        do = self.adapt(do_type=models.DataObjectType.TABLE,query=query,json_path=json_path)
        df = do.get_dataframe()
        do.delete()
        return df


    def delete(self):
        """
        delete deletes the datasource
        """
        response: Response[Any]= delete_data_source.sync_detailed(client=self.client,data_source_id=self.model.unique_id)
        validate_response(response)






def default_datasource_definition() -> models.DataSourceDefinition:
    """
    default_datasource_definition returns a default-valued DataSourceDefinition

    Returns:
        models.DataSourceDefinition: the definition with default values
    """
    return models.DataSourceDefinition(consent_type=models.DataSourceConsentType.UNKNOWN)



def new_postgres_config(host: str,port: str,name: str,user: str,password: str) -> models.DatabaseConnectionInfo:
    return models.DatabaseConnectionInfo(type=models.DatabaseType.POSTGRES,host=host,port=port,database=name,user=user,password=password)


def new_mariadb_config(host: str="mariadb",port: str="3306",name:str = "geco_0",user: str="geco",password:str = "geco")-> models.DatabaseConnectionInfo:
    return models.DatabaseConnectionInfo(type=models.DatabaseType.MYSQL,host=host,port=port,database=name,user=user,password=password)
