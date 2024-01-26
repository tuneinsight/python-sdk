from typing import List
import pandas as pd
import matplotlib.pyplot as plt
from tuneinsight.api.sdk import models
from tuneinsight.client.computations import ComputationRunner
from tuneinsight.utils.plots import style_plot


def revert_quantiles(
    quantiles: List[float], n: int, min_v: float, max_v: float
) -> List[float]:
    """
    revert_quantiles reverts the averaged/normalized quantiles returned by the aggregation to their original value

    Args:
        quantiles (List[float]): the normalized aggregated quantiles
        n (int): the total number of data points
        min_v (float): the minimum value used for normalizing
        max_v (float): the maximum value used for normalizing

    Returns:
        List[float]: the reverted quantiles list
    """
    res = []
    for q in quantiles:
        res.append(((q / n) * (max_v - min_v) + min_v))
    return res


class EncryptedAggregation(ComputationRunner):
    """
    EncryptedAggregation Represents the encrypted aggregation computation

    Args:
        ComputationRunner: Inherits all methods available from the computation runner parent class
    """

    cohort_id: str = ""
    join_id: str = ""
    float_precision: int = 2
    selected_cols: List[str] = None

    def get_model(self) -> models.EncryptedAggregation:
        model = models.EncryptedAggregation(
            type=models.ComputationType.ENCRYPTEDAGGREGATION
        )
        model.project_id = self.project_id
        model.cohort_id = self.cohort_id
        model.join_id = self.join_id
        if self.selected_cols is not None and len(self.selected_cols) > 0:
            model.aggregate_columns = self.selected_cols
        return model

    def get_aggregation(self, local: bool = False) -> pd.DataFrame:
        """
        get_aggregation computes the encrypted aggregation computation and returns the decrypted results as a dataframe

        Args:
            local (bool, optional): whether or not to run the computation locally. Defaults to False.

        Returns:
            pd.DataFrame: the decrypted results as a dataframe
        """
        model = self.get_model()
        dataobjects = super().run_computation(comp=model, local=local, release=True)
        result = dataobjects[0].get_float_matrix()
        totals = result.data[0]
        rounded_totals = [round(v, self.float_precision) for v in totals]

        if len(result.columns) == len(rounded_totals):
            data = {"Column": result.columns, "Total": rounded_totals}
        else:
            data = rounded_totals

        return pd.DataFrame(data)

    def get_averaged_quantiles(
        self, column: str, min_v: float = 0, max_v: float = 200, local: bool = False
    ) -> pd.DataFrame:
        """
        get_averaged_quantiles computes the averaged quantiles over all participants computed by aggregating (N * normalize_min_max(q_i,min,max))
        across all participants, where N is the number of local data points and q_i is the i'th quantile.

        Args:
            column (str): the column of the variable to compute the averaged quantiles from
            min_v (float, optional): the minimum the value can take. Defaults to 0.
            max_v (float, optional): the maximum the value can take. Defaults to 200.
            local (bool, optional): whether or not to compute the quantiles locally. Defaults to False.

        Returns:
            pd.DataFrame: a dataframe with one row recording all quantiles and the total number of data points
        """
        self.preprocessing.quantiles(column, min_v, max_v)
        df = self.get_aggregation(local=local)
        quantiles = list(df.Total)[1:]
        n = list(df.Total)[0]
        new_row = [n]
        new_row.extend(revert_quantiles(quantiles, n, min_v, max_v))
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
        plot_aggregation plots the results of the aggregation as a histogram

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

    def display_workflow(self):
        """
        display_workflow displays the workflow of the encrypted aggregation
        """
        return super().display_documentation(self.get_model())
