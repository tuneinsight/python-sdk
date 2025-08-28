"""Classes to compute simple univariate statistics."""

from typing import List, Dict, Any, Union
import warnings
import pandas as pd
import matplotlib.pyplot as plt

from tuneinsight.client.dataobject import DataContent, Result
from tuneinsight.computations.base import (
    ModelBasedComputation,
    ComputationResult,
)
from tuneinsight.computations.preprocessing import Comparator
from tuneinsight.cryptolib.postprocessing import statistics_confidence_interval
from tuneinsight.utils.plots import style_plot, style_title

from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import UNSET, is_set, value_if_unset

# [Proposal]: Do we want to have approximate quantiles here? (even though it's another computation)


class StatisticsResults(ComputationResult):
    """Results of a `Statistics` computation."""

    result_list: List[models.StatisticResult]

    def __init__(
        self,
        comp_def: models.DatasetStatistics,
        result: DataContent,
    ):
        # Extract the contents of the result as a statistics object.
        self._result = result
        stats = result.get_stats()
        self.result_list = stats.results
        self.raw_results = stats.raw_dp_results
        self.comp_def = comp_def

    def as_table(self) -> pd.DataFrame:
        """Returns a pandas DataFrame containing the statistics."""
        cols = ["name", "mean", "variance", "stddev", "min", "median", "max", "IQR"]
        data = []
        for res in self.result_list:
            data.append(
                [
                    res.name,
                    res.mean,
                    res.variance,
                    res.stddev,
                    res.min_,
                    res.median,
                    res.max_,
                    res.iqr,
                ]
            )
        return pd.DataFrame(data=data, columns=cols)

    def plot(self, metric: str = "", local=False):
        """Creates a Figure and plots the statistics, using TI branding."""
        plt.style.use("bmh")
        boxes = []
        fig, ax = plt.subplots(1, 2, sharey=True)
        names = []
        means = []
        deviations = []
        c = "#DE5F5A"
        for res in self.result_list:
            tmp = res.name.split()
            var_name = tmp[len(tmp) - 1]
            boxes.append(
                {
                    "label": var_name,
                    "whislo": res.min_,  # Bottom whisker position
                    "q1": res.quantiles[1],  # First quartile (25th percentile)
                    "med": res.median,  # Median (50th percentile)
                    "q3": res.quantiles[3],  # Third quartile (75th percentile)
                    "whishi": res.max_,  # Top whisker position
                    "fliers": [],  # Outliers
                }
            )
            names.append(var_name)
            means.append(res.mean)
            deviations.append(res.stddev)

        ax[0].errorbar(names, means, deviations, linestyle="None", marker="o", color=c)
        ax[1].bxp(boxes, showfliers=False, medianprops={"color": c})

        # Apply Tune Insight styling to the plots.
        style_plot(
            ax[0],
            fig,
            "Mean & Standard Deviation",
            None,
            y_label=metric,
            size=(3.5 + 3 * len(self.result_list), 5),
            local=local,
        )
        style_title(ax[1], title="Quantiles")
        plt.show()

    def confidence_intervals(self) -> pd.DataFrame:
        """
        Estimates 95% confidence intervals for all statistics computed, if computed with differential privacy.

        When statistics are computed with differential privacy, random noise is added at several points during
        the computation. The results obtained are thus randomized, and can vary significantly from the true
        value. Confidence intervals give an estimate of the range of plausible "true" values, given the observed
        noisy values. These intervals are estimated using Monte-Carlo estimation.

        Note: this presents a 95% confidence interval for each statistic independently (and not a multi-dimensional
        confidence interval for all statistics together).

        Raises:
            ValueError: If the result of the computation was a DataObject (should never happen).

        Returns:
            pd.DataFrame: A dataframe containing, in each row, the confidence interval for a statistic.
        """
        if not isinstance(self._result, Result):
            return ValueError("Got DataObject instead of Result.")
        dp_metadata = self._result.dp_metadata
        if dp_metadata is None:
            raise ValueError("No DP metadata available.")
        return statistics_confidence_interval(
            self.comp_def, [self.raw_results], dp_metadata
        )


