"""Classes to perform matching operations (also called Private Set Intersection)."""

from typing import List, Any, Union, Tuple
import pandas as pd
import matplotlib.pyplot as plt

from tuneinsight.client.dataobject import DataContent
from tuneinsight.computations.base import (
    ModelBasedComputation,
    ComputationResult,
)
from tuneinsight.computations.cohort import Cohort
from tuneinsight.utils.plots import style_plot

from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import UNSET, is_set, none_if_unset, false_if_unset


class MatchingResult(ComputationResult):
    """
    Output of a Matching operation when a cohort is not expected.
    To use this object as input, use `on_previous_result=this.as_input()` in `Computation.run`.
    """

    def __init__(self, results: List[DataContent]):
        if len(results) == 0:
            raise ValueError(
                "No results were sent by the server. Please contact your administrator."
            )
        result_dataobject = results[0].get_dataobject()
        self.encrypted = result_dataobject.encrypted
        self.data_object = result_dataobject
        if not self.encrypted:
            self.data = results[0].get_dataframe()

    def add_ratio(self, all_parties: List[str]):
        """
        Adds a column to this result giving the fraction of participants with a record.

        This modifies the results dataframe in place, and can be called multiple times
        without creating issues.

        Args:
            all_parties (List[str]): list of the names of the parties involved in the PSI.
                This should be a list of valid column names in the underlying dataframe.
        """
        if self.encrypted:
            raise AttributeError("add_ratio cannot be called on encrypted results")
        self.data["psi_ratio"] = (
            self.data[all_parties].replace({"true": 1, "false": 0}).mean(axis=1)
        )

    def as_table(self) -> pd.DataFrame:
        if self.encrypted:
            raise AttributeError("as_table cannot be called on encrypted results")
        return self.data

    def as_input(self) -> models.DataObject:
        """
        Returns a reference to the results that can be reused as inputs to computations.
        ⚠️ WARNING: Not all computations currently support reusing results as input.
        Computations currently supporting this:
        - Aggregation
        - Survival

        Returns:
            models.DataObject: The remote data object reference.
        """
        return self.data_object

    def plot(self, title: str = "", x_label: str = "", y_label: str = ""):
        """
        Plots the matching results as a bar graph.

        This requires that the psi_ratio column exists: use `.add_ratio` before.

        Args:
            title (str): plot title
            x_label (str): plot x label
            y_label (str): plot y label
        """
        if self.encrypted:
            raise AttributeError("plot cannot be called on encrypted results.")
        if "psi_ratio" not in self.data.columns:
            raise ValueError(
                "Columns psi_ratio not found. Run `.add_ratio` (the name of all parties must be provided)."
            )
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


