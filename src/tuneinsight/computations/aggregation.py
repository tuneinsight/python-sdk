"""Implementation of the encrypted aggregation (sum) operation."""

from typing import Any, List, Union
import json
import warnings
import pandas as pd
from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import UNSET, is_set, none_if_unset, false_if_unset
from tuneinsight.client.dataobject import DataContent
from tuneinsight.computations.base import ModelBasedComputation
from tuneinsight.utils.plots import hist_grouped, hist


class Aggregation(ModelBasedComputation):
    """
    An encrypted aggregation computes the sum of columns in the collective dataset.

    When launched with multiple participating instances, the local dataset is first
    aggregated locally, then shared encrypted, and the collective global result is computed
    from encrypted local results.

    This computation supports grouping operations, where the data is disaggregated by
    the value of one or more columns. For numerical variables, the groups are intervals
    of values (defined either by `cuts` or rules to create bins). For categorical variables,
    the groups are for each value that the variable can take.

    This computation should be used for:
     - Computing the sum of values in a set of columns from the input dataset.
     - Computing the average value of a set of columns from the input dataset.
     - Counting the number of occurrences of values in a dataset.
     - Performing frequency analysis, which involves creating subgroups based on specified grouping
       rules and aggregating the data points per subgroup.

    This computation supports differential privacy. When using differential privacy, each
    variable should have lower and upper bounds defined (in its models.ColumnProperties, see
    __init__). Values outside these bounds will be clipped. The noise added to preserve privacy
    is proportional to the bounds, so loose bounds will come at a cost in precision. It is recommended
    to set these bounds using domain expertise, but it is forbidden to use the data to estimate
    the min and max bounds (this could create a privacy hazard 🔥).

    When using differential privacy, the sum and/or count for each possible group will be computed.
    It is thus necessary to specify the list of all possible groups: continuous groups should be
    defined through the `cuts` attribute, while categorical groups should have `possible_values` defined.

    """

    float_precision: int = 2
    cohort_id: str = ""
    join_id: str = ""
    dp_epsilon = UNSET
    columns: List[models.ColumnProperties]
    groups: List[models.GroupingParameters]
    include_count: bool
    average: bool

    def __init__(
        self,
        project: "Project",  # type: ignore
        columns: Union[List[any], str] = None,
        groups: Union[List[any], any] = None,
        include_count: bool = False,
        allow_missing_columns: bool = False,
        average: bool = False,
        float_precision: int = 2,
        cohort: "Cohort" = None,  # type: ignore
        dp_epsilon: float = UNSET,
        **kwargs,
    ):
        """
        Creates a new encrypted aggregation workflow.
        This workflow computes the sum of the dataset's columns under encryption.

        Args:
            project (`Project`): The project to run the computation with.

            columns (`list[models.ColumnProperties|str]|str`):
                The list of column names or single column to aggregate from the input dataset.
                If no columns are specified, then the workflow will use all of the dataset's columns.
                Columns can be either provided as a list of string values corresponding to their column names or
                as a models.ColumnProperties, which can specify minimum and maximum bounds for the column values to be taken into account
                when clipping and/or differential privacy is being used.

            groups (`str|List[any]`):
                Groups to use to perform a group-by operation locally before aggregating the columns per-group.
                Groups can be specified using multiple syntax:
                    'column': groups the data according to categorical values found in the 'column'.
                    ('column',['category_1','category_2']): groups the data according to categorical values from
                        column' that matches either 'category_1' or 'category_2'.
                    ('column',['category_1','category_2'],'default_value'): assigns the 'default_value' group to
                        the record by default when the record does not match the specified categories.
                    ('column',bin_size): groups are determined using numerical bins with a bin size of 10 according to
                        the values in 'column'. For `bin_size = 10`, this results in intervals such as ..., [-10,0), [0,10), [10,20), ...
                    ('column',bin_size,bin_center): groups are determined using numerical bins with a bin size of `bin_size` centered
                        around `bin_center`. For `bin_size = 10` and `bin_center = -5`, this results in intervals such as ..., [-15,-5), [-5,5), [5,15), ...
                    ('column',[bin_edge_1,...,bin_edge_k]): groups are determined using numerical bins with varying bin sizes determined
                        by the provided list of cuts. This results in intervals such as (,0), [0,40), [40,50), [50,).
                    List[`models.GroupingParameters`]: to directly specify the grouping parameters using the API models.

            include_count (bool, optional):
                Controls whether the output will contain the total number of aggregated records.
                Defaults to False.

            allow_missing_columns (bool, optional):
                When set to true, dummy zero-value columns are created for any columns specified in the 'columns' parameter that are missing in the input dataset.
                If set to false, an error is returned if any of the specified columns are missing from the input dataset.
                If no columns are specified and the columns from each participant are not identical, an error is returned.
                When grouping columns are specified, they must exist in the dataset regardless of the value of this parameter.
                However, the records from each participant do not need to fall into all groups.

            average (bool, optional):
                Controls whether the aggregated results are automatically averaged on the client-side.
                If this is set, then the include_count parameter gets automatically set to True.
                This allows the client to use the record count to compute the average in the post-processing phase.
                Defaults to False.

            float_precision (int, optional):
                Numerical precision of the output aggregated values. Defaults to 2.

            cohort (Cohort, optional):
                Cohort (Set Intersection workflow result) that can be reused as an input to this workflow. Defaults to None.

            dp_epsilon (float, optional):
                The privacy budget to use with this workflow. Defaults to UNSET, in which case differential privacy is not used.
        """

        # convert columns to appropriate API representation
        columns = Aggregation._parse_columns(columns=columns)
        # convert groups to appropriate API representation
        groups = Aggregation._parse_groups(groups=groups)
        if project.is_differentially_private:
            self._assert_dp_groups_compatibility(groups)
        # if groups are specified but columns are not, then set include count to true
        # if the average is requested then include average in.
        if (len(groups) > 0 and len(columns) == 0) or average:
            include_count = True

        super().__init__(
            project,
            models.EncryptedAggregation,
            type=models.ComputationType.ENCRYPTEDAGGREGATION,
            dp_epsilon=dp_epsilon,
            columns=columns,
            groups=groups,
            include_count=include_count,
            allow_missing_columns=allow_missing_columns,
            **kwargs,
        )
        if cohort is not None:
            self.model.cohort_id = cohort.cohort_id
            self.model.join_id = cohort.join_id
        self.float_precision = float_precision
        self.average = average
        self.groups = groups
        self.columns = columns
        self.include_count = include_count

    @classmethod
    def from_model(
        cls, project: "Project", model: models.EncryptedAggregation
    ) -> "Aggregation":
        """Initializes an Aggregation from its API model."""
        model = models.EncryptedAggregation.from_dict(model.to_dict())
        with project.disable_patch():
            comp = cls(
                project,
                columns=none_if_unset(model.columns),
                groups=none_if_unset(model.groups),
                include_count=false_if_unset(model.include_count),
                allow_missing_columns=false_if_unset(model.allow_missing_columns),
                dp_epsilon=model.dp_epsilon,
            )
        comp._adapt(model)
        return comp

    def _process_results(self, results: List[DataContent]) -> pd.DataFrame:
        result = results[0].get_float_matrix()
        totals = result.data[0]
        rounded_totals = [round(v, self.float_precision) for v in totals]
        if len(self.groups) > 0:
            return self._process_grouped_results(result.columns, rounded_totals)
        if len(result.columns) == len(rounded_totals):
            data = {"Column": result.columns, "Total": rounded_totals}
            if self.average:
                count = 1
                if "count" in result.columns:
                    count = rounded_totals[result.columns.index("count")]
                averages = [round(v / count, self.float_precision) for v in totals]
                data["Average"] = averages
        else:
            data = rounded_totals
        return pd.DataFrame(data)

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

        if self.average:
            for record in df_data.values():
                if "count" not in record:
                    continue
                for agg_col in self.columns:
                    if agg_col.name not in record:
                        continue
                    if record["count"] > 0:
                        record[f"average_{agg_col.name}"] = round(
                            record[agg_col.name] / record["count"], self.float_precision
                        )
        return pd.DataFrame(data=list(df_data.values()))

    @staticmethod
    def parse_group_columns(encoded_columns: List[str]) -> List[dict]:
        cols: List[dict] = []
        # Parse json encoded columns.
        for col in encoded_columns:
            try:
                tmp = json.loads(col)
                cols.append(tmp)
            except json.JSONDecodeError as e:
                warnings.warn(f"parsing {col} output column to JSON: {e}")
                cols.append({"aggregatedColumn": col, "groups": [], "count": False})
        return cols

    @staticmethod
    def _assert_dp_groups_compatibility(groups: List[models.GroupingParameters]):
        """
        Asserts whether grouping parameters are compatible with differential privacy.
        """
        for group in groups:
            if false_if_unset(group.numeric):
                # Numerical attribute: check that cuts are defined.
                assert is_set(
                    group.cuts
                ), "cuts must be defined for numerical values when using differential privacy."
            else:
                assert is_set(
                    group.possible_values
                ), "possible_values must be defined for categorical values when using differential privacy."

    def compute_approximate_quantiles(
        self, column: str, min_v: float = 0, max_v: float = 200, local: bool = False
    ) -> pd.DataFrame:
        """
        Computes the approximated averaged quantiles of a column of the collective dataset.

        The approximation operates in two steps:
            1. Each instance computes the exact quantiles on their local dataset.
            2. The vector of quantiles is averaged collectively across all participants.

        This method can be used as a fast approximation of the collective quantiles.
        To compute exact quantiles, use the `computations.Statistics` computation.

        ⚠️ This method is not compatible with differential privacy.

        Args:
            column (str): the column of the variable to compute the averaged quantiles from
            min_v (float, optional): the minimum bound that the value can take. Defaults to 0.
            max_v (float, optional): the maximum bound that the value can take. Defaults to 200.
            local (bool, optional): whether or not to compute the quantiles locally. Defaults to False.

        Returns:
            pd.DataFrame: a dataframe with one row recording all quantiles and the total number of data points
        """
        # Run an Aggregation, where the input is preprocessed to be quantiles.
        self.preprocessing.quantiles(column, min_v, max_v)
        df = self.run(local=local)
        # Post-process the results of the computation.
        quantiles = list(df.Total)[1:]  # pylint: disable=no-member
        n = list(df.Total)[0]  # pylint: disable=no-member
        new_row = [n]
        # Un-normalize the normalized quantiles returned by the aggregation to their original value.
        new_row.extend([(q / n) * (max_v - min_v) + min_v for q in quantiles])
        cols = ["n"]
        cols.extend([f"q{i}" for i in range(len(quantiles))])
        rounded_values = [round(v, self.float_precision) for v in new_row]
        return pd.DataFrame(data=[rounded_values], columns=cols)

    @staticmethod
    def _convert_to_group(arg: Any) -> models.GroupingParameters:
        """
        converts a 'group' argument to a GroupingParameters by accepting various formats.

        Args:
            arg (Any): the argument to convert.

        Raises:
            ValueError: if the value is not in a correct format.

        Returns:
            models.GroupingParameters: the equivalent grouping params.
        """
        grp = models.GroupingParameters()
        if isinstance(arg, models.GroupingParameters):
            return arg
        # Single str-column
        if isinstance(arg, str):
            grp.column = arg
            return grp

        if not isinstance(arg, tuple) or len(arg) == 0:
            raise ValueError(f"invalid value for group {arg}")

        grp.column = str(arg[0])
        if len(arg) < 2:
            return grp

        # Numeric Bin case
        if isinstance(arg[1], (float, int)):
            grp.bin_size = float(arg[1])
            grp.numeric = True
            if len(arg) >= 3:
                grp.bin_center = float(arg[2])
            return grp

        if not isinstance(arg[1], list):
            raise ValueError(f"invalid value for group {arg}")

        # Either cuts are provided or whitelist of of categorical values.
        if len(arg[1]) > 0:
            if isinstance(arg[1][0], (float, int)):
                grp.cuts = [float(v) for v in arg[1]]
                grp.numeric = True
            else:
                grp.possible_values = [str(v) for v in arg[1]]
        if len(arg) > 2:
            grp.default_group = str(arg[2])
        return grp

    @staticmethod
    def _parse_columns(
        columns: Union[List[any], str] = None,
    ) -> List[models.ColumnProperties]:
        tmp: List[models.ColumnProperties] = []

        if columns is None:
            columns = []
        if not isinstance(columns, list):
            columns = [columns]

        for col in columns:

            if isinstance(col, models.ColumnProperties):
                tmp.append(col)
                continue

            if isinstance(col, str):
                tmp.append(models.ColumnProperties(name=col))
                continue

            raise ValueError(f"invalid value {col} for column")
        # Ensure there are no duplicate columns
        seen = set()
        result: List[models.ColumnProperties] = []
        for col in tmp:
            if col.name not in seen:
                result.append(col)
                seen.add(col.name)
        return result

    @staticmethod
    def _parse_groups(
        groups: Union[List[any], any] = None,
    ) -> List[models.GroupingParameters]:
        if groups is None:
            groups = []
        if not isinstance(groups, list):
            groups = [groups]
        for i, group in enumerate(groups):
            groups[i] = Aggregation._convert_to_group(group)
        return groups

    def plot(
        self,
        result: pd.DataFrame,
        title: str = "Aggregation Results",
        x_label: str = "",
        y_label: str = "",
        size: tuple = (8, 4),
        group: str = "",
        columns: List[str] = None,
    ):
        """
        Plots histogram results from the Encrypted Aggregation / Sum workflow
        automatically by leveraging the workflow's parameters.

        Args:
            result (pd.DataFrame): the dataframe returned by the workflow.
            title (str, optional): optional title to give to the plot. Defaults to "Aggregation Results".
            x_label (str, optional): x-axis label. Defaults to "".
            y_label (str, optional): y-axis label. Defaults to "".
            size (tuple, optional): size of the plot. Defaults to (8, 4).
            group (str, optional): specific group to plot when multiple groups are used. Defaults to "".
            columns (List[str], optional): list of columns to plot. Defaults to None.
            stacked (bool, optional): whether the plotted columns are stacked for each category. Defaults to False.
        """
        if len(result.values) == 0:
            print("No results to plot")
            return

        if len(self.groups) > 0:
            self._plot_groups(result, title, x_label, y_label, size, group, columns)
        else:
            self._plot_histogram(result, title, x_label, y_label, size)

    def _plot_histogram(
        self,
        result: pd.DataFrame,
        title: str = "",
        x_label: str = "",
        y_label: str = "",
        size: tuple = (8, 4),
    ):
        x = list(result.Column)
        y = list(result.Total)
        if self.average:
            y = list(result.Average)
            x.pop()
            y.pop()

        hist(x, y, title, x_label=x_label, y_label=y_label, size=size)

    def _plot_groups(
        self,
        result: pd.DataFrame,
        title: str = "",
        x_label: str = "",
        y_label: str = "",
        size: tuple = (16, 9),
        group: str = "",
        columns: List[str] = None,
    ):

        to_plot = result
        if group == "":
            if len(self.groups) == 0:
                raise ValueError("no group to plot")
            group = self.groups[0].column
            if len(self.groups) > 2:
                warnings.warn(
                    "grouped result plotting is limited to 2 groups maximum. using the first group instead"
                )

        if columns is None:
            if hasattr(self, "columns") and len(self.columns) > 0:
                columns = [v.name for v in self.columns]
                if self.average:
                    columns = [f"average_{v}" for v in columns]
            else:
                # Contingency Matrix Print case
                if len(self.groups) == 2:
                    second_group = self.groups[1].column
                    columns = list(set(to_plot[second_group]))
                    # Here we pivot the data frame to plot such that we get as values for each second group the count w.r.t the first group.
                    to_plot = to_plot.pivot(
                        index=group, columns=second_group, values="count"
                    ).reset_index()
                else:
                    aggregated_df = to_plot.groupby(group)["count"].sum().reset_index()
                    aggregated_df.columns = [group, "count"]
                    columns = ["count"]
                    to_plot = aggregated_df
        hist_grouped(group, columns, to_plot, title, x_label, y_label, size)


Sum = Aggregation
