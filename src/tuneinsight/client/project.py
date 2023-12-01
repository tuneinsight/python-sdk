from typing import List
import attr
import pandas as pd
from IPython.display import display, HTML, Markdown
from tuneinsight.api.sdk.types import UNSET,Unset
from tuneinsight.api.sdk.types import Response
from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.api.api_project import patch_project, post_project_computation
from tuneinsight.api.sdk.api.api_project import get_project
from tuneinsight.api.sdk.api.api_project import delete_project
from tuneinsight.api.sdk.api.api_datasource import get_data_source
from tuneinsight.computations.enc_aggregation import EncryptedAggregation
from tuneinsight.computations.gwas import GWAS
from tuneinsight.computations.survival_aggregation import SurvivalAggregation
from tuneinsight.computations.regression import LinearRegression, LogisticRegression, PoissonRegression
from tuneinsight.computations.cohort import Cohort
from tuneinsight.computations.secure_join import SecureJoin
from tuneinsight.computations.hybrid_fl import HybridFL
from tuneinsight.computations.stats import DatasetStatistics
from tuneinsight.computations.policy import Policy,display_policy
from tuneinsight.computations.types import Type
from tuneinsight.computations.dataset_schema import DatasetSchema
from tuneinsight.client.validation import validate_response
from tuneinsight.computations.statistical_aggregation import Aggregation
from tuneinsight.client.computations import ComputationRunner
from tuneinsight.client.datasource import DataSource
from tuneinsight.client.dataobject import DataObject
from tuneinsight.client.local_data_selection import LocalDataSelection


