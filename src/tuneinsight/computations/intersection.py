from typing import List, Any, Union
import pandas as pd
import matplotlib.pyplot as plt
from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import UNSET
from tuneinsight.computations.base import ModelBasedComputation, ComputationResult
from tuneinsight.computations.cohort import Cohort
from tuneinsight.utils.plots import style_plot


class SetIntersectionResult(ComputationResult):
    """Output of a PSI when a cohort is not expected."""

    def __init__(self, dataobjects):
        self.data = dataobjects[0].get_dataframe()

    def add_ratio(self, all_parties: List[str]):
        """
        Adds a column to this result giving the fraction of participants with a record.

        This modifies the results dataframe in place, and can be called multiple times
        without creating issues.

        Args:
            all_parties (List[str]): list of the names of the parties involved in the PSI.
                This should be a list of valid column names in the underlying dataframe.
        """
        self.data["psi_ratio"] = (
            self.data[all_parties].replace({"true": 1, "false": 0}).mean(axis=1)
        )

    def as_table(self) -> pd.DataFrame:
        return self.data

    def plot(self, title: str = "", x_label: str = "", y_label: str = ""):
        """
        Plots the PSI results as a bar graph.

        This requires that the psi_ratio column is created: use .add_ratio before.

        Args:
            title (str): plot title
            x_label (str): plot x label
            y_label (str): plot y label
        """
        if "psi_ratio" not in self.data.columns:
            raise ValueError("Run add_ratio before the plot.")
        plt.style.use("bmh")
        fig, ax = plt.subplots()
        ax.bar(
            self.data.index,
            self.data.psi_ratio,
            color="#DE5F5A",
            edgecolor="#354661",
            linewidth=2.5,
        )
        style_plot(ax, fig, title, x_label, y_label)
        plt.show()


class SetIntersection(ModelBasedComputation):
    """
    A Private Set Intersection (PSI) computation

    PSI finds all records that are shared by at least two participants in an
    encrypted way. No information about records outside the "intersection" is
    shared with any party.

    The output of the computation is a dataframe that contains the result of the
    PSI across all nodes using the provided column list as the matching columns.
    If an input is provided here then the remote instance will use it as its own
    input instead of querying the database.

    Alternatively, this computation can also return a Cohort. Cohorts are groups
    of (encrypted) matching records, on which further computations can be run.
    See the documentation at tuneinsight.computations.Cohort for more details.

    Since different datasets can contain different variables for the matching
    records, it is possible to specify which columns should match for the
    record to be considered the same. That match can also be approximate, based
    on the phonetics of the content ("fuzzy" matches).

    """

    def __init__(
        self,
        project: "Project",
        matching_columns: Union[str, List[str]],
        fuzzy: bool = False,
        fuzzy_columns: List[str] = None,
        cohort: bool = False,
    ):
        """
        Creates a Private Set Intersection.

        Args
            project (client.Project): the project to which this computation belongs.
            matching_columns (str or list[str]): the column or list of columns on which to
                match records.
            fuzzy (bool, default False): whether to use fuzzy matching.
            fuzzy_columns (list, optional): if using fuzzy matching, the columns on
                which to use fuzzy instead of exact matching. If not provided, all
                columns will use fuzzy matching.
            cohort (bool, default False): whether to create a Cohort from the
                matching records. If False, results will be returned as a DataFrame.
        """
        # Pre-process the inputs.
        if isinstance(matching_columns, str):
            matching_columns = [matching_columns]
        # Create fuzzy parameters using the API model.
        fuzzy_params = UNSET
        if fuzzy:
            if fuzzy_columns is None:
                fuzzy_columns = matching_columns
            fuzzy_params = models.FuzzyMatchingParameters(
                phonetic_columns=fuzzy_columns
            )
        # Handle the cohort case by setting the output format accordingly.
        self.cohort = cohort
        result_format = models.SetIntersectionOutputFormat(
            "cohort" if cohort else "dataset"
        )
        # Initialize the computation for these settings.
        super().__init__(
            project,
            models.SetIntersection,
            type=models.ComputationType.SETINTERSECTION,
            matching_columns=[str(c) for c in matching_columns],
            fuzzy_params=fuzzy_params,
            result_format=result_format,
        )

    def _process_results(self, dataobjects) -> Union[Cohort, SetIntersectionResult]:
        """Creates a Cohort or a DataFrame from the output of the computation."""
        if self.cohort:
            return Cohort(self.project, cohort_id=dataobjects[0].get_id())
        return SetIntersectionResult(dataobjects)

    def _process_encrypted_results(self, dataobjects) -> Cohort:
        if self.cohort:
            return Cohort(self.project, cohort_id=dataobjects[0].get_id())
        return dataobjects  # No post-processing otherwise.

    # High-level methods.

    def find_matches(self, values: Union[Any, List[Any], pd.DataFrame]) -> pd.DataFrame:
        """
        Performs the PSI on local inputs.

        This checks whether the values provided as argument are found in the
        datasets of other instances. This can be used to provide a query interface
        to other datasets (e.g., when this instance does not hold data).

        Args:
            values (value, list of values, or DataFrame): the values to use as
                local input, bypassing the project datasource. Default to None.

        Returns:
            pd.DataFrame: the list of items that matched with other instances.
        """
        # Convert the local input to a DataFrame with the right columns.
        if not isinstance(values, pd.DataFrame):
            if not isinstance(values, list):
                values = [values]
            values = pd.DataFrame(data=values, columns=self.model.matching_columns)
        self.set_local_input(values)
        return self.run(local=False, release=True)
