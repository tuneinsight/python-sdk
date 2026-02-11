"""High-level interface to implement a heat map on top of an Aggregation computation."""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import UNSET, is_unset
from tuneinsight.client.dataobject import DataContent
from tuneinsight.utils.plots import style_plot, DEFAULT_COLORMAP

from .aggregation import Aggregation
from .base import ComputationResult


def _get_lower_bound(interval: str, integer: bool = False) -> float:
    """Returns the lower bound of a string-formatted interval."""
    if integer:
        if interval.startswith("<"):  # Open-ended on the left <x -- no lower bound.
            return -np.inf
        if interval.startswith("≥"):  # Open-ended on the right ≥x.
            return int(interval.removeprefix("≥"))
        if interval.startswith("("):  # Negative value (-x)-...
            return int(interval.removeprefix("(").split(")")[0])
        return int(interval.split("-")[0])  # Positive value x-...
    if interval.startswith("("):  # Open-ended on the left (,...)
        return -np.inf
    return float(interval.removeprefix("[").split(",")[0])  # Normal interval [x,y)


def _get_upper_bound(interval: str, integer: bool = False) -> float:
    """Returns the upper bound of a string-formatted interval."""
    if integer:
        if interval.startswith("<"):  # Open-ended on the left <x.
            return int(interval.removeprefix("<"))
        if interval.startswith("≥"):  # Open-ended on the right ≥x -- no upper bound.
            return np.inf
        if interval.endswith(")"):  # Negative value ...-(-x)
            return int(interval.removesuffix(")").split("(")[-1])
        return int(interval.split("-")[1])  # Positive value x-...
    if interval.endswith(",)"):  # Open-ended on the right [...,)
        return np.inf
    return float(interval.removesuffix(")").split(",")[1])  # Normal interval [x,y)


def _sort_numeric_groups(groups: list[str], integer: bool = False) -> list[str]:
    """Sorts disjoint numeric groups (i.e., intervals) by their lower bound."""
    # Sort by the left side of the interval.
    keys = [_get_lower_bound(g, integer) for g in groups]
    order = np.argsort(keys)
    return [groups[idx] for idx in order]


def _get_sorted_groups(
    df: pd.DataFrame, grouping: models.GroupingParameters
) -> list[str]:
    """Returns all groups found in the data for a specific grouping, sorted if numeric."""
    groups = list(pd.unique(df[grouping.column]))
    if grouping.numeric:
        return _sort_numeric_groups(groups, grouping.integer_bin_bounds)
    return groups


def _get_ticks(groups: list[str], grouping: models.GroupingParameters):
    """Returns nice ticks and labels for the heatmap. Assumes that the groups are sorted, non-overlapping, and contiguous."""
    # Non-numeric groups: set the tick in the middle of each tile.
    if is_unset(grouping.numeric) or not grouping.numeric:
        return np.arange(len(groups)), groups
    # Numeric group: get the lower bounds and one upper bound.
    ticks, labels = [], []
    for i, g in enumerate(groups):
        lb = _get_lower_bound(g)
        if np.isfinite(lb):
            # Add lower bound at the beginning of the tile.
            ticks.append(i - 0.5)
            labels.append(lb)
        else:
            # Open-ended interval: use the group name for the (first) tile instead.
            ticks.append(i)
            labels.append(g)
    # Also handle the last tick.
    ub = _get_upper_bound(groups[-1])
    if np.isfinite(ub):
        # Add upper bound at the end of the tile.
        ticks.append(len(groups) - 0.5)
        labels.append(ub)
    else:
        # Open-ended interval: use the group name for the last tile.
        ticks.append(len(groups))
        labels.append(groups[-1])
    return ticks, labels


