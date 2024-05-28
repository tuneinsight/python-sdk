"""Classes to interact with Tune Insight projects."""

from typing import List, Tuple, Union
import warnings

from dateutil.parser import isoparse

import attr
import pandas as pd

from tuneinsight.api.sdk.types import UNSET, Unset
from tuneinsight.api.sdk.types import Response
from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.api.api_project import patch_project, post_project_computation
from tuneinsight.api.sdk.api.api_project import get_project
from tuneinsight.api.sdk.api.api_project import delete_project
from tuneinsight.api.sdk.api.api_datasource import get_data_source
from tuneinsight.api.sdk.api.api_computations import documentation

from tuneinsight.computations.enc_aggregation import EncryptedAggregation
from tuneinsight.computations.encrypted_mean import EncryptedMean
from tuneinsight.computations.gwas import GWAS
from tuneinsight.computations.intersection import SetIntersection
from tuneinsight.computations.survival import SurvivalAnalysis, SurvivalParameters
from tuneinsight.computations.regression import (
    LinearRegression,
    LogisticRegression,
    PoissonRegression,
)
from tuneinsight.computations.cohort import Cohort
from tuneinsight.computations.secure_join import SecureJoin
from tuneinsight.computations.hybrid_fl import HybridFL
from tuneinsight.computations.stats import Statistics
from tuneinsight.computations.policy import Policy, display_policy
from tuneinsight.api.sdk.models import ComputationType as Type
from tuneinsight.computations.dataset_schema import DatasetSchema
from tuneinsight.client.validation import validate_response
from tuneinsight.computations.statistical_aggregation import GroupByAggregation
from tuneinsight.client.datasource import DataSource
from tuneinsight.client.dataobject import DataObject
from tuneinsight.computations.local_data_selection import LocalDataSelection
from tuneinsight.utils import deprecation
from tuneinsight.utils.display import Renderer


