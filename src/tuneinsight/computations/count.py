"""Classes to perform counting queries on the collective dataset."""

from typing import List

from tuneinsight.client.dataobject import DataContent
from tuneinsight.computations.base import ModelBasedComputation

from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import UNSET


class Count(ModelBasedComputation):
    """
    A `Count` (also called `DatasetLength`) computation can be used to perform
    a counting query on a local or collective dataset.

    By default, this computation returns the size of the (collective) dataset.

    This computation supports differential privacy.

    """

    def __init__(self, project, dp_epsilon: float = UNSET):
        """
        Creates a `Count` computation.

        Args
            project (client.Project): the project to which this computation belongs.
            dp_epsilon (float, default unset): if using differential privacy, the
                privacy budget used by this computation.
        """
        super().__init__(
            project,
            model_class=models.AggregatedDatasetLength,
            type=models.ComputationType.AGGREGATEDDATASETLENGTH,
            dp_epsilon=dp_epsilon,
        )

    @classmethod
    def from_model(cls, project: "Project", model: models.AggregatedDatasetLength):
        """Creates a Count Computation from an API model."""
        with project.disable_patch():
            comp = cls(project, dp_epsilon=model.dp_epsilon)
        comp._adapt(model)
        return comp

    def _process_results(self, results: List[DataContent]) -> float:
        """Extracts the count value from the output results."""
        return results[0].get_float_matrix().data[0][0]

    def run_query(self, query, local: bool = False) -> float:
        """Performs a counting query on the dataset. This assumes that the input is a database."""
        self.datasource.set_database_query(query)
        return self.run(local)


# For "compatibility" with the frontend, also name this DatasetLength.
DatasetLength = Count
