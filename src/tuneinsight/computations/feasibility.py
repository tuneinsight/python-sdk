"""Implementation of the advanced feasibility operation."""

from typing import List, Union

import json
import matplotlib.pyplot as plt
import pandas as pd

from tuneinsight.computations.base import ModelBasedComputation, ComputationResult
from tuneinsight.computations.aggregation import Aggregation
from tuneinsight.utils.plots import (
    add_ti_branding,
    style_title,
    FONT_REGULAR,
    PLOT_TICK_COLOR,
    PLOT_EDGE_COLOR,
    TI_COLORS,
)

from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import none_if_unset, false_if_unset, value_if_unset


class FeasibilityResult(ComputationResult):
    """The result of a Feasibility computation."""

    def __init__(self, dataframes: List[pd.DataFrame]):
        self.dataframes = dataframes
        self.count = None
        self.grouped_counts = []
        for df in dataframes:
            # Special case: the count dataframe.
            if df.columns[0] == "count":
                self.count = df.values[0, 0]
                continue
            # Otherwise, parse the columns in JSON.
            self.grouped_counts.append(self._parse_grouped_dataframe(df))

    @staticmethod
    def _parse_column_group(s: str) -> List[str]:
        group_config = json.loads(s)
        group = group_config["groups"][0]
        return (group["column"], group["value"])

    @staticmethod
    def _parse_grouped_dataframe(df: pd.DataFrame) -> pd.DataFrame:
        groups = [FeasibilityResult._parse_column_group(c) for c in df.columns]
        values = df.values[0]
        data = [(c, v, x) for (c, v), x in zip(groups, values)]
        return pd.DataFrame(data, columns=["column", "value", "count"])

    def as_table(self) -> pd.DataFrame:
        """Collates together the results as one dataframe."""
        df = pd.DataFrame(
            [(None, None, self.count)], columns=["column", "value", "count"]
        )
        return pd.concat([df] + self.grouped_counts)

    def plot(self):
        """Displays all the grouped results on a single figure."""
        plt.figure(figsize=(15, 5))
        for i, df in enumerate(self.grouped_counts):
            ax = plt.subplot(1, 3, i + 1)
            style_title(ax, f'Count grouped by {df["column"][0]}')
            values = df["value"]
            counts = df["count"]
            xaxis = list(range(len(values)))
            plt.bar(
                xaxis,
                counts,
                color=TI_COLORS[0],
                edgecolor=PLOT_EDGE_COLOR,
            )
            plt.xticks(xaxis, values, font=FONT_REGULAR, color=PLOT_TICK_COLOR)
            plt.yticks(font=FONT_REGULAR, color=PLOT_TICK_COLOR)
            add_ti_branding(ax)


class Feasibility(ModelBasedComputation):
    """The feasibility computation computes multiple statistics from a single query to the data.

    The values computed can include:
     - the record count across al instances (feasibility count),
     - the counts disaggregated by grouping parameters.
     - the counts disaggregated by instance.
    """

    def __init__(
        self,
        project: "Project",
        groups: Union[List[any], any] = None,
        include_global_count: bool = True,
        per_instance_breakdown: bool = True,
        local_breakdown: bool = False,
        dp_epsilon: float = None,
    ):
        """Creates a new feasibility computation on this project.

        Args:
            project (Project): The project to run the computation with.
            groups (Union[List[any], any], optional): Groups to use to disaggregate the counts by (by default, no groups).
                See `aggregation.py` for the syntax to use to specify this operation.
            include_global_count (bool, optional): whether to include the global count. Defaults to True.
            per_instance_breakdown (bool, optional): whether to also disaggregate the global count by instance. Defaults to True.
            local_breakdown (bool, optional): whether to also show the breakdown when running locally (one bin only). Defaults to False.
            dp_epsilon (float, optional): the privacy budget to use with this workflow. Defaults to None, in which case differential privacy is not used.
        """
        # convert groups to appropriate API representation
        groups = Aggregation._parse_groups(groups=groups)
        super().__init__(
            project,
            model_class=models.Feasibility,
            type=models.ComputationType.FEASIBILITY,
            groups=groups,
            global_count=include_global_count,
            per_instance_breakdown=per_instance_breakdown,
            local_breakdown=local_breakdown,
            dp_epsilon=dp_epsilon,
        )

    def _process_results(self, results):
        # The feasibility computation has several results: the count, and the different groups.
        return FeasibilityResult([r.get_dataframe() for r in results])

    @classmethod
    def from_model(cls, project: "Project", model: models.Feasibility) -> "Aggregation":
        """Initializes a Feasibility from its API model."""
        model = models.Feasibility.from_dict(model.to_dict())
        with project.disable_patch():
            comp = cls(
                project,
                groups=none_if_unset(model.groups),
                include_global_count=value_if_unset(model.global_count, True),
                per_instance_breakdown=value_if_unset(
                    model.per_instance_breakdown, True
                ),
                local_breakdown=false_if_unset(model.local_breakdown),
                dp_epsilon=model.dp_epsilon,
            )
        comp._adapt(model)
        return comp
