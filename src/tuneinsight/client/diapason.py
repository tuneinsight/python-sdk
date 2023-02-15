from typing import List
import attr
import pandas as pd
from tuneinsight.api.sdk.types import Response
from tuneinsight.api.sdk import client as api_client
from tuneinsight.api.sdk.api.api_project import post_project
from tuneinsight.api.sdk.api.api_project import get_project
from tuneinsight.api.sdk.api.api_project import get_project_list
from tuneinsight.api.sdk.api.api_datasource import get_data_source_list, get_data_source
from tuneinsight.api.sdk import models

from tuneinsight.client.datasource import DataSource
from tuneinsight.client.project import Project
from tuneinsight.client.validation import validate_response
from tuneinsight.client import config
from tuneinsight.client import auth


@attr.s(auto_attribs=True)
class Diapason:
    """
    Client is a wrapper around the client.AuthenticatedClient providing some useful utilities for using the Geco server

    Args:
        client (client.AuthenticatedClient): underlying client used to perform the requests
    """
    conf: config.Client
    client: api_client.Client = None

    def __attrs_post_init__(self):
        if self.conf.security.static_token != "":
            self.client = api_client.AuthenticatedClient(base_url=self.conf.url,token=self.conf.security.static_token,verify_ssl=self.conf.security.verify_ssl)
        else:
            self.client = auth.KeycloakClient(base_url=self.conf.url,token="",
                            kc_config=self.conf.security.kc_config,
                            username=self.conf.security.username,
                            password=self.conf.security.password,
                            verify_ssl=self.conf.security.verify_ssl)

    @classmethod
    def from_config_path(cls,path: str):
        conf = config.LoadClient(path)
        return cls(conf = conf)

    @classmethod
    def from_env(cls,path: str = None):
        """
        from_env creates a client from the environment variables or a "dotenv" file

        Args:
            path (str): path to the dotenv file. If None, it uses environment variables
        """
        conf = config.LoadEnvClient(path)
        return cls(conf = conf)

    def get_client(self):
        if self.client is None:
            raise Exception("client has not been created")
        return self.client

    def new_datasource(self, dataframe: pd.DataFrame, name: str = "") -> DataSource:
        return DataSource.from_dataframe(client=self.get_client(),dataframe=dataframe,name=name)

    def new_csv_datasource(self,csv: str,name: str = "") -> DataSource:
        ds =  DataSource.local(client= self.get_client(),name=name)
        ds.load_csv_data(path=csv)
        return ds

    def new_database(self,pg_config: models.DatabaseConnectionInfo,name: str = "") -> DataSource:
        return DataSource.postgres(client=self.get_client(),config=pg_config,name=name)

    def new_project(self, name: str, clear_if_exists: bool = False) -> Project:
        if name in [p.get_name() for p in self.get_projects()]:
            if clear_if_exists:
                self.clear_project(name=name)
            else:
                raise Exception("project " + name + " already exists")
        proj_def = models.ProjectDefinition(name=name,local=True,allow_shared_edit=True)
        proj_response: Response[models.Project] = post_project.sync_detailed(client=self.client,json_body=proj_def)
        validate_response(proj_response)
        return Project(model=proj_response.parsed,client=self.client)

    def get_project(self, project_id: str= "",name: str = "") -> Project:
        if project_id == "":
            return self.get_project_by_name(name=name)
        proj_response: Response[models.Project] = get_project.sync_detailed(client=self.client,project_id=project_id)
        validate_response(proj_response)
        return Project(model=proj_response.parsed,client=self.client)

    def get_projects(self) -> List[Project]:
        response: Response[List[models.Project]] = get_project_list.sync_detailed(client=self.client)
        validate_response(response)
        projects = []
        for project in response.parsed:
            projects.append(Project(model=project,client=self.client))
        return projects

    def get_project_by_name(self, name:str) -> Project:
        projects = self.get_projects()
        for p in projects:
            if p.get_name() == name:
                return self.get_project(project_id=p.get_id())
        raise Exception("project not found")

    def get_datasources(self) -> List[DataSource]:
        response: Response[List[models.DataSource]] = get_data_source_list.sync_detailed(client=self.client)
        validate_response(response)
        datasources = []
        for datasource in response.parsed:
            datasources.append(DataSource(model=datasource,client=self.client))
        return datasources

    def get_datasource(self, ds_id: str= "",name: str = "") -> DataSource:
        if ds_id == "":
            return self.get_datasource_by_name(name=name)
        ds_response: Response[models.DataSource] = get_data_source.sync_detailed(client=self.client,data_source_id=ds_id)
        validate_response(ds_response)
        return DataSource(model=ds_response.parsed,client=self.client)

    def get_datasource_by_name(self, name:str) -> DataSource:
        datasources = self.get_datasources()
        found = []
        for ds in datasources:
            if ds.model.name == name:
                found.append(ds)
        # take most recent ds
        if len(found) > 0:
            latest_ds = found[-1]
            return self.get_datasource(ds_id=latest_ds.get_id())
        raise Exception("datasource not found")

    def clear_project(self, project_id: str = "", name: str = "") :
        p = self.get_project(project_id=project_id, name=name)
        p.delete()
