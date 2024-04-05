"""Classes to interact with computations to run on a Tune Insight instance.

This module defines the Computation class that represents a generic computation
(to be) run on a Tune Insight instance. It is a relatively low-level interface
that allows you to define a computation, run it, and retrieve its results.

Higher-level interfaces are implemented for specific computations in other
modules in tuneinsight.computations.*.

"""

from abc import ABC, abstractmethod
import json
from typing import Any, List
import warnings
import pandas as pd

from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import Unset, UNSET
from tuneinsight.api.sdk.types import Response
from tuneinsight.api.sdk.api.api_computations import (
    compute,
    get_computation,
    documentation,
)
from tuneinsight.api.sdk.api.api_project import post_project_computation
from tuneinsight.api.sdk.api.api_dataobject import get_data_object

from tuneinsight.computations.queries import QueryBuilder
from tuneinsight.computations.preprocessing import PreprocessingBuilder
from tuneinsight.client.validation import validate_response
from tuneinsight.client.dataobject import DataObject
from tuneinsight.computations.errors import raise_computation_error
from tuneinsight.utils import time_tools, deprecation
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
    # List of all computations "results" from running this Computation.
    recorded_computations: List[models.Computation]
    debug: bool

    # Output: the result from computations run on the instance.
    recorded_computations: List[models.Computation]

    def __init__(self, project: "Project"):
        """
        Create a Computation for a project.

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
            "get_model not implemented by generic Computation object."
        )

    def _pre_run_check(self):
        """Optional checks before a computation is run."""

    def _process_results(self, dataobjects):
        """Post-process the plaintext results of a computation."""
        return dataobjects

    def _process_encrypted_results(self, dataobjects):
        """Post-process encrypted results of a computation."""
        return dataobjects

    # API interfacing methods.

    @staticmethod
    def field_is_set(field: Any) -> bool:
        """Checks whether a field in a (API models) definition is set."""
        return not (field is UNSET or field == "")

    @staticmethod
    def is_done(comp: models.Computation) -> bool:
        """Returns whether a computation is done or not from its output model."""
        return comp.status in (
            models.ComputationStatus.ERROR,
            models.ComputationStatus.SUCCESS,
        )

    # This modifies an API model to enforce high-level constraints.

    def _update_computation_datasource(self, comp: models.ComputationDefinition):
        """
        Updates the definition of the input computation to have the specified datasource parameters.
        """
        if comp.type in [
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
            comp.data_source_parameters = self.datasource.get_parameters()
        # Otherwise, initialize empty data source parameters.
        else:
            if not self.field_is_set(comp.input_data_object):
                comp.data_source_parameters = models.ComputationDataSourceParameters()
            # And check 2. whether the datasource has a query set.
            if self.project.datasource is not None:
                ds = self.project.datasource
                if ds.query_parameters:
                    comp.data_source_parameters.data_source_query = ds.query_parameters

    def _update_computation_fields(self, comp: models.ComputationDefinition):
        """
        Updates the definition of the input computation to have the same basic configuration.
        """
        comp.wait = False
        if not self.field_is_set(comp.project_id):
            comp.project_id = self.project.get_id()
        comp.timeout = int(self.max_timeout / time_tools.SECOND)
        self._update_computation_datasource(comp=comp)
        if self.local_input is not None:
            comp.local_input = self.local_input
        if self.clipping_method is not None:
            comp.input_clipping_method = (
                models.ComputationDefinitionInputClippingMethod(self.clipping_method)
            )
        if self.aggregation_upper_bound is not None:
            comp.maximum_aggregated_value = self.aggregation_upper_bound

    def _update_computation_preprocessing(self, comp: models.ComputationDefinition):
        """
        Updates the definition of the input computation to have the specified preprocessing.

        Args
            comp (models.ComputationDefinition): the computation to post-process.
        """
        self.preprocessing.check_validity()

        if comp.preprocessing_parameters == UNSET:
            comp.preprocessing_parameters = models.ComputationPreprocessingParameters()
        comp.preprocessing_parameters = self.preprocessing.get_params()

    def _get_full_model(self):
        """Returns the API model for this computation, including additional parameters."""
        model = self._get_model()
        self._update_computation_datasource(model)
        self._update_computation_fields(model)
        self._update_computation_preprocessing(model)
        return model

    def display_documentation(self):
        """Displays documentation for this computation. Use display_workflow instead."""
        deprecation.warn("display_documentation", "display_workflow")
        return self.display_workflow()

    def display_workflow(self):
        """
        Displays documentation for this computation.

        This modifies the input computation definition to match the input datasource
        and other configuration of this ComputationRunner, hence describing the
        computation as it would be if it was run with this object.

        """
        model = self._get_full_model()
        response: Response[models.DocumentationResponse200] = (
            documentation.sync_detailed(client=self.client, json_body=model)
        )
        validate_response(response)
        r = Renderer()
        r(response.parsed.description)

    def _refresh(self, comp: models.Computation) -> models.Computation:
        """
        Refreshes a _computation_ by fetching it from the client.

        This fetches the computation linked to this computation ID comp.id,
        and returns the current state of this computation on the instance.

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
        Sets an upper bound on the total aggregated value of the result in order to choose appropriate
        aggregation parameters. Out of bound values will be treated according to the clipping method.

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
    ) -> List[DataObject]:
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
            max_sleep_time (int, optional): maximum total time in nanoseconds to wait.

        Returns:
            List[DataObject]: the results of the computation.
        """
        # Define initial sleeping time and start time.
        start_time = time_tools.now()
        sleep_time = interval
        current_comp = comp

        # Poll the computation until done.
        while not self.is_done(current_comp):
            if time_tools.since(start_time) > self.max_timeout:
                raise TimeoutError("The computation timed out.")
            time_tools.sleep(sleep_time)
            current_comp = self._refresh(comp)
            if len(current_comp.warnings) > 0:
                warnings.warn(current_comp.warnings[len(current_comp.warnings) - 1])
            if sleep_time < max_sleep_time:
                sleep_time = int(sleep_time * 1.05)

        # Raise an exception if there is an error.
        if (current_comp.status == models.ComputationStatus.ERROR) or (
            len(comp.errors) > 0
        ):
            raise_computation_error(current_comp.errors)

        if len(current_comp.results) < 1:
            raise ValueError("The computation has no results.")

        # Update recorded computation.
        self.recorded_computations.append(current_comp)
        # Get Result models.
        results: List[DataObject] = []
        for dataobject_id in current_comp.results:
            response: Response[models.DataObject] = get_data_object.sync_detailed(
                client=self.client, data_object_id=dataobject_id
            )
            validate_response(response)
            results.append(DataObject(model=response.parsed, client=self.client))
        return results

    def _launch(self, model, local: bool = False) -> models.Computation:
        """
        Launch this computation, given its model.

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
        """Launches a computation using the compute endpoint (for internal use only)."""
        response: Response[models.Computation] = compute.sync_detailed(
            client=self.client, json_body=comp
        )
        validate_response(response)
        return response.parsed

    def _launch_with_project(self, comp):
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
    ) -> Any:
        """
        Runs this computation.

        This launches this computation on the instance, waits for it to finish, and
        returns the (decrypted) results.

        Args:
            local (bool, optional): Whether to run the computation locally or remotely. Defaults to False.
            keyswitch (bool, optional): Whether to perform key switching on the results. Defaults to True.
            decrypt (bool, optional): Whether to request the decryption on the results. Defaults to True.
            release (bool, optional): Whether to release the results (overrides decrypt/keyswitch).
                If set, encrypted results are automatically key switched and decrypted and a Result
                entity is saved. Defaults to False.
            interval (int, optional): time in nanoseconds to wait between polls.
            max_sleep_time (int, optional): maximum total time in nanoseconds to wait.

        Returns:
            List[DataObject]: A list of DataObject objects representing the results of the computation.
        """
        # Perform optional checks to have user-friendly messages in case something is missing.
        self._pre_run_check()

        # Update the model to reflect high-level parameters (preprocessing etc.).
        model = self._get_full_model()
        # Override the decrypt/keyswitch flags if release and or local are set.
        if release:
            model.release_results = True
            decrypt = False
            keyswitch = False
        if local:
            keyswitch = False  # Only for collective computations.

        # Start the computation and wait until it finishes.
        computation = self._launch(model, local=local)
        results = self._poll_computation(
            comp=computation, interval=interval, max_sleep_time=max_sleep_time
        )

        # If needed, keyswitch and/or decrypt the results.
        if keyswitch:
            for i, dataobject in enumerate(results):
                results[i] = self.key_switch(dataobject)
                if decrypt:
                    results[i] = results[i].decrypt()

        # Perform (optional) post-processing of the results if in plaintext.
        self._last_raw_results = results
        if release or decrypt:
            return self._process_results(results)
        return self._process_encrypted_results(results)

    def key_switch(self, data_object: DataObject) -> DataObject:
        """
        Perform a collective key switch on a data object.

        Args:
            data_object: the object on which to perform the collective key switch.
        """
        key_switch = KeySwitch(self.project, cipher_vector=data_object.get_id())
        return key_switch.run(local=False, keyswitch=False)


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
        **kwargs
    ):
        """
        Create a Computation for a specific model.

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
            elif isinstance(self.model.dp_epsilon, Unset):
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

    # Interfacing with the model directly: use comp["attr"] = value to set a model value.

    def __setitem__(self, key, value):
        self.model[key] = value

    def __getitem__(self, key):
        return self.model[key]


class KeySwitch(ModelBasedComputation):
    """
    A collective key switch computation.

    Collective key switches are used to collaboratively change the encryption
    key of a ciphertext in order to enable its decryption.
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
