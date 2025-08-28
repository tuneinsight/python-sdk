"""Classes to interact with Tune Insight projects."""

from contextlib import contextmanager
import collections
from typing import Dict, List, Tuple, Union, Any
import warnings

from dateutil.parser import isoparse

import attr
import pandas as pd

from tuneinsight.api.sdk.types import (
    UNSET,
    is_set,
    is_unset,
    value_if_unset,
    false_if_unset,
)
from tuneinsight.api.sdk.types import Response
from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.api.api_project import (
    delete_project,
    get_project,
    patch_project,
    post_project_authorize,
    post_project_request_authorization,
)
from tuneinsight.api.sdk import client as api_client
from tuneinsight.api.sdk.api.api_datasource import get_data_source
from tuneinsight.api.sdk.api.api_computations import documentation, get_computation_list

from tuneinsight.computations import Computation
from tuneinsight.computations.policy import Policy
from tuneinsight.computations.dataset_schema import DatasetSchema
from tuneinsight.computations.types import model_type_to_class
from tuneinsight.client.validation import validate_response
from tuneinsight.client.datasource import DataSource, RemoteDataSource
from tuneinsight.computations.local_data_selection import LocalDataSelection
from tuneinsight.utils.display import Renderer

# pylint: disable=too-many-lines


@attr.s(auto_attribs=True)
class Project:
    """
    A project saved in the Tune Insight instance.

    Projects define a network of participants and a computation to run collectively,
    using one (input) datasource in each instance, potentially constrained by policies.
    Computations are added on this project by instantiating `tuneinsight.computations.Computation`
    objects with this object as first argument.

    Importantly, a project can only be linked to one computation at a time,
    but this computation can change over time. For instance, one can set up
    an aggregation, run the project, then set up a logistic regression, and
    run the project again. All results will remain available as data objects.

    This class wraps the `models.Project` API model, providing a more
    user-friendly interface, and interfaces several API endpoints. It is
    recommended to create a project through Diapason.new_project rather than
    manually building a models.Project object.

    Args for __init__ (to do it manually):
        `model`: the model.Project from the API that this object wraps.
        `client`: the low-level client used to access the API.
        `diapason`: the high-level API client (which has more functionality than the direct client).

    If `diapason` is provided, `client` is defined as `diapason.client`.
    """

    model: models.Project  # The underlying model
    client: api_client.Client = None  # The client used to access the api.
    # The higher level client (defined in tuneinsight.client.diapason).
    diapason: "Diapason" = None

    # SDK-level abstractions (links to SDK objects).
    datasource: DataSource = None
    local_data_selection: LocalDataSelection = None

    # Internal flag that disables PATCH operations. This is used to make breaking changes
    # to SDK objects without sending them to the instance. Do not set manually: use
    # .disable_patch() within a with statement.
    _disable_patch: bool = False

    def __attrs_post_init__(self):
        """Create a datasource object if one is defined in the project model."""
        if self.diapason is not None:
            self.client = self.diapason.client
        if is_set(self.model.data_source_id) and self.model.data_source_id:
            self.datasource = DataSource.fetch_from_id(
                self.client, self.model.data_source_id
            )

    @contextmanager
    def disable_patch(self):
        """
        Disables patching operations on this project within a `with` statement.

        Can be used to make breaking changes to SDK objects without sending them
        to the instance, such as changing parts of a locked project in several
        incompatible steps.

        Example:
            ```
            with project.disable_patch():
                # Operatio
            ```
        """
        _disable_patch_prev = self._disable_patch
        self._disable_patch = True
        yield self
        self._disable_patch = _disable_patch_prev

    # Internal methods.

    def _refresh(self):
        """
        Refreshes the project's model by fetching its model on the Tune Insight instance.

        Intended for internal use -- most getter methods will refresh the model.
        """
        resp: Response[models.Project] = get_project.sync_detailed(
            client=self.client, project_id=self.get_id()
        )
        validate_response(response=resp)
        self.model = resp.parsed

    def _patch(self, proj_def: models.ProjectDefinition):
        """
        Update (patch) this project's definition. Intended for internal use only.

        Args:
            proj_def (models.ProjectDefinition): the definition to patch with.
        """
        if self._disable_patch:
            return
        if not self.client_can(models.Capability.EDITPROJECTS):
            warnings.warn(
                "You do not have the capabilities to edit this project "
                "so changes made with this code will not be taken into account."
            )
            return
        resp: Response[models.Project] = patch_project.sync_detailed(
            client=self.client, project_id=self.get_id(), json_body=proj_def
        )
        validate_response(response=resp)
        self.model = resp.parsed
        self._display_error()

    def _display_error(self, hard: bool = False):
        """Raises warnings containing errors recorded in the project.

        Projects have an "error" field that logs errors that occurred during operations, but did
        not block these operations from completing. These errors typically occur when parts of the
        operation could complete, but some parts could not (usually, because of errors occurring in
        remote participants out of this user's control). This method displays the error as a
        warning

        Args:
            hard (bool, optional): Whether to raise an error instead of a warning. Defaults to False.
        """
        if is_set(self.model.error) and self.model.error:
            if hard:
                # pylint: disable=broad-exception-raised
                raise Exception(self.model.error)
            # If multiple errors occur, they will be listed on separate lines.
            for error in self.model.error.split("\n"):
                warnings.warn(f"Error occurred in project {self.get_id()}: {error}")

    def client_can(self, capability: models.Capability) -> bool:
        """Returns whether the Diapason client has a capability."""
        if self.diapason is None:
            return True
        return self.diapason.can(capability)

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

    def get_recurring_parameters(self) -> str:
        """
        get_recurring_parameters returns the recurring parameters of the project

        Returns:
            dict: recurring parameters of the project
        """
        return {
            "start_time": self.model.recurring_start_time,
            "interval": self.model.recurring_interval,
            "end_time": self.model.recurring_end_time,
        }

    def get_description(self) -> str:
        """
        Returns the description of this project.

        Returns:
            str: the description of the project
        """
        return self.model.description

    def get_topology(self) -> str:
        """
        Returns the topology of this project (either "star" or "tree").

        Returns:
            str: the topology of the project
        """
        return str(self.model.topology)

    def get_authorization_status(self) -> models.AuthorizationStatus:
        """
        Returns the project's authorization status on this client.

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
            `client.DataSource`: the datasource linked to the project.
        """
        self._refresh()
        if self.model.data_source_id == "":
            raise LookupError("This project has no datasource set.")
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
        Returns the email addresses of all authorized users in this instance.

        Returns:
            List[str]: a list of the email addresses of the authorized users
        """
        self._refresh()
        return self.model.authorized_users

    # Setters for model values.

    def set_min_contributors(self, min_contributors: int):
        """Sets the minimum number of contributors required to run the project.

        By default, all participants are required to contribute data.

        Args:
            min_contributors (int): The minimum number of contributors needed.
        """
        self._patch(models.ProjectDefinition(min_contributors=min_contributors))

    def set_contribution_status(self, contributes: bool):
        """
        Sets the local contributing status of the instance.

        If set to False, this instance will not contribute any data when running computations.

        Args:
            contributes (bool): whether the instance contributes data.
        """
        if is_unset(self.model.min_contributors):
            raise ValueError(
                "A minimum number of contributors must first be set (use project.set_min_contributors)."
            )
        proj_def = models.ProjectDefinition()
        proj_def.non_contributor = not contributes
        self._patch(proj_def=proj_def)

    def set_input_schema(self, schema: DatasetSchema):
        """
        Sets an expected schema to enforce on the inputs.

        See `computations.DatasetSchema` for details.

        Args:
            schema (DatasetSchema): the schema definition.
        """
        lds = self.get_local_data_selection()
        lds.preprocessing.schema = schema

    def set_computation(
        self, definition: Union[Computation, models.ComputationDefinition]
    ):
        """
        Sets the project's current computation.

        This method can be used to manually change the computation to run. Note that
        computations call this when they are created or when .run is called, so this
        method should only be used in cases not covered by these (which should be rare).

        Args:
            definition (models.ComputationDefinition or Computation): the definition to apply.
        """
        if isinstance(definition, Computation):
            definition: models.ComputationDefinition = definition.get_full_model()
        self._patch(
            proj_def=models.ProjectDefinition(computation_definition=definition)
        )

    def set_datasource(self, ds: Union[DataSource, str, RemoteDataSource]):
        """Sets the project's input datasource.

        If a Datasource is provided, this sets the datasource to use by this instance on the project.
        Equivalently, the unique identifier of that string can be provided (as a string).
        If this instance does not contribute data, a remote datasource can be connected instead.

        Args:
            ds (DataSource | str | RemoteDataSource): the datasource to link to the project, or its ID.
        """
        if isinstance(ds, RemoteDataSource):
            self._set_remote_datasource(ds)
            return
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

        To edit the policy of the project, first fetch its current state with
        `Project.get_policy`, edit that object, and use `set_policy` to update the project.

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

    def reset_policy(self):
        """Resets the policy of this project (sets an empty policy)."""
        self.set_policy(models.ComputationPolicy())

    def add_authorized_users(self, users: Union[str, List[str]]):
        """
        Adds authorized users to this project.

        Args
            users (string or list of strings): user or users to be added as
                authorized users to this project. Users that are already authorized
                will be ignored.
        """
        if isinstance(users, str):
            users = [users]
        already_authorized = self.model.authorized_users or []
        if is_unset(already_authorized):
            already_authorized = []
        # Get the (sorted) list of unique users in the lists.
        unique_users = sorted(list(set(already_authorized).union(set(users))))
        self._patch(proj_def=models.ProjectDefinition(authorized_users=unique_users))

    # Project administration.

    def delete(self):
        """
        Deletes this project.

        Note that this only deletes the project locally. Other instances must
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
        if self.get_authorization_status() == models.AuthorizationStatus.AUTHORIZED:
            raise ValueError("Project already authorized.")
        model_def = models.ProjectDefinition.from_dict(self.model.to_dict())
        model_def.participants = UNSET
        resp = post_project_authorize.sync_detailed(
            client=self.client,
            project_id=self.get_id(),
            json_body=model_def,  # The current version of the project.
            authorize=True,
        )
        validate_response(response=resp)

    def unauthorize(self):
        """
        Unauthorizes any collective computation with this project.

        Other participants will not be able to run collective computations on this project.
        """
        if self.get_authorization_status() == models.AuthorizationStatus.DENIED:
            raise ValueError("Project authorization already denied.")
        resp = post_project_authorize.sync_detailed(
            client=self.client,
            project_id=self.get_id(),
            json_body=models.ProjectDefinition(),  # Not required.
            authorize=False,
        )
        validate_response(response=resp)

    def request_authorization(self, revoke=False):
        """
        Requests authorization to run this project.

        Projects need to be approved by data protection officiers or administrators
        before they can be run (even locally). This function requests authorization.
        Once authorization is requested, the project becomes locked according to
        the authorization contract.

        If revoke is set to True, this revokes a previous authorization request,
        allowing the project to be modified again.

        Args:
            revoke (bool, default False): whether to revoke a previous authorization
                request instead of requesting authorization.
        """
        resp = post_project_request_authorization.sync_detailed(
            client=self.client,
            project_id=self.get_id(),
            revoke=revoke,
        )
        validate_response(response=resp)

    def revoke_authorization(self):
        """
        Revokes the authorization request of this project.

        This resets all previously given authorization of all participants and resets the
        project to draft status, meaning it can be edited again.

        This is identical to `request_authorization(revoke=True)`.
        """
        self.request_authorization(revoke=True)

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

    def archive(self):
        """
        Archives the project. Archived projects can no longer be edited or run.
        """
        self._patch(models.ProjectDefinition(archived=True))

    def unarchive(self):
        """
        Unarchives the project, if it is archived. This will reset the authorization to draft.
        """
        self._patch(models.ProjectDefinition(archived=False))

    # End-to-end encryption
    def enable_end_to_end_encryption(self):
        """
        Enables end-to-end encryption (E2EE) of results in this project.

        Under E2EE, the results of a computation are left encrypted on the
        instance, and must be decrypted locally. This offers better security,
        as decrypted results are never sent over a network.

        """
        proj_def = models.ProjectDefinition(end_to_end_encrypted=True)
        self._patch(proj_def=proj_def)

    def disable_end_to_end_encryption(self):
        """
        Disables end-to-end encryption of results in this project.

        Results computes previously with end-to-end encryption will remain encrypted.
        """
        proj_def = models.ProjectDefinition(end_to_end_encrypted=False)
        self._patch(proj_def=proj_def)

    @property
    def end_to_end_encrypted(self):
        """Whether this project uses end-to-end encryption."""
        return self.model.end_to_end_encrypted

    # Advanced data management.

    def query_datasource(self, query: str = "") -> pd.DataFrame:
        """
        Fetches the content of this project's datasource through a data query.

        Args
            query (str, optional): the query to select records in the data.
        """
        ds = self.get_input_datasource()
        return ds.get_dataframe(query=query)

    def set_recurring(
        self,
        start_time: Union[str, None],
        interval: Union[int, None],
        end_time: Union[str, None],
    ):
        """
        set_recurring Sets the project's recurring parameters

        Args:
            start_time (str): start time (ISO 8601) of the recurring execution
            end_time (str): end time (ISO 8601) of the recurring execution
            interval (int): interval of the recurring execution in minutes
        """

        self._patch(
            proj_def=models.ProjectDefinition(
                recurring_start_time=str(start_time),
                recurring_interval=interval,
                recurring_end_time=str(end_time),
                broadcast=True,
            )
        )

    def get_local_data_selection(self) -> LocalDataSelection:
        """
        Returns the local data selection settings for the project.

        A LocalDataSelection contains both data source and preprocessing parameters, and
        can be used to apply the same data processing operations to multiple computations.
        The local data selection overrides computation parameters for data processing if
        they are left empty.

        Returns:
            LocalDataSelection: the data selection settings that can be updated by the user
        """
        self._refresh()
        if self.local_data_selection is None:
            # Initialize a local data selection based on the current parameters.
            self.local_data_selection = LocalDataSelection(
                self.model.computation_definition
            )
        return self.local_data_selection

    # Retrieving computations run on this project.
    def get_computation(
        self, computation_definition: models.ComputationDefinition = None
    ) -> Computation:
        """
        Fetches the current computation definition of this project as a Computation object.

        Args:
            computation_definition (`models.ComputationDefinition`, optional): the computation definition
                for which to produce a `Computation` object. If left to None, the current computation
                definition in the project is used.

        Returns:
            computation: a `tuneinsight.Computation` object that can be used to modify the
                computation set on this project.

        Raises:
            ValueError: if the computation is not supported by the SDK. This occurs if the computation
                type is unknown or there is no computation class in the SDK handling this type.
        """
        # Instantiating computations patches the project -- we do not want this here.
        with self.disable_patch():
            if computation_definition is None:
                self._refresh()
                computation_definition = self.model.computation_definition
                if is_unset(computation_definition):
                    raise ValueError("This project has no computation definition.")
            _class = model_type_to_class(computation_definition.type)
            return _class.from_model(self, computation_definition)

    def get_computations(self, num_computations: int = 10) -> List[models.Computation]:
        """Returns the list of the latest computations that have been run on this project.

        Args:
            num_computations (int, optional): Number of computations to fetch. Defaults to 10.
        """
        resp = get_computation_list.sync_detailed(
            client=self.client,
            project_id=self.get_id(),
            per_page=num_computations,
            order=models.GetComputationListOrder.DESC,
            sort_by=models.GetComputationListSortBy.UPDATEDAT,
        )
        validate_response(resp)
        return resp.parsed.items

    def fetch_results(self) -> List[Tuple[Computation, Any]]:
        """
        Fetches the results of all successful computations run on this project.

        Retrieves the list of all computations that have been run on this project,
        then fetches and post-processes the results of all successful ones.

        Returns:
            A list of pairs (`Computation`, result) consisting of the computation definition
            as a `Computation` object and a post-processed result (whose type depends on the
            specific computation being run). If a computation is not supported by the SDK,
            it is skipped and its result will not be included.
        """
        output = []
        for computation in self.get_computations():
            if computation.status == models.ComputationStatus.SUCCESS and is_set(
                computation.definition
            ):
                if (
                    computation.definition.type
                    == models.ComputationType.COLLECTIVEKEYSWITCH
                ):
                    continue
                try:
                    comp: Computation = self.get_computation(computation.definition)
                except ValueError as err:
                    warnings.warn(f"A computation could not be loaded: {err}")
                    continue
                result = comp.fetch_results(computation)
                output.append((comp, result))
        # Revert the order of entries (they are in reverse chronological order in the answer).
        return output[::-1]

    # User-friendly displays.

    def get_latest_measurements(self):
        """
        Returns benchmarking measurements for the last computation.

        Returns a dictionary that contains the benchmarking measurements of the
        last computation that was run in the project. The dictionary contains
        benchmarking information about the processing time and memory allocation
        at each phase of the computation.

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
        Builds a human-readable string representation of this project.

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
                is_set(p.input_metadata)
                and is_set(p.input_metadata.tables)
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
        if is_set(self.model.computations) and len(self.model.computations) > 0:
            res += "computations: \n"
            computations: List[models.Computation] = self.model.computations
            for comp in computations:
                res += f"\t{comp.created_at},{comp.definition.type}\n"
        return res

    def display_previous_workflow(self):
        """
        Displays a markdown workflow summary of the last computation that was run on the project.
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
        Displays the workflow description for the project in markdown.
        """
        self._refresh()
        r = Renderer()
        r(self.model.workflow_description)

    def display_datasources(self):
        """
        Displays the datasources linked to this project in markdown.
        """
        self._refresh()
        participants = self.get_participants()
        r = Renderer()
        for p in participants:
            if is_unset(p.input_metadata):
                continue
            tables = p.input_metadata.tables
            contributes_text = "contributor" if p.is_contributor else "non-contributor"
            r.h3("Participant: ", r.code(p.node.name), f"({contributes_text})")
            for t in tables:
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
        if is_unset(self.model.participants):
            return []
        return [p.node.name for p in self.model.participants]

    def display_policy(self, detailed: bool = False, show_queries: bool = True):
        """
        Displays the policies associated to the project in markdown.

        Args:
            detailed (bool, optional): if True, shows additional policy details
                such as the json of the policy. Defaults to False.
            show_queries (bool, optional): shows the set of authorized SQL queries.
                Defaults to False.
        """
        self._refresh()
        r = Renderer()
        r.h1(self.model.name, "Policy")
        if is_unset(self.model.policy):
            r("Project has no policy.")
            return
        policy = self.get_policy()
        policy.display(detailed=detailed, show_queries=show_queries)

    @contextmanager
    def policy(self):
        """
        Context manager to modify the project's policy.

        Usage:

        ```python
            with project.policy() as p:
                # Modify p here.
        ```

        This is equivalent to the more unwieldy:

        ```python
        p = project.get_policy()
        # Modify p here.
        project.set_policy(p)
        ```
        """
        policy = self.get_policy()
        yield policy
        self.set_policy(policy)

    def get_policy(self) -> Policy:
        """
        Returns the project's policy, which can then be edited.

        Returns:
            Policy: the editable policy
        """
        self._refresh()
        return Policy.from_model(self.model.policy)

    @property
    def is_differentially_private(self):
        """Returns whether differential privacy is enabled for this project."""
        policy = self.get_policy()
        dp_policy = policy.data_policy.dp_policy
        if is_unset(dp_policy):
            return False
        return dp_policy.use_differential_privacy

    def get_remaining_quota(
        self, include_next_allocation_date: bool = False
    ) -> Union[Tuple[str, str], str]:
        """
        Returns the remaining quota from the project and optionally, the next allocation date.

        Args:
            include_next_allocation_date (bool, optional): Whether to include the allocation date in the result. Defaults to False.

        Raises:
            ValueError: if no quota has been setup with the project.

        Returns:
            Union[Tuple[str, str], str]: the remaining quota along with the allocation date if specified.
        """
        self._refresh()
        quota = self.model.privacy_summary.execution_quota
        if is_unset(quota):
            raise ValueError("No quota has been set up with the project.")
        quota_val = quota.remaining_quota
        if is_unset(quota_val):
            quota_val = 0.0
        if include_next_allocation_date:
            if is_unset(quota.next_allocation):
                return quota_val, None
            next_alloc = quota.next_allocation.strftime("%Y-%m-%d %H:%M:%S %Z%z")
            return quota_val, next_alloc
        return quota_val

    def get_sharing_links(self) -> Dict[str, str]:
        """
        Returns sharing links for each instance.

        When a project is shared, only administrators have access to the project.
        An administrator must then manually add other users to the project.
        Alternatively, users can be provided with a *sharing link*, that when clicked,
        will open the web interface and register them to the project.

        Returns:
            A dictionary mapping instance name to the sharing link for that instance.
        """
        if is_unset(self.model.participants):
            return {}
        token = self.get_sharing_token()
        links = {}
        for participant in self.model.participants:
            node = participant.node
            if is_set(node):
                # For the test development:
                url = node.url.replace("http://nginx:3100", "http://localhost:4200")
                links[node.name] = f"{url}/join/{token}"
        return links

    def get_sharing_token(self) -> str:
        """Returns the sharing token for this project. See get_sharing_links for more info."""
        if not self.model.shared:
            warnings.warn("Project not shared yet: sharing token will not work.")
        return self.model.share_token

    def get_remote_datasources(self) -> List[RemoteDataSource]:
        """Returns a list of remote datasources that can be used on this project."""
        self._refresh()
        datasources = []
        for part in self.model.participants:
            if is_set(part.node) and not false_if_unset(part.node.current):
                datasources += value_if_unset(part.data_sources, [])
        return [RemoteDataSource(ds) for ds in datasources]

    def _set_remote_datasource(self, ds: RemoteDataSource):
        """Sets the remote datasource to be used in the project.

        If this instance does not contribute data to the project, it is allowed to define
        a datasource to be used at other, remote, nodes (subject to authorization).

        Args:
            ds (RemoteDataSource): the remote datasource to use, one of the results returned
                by project.get_remote_datasources().

        Raises:
            PermissionError: if this node is contributor. Set the contribution status to False first.
        """
        if not value_if_unset(self.model.non_contributor, True):
            raise PermissionError("Only non-contributors can set remote datasources.")
        self._patch(
            models.ProjectDefinition(
                data_source_auto_match=True, auto_match_criteria=ds.auto_match
            )
        )

    def display_overview(self):
        """
        Displays a human-readable overview of the project in Markdown.
        """
        self._refresh()
        p = self.model
        r = Renderer()
        r.h2(p.name, "(shared" if p.shared else "(local", "project)")

        if is_set(p.description) and p.description != "":
            r(p.description)

        created_by_user = is_set(p.created_by_user)
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
        elif (
            p.authorized_users is not None
            and is_set(p.authorized_users)
            and len(p.authorized_users) > 0
        ):
            r("Authorized users:", r.code(p.authorized_users), end=".")
        else:
            r(
                "*Only administrators from this organization have access to this project.",
                "Administrators may add more users through the instance's web interface.*",
            )
        if is_set(p.computation_definition):
            r("Default workflow Type:", p.computation_definition.type, end=".")

        ## Participants
        r.h3(
            "Participating Organizations",
            "(peer-to-peer" if p.topology == models.Topology.TREE else "(star",
            "topology)",
        )
        participants: List[models.Participant] = value_if_unset(
            self.model.participants, []
        )
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

    def display_actions(
        self,
    ):  # pylint: disable=too-many-branches disable=too-many-statements
        """
        Displays a human-readable summary of what actions are allowed on this project, along
        with explanations on why some actions are not allowed.
        """
        self._refresh()
        r = Renderer()
        if is_unset(self.model.actions):
            r.text("No actions available on the project.")
            return
        actions: models.ProjectActions = self.model.actions
        r.h1("Project Actions")
        r.h2("Editing a project")
        _render_action(r, "Edit Data Source", actions.edit_data_source)
        _render_action(r, "Edit Operation Type", actions.edit_operation_type)
        _render_action(r, "Edit Operation Parameters", actions.edit_operation_params)
        _render_action(r, "Edit Preprocessing", actions.edit_preprocessing)
        _render_action(r, "Edit Query", actions.edit_query)
        _render_action(r, "Edit Policy", actions.edit_policy)

        r.h2("Managing a project")
        _render_action(r, "Request Authorization", actions.request_auth)
        _render_action(r, "Revoke Authorization Request", actions.revoke_auth_request)
        _render_action(r, "Share Project", actions.share)
        _render_action(r, "Run Locally", actions.run_local)
        _render_action(r, "Run Collectively", actions.run_collective)

        r.h2("Number of remaining runs")
        local_runs = value_if_unset(actions.remaining_local_runs, "unlimited")
        coll_runs = value_if_unset(actions.remaining_collective_runs, "unlimited")
        r.item("Local runs:", local_runs)
        r.item("Collective runs:", coll_runs)

        if is_set(actions.available_run_modes):
            r.h2("Available run modes")
            if not actions.available_run_modes:
                r.item("Project cannot be run")
            for mode in actions.available_run_modes:
                r.item(mode)

        # Auto-approve and auto-reject specifications status.
        participants = value_if_unset(self.model.participants, [])
        auto_approve: List[models.AvailabilityStatus] = []
        auto_reject: List[models.AvailabilityStatus] = []
        for part in participants:
            auto_approve += value_if_unset(part.matches_auto_approve_specifications, [])
            auto_reject += value_if_unset(part.matches_auto_reject_specifications, [])
        if auto_approve or auto_reject:
            r.h2("Project specifications")
            if auto_approve:
                r.h3("Auto-approve specifications")
                for i, status in enumerate(auto_approve):
                    if is_unset(status):
                        continue
                    if status.available:
                        r.item(
                            f'✅ Project satisfies specification _"{value_if_unset(status.context, i+1)}"_. The project will be approved automatically.'
                        )
                    else:
                        r.item(
                            f'❌ Project does not satisfy specification _"{value_if_unset(status.context, i+1)}"_ because {status.reason}.'
                        )
            if auto_reject:
                r.h3("Auto-reject specifications")
                for i, status in enumerate(auto_reject):
                    if is_unset(status):
                        continue
                    if status.available:
                        r.item(f"✅ Project satisfies specification {i+1}.")
                    else:
                        r.item(
                            f'❌ The project will be automatically rejected, because it does not satisfy specification _"{value_if_unset(status.context, i+1)}"_: {status.reason}.'
                        )

    def display_privacy_warnings(self) -> bool:
        """
        Displays the privacy warnings of this project in a human-readable format.

        Some project configurations can lead to privacy vulnerabilities. The Tune Insight instance
        automatically screens project for known potential issues. These might not be a problem for
        your specific use case, but it is important to review these carefully to ensure that issues
        found (if any) are an acceptable risk.

        Returns:
            bool: whether a privacy warning was found.
        """
        r = Renderer()
        if is_unset(self.model.privacy_summary):
            return False
        project_warnings = self.model.privacy_summary.privacy_warnings
        if is_unset(project_warnings) or not project_warnings:
            r.text("This project has no privacy warnings ✅")
            return False
        header_by_severity = {
            models.PrivacyWarningSeverity.HIGH: "🔥 High risk",
            models.PrivacyWarningSeverity.MEDIUM: "⚠️ Medium risk",
            models.PrivacyWarningSeverity.LOW: "👉 Low risk",
        }
        warnings_by_severity = collections.defaultdict(list)
        for warning in project_warnings:
            warnings_by_severity[warning.severity].append(warning.description)
        r.h1("Privacy warnings")
        r.text(
            "The current configuration of the project could lead to one or more privacy risks. Please review these risks carefully."
        )
        for severity, header in header_by_severity.items():
            ws = warnings_by_severity[severity]
            if not ws:
                continue
            r.h2(header)
            for w in ws:
                r.item(w)
        return True


def _render_action(r: Renderer, name: str, status: models.AvailabilityStatus):
    if is_unset(status):
        return
    r.item(
        r.bf(name),
        "\t",
        "✅" if status.available else "❌",
        value_if_unset(status.reason, ""),
    )