class Matching(ModelBasedComputation):
    """
    A Matching operation that securely computes the list of matching records across multiple participants.
    Behind the scenes, a Private Set Intersection (PSI) is executed across participating
    instances:

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
        project: "Project",  # type: ignore
        columns: Union[str, List[str]] = None,
        fuzzy: bool = False,
        fuzzy_columns: Union[str, List[str]] = None,
        local_input: Union[Any, List[Any], pd.DataFrame] = None,
        hide_origin: bool = False,
        share_results: bool = False,
        encrypted_results: bool = False,
    ):
        """
        Creates a Matching computation.

        Args
            project (client.Project): the project to which this computation belongs.


            columns (list[str], optional): the column(s) used to match the records with.

            fuzzy (bool, default False): if set to true, then fuzzy matching will be used using fuzzy column encoding.
                If no fuzzy column is specified, then all specified matching columns will be fuzzy-encoded.

            fuzzy_columns (list[str], optional): The column(s) that should be specifically fuzzy-encoded.

            local_input (Union[Any, List[Any], pd.DataFrame], optional): user-provided list of records to match.
                If provided, this overrides the datasource of the project.
                matching records. If False, results will be returned as a DataFrame.

            hide_origin (bool, optional): If set to True, matches are aggregated across instances before decryption.
              This prevents revealing which instances held matching records.

            share_results (bool,optional): If set to True, then the decrypted matching identifiers are shared with the other participating instances.
                This is useful when the goal is to reuse the result of the matching in another collective computation, as it ensures that all participants can reuse the result.

            encrypted_results (bool,optional): If set to True, then the matches are not decrypted by the requesting instance. Instead the matches are kept encrypted under a collective key
                and can be reused to compute statistics over all matching records, without revealing which records have matched.
                This mode is currently 🧪 experimental: it is subject to change in next versions, and is time-consuming (about 15 minutes per run).
        """

        matching_columns, fuzzy_params = self._parse_columns(
            columns=columns,
            fuzzy=fuzzy,
            fuzzy_columns=fuzzy_columns,
        )
        self.encrypted_results = encrypted_results
        # Initialize the computation for these settings.
        super().__init__(
            project,
            models.SetIntersection,
            type=models.ComputationType.SETINTERSECTION,
            matching_columns=[str(c) for c in matching_columns],
            fuzzy_params=fuzzy_params,
            hide_matching_origin=hide_origin,
            encrypted_results=encrypted_results,
            share_results=share_results,
        )
        self.all_columns = []
        self.all_columns.extend(matching_columns)
        if fuzzy_params is not UNSET:
            self.all_columns.extend(fuzzy_params.phonetic_columns)
        self.all_columns = list(set(self.all_columns))
        if local_input is not None:
            self._setup_local_input(local_input=local_input)

    @classmethod
    def from_model(
        cls, project: "Project", model: models.SetIntersection  # type: ignore
    ) -> "Matching":
        """Initializes a Matching computation from its API model."""
        model = models.SetIntersection.from_dict(model.to_dict())
        with project.disable_patch():
            comp = Matching(
                project,
                columns=none_if_unset(model.matching_columns),
                fuzzy=is_set(model.fuzzy_params),
                fuzzy_columns=(
                    model.fuzzy_params.phonetic_columns  # pylint: disable=no-member
                    if is_set(model.fuzzy_params)
                    else None
                ),
                hide_origin=false_if_unset(model.hide_matching_origin),
                encrypted_results=model.encrypted_results,
                share_results=model.share_results,
            )
        comp._adapt(model)
        return comp

    def _process_results(
        self, results: List[DataContent]
    ) -> Union[Cohort, MatchingResult]:
        """Creates a MatchingResult from the output of the computation."""
        return MatchingResult(results)

    def _process_encrypted_results(
        self, results: List[DataContent]
    ) -> Union[Cohort, MatchingResult]:
        """Creates a MatchingResult from the output of the computation (encrypted)."""
        return self._process_results(results)

    @staticmethod
    def _parse_columns(
        columns: List[str] = None,
        fuzzy: bool = False,
        fuzzy_columns: List[str] = None,
    ) -> Tuple[List[str], models.FuzzyMatchingParameters]:
        # Pre-process the inputs.
        matching_columns = []
        if columns is not None:
            if isinstance(columns, str):
                matching_columns.append(columns)
            else:
                matching_columns.extend(columns)
        for i, c in enumerate(matching_columns):
            matching_columns[i] = str(c)

        fuzzy_cols = []
        if fuzzy_columns is not None:
            if isinstance(fuzzy_columns, str):
                fuzzy_cols.append(fuzzy_columns)
            else:
                fuzzy_cols.extend(fuzzy_columns)
        for i, c in enumerate(fuzzy_cols):
            fuzzy_cols[i] = str(c)

        # Create fuzzy parameters using the API model.
        fuzzy_params = UNSET
        if fuzzy and len(fuzzy_cols) == 0:
            fuzzy_cols = matching_columns
        if len(fuzzy_cols) > 0:
            fuzzy_params = models.FuzzyMatchingParameters(phonetic_columns=fuzzy_cols)
        if len(matching_columns) == 0 and len(fuzzy_cols) == 0:
            raise ValueError(
                "At least one matching column (or fuzzy column) must be provided."
            )
        return matching_columns, fuzzy_params

    def _setup_local_input(self, local_input: Union[Any, List[Any], pd.DataFrame]):
        if not isinstance(local_input, pd.DataFrame):
            if not isinstance(local_input, list):
                local_input = [local_input]
            local_input = pd.DataFrame(data=local_input, columns=self.all_columns)
        self.set_local_input(local_input)