class Statistics(ModelBasedComputation):
    """
    A computation of basic statistics about individual variables in a dataset.

    The statistics that can be computed include the mean, variance, and quantiles
    (min, 25%, median, 75%, max), as well as the inter-quartile range (IQR).

    For each variable, a min and max bound need to be specified for the encrypted
    computations. These bounds do not need to be very accurate. By default, each
    variable is assumed to have bounds [0, 200]. Variables can be specified either
    in the constructor, or using the `.add_variable` method.

    Optionally, each variable can be augmented with a filter operation that describes
    a subset of the data for which the statistics can be computed.

    """

    _variables: Dict[str, models.StatisticDefinition] = {}

    def __init__(
        self,
        project,
        variables: Union[List[Union[str, dict]], str] = None,
        quantities: List[models.StatisticalQuantity] = UNSET,
        dp_epsilon: float = UNSET,
    ):
        """
        Create a Statistics Computation.

        Args
            project (client.Project): the project to which this computation belongs.
            variables (str or list of (str or dict)): the variables to which this computation
                should be applied. Each variable can be specified either as a string
                (its name), in which case default bounds [0, 200] apply, or as a
                dictionary with entry "name" and optional "min_bound" and "max_bound".
                If this is a single string, then the input is equivalent to `[variables]`.
            quantities (list of StatisticalQuantity): if provided, only compute the
                restricted set of statistics. If not provided, all quantities (mean,
                variance, and quantiles) will be computed.
        """
        self.quantities = quantities
        # The computation expects a dict mapping strings to models.StatisticDefinition
        # as input containing min and max bounds. We implement a high-level interface
        # where users can call add_variable to instantiate the variables.
        self._variables = {}
        if isinstance(variables, str):
            # Prevent easy error where the user sets variable="my_variable".
            variables = [variables]
        for var in variables or []:
            if isinstance(var, str):
                self.add_variable(var, var)
            elif isinstance(var, dict):
                if "variable" not in var:
                    var["variable"] = var["name"]
                self.add_variable(**var)
        super().__init__(
            project,
            models.DatasetStatistics,
            type=models.ComputationType.DATASETSTATISTICS,
            dp_epsilon=dp_epsilon,
        )

    @classmethod
    def from_model(
        cls, project: "Project", model: models.DatasetStatistics
    ) -> "Statistics":
        """Initializes a Statistics object from its API model."""
        model = models.DatasetStatistics.from_dict(model.to_dict())
        # Parse the statistics in the object, and convert them to variables.
        conf = model.statistics
        quantities = UNSET
        if is_set(conf) and len(conf) > 0:
            quantities = conf[0].quantities
            for qt in conf[1:]:
                if quantities != qt.quantities:
                    warnings.warn(
                        f"Quantities mismatching between variables (will use {quantities})."
                    )
        with project.disable_patch():
            comp = Statistics(project, variables=[], quantities=quantities)
        # Add the variables one by one.
        if is_set(conf):
            for variable in conf:
                comp.add_variable(
                    name=variable.name,
                    variable=variable.variable,
                    min_bound=value_if_unset(variable.min_bound, 0),
                    max_bound=value_if_unset(variable.max_bound, 200),
                )
                if is_set(variable.filter_):
                    comp._variables[variable.name].filter_ = variable.filter_
        comp._adapt(model)
        return comp

    def create_subgroups(
        self, variable_name: str, column: str, values: List[str], numerical=False
    ):
        """
        Divides the dataset by groups defined by the value of a variable.

        Args
            variable_name (str): the variable for which the statistics are computed.
            column (str): the column to group by.
            values (list[str]): the list of possible group values.
            numerical (bool): whether the comparison is numerical.
        """
        if variable_name not in self._variables:
            raise ValueError(f"Variable is not used in computation: {variable_name}.")

        variable = self._variables[variable_name]
        for v in values:
            new_var_name = str(column) + "=" + str(v)
            self.add_variable(
                name=new_var_name,
                variable=variable.variable,
                min_bound=variable.min_bound,
                max_bound=variable.max_bound,
            )
            self.set_filter(
                variable_name=new_var_name,
                column=column,
                comparator=models.ComparisonType.EQUAL,
                value=v,
                numerical=numerical,
            )

    def set_filter(
        self,
        variable_name: str,
        column: str,
        comparator: Union[str, Comparator, models.ComparisonType],
        value: Any,
        numerical: bool = True,
    ):
        """
        Specifies a filter operation to apply to a variable.

        The filter applies to `column`, which can be different from the column for
        which statistics are computed (`variable_name`).

        Args
            variable_name (str): the variable for which the statistics are computed.
            column (str): the column to filter.
            comparator (str or Comparator): type of comparison. Either use the Comparator enum,
                or a user-friendly string ("==", ">", ">=", "<", "<=", or "!=").
            value: value with which to compare.
            numerical (bool): whether the comparison is numerical.
        """
        if variable_name not in self._variables:
            raise ValueError(f"Variable is not used in computation: {variable_name}.")
        if isinstance(comparator, str):
            comparator = Comparator.parse(comparator)
        f = models.Filter(
            type=models.PreprocessingOperationType.FILTER,
            col_name=column,
            comparator=comparator,
            value=str(value),
            numerical=numerical,
        )
        self._variables[variable_name].filter_ = f

    def add_variable(
        self, name: str, variable: str, min_bound: float = 0.0, max_bound: float = 200.0
    ):
        """
        Adds a new variable for the statistics computation.

        Args:
            name (str): The name of the variable.
            variable (str): The variable to compute statistics for.
            min_bound (float, optional): The minimum bound for the variable. Defaults to 0.0.
            max_bound (float, optional): The maximum bound for the variable. Defaults to 200.0.
        """
        self._variables[name] = models.StatisticDefinition(
            name=name,
            variable=variable,
            min_bound=min_bound,
            max_bound=max_bound,
            quantiles_k_value=1,
            quantities=self.quantities,
        )

    def _get_model(self) -> models.DatasetStatistics:
        """
        Returns the API model definition of this computation (overrides Computation._get_model).

        Returns:
            models.DatasetStatistics: the computation definition
        """
        # Update the variables of this model.
        self.model.statistics = list(self._variables.values())
        return self.model

    def _pre_run_check(self):
        """Checks that the user provided at least one variable to compute stats for."""
        if len(self._variables) == 0:
            raise ValueError(
                "At least one variable must be added to the computation (use `variables` in the constructor)."
            )

    def _process_results(self, results: List[DataContent]) -> StatisticsResults:
        """Post-processes results by converting them to StatisticsResults."""
        return StatisticsResults(self.model, results[0])
