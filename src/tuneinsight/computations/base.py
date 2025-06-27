"""Classes to interact with computations to run on a Tune Insight instance.

This module defines the Computation class that represents a generic computation
(to be) run on a Tune Insight instance. It is a relatively low-level interface
that allows you to define a computation, run it, and retrieve its results.

Higher-level interfaces are implemented for specific computations in other
modules in tuneinsight.computations.*.

"""

from abc import ABC, abstractmethod
import json
from typing import Any, List, Union
import warnings
import pandas as pd

from tuneinsight.api.sdk import client as api_client
from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import is_set, is_unset, is_empty, UNSET, value_if_unset
from tuneinsight.api.sdk.types import Response
from tuneinsight.api.sdk.models import DataObjectType as InputType
from tuneinsight.api.sdk.api.api_computations import (
    compute,
    get_computation,
    documentation,
)
from tuneinsight.api.sdk.api.api_project import post_project_computation

from tuneinsight.computations.queries import QueryBuilder
from tuneinsight.computations.preprocessing import PreprocessingBuilder
from tuneinsight.client import e2ee
from tuneinsight.client.validation import validate_response
from tuneinsight.client.dataobject import DataObject, Result, DataContent
from tuneinsight.computations.errors import raise_computation_error
from tuneinsight.utils import time_tools
from tuneinsight.utils.display import Renderer


