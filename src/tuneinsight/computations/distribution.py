"""Implementation of the value distribution operation."""

from typing import List
import pandas as pd
from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import UNSET, value_if_unset
from tuneinsight.client.dataobject import DataContent
from tuneinsight.computations.aggregation import Aggregation
from tuneinsight.computations.base import ModelBasedComputation


class Distribution(ModelBasedComputation):
    """
    A value distribution computes a histogram of record counts from a single variable or column in a dataset.

    When launched with multiple participating instances, the local histogram is first
    computed locally, then shared encrypted, and the collective global result is computed
    from encrypted local results.

    This operation can also be achieved using the Aggregation operation, and serves as a simpler
    and more restrictive alternative when only simple histograms need to be computed.


    This computation supports differential privacy.
    When using differential privacy, the sum and/or count for each possible group will be computed.
    It is thus necessary to specify the list of all possible groups: continuous groups should be
    defined through the `cuts` attribute, while categorical groups should have `possible_values` defined.

    """

    float_precision: int = 2
    dp_epsilon = UNSET
    column: str
    numeric: bool
    cuts: List[float]
    bin_size: float
    bin_center: float
    bin_min: float
    bin_max: float
    grouping_params: models.GroupingParameters
    possible_values: List[str]

    def __init__(
        self,
        project: "Project",  # type: ignore
        column: str = None,
        numeric: bool = False,
        cuts: List[float] = None,
        bin_size: float = 10,
        bin_center: float = 0,
        bin_min: float = UNSET,
        bin_max: float = UNSET,
        possible_values: List[str] = None,
        float_precision: int = 2,
        dp_epsilon: float = UNSET,
        **kwargs,
    ):
        """
        Creates a new value distribution workflow.
        This workflow computes a histogram/distribution for a specific column of the datasets.

        Args:
            project (`Project`): The project to run the computation with.

            column (str): The column to compute the distribution on.

            numeric (bool, optional): Whether the column is numeric. Defaults to False.

            cuts (List[float], optional): The list of cuts to use for the distribution if the column is numeric. Defaults to None.

            bin_size (float, optional): The size of the bins to use for the distribution if the column is numeric. Defaults to 10.

            bin_center (float, optional): The center of the bins to use for the distribution if the column is numeric. Defaults to 0.

            bin_min (float, optional): The minimum value to use for the distribution if the column is numeric. Defaults to UNSET. This is required if differential privacy is used.

            bin_max (float, optional): The maximum value to use for the distribution if the column is numeric. Defaults to UNSET. This is required if differential privacy is used.

            possible_values (List[str], optional): The list of possible values for the column if the column is categorical. Defaults to None. This is required if differential privacy is used.

            float_precision (int, optional):
                Numerical precision of the output aggregated values. Defaults to 2.

            dp_epsilon (float, optional):
                The privacy budget to use with this workflow. Defaults to UNSET, in which case differential privacy is not used.
        """

        if cuts is not None:
            numeric = True

        group = models.GroupingParameters(
            column=column,
            bin_size=bin_size,
            bin_center=bin_center,
            bin_min=bin_min,
            bin_max=bin_max,
            cuts=cuts,
            possible_values=possible_values,
            numeric=numeric,
        )
        self.float_precision = float_precision
        self.column = column
        self.bin_size = bin_size
        self.bin_center = bin_center
        self.bin_min = bin_min
        self.bin_max = bin_max
        self.cuts = cuts
        self.possible_values = possible_values
        self.numeric = numeric
        self.grouping_params = group

        if project.is_differentially_private:
            Aggregation._assert_dp_groups_compatibility([group])

        super().__init__(
            project,
            models.ValueDistribution,
            type=models.ComputationType.VALUEDISTRIBUTION,
            dp_epsilon=dp_epsilon,
            column=column,
            bin_size=bin_size,
            bin_center=bin_center,
            bin_min=bin_min,
            bin_max=bin_max,
            cuts=cuts,
            possible_values=possible_values,
            numeric=numeric,
            **kwargs,
        )

    @classmethod
    def from_model(
        cls, project: "Project", model: models.ValueDistribution
    ) -> "Distribution":
        """Initializes a Distribution from its API model."""
        model = models.ValueDistribution.from_dict(model.to_dict())
        with project.disable_patch():
            comp = cls(
                project,
                column=model.column,
                numeric=model.numeric,
                cuts=model.cuts,
                bin_size=model.bin_size,
                bin_center=model.bin_center,
                bin_min=model.bin_min,
                bin_max=model.bin_max,
                possible_values=model.possible_values,
                float_precision=value_if_unset(model.precision, 2),
                dp_epsilon=model.dp_epsilon,
            )
        comp._adapt(model)
        return comp

    def _process_results(self, results: List[DataContent]) -> pd.DataFrame:
        result = results[0].get_float_matrix()
        totals = result.data[0]
        rounded_totals = [round(v, self.float_precision) for v in totals]
        return self._process_grouped_results(result.columns, rounded_totals)

    def _process_grouped_results(
        self, encoded_columns: List[str], data: List[float]
    ) -> pd.DataFrame:

        df_data = {}
        cols = Aggregation.parse_group_columns(encoded_columns)
        for col, data_entry in zip(cols, data):
            record = {}
            group_key = ":".join([group["value"] for group in col["groups"]])
            if group_key not in df_data:
                for group in col["groups"]:
                    record[group["column"]] = group["value"]
                df_data[group_key] = record
            else:
                record = df_data[group_key]

            if col["count"]:
                record["count"] = int(round(data_entry))
            if col["aggregatedColumn"] != "":
                record[col["aggregatedColumn"]] = data_entry

        return pd.DataFrame(data=list(df_data.values()))

    def plot(
        self,
        result: pd.DataFrame,
        title: str = "Distribution Results",
        x_label: str = "",
        y_label: str = "",
        size: tuple = (8, 4),
    ):
        """
        Plots histogram results from the Value Distribution workflow
        automatically by leveraging the workflow's parameters.

        Args:
            result (pd.DataFrame): the dataframe returned by the workflow.
            title (str, optional): optional title to give to the plot. Defaults to "Distribution Results".
            x_label (str, optional): x-axis label. Defaults to "".
            y_label (str, optional): y-axis label. Defaults to "".
            size (tuple, optional): size of the plot. Defaults to (8, 4).
        """
        aggregation_equivalent = Aggregation(
            project=None, include_count=True, groups=[self.grouping_params]
        )
        return aggregation_equivalent.plot(
            result, title, x_label, y_label, size, group=self.column
        )


Histogram = Distribution
