"""Perform counting queries on the collective dataset."""

from tuneinsight.computations.base import ModelBasedComputation
from tuneinsight.api.sdk import models


class Count(ModelBasedComputation):
    """
    Perform a counting query on the collective dataset.

    By default, this computation returns the size of the (collective) dataset.

    """

    def __init__(self, project):
        super().__init__(
            project,
            model_class=models.AggregatedDatasetLength,
            type=models.ComputationType.AGGREGATEDDATASETLENGTH,
        )

    def _process_results(self, dataobjects) -> float:
        """Extracts the count value from the output dataobjects."""
        return dataobjects[0].get_float_matrix().data[0][0]

    def run_query(self, query, local: bool = False) -> float:
        """Perform a counting query on the dataset. This assumes that the input is a database."""
        self.datasource.set_database_query(query)
        return self.run(local, release=True)


# For "compatibility" with the frontend, also name this DatasetLength.
DatasetLength = Count
