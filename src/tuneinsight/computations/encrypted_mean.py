"""Computing the mean and stddev of some variables after filtering outliers."""

from typing import List
from tuneinsight.computations.base import ModelBasedComputation
from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import UNSET


class EncryptedMean(ModelBasedComputation):
    """
    Computes the mean and standard deviation of a list of numbers without outliers.

    This computation operates in three stages:
        1. the mean and stddev are computed,
        2. outliers are removed from the dataset (defined by some threshold),
        3. the mean of the remaining samples is computed.

    This computation assumes that multiple "participants" contribute records to the
    dataset (identified by the `participant` column). Only one record per participant
    per value in a set of grouping columns (grouping key) is used for the computation.

    A value is marked as an outlier if it is more than a threshold (default 2) times
    the standard deviation away from the mean.

    """

    def __init__(
        self,
        project,
        variables: List[str],
        participant: str,
        grouping_keys: List[str] = UNSET,
        min_participants: int = 5,
        outlier_threshold: int = 2,
    ):
        """
        Creates an EncryptedMean computation.

        Args
            project (client.Project): the project to which this computation belongs.
            variables (list[str]): the variables for which to compute the mean and stddev.
            participant (str): name of the participants column.
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
            variables=variables,
            participant=participant,
            grouping_keys=grouping_keys,
            min_participants=min_participants,
            outlier_threshold=outlier_threshold,
        )

    def _process_results(self, dataobjects):
        return dataobjects[0].get_dataframe()
