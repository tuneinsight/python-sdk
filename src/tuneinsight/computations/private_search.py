"""Privately search a database for one or more values."""

from typing import List
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

from tuneinsight.client.dataobject import DataContent
from tuneinsight.client.session import PIRSession
from tuneinsight.computations.base import ModelBasedComputation, ComputationResult
from tuneinsight.client.validation import validate_response
from tuneinsight.utils.plots import style_plot

from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import Response
from tuneinsight.api.sdk.api.api_private_search import get_private_search_database

# pylint: disable=arguments-differ


class PrivateSearchResult(ComputationResult):
    """The output of a PrivateSearch computation."""

    def __init__(self, result):
        self.data = result

    def as_table(self) -> pd.DataFrame:
        return self.data

    def filter_result(
        self,
        start: str = None,
        end: str = None,
        granularity: str = None,
    ) -> pd.DataFrame:
        """
        Filters the query result between specific dates.

        Args:
            start (str, optional): If given, filter out results before this date.
            end (str, optional): If given, filter out results after this date.
            granularity (str, optional): If provided, rule on which to resample
                results (e.g. 'W-Mon' resamples results on a week granularity
                where weeks begin on a Monday).

        Returns:
            pd.DataFrame: filtered result.
        """
        filtered_result = self.data.transpose(copy=True)
        if start is not None:
            filtered_result = filtered_result.loc[start:]
        if end is not None:
            filtered_result = filtered_result.loc[:end]
        if granularity is not None:
            filtered_result = filtered_result.reset_index()
            filtered_result["Date"] = pd.to_datetime(filtered_result["index"])
            filtered_result = filtered_result.resample(granularity, on="Date").sum()
        return filtered_result.transpose()

    def plot(
        self,
        title: str,
        x_label: str,
        y_label: str,
        size: tuple = (8, 4),
        timestamps: bool = False,
    ):
        """
        Plots the private search result.

        Args:
            title (str): plot title.
            x_label (str): plot x axis label.
            y_label (str): plot y axis label.
            size (tuple, optional): size of the figure. Defaults to (8,4).
            timestamps (bool, default False): whether or not the result columns are timestamps.
        """
        plt.style.use("bmh")
        fig, ax = plt.subplots()
        x_vals = self.data.columns
        if timestamps:
            x_vals = pd.to_datetime(x_vals)
        x = list(x_vals)
        y = [int(v) for v in list(self.data.iloc[0])]
        if timestamps:
            ax.plot(x, y, color="#DE5F5A", linewidth=2.5)
            ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        else:
            ax.bar(x, y, color="#DE5F5A", edgecolor="#354661", linewidth=2.5)
        style_plot(ax, fig, title, x_label, y_label, size=size)

        plt.show()


class PrivateSearch(ModelBasedComputation):
    """
    A Private Search computation.

    Private Search uses private information retrieval to search for records in
    a dataset (hosted by another instance) without disclosing anything about
    what is being searched for or information about any other record.

    This operation requires the querier to know the unique identifier of the
    dataset being search (`pir_dataset_id`). No other information is required.

    """

    def __init__(self, project: "Project", pir_dataset_id: str):
        """
        Initializes a private search computation and its corresponding session.

        Args:
            project (Project): project to initialize the private search computation from
            pir_dataset_id (str): id of the private search dataset

        """
        super().__init__(
            project,
            models.PrivateSearch,
            type=models.ComputationType.PRIVATESEARCH,
            pir_dataset_object_id=pir_dataset_id,
        )
        self.pir_dataset_id = pir_dataset_id
        self.pir_db = self._get_pir_db()
        # A PIR comes with a Session to encrypt queries and decrypt results.
        self.session = PIRSession(self.client, self.pir_db)
        self.session.upload_eval_keys()

    def _get_pir_db(self) -> models.PrivateSearchDatabase:
        """
        Retrieves the private search database represented by a database ID.

        Returns:
            models.PrivateSearchDatabase: the private search database
        """
        with self.client.timeout(30) as client:
            response: Response[models.PrivateSearchDatabase] = (
                get_private_search_database.sync_detailed(
                    client=client, database_id=self.pir_dataset_id
                )
            )
            validate_response(response)
            return response.parsed

    def _process_results(self, results: List[DataContent]) -> PrivateSearchResult:
        """Decrypts the results from a query."""
        result = results[0].get_raw_data()
        decrypted_df = self.session.decrypt_response(result)
        return PrivateSearchResult(decrypted_df)

    def query(self, query: str) -> PrivateSearchResult:
        """
        Performs a private search query.

        Args:
            query (str): the search query.

        Returns:
            pd.DataFrame: private search result
        """
        self.model.pir_search_object_id = self.session.encrypt_query(query)
        return self.run()
