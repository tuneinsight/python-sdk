"""Defines Cohorts, the output of PSI computations."""

from typing import List
import pandas as pd
import matplotlib.pyplot as plt
from tuneinsight.api.sdk import models
from tuneinsight.utils.plots import style_plot
from tuneinsight.client.dataobject import DataObject
from tuneinsight.computations.enc_aggregation import EncryptedAggregation
from tuneinsight.computations.gwas import GWAS
from tuneinsight.utils import deprecation

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

    def __init__(self, project: "Project", cohort_id: str = "", join_id: str = ""):
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

    def new_aggregation(self) -> EncryptedAggregation:
        """
        Create an aggregation computation on the cohort.

        The EncryptedAggregation returned can be used to perform sums etc. on
        the cohort "dataset" rather than on a datasource.

        Raises:
            Exception: if the cohort hasn't been created beforehand

        Returns:
            EncryptedAggregation: the encrypted aggregation computation
        """
        if self.cohort_id == "" and self.join_id == "":
            raise ValueError("A cohort must be created before running an aggregation.")
        return EncryptedAggregation(project=self.project, cohort=self)

    def new_gwas(self) -> GWAS:
        """
        Create a GWAS computation on the cohort.

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

    @staticmethod
    def get_psi_ratio(
        all_parties: List[str], dataobjects: List[DataObject]
    ) -> pd.DataFrame:
        """
        Add a column to a PSI result indicating the percentage of participants at which the record was observed.

        Args:
            all_parties (List[str]): list of the names of the parties involved in the private set intersection
            dataobjects (List[DataObject]): psi result

        Returns:
            pd.DataFrame: parsed data
        """
        deprecation.warn(
            "Cohort.get_psi_ratio", "SetIntersectionResults.as_table(ratio=True)"
        )
        df = dataobjects[0].get_dataframe()
        num_parties = len(all_parties)
        percentages = []
        results = df.to_dict(orient="records")
        for row in results:
            match = 0
            for org in all_parties:
                if org in row and row[org] == "true":
                    match += 1
            percentages.append(match / num_parties * 100)
        df["psi_ratio"] = pd.Series(percentages)
        return df

    @staticmethod
    def plot_psi(x, y, title, x_label, y_label):
        """Plot the PSI results as a bar graph

        Args:
            x (_type_): x values
            y (_type_): y values
            title (_type_): plot title
            x_label (_type_): plot x label
            y_label (_type_): plot y label
        """
        deprecation.warn("Cohort.get_psi_ratio", "SetIntersectionResult.plot")
        plt.style.use("bmh")
        fig, ax = plt.subplots()
        ax.bar(x, y, color="#DE5F5A", edgecolor="#354661", linewidth=2.5)
        style_plot(ax, fig, title, x_label, y_label)
        plt.show()

    # Deprecated methods.

    def create_from_matching(
        self,
        matching_columns: List[str],
        result_format: models.SetIntersectionOutputFormat,
        local_input: models.LocalInput = None,
    ) -> List[DataObject]:
        """Create a cohort from matching columns.

        Args:
            matching_columns (List[str]): a list of column names to match on.
            result_format (models.SetIntersectionOutputFormat): the format to output the resulting cohort as
            local_input (models.LocalInput): optional local input to use in the computation

        Returns:
            List[DataObject]: The resulting dataobjects
        """
        deprecation.warn(
            "create_from_matching", "SetIntersection(..., cohort=True).run()", True
        )

    def create_from_join(self, target_columns: List[str], join_columns: List[str]):
        """Create a cohort from a Join operation over vertically partitioned data.

        Args:
            target_columns (List[str]): column names of target columns
            join_columns (List[str]): column names to join the data on
        """
        deprecation.warn("create_from_join", "DistributedJoin().run()", True)
