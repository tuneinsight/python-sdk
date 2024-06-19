"""Defines Cohorts, the output of PSI computations."""

from typing import List
import pandas as pd
from tuneinsight.computations.aggregation import Aggregation
from tuneinsight.computations.gwas import GWAS

# pylint: disable=unused-argument


class Cohort:
    """
    A Cohort is a dataset that results from a collective computation.

    Cohorts are created by:
        1) Private Set Intersection, where the cohort groups all records found
           in several (> 1) participating instances;
        2) Join queries, for vertically partitioned data, where different instances
           hold different attributes about the same records.

    A Cohort aims to allow developers to perform multiple post-hoc operations on the
    output of a PSI/Join without needing to perform the operation multiple times.

    """

    def __init__(self, project: "Project", cohort_id: str = "", join_id: str = ""):  # type: ignore
        """
        Creates a Cohort interface.

        Args
            project: the project which produced this cohort.
            cohort_id: the unique ID of a cohort created by a Private Set Intersection.
            join_id: the unique ID of a cohort created by a Join query.
        """
        self.project = project
        self.cohort_id = cohort_id
        self.join_id = join_id
        if not cohort_id and not join_id:
            raise ValueError("At least one of cohort_id or join_id must be provided.")

    # Utility functions for Cohorts.

    def get_size(self, nodes: List[str]) -> pd.DataFrame:
        """Computes the size of each participants' dataset in the cohort.

        Args:
            nodes (List[str]): list of participant names to get the dataset size of

        Returns:
            pd.DataFrame: a dataframe containing the size of the resulting cohort dataset for each node
        """
        agg = self.new_aggregation()
        for n in nodes:
            agg.preprocessing.counts(output_column_name=n, nodes=[n])
            agg.preprocessing.select(
                columns=nodes, create_if_missing=True, dummy_value="0", nodes=[n]
            )
        agg.preprocessing.select(columns=nodes, create_if_missing=True, dummy_value="0")
        return agg.run()

    # Computations performed on a cohort.
    # [Proposal]: if relevant, make these more generic, or enable easily the construction of
    # computations run on cohorts. This will probably be part of the computations refactoring.

    def new_aggregation(self) -> Aggregation:
        """
        Creates an aggregation computation on the cohort.

        The Aggregation returned can be used to perform sums etc. on
        the cohort "dataset" rather than on a datasource.

        Raises:
            Exception: if the cohort hasn't been created beforehand

        Returns:
            Aggregation: the encrypted aggregation computation
        """
        if self.cohort_id == "" and self.join_id == "":
            raise ValueError("A cohort must be created before running an aggregation.")
        return Aggregation(project=self.project, cohort=self)

    def new_gwas(self) -> GWAS:
        """
        Creates a GWAS computation on the cohort.

        The GWAS computation returned can be used to perform sums etc. on
        the cohort "dataset" rather than on a datasource.

        Raises:
            Exception: if the cohort hasn't been created beforehand

        Returns:
            GWAS: the GWAS computation
        """
        if self.cohort_id == "" and self.join_id == "":
            raise ValueError("A cohort must be created before running a GWAS.")
        return GWAS(project=self.project, cohort=self)
