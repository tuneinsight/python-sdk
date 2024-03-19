"""Classes for computations on vertically-partitioned data."""

from typing import List
import pandas as pd
from tuneinsight.api.sdk import models
from tuneinsight.computations.base import ModelBasedComputation
from tuneinsight.computations.cohort import Cohort
from tuneinsight.utils import deprecation


class SampleExtraction(ModelBasedComputation):
    """
    Computation for a Sample Extraction.

    This extracts a sample from a vertically-partitioned dataset obtained
    through a distributed JOIN operation.

    """

    def __init__(
        self,
        cohort: "Cohort",
        sample_size: int = 1,
        seed: str = "default-seed",
    ):
        """
        Creates a SampleExtraction.

        Args
            cohort (Cohort): the Cohort from which to extract a sample.
            sample_size (int, optional): size of the sample as number of rows. Defaults to 1.
            seed (str, optional): seed to use for the sampling. Defaults to "default-seed".

        """
        if not cohort.join_id:
            raise ValueError(
                "The cohort does not have a join_id (was it created by a DistributedJoin?)"
            )
        super().__init__(
            cohort.project,
            models.SampleExtraction,
            type=models.ComputationType.SAMPLEEXTRACTION,
            sample_size=sample_size,
            seed=seed,
            join_id=cohort.join_id,
        )

    def _process_results(self, dataobjects) -> pd.DataFrame:
        return dataobjects[0].get_dataframe()


class SecureJoin(ModelBasedComputation):
    """
    Computation for securely joining vertically partitioned data.

    This joins data from different instances, matching on one or more columns,
    into one virtual dataset with all the "target" columns. The data held by
    one instance never leaves that instance: the target columns are only
    accessed during collective computations (restricted to aggregation and GWAS).

    """

    def __init__(
        self, project: "Project", target_columns: List[str], join_columns: List[str]
    ):
        """
        Creates a SecureJoin.

        Args
            project (client.Project): the project to which this computation belongs.
            target_columns (List[str]): column names of target columns
            join_columns (List[str]): column names to join the data on
        """
        super().__init__(
            project,
            models.DistributedJoin,
            type=models.ComputationType.DISTRIBUTEDJOIN,
            target_columns=target_columns,
            join_columns=join_columns,
            missing_patterns=["", "NaN"],
        )
        # The Cohort output by the last run of the Computation.
        self.cohort = None

    def _process_results(self, dataobjects) -> Cohort:
        """Computes a Cohort from the join ID of the last computation run."""
        join_id = dataobjects[0].get_id()
        self.cohort = Cohort(self.project, join_id=join_id)
        return self.cohort

    def _process_encrypted_results(self, dataobjects) -> Cohort:
        return self._process_results(dataobjects)

    def sample_from(self, sample_size: int = 1, seed: str = "default-seed"):
        """
        Sample from this join.

        Call this only after running the computation. This is a wrapper over the
        SampleExtraction computation.

        Args
            sample_size (int, optional): size of the sample as number of rows. Defaults to 1.
            seed (str, optional): seed to use for the sampling. Defaults to "default-seed".
        """
        if self.cohort is None:
            raise ValueError("The SecureJoin must be run before sampling.")
        extractor = SampleExtraction(self.cohort, sample_size, seed)
        return extractor.run()

    def create(self, target_columns: List[str], join_columns: List[str]):
        """Create a dataset from a distributed join.

        Args:
            target_columns (List[str]): column names of target columns
            join_columns (List[str]): column names to join the data on

        """
        deprecation.warn("SecureJoin.create", "SecureJoin(...).run")
        return SecureJoin(self.project, target_columns, join_columns).run()

    def new_sample_extraction(self) -> SampleExtraction:
        """Create a Sample Extraction computation.

        Raises:
            Exception: if the join_id is not set.

        Returns:
            SampleExtraction: resulting computation.
        """
        deprecation.warn(
            "SecureJoin.new_sample_extraction", "SampleExtraction(SecureJoin().run())"
        )
        return SampleExtraction(self.cohort)