@attr.s(auto_attribs=True)
class Project:
    """
    A project saved in the Tune Insight instance.

    Projects define a network of participants and a computation to run collectively,
    using one (input) datasource in each instance, potentially constrained by
    policies. The core of a project is thus the definition of the computation that
    will be run: a project object has many new_... methods to create a computation
    on the project.

    Importantly, a project can only be linked to one computation at a time,
    but this computation can change over time. For instance, one can set up
    an aggregation, run the project, then set up a logistic regression, and
    run the project again. All results will remain available as data objects.

    This class wraps the models.Project class from the API, providing a more
    user-friendly interface, and interfaces several API endpoints. It is
    recommended to create a project through Diapason.new_project rather than
    manually building a models.Project object.

    Args for __init__ (to do it manually):
        model: the model.Project from the API that this object wraps.
        client: the client used to access the API.
    """

    model: models.Project  # The underlying model
    client: Unset  # the client used to access the api

    datasource: DataSource = None

    def __attrs_post_init__(self):
        """Create a datasource object if one is defined in the project model."""
        if (
            not isinstance(self.model.data_source_id, Unset)
            and self.model.data_source_id
        ):
            self.datasource = DataSource.fetch_from_id(
                self.client, self.model.data_source_id
            )

    # Internal methods.

    def _refresh(self):
        """
        Refreshes the project's model by fetching its model on the Tune Insight instance.
        """
        resp: Response[models.Project] = get_project.sync_detailed(
            client=self.client, project_id=self.get_id()
        )
        validate_response(response=resp)
        self.model = resp.parsed

    def _patch(self, proj_def: models.ProjectDefinition):
        """
        Update (patch) this project's definition.

        Args:
            proj_def (models.ProjectDefinition): the definition to patch with.
        """
        resp: Response[models.Project] = patch_project.sync_detailed(
            client=self.client, project_id=self.get_id(), json_body=proj_def
        )
        validate_response(response=resp)
        self.model = resp.parsed

    # Getters for model values.

    def get_id(self) -> str:
        """
        Returns the unique identifier of this project.

        Returns:
            str: the project's ID.
        """
        return self.model.unique_id

    def get_name(self) -> str:
        """
        Returns the name of this project.

        Returns:
            str: the name of the project.
        """
        return self.model.name

    def get_description(self) -> str:
        """
        Returns the description of this project.

        Returns:
            str: the description of the project
        """
        return self.model.description

    def get_topology(self) -> str:
        """
        Returns the topology of this project.

        Returns:
            str: the topology of the project
        """
        return str(self.model.topology)

    def get_computation(self) -> models.ComputationDefinition:
        """
        Returns the project's current computation definition.

        Returns:
            models.ComputationDefinition: the project's current computation definition
        """
        self._refresh()
        return self.model.computation_definition

    def get_authorization_status(self) -> models.AuthorizationStatus:
        """
        Returns the project's authorization status.

        Returns:
            models.AuthorizationStatus: the project's authorization status
        """
        self._refresh()
        return self.model.authorization_status

    def get_input_datasource(self) -> DataSource:
        """
        Returns the datasource linked to the project.

        Raises:
            LookupError: if no datasource was linked to the project

        Returns:
            DataSource: the datasource linked to the project.
        """
        self._refresh()
        if self.model.data_source_id == "":
            raise LookupError("no data source set to project")
        resp: Response[models.DataSource] = get_data_source.sync_detailed(
            data_source_id=self.model.data_source_id, client=self.client
        )
        validate_response(resp)
        return DataSource(model=resp.parsed, client=self.client)

    def get_participants(self) -> List[str]:
        """
        Refreshes the state of the project and returns the list of participants.

        Returns:
            List[str]: a list of the names of the participating nodes
        """
        self._refresh()
        parts: List[models.Participant] = self.model.participants
        return parts

    def get_authorized_users(self) -> List[str]:
        """
        Returns the email addresses of the authorized users.

        Returns:
            List[str]: a list of the email addresses of the authorized users
        """
        return self.model.authorized_users

    # Setters for model values.

    def set_computation_type(self, comp_type: Type):
        """
        Sets the computation type of the project's computation definition.

        This creates an empty computation definition of the chosen type. Intended for tests.

        """
        definition = models.ComputationDefinition(type=comp_type)
        self.set_computation(definition)

    def set_contribution_status(self, contributes: bool):
        """
        Sets the local contributing status of the instance. If set to False, this instance
        will not contribute any data when running computations.

        Args:
            contributes (bool): whether the instance contributes data.
        """
        proj_def = models.ProjectDefinition()
        proj_def.non_contributor = not contributes
        self._patch(proj_def=proj_def)

    def set_input_schema(self, schema: DatasetSchema):
        """
        Sets an expected schema to enforce on the inputs.

        Args:
            schema (DatasetSchema): the schema definition.
        """
        lds = self.get_local_data_selection()
        lds.preprocessing.schema = schema
        lds.save()

    def set_computation(self, definition: models.ComputationDefinition):
        """
        Sets the project's current computation definition.

        This method can be used to manually change the computation to run. It is
        however recommended to use the relevant new_... method instead.

        Args:
            definition (models.ComputationDefinition): the definition to apply
        """
        self._patch(
            proj_def=models.ProjectDefinition(
                computation_definition=definition, broadcast=True
            )
        )

    def set_input_datasource_id(self, datasourceId: str):
        """
        Sets this project's input datasource with its ID.

        Args:
            datasourceId (str): the datasource ID to the project
        """
        deprecation.warn("set_input_datasource_id", "set_input_datasource")
        proj_def = models.ProjectDefinition(data_source_id=datasourceId)
        self._patch(proj_def=proj_def)

    def set_input_datasource(self, ds: Union[DataSource, str]):
        """
        Sets this project's input datasource.

        Args:
            ds (DataSource | str): the datasource to link to the project, or its ID.
        """
        ds_id = ds
        if isinstance(ds, DataSource):
            ds_id = ds.get_id()
        proj_def = models.ProjectDefinition(data_source_id=ds_id)
        self._patch(proj_def=proj_def)
        # If the user provided an ID, create a datasource from this ID. Otherwise the same object is reused.
        if isinstance(ds, DataSource):
            self.datasource = ds
        else:
            self.datasource = DataSource.fetch_from_id(self.client, ds)

    def set_policy(self, policy: Policy):
        """
        Sets the policy of this project.

        Args:
            policy (Policy): the policy to add to the project
        """
        self._refresh()
        participants: List[models.Participant] = self.model.participants
        for participant in participants:
            if (
                participant.authorization_status
                == models.AuthorizationStatus.AUTHORIZED
            ):
                warnings.warn(
                    f"{participant.node.name} has already authorized their project, policy modifications will likely be refused by their instance."
                )

        proj_def = models.ProjectDefinition(policy=policy)
        self._patch(proj_def=proj_def)

    # Project administration.

    def delete(self):
        """
        Deletes this project.

        Note that this only deleted the project locally. Other instances must
        delete the project themselves.
        """
        resp: Response[str] = delete_project.sync_detailed(
            client=self.client, project_id=self.get_id()
        )
        validate_response(response=resp)

    def authorize(self):
        """
        Authorizes the project.

        This enables other participants will be able to run collective computations.
        Only authorize a project after you have carefully reviewed the computation
        parameters, data query parameters, and policy of this project.
        """
        self._patch(
            proj_def=models.ProjectDefinition(
                authorization_status=models.AuthorizationStatus.AUTHORIZED
            )
        )

    def unauthorize(self):
        """
        Unauthorize any collective computation with this project.

        Other participants will not be able to run collective computations on this project.
        """
        self._patch(
            proj_def=models.ProjectDefinition(
                authorization_status=models.AuthorizationStatus.UNAUTHORIZED
            )
        )

    def share(self):
        """
        Shares the project with the network. The project can still be updated afterwards.
        """
        proj_def = models.ProjectDefinition(shared=True, local=False)
        self._patch(proj_def=proj_def)

    def unshare(self):
        """
        Unshares the project with the network.
        """
        proj_def = models.ProjectDefinition(shared=False)
        self._patch(proj_def=proj_def)

    # Advanced data management.

    def query_datasource(self, query: str = "") -> pd.DataFrame:
        """
        Fetches the content of this project's datasource through a data query.

        Args
            query (str, optional): the query to select records in the data.

        """
        ds = self.get_input_datasource()
        return ds.get_dataframe(query=query)

    def get_local_data_selection(self) -> LocalDataSelection:
        """
        Returns the local data selection settings for the project.

        A LocalDataSelection contains both data source and preprocessing parameters, and
        can be used to abstract data processing operations from computations.

        Returns:
            LocalDataSelection: the data selection settings that can be updated by the user
        """

        def update_func(
            definition: models.LocalDataSelectionDefinition,
        ) -> models.LocalDataSelection:
            proj_def = models.ProjectDefinition()
            proj_def.local_data_selection_definition = definition
            self._patch(proj_def)
            self._refresh()
            return self.model.local_data_selection_definition

        lds = LocalDataSelection(update_func)
        self._refresh()
        return lds

    # Advanced computations interface.

    def run_computation(
        self,
        comp: models.ComputationDefinition,
        local: bool = False,
        keyswitch: bool = True,
        decrypt: bool = True,
    ) -> List[DataObject]:
        """
        Runs the given computation definition and returns the list of resulting dataobjects

        Args:
            comp (models.ComputationDefinition): the computation definition to run
            local (bool, optional): whether or not to run the computation locally. Defaults to False.
            keyswitch (bool, optional): whether or not to key switch the results from the computation. Defaults to True.
            decrypt (bool, optional): whether or not to decrypt the results. Defaults to True.

        Returns:
            List[DataObject]: the list of resulting dataobjects
        """
        deprecation.warn("project.run_computation", "project.run")
        self.set_computation(comp)
        comp.local = local
        comp.keyswitch = keyswitch
        comp.decrypt = decrypt
        return self.run()

    def run(
        self,
    ) -> models.Project:
        """
        Run the computation defined on the project.

        This runs the computation set with self.set_computation.

        Returns:
            models.Project: Project Computation Created
        """
        response: Response[models.Project] = post_project_computation.sync_detailed(
            project_id=self.get_id(), client=self.client, json_body=None
        )
        validate_response(response)
        return response.parsed

    # List of all computations that can be created in this project.

    def new_aggregation(self) -> GroupByAggregation:
        """
        Returns a new Aggregation Computation which can be computed by running the project.

        Returns:
            Aggregation: The aggregation computation.
        """
        return GroupByAggregation(project=self)

    def new_enc_aggregation(
        self, selected_columns: List[str] = UNSET
    ) -> EncryptedAggregation:
        """
        Returns a new Aggregation Computation which can be computed by running the project.

        Args:
            selected_columns (optional): list of columns to perform the aggregation on.

        Returns:
            Aggregation: The aggregation computation
        """
        return EncryptedAggregation(project=self, selected_columns=selected_columns)

    def new_enc_mean(self, variables: List[str], participant: str) -> EncryptedMean:
        """
        Returns a new EncryptedMean computation runner.

        Args
            variables (list[str]): the variables for which to compute the mean and stddev.
            participant (str): name of the participants column.
        """
        return EncryptedMean(project=self, variables=variables, participant=participant)

    def new_cohort(self) -> Cohort:
        """
        Returns a new Cohort.

        Note: creating a Cohort to run a set intersection is deprecated.
        Use SetIntersection or SecureJoin instead, both of which output a Cohort.

        Returns:
            Cohort: The cohort
        """
        deprecation.warn("project.new_cohort", "Intersection / SecureJoin", True)
        return Cohort(project=self)

    def new_gwas(self) -> GWAS:
        """
        Returns a new GWAS which can be computed by running the project.

        Returns:
            GWAS: The GWAS computation
        """
        return GWAS(project=self)

    def new_linear_regression(
        self, continuous_labels: bool = False
    ) -> LinearRegression:
        """
        Returns a new LinearRegression which can be computed by running the project.

        Args:
            continuous_labels (bool): If true, then expects continuous labels (i.e. not binary).

        Returns:
            LinearRegression: The linear regression computation
        """
        return LinearRegression(
            project=self,
            continuous_labels=continuous_labels,
        )

    def new_logistic_regression(
        self,
        approximation_params: models.approximation_params.ApproximationParams = UNSET,
    ) -> LogisticRegression:
        """
        Returns a new LogisticRegression which can be computed by running the project.

        Args:
            approximation_params: parameters of the sigmoid approximation.

        Returns:
            LogisticRegression: The logistic regression computation
        """
        return LogisticRegression(
            project=self,
            approximation_params=approximation_params,
        )

    def new_poisson_regression(self) -> PoissonRegression:
        """
        Returns a new PoissonRegressor which can be computed by running the project.

        Returns:
            PoissonRegressor: The poisson regression computation
        """
        return PoissonRegression(project=self)

    def new_survival_aggregation(
        self, parameters: SurvivalParameters
    ) -> SurvivalAnalysis:
        """
        Returns a new SurvivalAggregation which can be computed by running the project.

        Args:
            parameters (SurvivalParameters): configuration for the survival aggregation.

        Returns:
            SurvivalAggregation: The survival aggregation computation
        """
        return SurvivalAnalysis(project=self, survival_parameters=parameters)

    def new_secure_join(self, target_columns, join_columns) -> SecureJoin:
        """
        Returns a new SecureJoin which can be computed by running the project

        Args
            target_columns (List[str]): column names of target columns
            join_columns (List[str]): column names to join the data on

        Returns:
            SecureJoin: the secure join computation instance
        """
        return SecureJoin(
            project=self, target_columns=target_columns, join_columns=join_columns
        )

    def new_hybrid_fl(
        self,
        task_id: str,
        learning_params: models.HybridFLLearningParams,
    ) -> HybridFL:
        """
        Returns a new HybridFL which can be computed by running the project.

        Args
            task_id (str): a unique identifier for this learning task.
            learning_params (models.HybridDFLLEarningParams): parameters of the computation.

        Returns:
            HybridFL: the hybrid federated learning computation instance
        """
        return HybridFL(project=self, task_id=task_id, learning_params=learning_params)

    def new_statistics(self, variables: List[str] = None) -> Statistics:
        """
        Returns a new DatasetStatistics instance which can run statistics on the project.

        Args:
            variables (list of str or dict): the variables to which this computation applies.

        Returns:
            DatasetStatistics: the dataset statistics computation instance
        """
        return Statistics(project=self, variables=variables)

    def new_intersection(self, columns: Union[str, List[str]]) -> SetIntersection:
        """
        Creates a new set intersection computation instance.

        Args:
            columns (str or list[str]): the column or list of columns on which to match records.

        Returns:
            SetIntersection: the set intersection computation instance
        """
        return SetIntersection(project=self, matching_columns=columns)

    # User-friendly displays.

    def get_latest_measurements(self):
        """
        get_latest_measurements returns a dictionary that contains the benchmarking measurement of the last computation
        that was run in the project. The dictionary contains benchmarking information about the processing time and
        memory allocation at each phase of the computation.

        Returns:
            dict: a dictionary containing the measurements.
        """
        self._refresh()
        res = {}
        latest_comp = None
        comps: List[models.Computation] = self.model.computations
        for comp in comps:
            if comp.definition.type != models.ComputationType.COLLECTIVEKEYSWITCH:
                latest_comp = comp
                break
        if latest_comp is None:
            return res
        measurements: List[models.Measurement] = latest_comp.measurements
        for measure in measurements:
            start_datetime = isoparse(measure.start[:-1])
            end_datetime = isoparse(measure.end[:-1])
            time_diff_seconds = (end_datetime - start_datetime).total_seconds()
            measurement = {
                "Processing time (seconds)": round(time_diff_seconds, 3),
                "Memory allocated (bytes)": measure.allocated,
            }
            res[measure.name] = measurement
        start_datetime = isoparse(latest_comp.started_at[:-1])
        end_datetime = isoparse(latest_comp.ended_at[:-1])
        time_diff_seconds = (end_datetime - start_datetime).total_seconds()
        res["Total time"] = round(time_diff_seconds, 3)
        return res

    def __str__(self):
        """
        Computes a human-readable string representation of this project.

        Returns:
            str: returns the string representation of a project
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

            if (
                p.input_metadata != UNSET
                and UNSET not in (p.input_metadata, p.input_metadata.tables)
                and len(p.input_metadata.tables)
            ):
                res += "\tinput tables :\n"
                tables: List[models.DataSourceTable] = p.input_metadata.tables
                for table in tables:
                    res += f"\t\ttable name: {table.name}\n"
                    res += "\t\tcolumns:\n"
                    cols: List[models.DataSourceColumn] = table.columns
                    for col in cols:
                        res += f"\t\t\tname: {col.name}, type: {col.type} type group: {col.type_group}\n"
                    res += "\n"
            res += "\n"
        if self.model.computations != UNSET and len(self.model.computations) > 0:
            res += "computations: \n"
            computations: List[models.Computation] = self.model.computations
            for comp in computations:
                res += f"\t{comp.created_at},{comp.definition.type}\n"
        return res

    def display_previous_workflow(self):
        """
        display_previous_workflow displays (compatible with jupyter notebooks) a markdown workflow summary of the last computation
        that was run in the project.
        """
        r = Renderer()
        if len(self.model.computations) == 0:
            r("No computation have been run with this project")
            return
        comp = self.model.computations[0].definition
        response: Response[models.DocumentationResponse200] = (
            documentation.sync_detailed(client=self.client, json_body=comp)
        )
        validate_response(response)
        md_doc = response.parsed.description.replace("\n", "\n\n")
        r(md_doc)

    def display_workflow(self):
        """
        display_workflow displays the workflow description for the project
        """
        self._refresh()
        r = Renderer()
        r(self.model.workflow_description)

    def display_datasources(self):
        """
        Displays the datasources linked to this project using IPython.display.
        """
        self._refresh()
        participants = self.get_participants()
        r = Renderer()
        for p in participants:
            if isinstance(p.input_metadata, Unset):
                continue
            tables = p.input_metadata.tables
            contributes_text = "contributor" if p.is_contributor else "non-contributor"
            r.h3("Participant: ", r.code(p.node.name), f"({contributes_text})")
            for t in tables:
                # print(f"Table name: {t.name}")
                r.h4("Table name:", r.code(t.name))
                data = {"Column": [], "Type": []}
                num_cols = len(t.columns)
                for i in range(num_cols):
                    data["Column"].append(t.columns[i].name)
                    data["Type"].append(t.columns[i].type)
                df = pd.DataFrame(data["Type"], index=data["Column"]).T
                r.df(df)
            r.end_paragraph()

    def get_participants_names(self) -> List[str]:
        """
        Returns the names of the participating nodes.

        Returns:
            List[str]: a list of the names of the participating nodes
        """
        return [p.node.name for p in self.model.participants]

    def display_policy(self, detailed: bool = False, show_queries: bool = True):
        """
        Displays the policies associated to the project.

        Args:
            detailed (bool, optional): if True, shows additional policy details
                such as the json of the policy. Defaults to False.
            show_queries (bool, optional): shows the set of authorized SQL queries.
                Defaults to False.
        """
        self._refresh()
        policy = self.model.policy
        r = Renderer()
        r.h1(self.model.name, "Policy")
        if policy is Unset:
            r("Project has no policy.")
        if isinstance(policy, Unset):
            return
        display_policy(policy, detailed=detailed, show_queries=show_queries)

    def get_policy(self) -> Policy:
        """
        Returns the project's policy that can then be edited.

        Returns:
            Policy: the editable policy
        """
        self._refresh()
        return Policy.from_model(self.model.policy)

    @property
    def is_differentially_private(self):
        """Returns whether differential privacy is enabled for this project."""
        if isinstance(self.model.policy, Unset):
            return False
        dp_policy = self.model.policy.dp_policy
        if isinstance(dp_policy, Unset):
            return False
        return dp_policy.use_differential_privacy

    def get_computations(self) -> List[models.Computation]:
        self._refresh()
        return self.model.computations

    def get_remaining_quota(
        self, include_next_allocation_date: bool = False
    ) -> Union[Tuple[str, str], str]:
        """
        Returns the remaining quota from the project and optionally, a second string value indicating the next allocation date.

        Args:
            include_next_allocation_date (bool, optional): Whether to include the allocation date int he result. Defaults to False.

        Raises:
            ValueError: if no quota has been setup with the project.

        Returns:
            Union[Tuple[str, str], str]: the remaining quota along with the allocation date if specified.
        """
        self._refresh()
        quota = self.model.privacy_summary.execution_quota
        if isinstance(quota, Unset):
            raise ValueError("No quota has been set up with the project.")
        quota_val = quota.remaining_quota
        if isinstance(quota_val, Unset):
            quota_val = 0.0
        if include_next_allocation_date:
            if isinstance(quota.next_allocation, Unset):
                return quota_val, None
            next_alloc = quota.next_allocation.strftime("%Y-%m-%d %H:%M:%S %Z%z")
            return quota_val, next_alloc
        return quota_val

    def display_overview(self):
        """
        Displays a human-readable overview of the project, using Ipython.display.
        """
        self._refresh()
        p = self.model
        r = Renderer()
        r.h2(p.name, "(shared" if p.shared else "(local", "project)")

        if not isinstance(p.description, Unset) and p.description != "":
            r(p.description)

        created_by_user = not isinstance(p.created_by_user, Unset)
        r(
            "Created by",
            r.bf(p.created_by_user if created_by_user else p.created_by_node),
            end=".",
        )

        r(
            "Status:",
            r.code(p.status) + ",",
            "Authorization Status:",
            r.code(p.authorization_status),
        )

        ## Local Information
        if p.unrestricted_access:
            r(
                r.bf(
                    "All users from this organization are authorized to run this project."
                )
            )
        elif len(p.authorized_users) > 0:
            r("Authorized users:", r.code(p.authorized_users), end=".")
        else:
            r(
                "*Only administrators from this organization have access to this project.",
                "Administrators may add more users through the instance's web interface.*",
            )
        if not isinstance(p.computation_definition, Unset):
            r("Default workflow Type:", p.computation_definition.type, end=".")

        ## Participants
        r.h3(
            "Participating Organizations",
            "(peer-to-peer" if p.topology == models.Topology.TREE else "(star",
            "topology)",
        )
        participants: List[models.Participant] = self.model.participants
        for part in participants:
            r(
                r.bf(part.node.name) + ":",
                "Organization:",
                part.node.organization.name,
                f"({part.node.organization.country}):",
            )
            r("Node Status:", r.code(part.participation_status))
            r("Project Status:", r.code(part.status))
            r("Authorization Status:\n", r.code(part.authorization_status))
            r.end_paragraph()
