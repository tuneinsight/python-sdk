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

from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import is_set, is_unset, UNSET
from tuneinsight.api.sdk.types import Response
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
from tuneinsight.utils import deprecation
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
    project = UNSET
    client = UNSET
    model = UNSET

    # High-level interfaces to set the computation definition.
    # Note that these are not direct attributes of the computation definition.
    preprocessing: PreprocessingBuilder
    datasource: QueryBuilder
    local_input: models.LocalInput
    max_timeout: int
    polling_initial_interval: int
    aggregation_upper_bound: float
    clipping_method: str
    debug: bool
    # If the computation times out, it is stored so that it can be resumed.
    _timedout_computation: models.Computation = None
    # Output: the result from computations run on the instance.
    recorded_computations: List[models.Computation]

    def __init__(self, project: "Project"):
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
        self.preprocessing = PreprocessingBuilder()
        self.datasource = QueryBuilder()
        self.local_input = None
        self.recorded_computations = []
        self.max_timeout = 600 * time_tools.SECOND
        self.aggregation_upper_bound = None
        self.clipping_method = None
        self.debug = False
        # Useful for debugging the post-processing.
        self._last_raw_results = None

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
        # The data source query can be set at three levels (in decreasing precedence):
        #  1. In this object (computation definition),
        #  2. In the Datasource object of the project (project),
        #  3. In the local data source (enforced on the server level).
        # Check 1.: whether this computation has a query set.
        if self.datasource.query_set:
            model.data_source_parameters = self.datasource.get_model()
        # Otherwise, initialize empty data source parameters.
        else:
            if is_unset(model.input_data_object):
                model.data_source_parameters = models.ComputationDataSourceParameters()
            # And check 2. whether the datasource has a query set.
            if self.project.datasource is not None:
                ds = self.project.datasource
                if ds.query_parameters is not None:
                    model.data_source_parameters.data_source_query = ds.query_parameters

    def _update_computation_fields(self, model: models.ComputationDefinition):
        """
        Updates the definition of the input computation to have the same basic configuration.
        """
        model.wait = False
        if not self._field_is_set(model.project_id):
            model.project_id = self.project.get_id()
        model.timeout = int(self.max_timeout / time_tools.SECOND)
        if self.local_input is not None:
            model.local_input = self.local_input
        if self.clipping_method is not None:
            model.input_clipping_method = (
                models.ComputationDefinitionInputClippingMethod(self.clipping_method)
            )
        if self.aggregation_upper_bound is not None:
            model.maximum_aggregated_value = self.aggregation_upper_bound

    def _update_computation_preprocessing(self, model: models.ComputationDefinition):
        """
        Updates the definition of the input computation to have the specified preprocessing.

        Args
            comp (models.ComputationDefinition): the computation to post-process.
        """
        self.preprocessing.check_validity()
        if is_unset(model.preprocessing_parameters):
            model.preprocessing_parameters = models.ComputationPreprocessingParameters()
        model.preprocessing_parameters = self.preprocessing.get_model()

    def get_full_model(self):
        """
        Returns the API model for this computation, including datasource and preprocessing parameters.
        """
        model = self._get_model()
        self._update_computation_datasource(model)
        self._update_computation_fields(model)
        self._update_computation_preprocessing(model)
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

    def set_aggregation_bound(self, max_bound: float, clipping_method: str = "error"):
        """
        Sets an upper bound on the total aggregated value of the result.

        This is used to choose appropriate aggregation parameters. Out-of-bound values
        will be treated according to the clipping method (by default, an error is raised).

        Args:
            max_bound (float): the numerical bound which represents the maximum collective value.
            clipping_method (str, optional): the method used to treat out of bound values:
                'error': abort computation,
                'warning': clip values and issue a warning to the user,
                'silent': clip without any warning,
                'none': values are never clipped. Defaults to 'error'.
        """
        self.clipping_method = clipping_method
        self.aggregation_upper_bound = max_bound

    def _poll_computation(
        self,
        comp: models.Computation,
        interval=100 * time_tools.MILLISECOND,
        max_sleep_time=30 * time_tools.SECOND,
    ) -> Union[Result, List[DataObject]]:
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
            Result or List[DataObject]: the result of the computation, parsed as a
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

        # In some cases, the result ID can be unset even though the computation has results.
        # When that happens, we fetch the dataobjects of the computation directly.
        result_id = current_comp.result_id
        if is_unset(result_id) or not result_id:
            return [
                DataObject.fetch_from_id(id, self.client) for id in current_comp.results
            ]

        return Result.fetch_from_id(result_id, self.client)

    def _launch(self, model, local: bool = False) -> models.Computation:
        """
        Launches this computation, given its current API model.

        This starts a computation on the connected instance and returns the
        resulting computation definition from the instance. It does not wait
        for the computation to complete. Use _poll_computation to wait.

        Args
            model (models.ComputationDefinition): The model definition of the computation.
            local (bool, optional): Whether to run the computation locally or remotely. Defaults to False.
        """
        model.local = local
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

    def _launch_with_project(self, comp) -> models.Computation:
        """Launches a computation through the project computation endpoint."""
        project_id = self.project.get_id()
        if project_id is None or project_id == "":
            raise ValueError("This computation is not linked to a project.")
        # Refresh the computation model in the project to this computation.
        # This is required, otherwise calling comp.run() could run another computation.
        # Note that this will not work if the client does not have the appropriate authorization.
        self.project.set_computation(comp)
        params = models.RunProjectParameters(computation_definition=comp)
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
        keyswitch: bool = False,
        decrypt: bool = False,
        release: bool = True,
        interval=100 * time_tools.MILLISECOND,
        max_sleep_time=30 * time_tools.SECOND,
        resume_timedout: bool = False,
    ) -> Any:
        """
        Runs this computation.

        This launches this computation on the instance, waits for it to finish, and
        returns the (decrypted) results.

        Args:
            local (bool, optional): Whether to run the computation locally or remotely. Defaults to False.
            keyswitch (bool, optional): Whether to perform key switching on the results. Defaults to True.
                [This parameter is deprecated.]
            decrypt (bool, optional): Whether to request the decryption on the results. Defaults to True.
                [This parameter is deprecated.]
            release (bool, optional): Whether to release the results (overrides decrypt/keyswitch).
                If set, encrypted results are automatically key switched and decrypted and a Result
                entity is saved. Defaults to False.
            interval (int, optional): time in nanoseconds to wait between polls.
            max_sleep_time (int, optional): maximum total time in nanoseconds to wait.
            resume_timedout (bool, False by default): whether to resume a computation that previously timed
                out. This will raise an error if the last computation did not time out. When resuming a
                timed out computation, all current changes to this computation are ignored, but not overwritten.

        """
        # Perform optional checks to have user-friendly messages in case something is missing.
        self._pre_run_check()
        if decrypt:
            deprecation.warn("decrypt = True", breaking=True)
        if keyswitch:
            deprecation.warn("keyswitch = True", breaking=True)

        if resume_timedout and self._timedout_computation is None:
            raise LookupError("The previous computation did not time out.")

        # Update the model to reflect high-level parameters (preprocessing etc.).
        model: models.ComputationDefinition = self.get_full_model()
        if self.project.end_to_end_encrypted:
            # If using end-to-end encryption, override other flags.
            release = True
        model.release_results = release

        # Start the computation and wait until it finishes.
        if resume_timedout:
            computation = self._timedout_computation
        else:
            computation = self._launch(model, local=local)

        return self.fetch_results(computation, interval, max_sleep_time)

    def fetch_results(
        self,
        computation: models.Computation,
        interval=100 * time_tools.MILLISECOND,
        max_sleep_time=30 * time_tools.SECOND,
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
        result: Union[Result, List[DataObject]] = self._poll_computation(
            comp=computation, interval=interval, max_sleep_time=max_sleep_time
        )
        # If using end-to-end encryption, decrypt each result.
        if isinstance(result, Result):
            if result.end_to_end_encrypted:
                result = e2ee.decrypt(self.client, result)
            # Convert the result to a list for compatibility with dataobjects.
            if isinstance(result, Result):
                result = [result]

        # Perform (optional) post-processing of the results if in plaintext.
        self._last_raw_results = result
        if result[0].is_encrypted():
            return self._process_encrypted_results(result)
        return self._process_results(result)

    def key_switch(self, data_object: DataObject) -> DataObject:
        """
        Performs a collective key switch on a data object.

        Args:
            data_object: the object on which to perform the collective key switch.
        """
        key_switch = KeySwitch(self.project, cipher_vector=data_object.get_id())
        return key_switch.run(local=False, keyswitch=False)

    @classmethod
    def from_model(
        cls, project: "Project", model: models.ComputationDefinition
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
        project: "Project",
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
        super().__init__(project)
        self.model = model_class(type=type, project_id=project.get_id(), **kwargs)
        # Check DP compatibility (for now, with a friendly warning).
        if project.is_differentially_private:
            warn_message = (
                "This project has differential privacy enabled, but %s."
                + "This will likely cause an error when running the computation."
                + "Contact your administrator for more details."
            )
            if not hasattr(self.model, "dp_epsilon"):
                warnings.warn(
                    warn_message
                    % "this computation does not appear to support differential privacy"
                )
            elif is_unset(self.model.dp_epsilon):
                warnings.warn(
                    warn_message
                    % "the parameter dp_epsilon was not set. Using default value 0.1."
                )
                self.model.dp_epsilon = 0.1
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
        self.datasource.set_model(model.data_source_parameters)
        if is_set(model.timeout):
            self.max_timeout = model.timeout * time_tools.SECOND
        if is_set(model.local_input):
            self.local_input = model.local_input
        if is_set(model.input_clipping_method):
            self.clipping_method = model.input_clipping_method
        if is_set(model.maximum_aggregated_value):
            self.aggregation_upper_bound = model.maximum_aggregated_value

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