@attr.s(auto_attribs=True)
class Project:
    """
    Represents a project from the backend Agent
    """
    model: models.Project # The underlying model
    client: UNSET # the client used to access the api

    def get_id(self) -> str:
        """
        get_id returns the project id

        Returns:
            str: the project's id
        """
        return self.model.unique_id

    def __str__(self):
        """
        __str__ computes the string representation of a project

        Returns:
            _type_: returns the string representation of a project
        """
        res = ""
        res += f"id: {self.get_id()} \n"
        res += f"name: {self.get_name()} \n"
        res += f"topology: {self.get_topology()} \n"
        res += "participants:\n"
        participants: List[models.Participant] = self.model.participants
        for p in participants:
            org = p.node.organization
            res += f"\tnode: {p.node.name}"
            if org.name:
                res += f" (organization: {org.name})"
            res += "\n"

            if p.input_metadata != UNSET\
                and UNSET not in (p.input_metadata,p.input_metadata.tables)\
                and len(p.input_metadata.tables):
                res += "\tinput tables :\n"
                tables: List[models.DataSourceTable] = p.input_metadata.tables
                for table in tables:
                    res += f'\t\ttable name: {table.name}\n'
                    res += '\t\tcolumns:\n'
                    cols: List[models.DataSourceColumn] = table.columns
                    for col in cols:
                        res += f'\t\t\tname: {col.name}, type: {col.type} type group: {col.type_group}\n'
                    res += '\n'
            res += "\n"
        if self.model.computations != UNSET and len(self.model.computations) > 0:
            res += "computations: \n"
            computations: List[models.Computation] = self.model.computations
            for comp in computations:
                res += f"\t{comp.created_at},{comp.definition.type}\n"
        return res

    def get_name(self) -> str:
        """
        get_name returns the name of the project

        Returns:
            str: the name of the project
        """
        return self.model.name

    def get_topology(self) -> str:
        """
        get_topology returns the topology of the project

        Returns:
            str: the topology of the project
        """
        return str(self.model.topology)

    def display_datasources(self):
        self.refresh()
        participants = self.model.participants
        for p in participants:
            tables = p.input_metadata.tables
            display(Markdown("### Participant: " + "`" + str(p.node.name) + "`"))
            for t in tables:
                # print(f"Table name: {t.name}")
                display(Markdown("#### Table name: " + "`" + str(t.name) + "`"))
                data={'Column': [], 'Type': []}
                num_cols = len(t.columns)
                for i in range(num_cols):
                    data['Column'].append(t.columns[i].name)
                    data['Type'].append(t.columns[i].type)
                df = pd.DataFrame(data['Type'], index=data['Column']).T
                display(HTML(df.to_html(index=False)))
            print("\n")


    def set_input_schema(self,schema: DatasetSchema):
        '''
        set_input_schema sets an expected schema to enforce on the inputs.

        Args:
            schema (DatasetSchema): the schema definition
        '''
        lds = self.local_data_selection()
        lds.preprocessing.schema = schema
        lds.save()

    def delete(self):
        resp: Response[str] = delete_project.sync_detailed(client=self.client,project_id=self.get_id())
        validate_response(response=resp)



    def refresh(self):
        """
        refresh refreshes the project's model with its backend state
        """
        resp: Response[models.Project] = get_project.sync_detailed(client=self.client,project_id=self.get_id())
        validate_response(response=resp)
        self.model = resp.parsed


    def query_datasource(self,query: str) -> pd.DataFrame:
        ds = self.get_input_datasource()
        return ds.get_dataframe(query=query)


    def patch(self,proj_def: models.ProjectDefinition):
        """
        patch perform a patch operation on the project

        Args:
            proj_def (models.ProjectDefinition): the definition to patch with
        """
        resp: Response[models.Project] = patch_project.sync_detailed(client=self.client,project_id=self.get_id(),json_body=proj_def)
        validate_response(response=resp)
        self.model = resp.parsed

    def authorize(self):
        self.patch(proj_def=models.ProjectDefinition(authorization_status=models.AuthorizationStatus.AUTHORIZED))


    def unauthorize(self):
        self.patch(proj_def=models.ProjectDefinition(authorization_status=models.AuthorizationStatus.UNAUTHORIZED))

    def share(self):
        """
        share shares the project with the network
        """
        proj_def = models.ProjectDefinition(shared=True,local=False)
        self.patch(proj_def=proj_def)

    def unshare(self):
        """
        unshare unshares the project with the network
        """
        proj_def = models.ProjectDefinition(shared=False)
        self.patch(proj_def=proj_def)

    def set_computation(self,definition: models.ComputationDefinition):
        """
        set_computation Sets the project's current computation definition

        Args:
            definition (models.ComputationDefinition): the definition to apply
        """
        self.patch(proj_def=models.ProjectDefinition(computation_definition=definition,broadcast=True))

    def set_input_datasource_id(self, datasourceId: str):
        """
        set_input_datasource_id sets the project's input datasource with its ID

        Args:
            datasourceId (str): the datasource ID to the project
        """
        proj_def = models.ProjectDefinition(data_source_id=datasourceId)
        self.patch(proj_def=proj_def)

    def set_input_datasource(self,ds: DataSource):
        """
        set_input_datasource sets the project's input datasource

        Args:
            ds (DataSource): the datasource to link to the project
        """
        proj_def = models.ProjectDefinition(data_source_id=ds.get_id())
        self.patch(proj_def=proj_def)


    def get_input_datasource(self) -> DataSource:
        """
        get_input_datasource returns the datasource linked to the project

        Raises:
            Exception: if no datasource was linked to the project

        Returns:
            DataSource: the datasource linked to the project
        """
        self.refresh()
        if self.model.data_source_id == "":
            raise Exception("no data source set to project")
        resp: Response[models.DataSource] = get_data_source.sync_detailed(data_source_id=self.model.data_source_id,client=self.client)
        validate_response(resp)
        return DataSource(model=resp.parsed,client=self.client)

    def get_runner(self) -> ComputationRunner:
        """
        get_runner returns the computation runner for the project

        Returns:
            ComputationRunner: the computation runner set with the project id
        """
        return ComputationRunner(client=self.client,project_id=self.get_id())

    def get_participants(self) -> List[str]:
        """
        get_participants returns the names of the participating nodes

        Returns:
            List[str]: a list of the names of the participating nodes
        """
        return [p.node.name for p in self.model.participants]


    def run_computation(self,comp: models.ComputationDefinition,local: bool=False,keyswitch: bool=True,decrypt: bool=True) -> List[DataObject]:
        """
        run_computation runs the given computation definition and returns the list of resulting dataobjects

        Args:
            comp (models.ComputationDefinition): the computation definition to run
            local (bool, optional): whether or not to run the computation locally. Defaults to False.
            keyswitch (bool, optional): whether or not to key switch the results from the computation. Defaults to True.
            decrypt (bool, optional): whether or not to decrypt the results. Defaults to True.

        Returns:
            List[DataObject]: the list of resulting dataobjects
        """
        runner = self.get_runner()
        comp.data_source_parameters = models.ComputationDataSourceParameters()
        return runner.run_computation(comp=comp,local=local,keyswitch=keyswitch,decrypt=decrypt)

    def run_project(self) -> models.Project:
        """Run the computation defined on the project

        Returns:
            models.Project: Project Computation Created
        """
        response : Response[models.Project] = post_project_computation.sync_detailed(
            project_id=self.get_id(),
            client=self.client,
            json_body=None
        )
        validate_response(response)
        return response.parsed


    def new_aggregation(self) -> Aggregation:
        """
        new_aggregation returns a new Aggregation Computation which can be computed by running the project

        Returns:
            StatisticalAggregation: The aggregation computation
        """
        return Aggregation(client=self.client,project_id=self.get_id())


    def new_enc_aggregation(self) -> EncryptedAggregation:
        """
        new_aggregation returns a new Aggregation Computation which can be computed by running the project

        Returns:
            Aggregation: The aggregation computation
        """
        return EncryptedAggregation(client=self.client,project_id=self.get_id())


    def new_cohort(self) -> Cohort:
        """
        new_cohort returns a new Cohort

        Returns:
            Cohort: The cohort
        """
        return Cohort(client=self.client,project_id=self.get_id())

    def new_gwas(self) -> GWAS:
        """
        new_gwas returns a new GWAS which can be computed by running the project

        Returns:
            GWAS: The GWAS computation
        """
        return GWAS(client=self.client,project_id=self.get_id())

    def new_linear_regression(self, continuous_labels:bool = False) -> LinearRegression:
        """
        new_linear_regression returns a new LinearRegression which can be computed by running the project
        Returns:
            LinearRegression: The linear regression computation
        """
        return LinearRegression(client=self.client,project_id=self.get_id(), continuous_labels=continuous_labels)

    def new_logistic_regression(self, approximation_params:models.approximation_params.ApproximationParams=UNSET) -> LogisticRegression:
        """
        new_logistic_regression returns a new LogisticRegression which can be computed by running the project
        Returns:
            LogisticRegression: The logistic regression computation
        """
        return LogisticRegression(client=self.client,project_id=self.get_id(), approximation_params=approximation_params)

    def new_poisson_regression(self) -> PoissonRegression:
        """
        new_poisson_regression returns a new PoissonRegressor which can be computed by running the project
        Returns:
            PoissonRegressor: The poisson regression computation
        """
        return PoissonRegression(client=self.client,project_id=self.get_id())


    def new_survival_aggregation(self) -> SurvivalAggregation:
        """
    new_survival_aggregation returns a new SurvivalAggregation which can be computed by running the project
    Returns:
        SurvivalAggregation: The survival aggregation computation
    """
        return SurvivalAggregation(client=self.client,project_id=self.get_id())


    def new_secure_join(self) -> SecureJoin:
        '''
        new_secure_join returns a new SecureJoin which can be computed by running the project

        Returns:
            SecureJoin: the secure join computation instance
        '''
        return SecureJoin(client=self.client,project_id=self.get_id())

    def new_hybrid_fl(self) -> HybridFL:
        '''
        new_hybrid_fl returns a new HybridFL which can be computed by running the project

        Returns:
            HybridFL: the hybrid federated learning computation instance
        '''
        return HybridFL(client=self.client, project_id=self.get_id())

    def new_statistics(self) -> DatasetStatistics:
        '''
        new_statistics returns a new DatasetStatistics instance which can run statistics on the project

        Returns:
            DatasetStatistics: the dataset statistics computation instance
        '''
        return DatasetStatistics(client=self.client,project_id=self.get_id())


    def set_policy(self,policy: Policy):
        '''
        set_policy sets the policy to the project

        Args:
            policy (Policy): the policy to add to the project
        '''
        proj_def = models.ProjectDefinition(policy=policy)
        self.patch(proj_def=proj_def)

    def display_policy(self,detailed:bool = False,show_queries: bool = False):
        '''
        display_policy displays the policies associated to the project

        Args:
            detailed (bool, optional): shows additional policy details if set to true such as the json of the policy. Defaults to False.
            show_queries (bool, optional): shows the set of authorized SQL queries. Defaults to False.
        '''
        policy = self.model.policy
        display(Markdown(f'# {self.model.name} Policy'))
        if policy is Unset:
            print("project has no policy")
        if isinstance(policy,Unset):
            return
        display_policy(policy,detailed=detailed,show_queries=show_queries)


    def local_data_selection(self) -> LocalDataSelection:
        '''
        local_data_selection returns the local data selection settings for the project

        Returns:
            LocalDataSelection: the data selection settings that can be updated by the user
        '''

        def update_func(definition: models.LocalDataSelectionDefinition) -> models.LocalDataSelection:
            proj_def = models.ProjectDefinition()
            proj_def.local_data_selection_definition = definition
            self.patch(proj_def)
            self.refresh()
            return self.model.local_data_selection_definition

        lds = LocalDataSelection(update_func)
        self.refresh()
        return lds


    def display_workflow(self):
        '''
        display_workflow displays the workflow description for the project
        '''
        self.refresh()
        display(Markdown(self.model.workflow_description))


    def set_computation_type(self,comp_type: Type):
        definition = models.ComputationDefinition(type=comp_type)
        self.set_computation(definition)