class HeatMapResult(ComputationResult):
    """The result of a heatmap operation."""

    def __init__(self, df: pd.DataFrame, groupings: list[models.GroupingParameters]):
        """Post-processes the operation result.

        Args:
            df (pd.DataFrame): the raw results of the computation.
            groupings (list[models.GroupingParameters]): the groupings of the computation.
        """
        # The input dataframe has columns (group_variable_1, group_variable_2, count), and each
        # line contains the count for every combination of group 1 and 2. This code transforms this
        # count of list into a matrix with one row per "y group" (group 1) and one column per "x group" (group 2).
        # For example the following input dataset:
        #
        #  age      | gender | count
        #  --------------------------
        #  [20,30)  | F      | 3
        #  [20,30)  | M      | 4
        #  [30,40)  | F      | 2
        #
        # would be mapped to
        #
        # age     | F | M
        # ----------------
        # [20,30) | 3 | 4
        # [30,40) | 2 | 0
        #
        # Note that the choice of grouping 1 as "y" variable is arbitrary. To select the other variable instead,
        # one can simply transpose the dataframe with df.T.
        self.variables = var_y, _ = [group.column for group in groupings]
        self.y_groups = _get_sorted_groups(df, groupings[0])
        self.x_groups = _get_sorted_groups(df, groupings[1])
        # Format the table as a matrix of counts.
        count_matrix = np.zeros((len(self.y_groups), len(self.x_groups)))
        for (group_y, group_x), sub_df in df.groupby(self.variables):
            idx_x = self.x_groups.index(group_x)
            idx_y = self.y_groups.index(group_y)
            count_matrix[idx_y][idx_x] = sub_df["count"].iloc[0]

        # A bit of pandas magic to format this in a nice DataFrame: add the x group at the front of the row,
        # then add the y groups as title of the columns. At the end, set_index to make the x group the index.
        rows = [
            [group_y] + list(counts)
            for group_y, counts in zip(self.y_groups, count_matrix)
        ]
        self.results = pd.DataFrame(rows, columns=[var_y] + self.x_groups)
        self.results.set_index(var_y, inplace=True)
        self.groupings = groupings

    def as_table(self):
        """Returns the heatmap as a DataFrame (the counts disaggregated by groups as a matrix)."""
        return self.results

    def plot(self, flip: bool = False, title: str = None):
        """Displays the heatmap using Matplotlib.

        Args:
            flip (bool, optional): whether to switch the X and Y axes. By default, the first group is
                used for the Y axis, and the second group for the X axis. Setting flip=True has the
                opposite behavior.
            title (str, optional): title of the figure. Defaults to "Heatmap of {variable x} and {variable y}".
        """
        df = self.results
        var_y, var_x = self.variables
        x_groups, y_groups = self.x_groups, self.y_groups
        groupings = self.groupings
        if flip:
            var_x, var_y = var_y, var_x
            x_groups, y_groups = y_groups, x_groups
            df = df.T
            groupings = groupings[::-1]
        if title is None:
            title = f"Heatmap of {var_x} and {var_y}"
        plt.style.use("bmh")
        fig, ax = plt.subplots()
        plt.imshow(df, cmap=DEFAULT_COLORMAP)
        x_ticks, x_labels = _get_ticks(x_groups, groupings[1])
        plt.xticks(x_ticks, labels=x_labels, rotation=40)
        y_ticks, y_labels = _get_ticks(y_groups, groupings[0])
        plt.yticks(y_ticks, labels=y_labels)
        plt.colorbar()
        style_plot(ax, fig, title, var_x, var_y)


class HeatMap(Aggregation):
    """Wrapper over the `Aggregation` to compute a heatmap, i.e., counts disaggregated by two variables."""

    def __init__(self, project, groups: list, dp_epsilon=UNSET):
        assert len(groups) == 2, "two grouping variables are required"
        super().__init__(
            project,
            groups=groups,
            include_count=True,
            dp_epsilon=dp_epsilon,
        )

    def _process_results(self, results: list[DataContent]):
        # Use the Aggregation parser to get a dataframe with one row per count
        df = super()._process_results(results)
        # Wrap using the specific result class to provide smart plotting utilities.
        return HeatMapResult(df, self.model.groups)