class Computation(ABC):
    """
    A computation (to be) run on a Tune Insight instance.

    In the Tune Insight API, computations are represented by _models_ that
    contain all the parameters needed to configure the computation. Each
    computation has a different model class (with potentially different
    parameters), including at least all parameters from models.ComputationDefinition.

    This class is abstract, and requires a .get_model method to be implemented,
    that, given the state of the object, returns an api model to use. This allows
    for subclasses to define the model based on user parameters. In most cases,
    however, each computation has a single class defined. For that, use the
    non-abstract ModelBasedComputation class defined below.

    Note that the API makes a difference between computation definitions (describing
    what should run) and computations (the output of the run). This class aims at
    simplifying the interface by integrating both under the hood.

    """

    # Low-level attributes: the project, client, and model of the current computation.
    project: "Project" = UNSET
    client: api_client.Client = UNSET
    model: models.Project = UNSET

    # High-level interfaces to set the computation definition.
    # Note that these are not direct attributes of the computation definition.
    preprocessing: PreprocessingBuilder
    datasource: QueryBuilder
    units: List[models.UnitFilter]
    local_input: models.LocalInput
    max_timeout: int
    polling_initial_interval: int
    precision: int
    ignore_boundary_checks: bool
    debug: bool
    # If the computation times out, it is stored so that it can be resumed.
    _timedout_computation: models.Computation = None
    # Output: the result from computations run on the instance.
    recorded_computations: List[models.Computation]

    def __init__(self, project: "Project"):  # type: ignore
        """
        Creates a `Computation` for a project.

        This sets the `Computation` in the project definition.

        Args:
            project (client.Project): the project to which this computation belongs.
                The client linked to the project is used for the computation. The
                client can be changed manually at any time if needed.
        """
        # Initialize project and client parameters.
        self.project = project
        self.client = project.client if project is not None else None
        if self.client is None:
            warnings.warn(
                "A computation initialized without a client will not be able to run."
            )
        # Set the "high-level" interfaces.
        self.preprocessing = PreprocessingBuilder(self._patch_project)
        self.datasource = QueryBuilder(self._patch_project)
        self.units = []
        self.local_input = None
        self.recorded_computations = []
        self.max_timeout = 600 * time_tools.SECOND
        self.precision = None
        self.ignore_boundary_checks = False
        self.debug = False
        # Useful for debugging the post-processing.
        self._last_raw_results = None
        # Once the parameters are set, set this as a computation in the project.
        # The project computation will be overwritten at each .run -- this is used for authorization purposes.
        self.project.set_computation(self.get_full_model())

    def _patch_project(self):
        """Called whenever the preprocessing or datasource is updated."""
        self.project.set_computation(self)

    # Methods to override.

    @abstractmethod
    def _get_model(self):
        """
        Returns the API model that represents this computation and its parameters.

        This model will be modified afterwards to add the preprocessing, datasource,
        and local input requirements.
        """
        raise NotImplementedError(
            "self._get_model not implemented by generic Computation object."
        )

    def _pre_run_check(self):
        """Optional checks before a computation is run. This should raise an error if the checks fail."""

    def _override_model(self, _: models.ComputationDefinition):
        """Optional model overrides before running the computation"""

    def _process_results(self, results: List[DataContent]) -> Any:
        """Post-process the plaintext results of a computation."""
        return results

    def _process_encrypted_results(self, results: List[DataContent]) -> Any:
        """Post-process encrypted results of a computation."""
        return results

    # API interfacing methods.

    @staticmethod
    def _field_is_set(field: Any) -> bool:
        """Checks whether a field in a (API models) definition is set."""
        return is_set(field) or field != ""

    @staticmethod
    def _is_done(comp: models.Computation) -> bool:
        """Returns whether a computation is done or not from its output model."""
        return comp.status in (
            models.ComputationStatus.ERROR,
            models.ComputationStatus.SUCCESS,
        )

    @staticmethod
    def _validate_input_data(
        input_data: models.DataObject, model: models.ComputationDefinition, local: bool
    ):
        if input_data.type not in [
            InputType.COHORT,
            InputType.FLOAT_MATRIX,
            InputType.TABLE,
        ]:
            raise ValueError(f"invalid input type: {input_data.type}.")
        if input_data.type == InputType.COHORT and model.type not in [
            models.ComputationType.ENCRYPTEDAGGREGATION,
            models.ComputationType.GWAS,
        ]:
            raise ValueError(
                f"cohort cannot be used as an input to a {model.type} computation."
            )
        if not local and not input_data.shared:
            raise ValueError(
                "local object cannot be used as input to a collective computation."
            )

    # This modifies an API model to enforce high-level constraints.

    def _update_computation_datasource(self, model: models.ComputationDefinition):
        """
        Updates the definition of the input computation to have the specified datasource parameters.
        """
        if model.type in [
            models.ComputationType.COLLECTIVEKEYSWITCH,
            models.ComputationType.ENCRYPTEDPREDICTION,
            models.ComputationType.PRIVATESEARCH,
        ]:
            return
        # Apply the datasource query.
        if self.datasource.query_set:
            model.data_source_parameters = self.datasource.get_model()
        # Otherwise, initialize empty data source parameters.
        else:
            if is_unset(model.input_data_object):
                model.data_source_parameters = models.ComputationDataSourceParameters()
                # Check if the project has a local data selection.

    def _update_computation_fields(self, model: models.ComputationDefinition):
        """
        Updates the definition of the input computation to have the same basic configuration.
        """
        model.wait = False
        model.ignore_boundary_checks = self.ignore_boundary_checks
        if not self._field_is_set(model.project_id):
            model.project_id = self.project.get_id()
        model.timeout = int(self.max_timeout / time_tools.SECOND)
        if self.local_input is not None:
            model.local_input = self.local_input
        if self.precision is not None:
            if self.precision < 1 or self.precision > 32:
                raise ValueError("precision must be set to a value in [1,32]")
            model.precision = int(round(self.precision))
        if self.units:
            model.units = self.units

    def _update_computation_preprocessing(self, model: models.ComputationDefinition):
        """
        Updates the definition of the input computation to have the specified preprocessing.
        """
        self.preprocessing.check_validity()
        if is_unset(model.preprocessing_parameters):
            model.preprocessing_parameters = models.ComputationPreprocessingParameters()
        model.preprocessing_parameters = self.preprocessing.get_model()

    def _update_computation_from_project(self, model: models.ComputationDefinition):
        """
        Updates the definition of the input computation from fields in the project model.

        If defined, this applies the client-side local data selection of the project, modifying
        the datasource query and preprocessing parameters of the computation.

        """
        lds = self.project.local_data_selection
        if lds is not None:
            if is_set(lds.preprocessing) and is_empty(model.preprocessing_parameters):
                model.preprocessing_parameters = lds.preprocessing.get_model()
            if is_set(lds.datasource) and is_empty(model.data_source_parameters):
                model.data_source_parameters = lds.datasource.get_model()

    def get_full_model(self):
        """
        Returns the API model for this computation, including datasource and preprocessing parameters.
        """
        model = self._get_model()
        self._update_computation_datasource(model)
        self._update_computation_fields(model)
        self._update_computation_preprocessing(model)
        self._update_computation_from_project(model)
        return model

    def display_workflow(self):
        """
        Displays documentation for this computation.

        This modifies the input computation definition to match the input datasource
        and other configuration of this ComputationRunner, hence describing the
        computation as it would be if it was run with this object.

        """
        model = self.get_full_model()
        response: Response[models.DocumentationResponse200] = (
            documentation.sync_detailed(client=self.client, json_body=model)
        )
        validate_response(response)
        r = Renderer()
        r(response.parsed.description)

    def _refresh(self, comp: models.Computation) -> models.Computation:
        """
        Refreshes a `models.Computation` by fetching it from the client.

        This fetches the computation linked to this computation ID comp.id,
        and returns the current state of this computation on the instance.

        Note that this is not a computation definition, but a `models.Computation`.
        It representations a computation that is running or has been run, and
        includes additional fields such as the results.

        Args:
            comp (models.Computation): the computation to refresh.
        """
        response: Response[models.Computation] = get_computation.sync_detailed(
            client=self.client, computation_id=comp.id
        )
        validate_response(response)
        return response.parsed

    def set_local_input(self, df: pd.DataFrame):
        """
        Sets the local user-provided plaintext input to the computation.

        If a local input is provided, the node initiating the computation will
        use it instead of querying the datasource. This data is *not* shared to
        other nodes, only used for the duration of the computation.

        Args:
            df (pd.DataFrame): the dataframe to use as a local input
        """
        cols = df.columns
        local_input = models.LocalInput()
        for col in cols:
            col_list = df[col].to_list()
            for i, v in enumerate(col_list):
                col_list[i] = str(v)
            local_input.additional_properties[str(col)] = col_list
        self.local_input = local_input

    def _poll_computation(
        self,
        comp: models.Computation,
        interval=100 * time_tools.MILLISECOND,
        max_sleep_time=30 * time_tools.SECOND,
    ) -> Union[List[Result], List[DataObject]]:
        """
        Waits until a [models.]computation is finished and returns its result(s).

        This attempts to fetch the results of a computation until it succeeds,
        or at least self.max_timeout seconds have passed.

        This function is intended for internal use. In principle, the computation
        doesn't need to be the output of the computation model in this object
        (self.model), but that is not recommended.

        Args:
            comp (models.Computation): the computation to wait for.
            interval (int, optional): time in nanoseconds to wait between polls.
            max_sleep_time (int, optional): maximum total time in nanoseconds to wait between polls.

        Returns:
            List[Result] or List[DataObject]: the result of the computation, parsed as a
               Result object. If no result is provided (which can happen in some corner cases),
               the list of dataobjects containing data results is returned instead.
        """
        # Define initial sleeping time and start time.
        start_time = time_tools.now()
        sleep_time = interval
        current_comp = comp

        # Poll the computation until done.
        while not self._is_done(current_comp):
            if time_tools.since(start_time) > self.max_timeout:
                self._timedout_computation = current_comp
                raise TimeoutError(
                    f"The computation is taking longer than {self.max_timeout/time_tools.SECOND} seconds to complete. "
                    + "While .run has timed out, the computation is still running in the backend. "
                    + "Use .run(resume_timedout=True) to poll the computation again and wait for results."
                )
            time_tools.sleep(sleep_time)
            current_comp = self._refresh(comp)
            if len(current_comp.warnings) > 0:
                warnings.warn(current_comp.warnings[len(current_comp.warnings) - 1])
            if sleep_time < max_sleep_time:
                sleep_time = int(sleep_time * 1.05)

        # Reset the last timed out computation.
        self._timedout_computation = None

        # Raise an exception if there is was an error during the computation.
        if (current_comp.status == models.ComputationStatus.ERROR) or (
            len(comp.errors) > 0
        ):
            raise_computation_error(current_comp.errors)

        if len(current_comp.results) < 1:
            raise ValueError("The computation has no results.")

        # Update recorded computation.
        self.recorded_computations.append(current_comp)

        # Get the result(s) of the computation. Most computations only have one result, but some can have several,
        # so all results post-processing operates over lists of DataContents.
        result_ids: List[str] = value_if_unset(current_comp.result_ids, [])
        if not result_ids:
            # Note: result_id will be deprecated soon, but is still supported at the moment.
            result_id = value_if_unset(current_comp.result_id, "")
            if result_id:
                result_ids.append(result_id)

        # In some cases, the result IDs can be unset even though the computation has results.
        # When that happens, we fetch the dataobjects of the computation directly. This means that E2EE will not work.
        if not result_ids:
            if self.project.end_to_end_encrypted:
                warnings.warn(
                    "The computation is end-to-end encrypted but completed without a result. "
                    "This is unexpected and will result in an error. "
                    "Contact your administrator if this occurs consistently."
                )
            return [
                DataObject.fetch_from_id(id, self.client) for id in current_comp.results
            ]

        return [Result.fetch_from_id(r_id, self.client) for r_id in result_ids]

    def _launch(self, model: models.ComputationDefinition) -> models.Computation:
        """
        Launches this computation, given its current API model.

        This starts a computation on the connected instance and returns the
        resulting computation definition from the instance. It does not wait
        for the computation to complete. Use _poll_computation to wait.

        Args
            model (models.ComputationDefinition): The model definition of the computation.
        """
        if self.debug:
            print("Launching computation with definition:")
            print(json.dumps(model.to_dict(), indent=4))
        # Computations can be launched one of two ways: either using the compute API,
        # which does not require a project to be specified, or using the project API.
        project_id = self.project.get_id()
        if project_id is None or project_id == "":
            return self._launch_with_compute(model)
        return self._launch_with_project(model)

    def _launch_with_compute(self, comp):
        """
        Launches a computation using the compute endpoint.

        ⛔ This API endpoint is intended for tests, and is likely to result in errors
        when used in production and to be deprecated. Do not use.
        """
        response: Response[models.Computation] = compute.sync_detailed(
            client=self.client, json_body=comp
        )
        validate_response(response)
        return response.parsed

    def _launch_with_project(
        self, comp: models.ComputationDefinition
    ) -> models.Computation:
        """Launches a computation through the project computation endpoint."""
        project_id = self.project.get_id()
        if project_id is None or project_id == "":
            raise ValueError("This computation is not linked to a project.")
        run_mode = models.RunMode.COLLECTIVE
        if comp.local or not self.project.model.shared:
            run_mode = models.RunMode.LOCAL
        params = models.RunProjectParameters(
            run_mode=run_mode,
        )
        # If the user can edit the computation definition, we pass the (modified)
        # compDef as run parameters. This means that the project will run with this
        # compDef without requiring a PATCH beforehand.
        if self.project.client_can(models.Capability.EDITPROJECTCOMPDEF):
            params.computation_definition = comp
        response: Response[models.ProjectComputation] = (
            post_project_computation.sync_detailed(
                project_id=project_id, client=self.client, json_body=params
            )
        )
        validate_response(response)
        return response.parsed.computation

    def run(
        self,
        local: bool = False,
        interval=100 * time_tools.MILLISECOND,
        max_sleep_time=30 * time_tools.SECOND,
        on_previous_result: models.DataObject = None,
        resume_timedout: bool = False,
    ) -> Any:
        """
        Runs this computation.

        This launches this computation on the instance, waits for it to finish, and
        returns the (decrypted) results.

        Args:
            local (bool, optional): Whether to run the computation locally or remotely. Defaults to False.
            interval (int, optional): time in nanoseconds to wait between polls.
            max_sleep_time (int, optional): maximum total time in nanoseconds to wait.
            on_previous_result (models.DataObject,optional): remote object (usually output from another computation) to
                use as an input. This overrides the datasource of the project.
            resume_timedout (bool, False by default): whether to resume a computation that previously timed
                out. This will raise an error if the last computation did not time out. When resuming a
                timed out computation, all current changes to this computation are ignored, but not overwritten.

        """
        # Perform optional checks to have user-friendly messages in case something is missing.
        self._pre_run_check()

        if resume_timedout and self._timedout_computation is None:
            raise LookupError("The previous computation did not time out.")

        # Update the model to reflect high-level parameters (preprocessing etc.).
        model: models.ComputationDefinition = self._get_model_before_launch(
            local, on_previous_result
        )

        # Start the computation and wait until it finishes.
        if resume_timedout:
            computation = self._timedout_computation
        else:
            computation = self._launch(model)

        results = self.fetch_results(computation, interval, max_sleep_time)

        return results

    def fetch_results(
        self,
        computation: models.Computation,
        interval: int = 100 * time_tools.MILLISECOND,
        max_sleep_time: int = 30 * time_tools.SECOND,
    ):
        """
        Fetches results for a `models.Computation` that has been started on the backend.

        This waits until the computation completes (potentially timing out if the
        computation takes too long), then fetches the results of the computation and
        parses them as user-friendly objects.

        Args:
            computation (models.Computation): a computation that has been launched on the
                backend. Note that this is a `models.Computation` object created by launching
                a computation definition. You can retrieve this from the project definition.
            interval (int, optional): time in nanoseconds to wait between polls.
            max_sleep_time (int, optional): maximum total time in nanoseconds to wait.
        """
        # Handle the edge case where the types of the computation that was run and this computation
        # mismatch (e.g. if a user without the proper permissions tries to edit the project).
        if computation.definition.type != self._get_model().type:
            comp = self.project.get_computation(computation.definition)
            return comp.fetch_results(computation, interval, max_sleep_time)

        results: Union[List[Result], List[DataObject]] = self._poll_computation(
            comp=computation, interval=interval, max_sleep_time=max_sleep_time
        )

        # If using end-to-end encryption, decrypt each encrypted result.
        results = [
            (
                e2ee.decrypt(self.client, r)
                if isinstance(r, Result) and r.end_to_end_encrypted
                else r
            )
            for r in results
        ]

        # The last unprocessed results are stored for debug purposes.
        self._last_raw_results = results

        # Perform (optional) post-processing of the results if in plaintext.
        if results[0].is_encrypted():
            return self._process_encrypted_results(results)
        return self._process_results(results)

    def _get_model_before_launch(
        self,
        local: bool = False,
        on_previous_result: models.DataObject = None,
    ) -> models.ComputationDefinition:
        # Update the model to reflect high-level parameters (preprocessing etc.).
        model: models.ComputationDefinition = self.get_full_model()
        model.local = local
        model.run_mode = models.RunMode.LOCAL if local else models.RunMode.COLLECTIVE

        if on_previous_result is not None:
            self._validate_input_data(on_previous_result, model, local)
            if local:
                model.local_input_id = on_previous_result.unique_id
            else:
                model.input_data_object = on_previous_result.unique_id

        # Start the computation and wait until it finishes.
        self._override_model(model)
        return model

    def key_switch(self, data_object: DataObject) -> DataObject:
        """
        Performs a collective key switch on a data object.

        Args:
            data_object: the object on which to perform the collective key switch.
        """
        key_switch = KeySwitch(self.project, cipher_vector=data_object.get_id())
        return key_switch.run(local=False)

    def add_unit(
        self,
        unit_column: str,
        unit: str,
        value_column: str = UNSET,
        allow_missing: bool = False,
    ):
        """Adds a unit specification to this computation.

        Units are checked before running a computation, by filtering out all records that do not
        have the correct units for the specified columns. Effectively, this checks that the value
        of the unit (given in the `unit_column`) matches `unit`. The numerical column associated
        with that unit can also be specified, although it is not currently used.

        Args:
            unit_column (str): The column in the data that gives the unit.
            unit (str): The value of the unit to select for.
            value_column (str): The column in the data containing numerical values (optional).
            allow_missing (bool): Whether to include records that don't have a unit.
        """
        self.units.append(
            models.UnitFilter(
                allow_empty_units=allow_missing,
                unit=unit,
                unit_column=unit_column,
                value_column=value_column,
            )
        )

    @classmethod
    def from_model(
        cls, project: "Project", model: models.ComputationDefinition  # type: ignore
    ) -> "Computation":
        """Initializes a Computation from its API model."""
        raise NotImplementedError("Use <ComputationClass>.from_model.")


