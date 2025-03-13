"""Computing the mean and standard deviation of some variables after filtering outliers."""

from typing import List
import pandas as pd

from tuneinsight.client.dataobject import DataContent
from tuneinsight.computations.base import ModelBasedComputation

from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import UNSET, value_if_unset


class EncryptedMean(ModelBasedComputation):
    """
    Computes the mean and standard deviation of a list of numbers without outliers.

    This computation operates in three stages:
        1. the mean and standard deviation are computed collectively,
        2. outliers are removed from each local dataset,
        3. the mean of the remaining samples is computed collectively.

    A value is marked as an outlier if it is more than a threshold (default 2) times
    the standard deviation away from the mean.

    Optionally, the data can be divided into groups, defined by the value of the
    record in a set of columns (defined by `grouping_keys`). In this case, a mean
    value is computed for each group (combination of values for grouping columns).

    This computation assumes that the dataset has a participant column (identified by
    the `participant` parameter) that contains the source of each data sample. Only
    one record per participant and per group is used for the computation.

    """

    def __init__(
        self,
        project,
        columns: List[str],
        grouping_columns: List[str] = UNSET,
        min_participants: int = 5,
        outlier_threshold: int = 2,
    ):
        """
        Creates an EncryptedMean computation.

        Args
            project (client.Project): the project to which this computation belongs.
            columns (list[str]): the columns for which to compute the mean and stddev.
            grouping_keys (list[str]): columns by which to disaggregate the mean (groupby).
            min_participants (int, default 5): minimum number of participants required for
                this computation. If less participants are available for a set of grouping
                values, no result is returned for that set.
            outlier_threshold (int, default 2): number of standard deviations that a value
                must differ from the mean to be marked as an outlier.
        """
        super().__init__(
            project,
            model_class=models.EncryptedMean,
            type=models.ComputationType.ENCRYPTEDMEAN,
            variables=columns,
            grouping_keys=grouping_columns,
            min_participants=min_participants,
            outlier_threshold=outlier_threshold,
        )

    @classmethod
    def from_model(
        cls, project: "Project", model: models.EncryptedMean  # type: ignore
    ) -> "EncryptedMean":
        """Initializes an EncryptedMean from its API model."""
        model = models.EncryptedMean.from_dict(model.to_dict())
        with project.disable_patch():
            comp = cls(
                project,
                columns=model.variables,
                grouping_columns=model.grouping_keys,
                min_participants=value_if_unset(model.min_participants, 5),
                outlier_threshold=value_if_unset(model.outlier_threshold, 2),
            )
        comp._adapt(model)
        return comp

    def _process_results(self, results: List[DataContent]) -> pd.DataFrame:
        return results[0].get_dataframe()
