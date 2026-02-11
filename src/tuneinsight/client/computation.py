"""Classes to interact with computations stored in a Tune Insight instance."""

from typing import Any, List

from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.api.api_computations import get_computation
from tuneinsight.client.validation import validate_response
from tuneinsight.utils import time_tools

from tuneinsight import Diapason
from tuneinsight.computations.base import Computation as BaseComputation
from tuneinsight.computations.types import model_type_to_class


class Computation:
    """
    A computation that has been run on a Tune Insight instance.

    This class wraps the `models.Computation` API model and provides methods to
    interact with the computation, such as fetching results.

    Unlike the `Computation` class in `tuneinsight.computations.base` that represents
    the definition of a computation to be run, this class represents a computation that
    has already been created on the instance (according to a specific definition).
    """

    client: Diapason
    model: models.Computation

    def __init__(self, client: Diapason, model: models.Computation) -> None:
        self.client = client
        self.model = model

    def __getattr__(self, name: str) -> Any:
        """Delegate attribute access to the underlying model."""
        return getattr(self.model, name)

    @classmethod
    def from_id(cls, client: Diapason, computation_id: str) -> "Computation":
        """
        Returns the computation identified by the given unique identifier.

        Args:
            client (Diapason):
            computation_id (str): The ID of the computation.
        Returns:
            Computation: The Computation.
        """
        client.check_api_compatibility()
        response = get_computation.sync_detailed(
            client=client.client, computation_id=computation_id
        )
        validate_response(response)
        return cls(
            client=client,
            model=response.parsed,
        )

    @classmethod
    def from_model(
        cls,
        client: Diapason,
        model: models.Computation,
    ) -> "Computation":
        """
        Creates a Computation instance from an API model.

        Args:
            client (Diapason):
            model (models.Computation): The API model representing the computation.

        Returns:
            Computation: The Computation instance.
        """

        return cls(
            client=client,
            model=model,
        )

    def _refresh(self) -> None:
        """
        Refreshes the computation model from the server.
        """
        self.model = Computation.from_id(self.client, self.model.id)

    def _resolve_computation_class(self) -> BaseComputation:
        """
        Resolves the computation class based on the computation type using model_type_to_class from types.py.

        Returns:
            BaseComputation: The computation class.
        """

        try:
            comp_class = model_type_to_class(self.model.definition.type)
            return comp_class.from_model(
                self.client.get_project(project_id=self.model.project_id),
                self.model.definition,
            )
        except Exception as e:  # pylint: disable=broad-exception-caught
            raise ValueError(
                f"Unsupported computation type: {self.model.definition.type}"
            ) from e

    def fetch_results(
        self,
        interval: int = 100 * time_tools.MILLISECOND,
        max_sleep_time: int = 30 * time_tools.SECOND,
        verbose: bool = False,
    ) -> Any:
        """
        Fetches results for this computation.

        This waits until the computation completes (potentially timing out if the
        computation takes too long), then fetches the results of the computation and
        parses them as user-friendly objects.

        Args:
            interval (int, optional): time in nanoseconds to wait between polls.
            max_sleep_time (int, optional): maximum total time in nanoseconds to wait.
            verbose (bool, optional): whether to print progress.
        """
        # Delegate fetching results to the computation base class
        comp = self._resolve_computation_class()

        return comp.fetch_results(
            computation=self.model,
            interval=interval,
            max_sleep_time=max_sleep_time,
            verbose=verbose,
        )

    def get_status(self) -> models.ComputationStatus:
        """
        Fetches the latest status of this computation.

        Returns:
            models.ComputationStatus: The current status of the computation.
        """
        self._refresh()
        return self.model.status

    def get_errors(self) -> List[models.ComputationError]:
        """
        Fetches the errors associated with this computation.

        Returns:
            List[models.ComputationError]: The errors of the computation.
        """
        self._refresh()
        return self.model.errors
