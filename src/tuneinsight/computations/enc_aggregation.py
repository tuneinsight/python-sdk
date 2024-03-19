from typing import List
import pandas as pd
import matplotlib.pyplot as plt
from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import UNSET
from tuneinsight.computations.base import ModelBasedComputation
from tuneinsight.utils import deprecation
from tuneinsight.utils.plots import style_plot


class EncryptedAggregation(ModelBasedComputation):
    """
    An encrypted aggregation, computing the sum of each column in the collective dataset.

    Args:
        Computation: Inherits all methods available from the computation runner parent class
    """

    float_precision: int = 2
    cohort_id: str = ""
    join_id: str = ""
    selected_coselected_colsls: List[str] = None
    dp_epsilon = None
    lower_bounds = []
    upper_bounds = []

    def __init__(
        self,
        project: "Project",
        selected_columns: List[str] = UNSET,
        float_precision: int = 2,
        cohort: "Cohort" = None,
        dp_epsilon: float = UNSET,
        lower_bounds: list = UNSET,
        upper_bounds: list = UNSET,
        **kwargs,
    ):
        """
        Creates an EncryptedAggregation.

        Args
            project (client.Project): the project to which this computation belongs.
            selected_columns (list of strings, or UNSET): the columns to aggregate.
            float_precision (int, default 2): number of digits to round results to.
            cohort (Cohort, default None): if specified, the cohort of records over
                which this aggregation is computed.
            dp_epsilon (float, default unset): if using differential privacy, the
                privacy budget used by this computation.
            lower_bounds (list, default unset): if using differential privacy, the lower
                bounds on the values of each selected column.
            upper_bounds (list, default unset): similarly, upper bounds.

        """
        super().__init__(
            project,
            models.EncryptedAggregation,
            type=models.ComputationType.ENCRYPTEDAGGREGATION,
            aggregate_columns=selected_columns,
            dp_epsilon=dp_epsilon,
            lower_bounds=lower_bounds,
            upper_bounds=upper_bounds,
            **kwargs,
        )
        if cohort is not None:
            self.model.cohort_id = cohort.cohort_id
            self.model.join_id = cohort.join_id
        self.float_precision = float_precision

    def _process_results(self, dataobjects) -> pd.DataFrame:
        result = dataobjects[0].get_float_matrix()
        totals = result.data[0]
        rounded_totals = [round(v, self.float_precision) for v in totals]
        if len(result.columns) == len(rounded_totals):
            data = {"Column": result.columns, "Total": rounded_totals}
        else:
            data = rounded_totals
        return pd.DataFrame(data)

    def get_aggregation(self, local: bool = False) -> pd.DataFrame:
        """
        Performs the encrypted aggregation computation and returns the decrypted results.

        Args:
            local (bool, optional): whether or not to run the computation locally. Defaults to False.

        Returns:
            pd.DataFrame: the decrypted results as a dataframe
        """
        deprecation.warn(
            "EncryptedAggregation.get_aggregation", "EncryptedAggregation.run"
        )
        return self.run(local=local, release=True)

    def compute_approximate_quantiles(
        self, column: str, min_v: float = 0, max_v: float = 200, local: bool = False
    ) -> pd.DataFrame:
        """
        Computes the approximated averaged quantiles over all participants computed by aggregating (N * normalize_min_max(q_i,min,max))
        across all participants, where N is the number of local data points and q_i is the i'th quantile.
        This method enables fast approximation of the quantiles instead of going through the costly exact computation.

        Args:
            column (str): the column of the variable to compute the averaged quantiles from
            min_v (float, optional): the minimum the value can take. Defaults to 0.
            max_v (float, optional): the maximum the value can take. Defaults to 200.
            local (bool, optional): whether or not to compute the quantiles locally. Defaults to False.

        Returns:
            pd.DataFrame: a dataframe with one row recording all quantiles and the total number of data points
        """
        # The .quantiles preprocessing operation
        self.preprocessing.quantiles(column, min_v, max_v)
        df = self.run(local=local, release=True)
        quantiles = list(df.Total)[1:]  # pylint: disable=no-member
        n = list(df.Total)[0]  # pylint: disable=no-member
        new_row = [n]
        # Unnormalizes the normalized quantiles returned by the aggregation to their original value.
        new_row.extend([(q / n) * (max_v - min_v) + min_v for q in quantiles])
        cols = ["n"]
        cols.extend([f"q{i}" for i in range(len(quantiles))])
        rounded_values = [round(v, self.float_precision) for v in new_row]
        return pd.DataFrame(data=[rounded_values], columns=cols)

    @staticmethod
    def plot_aggregation(
        result: pd.DataFrame,
        title: str,
        x_label: str,
        y_label: str,
        size: tuple = (8, 4),
    ):
        """
        Plots the results of the aggregation as a bar plot.

        Args:
            result (pd.DataFrame): the aggregation result dataframe
            title (str): the title to give to the plot
            x_label (str): the x label to give to the plot
            y_label (str): the y label to give to the plot
            size (tuple, optional): the sizing of the plot. Defaults to (8,4).
        """
        plt.style.use("bmh")
        fig, ax = plt.subplots()

        x = list(result.Column)
        y = list(result.Total)

        ax.bar(x, y, color="#DE5F5A", edgecolor="#354661", linewidth=2.5)

        style_plot(ax, fig, title, x_label, y_label, size=size)

        plt.show()


Sum = EncryptedAggregation