class ModelBasedComputation(Computation):
    """
    A computation based on a single API model.

    This class provides a wrapper over a model class that is easier to use and
    interfaces with the API to run computations and retrieve results. However, it is
    generic and requires specific parameters of the computation to be set manually.
    For specific computations, it is recommended to use dedicated (sub)classes.

    Objects of this class have a .model attribute that contains the API model instance
    that will be used. This object can be modified directly if needed using this
    computation as a dictionary (i.e., self["k"] = v is equivalent to self.model.k = v).

    """

    def __init__(
        self,
        project: "Project",  # type: ignore
        model_class,
        type: models.ComputationType,  # pylint: disable=redefined-builtin
        **kwargs,
    ):
        """
        Creates a Computation for a specific model.

        Args:
            project (client.Project): the project to which this computation belongs.
                The client linked to the project is used for the computation. The
                client can be changed manually at any time if needed.
            model_class: the class of the API model for this computation.
            type: the computation type (required by all API models).
            **kwargs (optional): additional keyword arguments to pass to the model class.
        """
        self.model = model_class(type=type, project_id=project.get_id(), **kwargs)
        super().__init__(project)
        # Check DP compatibility (for now, with a friendly warning).
        if project.is_differentially_private:
            warn_message = (
                "This project has differential privacy enabled, but %s. "
                "This will likely cause an error when running the computation. "
                "Contact your administrator for more details."
            )
            if not hasattr(self.model, "dp_epsilon"):
                warnings.warn(
                    warn_message
                    % "this computation does not appear to support differential privacy"
                )
            elif is_unset(self.model.dp_epsilon):
                warnings.warn(
                    warn_message
                    % "the parameter dp_epsilon was not set. Using default value 1."
                )
                self.model.dp_epsilon = 1
            else:
                epsilon = float(
                    self.model.dp_epsilon
                )  # Will raise an error if not float.
                if epsilon <= 0:
                    raise ValueError(
                        "The parameter dp_epsilon must be a positive number."
                    )

    def _get_model(self):
        return self.model

    def _adapt(self, model: models.ComputationDefinition):
        """
        Updates internal fields of this computation to match a given API model of the same type.

        This overwrites the .model attribute of this object, and adapts user-friendly fields
        (e.g., preprocessing and datasource) of the object to reflect changes in the model.

        This is used internally to initialize an object from a model (Computation.from_model).
        """
        assert self.model.type == model.type, "Mismatching computation types."
        # Overwrite the model at the core of the object.
        self.model = model
        # Update all internal variables to be up-to-date with the model.
        self.preprocessing = PreprocessingBuilder.from_model(
            model.preprocessing_parameters
        )
        self.preprocessing.update_function = self._patch_project
        self.datasource.set_model(model.data_source_parameters)
        if is_set(model.timeout):
            self.max_timeout = model.timeout * time_tools.SECOND
        if is_set(model.local_input):
            self.local_input = model.local_input
        if is_set(model.ignore_boundary_checks):
            self.ignore_boundary_checks = model.ignore_boundary_checks
        if is_set(model.precision):
            self.precision = model.precision
        # Update the computation in the project to send the updates to the .
        self.project.set_computation(self)

    # Interfacing with the model directly: use comp["attr"] = value to set a model value.

    def __setitem__(self, key, value):
        self.model[key] = value

    def __getitem__(self, key):
        return self.model[key]


class KeySwitch(ModelBasedComputation):
    """
    A collective key switch computation.

    Collective key switches are used to collaboratively change the encryption
    key of a ciphertext in order to enable its decryption. This is a necessary
    step at the end of a collective computation to be able to decrypt the result.

    🔎 the `Computation.run` method automatically performs the keyswitch in the
       backend, so you should not have to use this computation.
    """

    def __init__(
        self,
        project,
        cipher_vector,
    ):
        super().__init__(
            project,
            models.CollectiveKeySwitch,
            # Additional kwargs defining specific parameters.
            type=models.ComputationType.COLLECTIVEKEYSWITCH,
            cipher_vector=cipher_vector,
        )


class ComputationResult(ABC):
    """
    Abstract class for the results of a Computation.

    Some computations output complex results, on which users might want to
    do several post-processing analyses. In this case, it is best practice
    to group these results in a ComputationResult class.

    """

    @abstractmethod
    def as_table(self) -> pd.DataFrame:
        raise NotImplementedError()

    @abstractmethod
    def plot(self):
        raise NotImplementedError()
