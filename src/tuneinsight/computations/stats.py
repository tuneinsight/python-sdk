"""Simple univariate statistics."""

from typing import List, Dict, Any, Union
import math
import pandas as pd
import matplotlib.pyplot as plt
from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import UNSET
from tuneinsight.computations.base import ModelBasedComputation, ComputationResult
from tuneinsight.utils import time_tools
from tuneinsight.utils.plots import style_plot, style_title


# [Proposal]: Do we want to have approximate quantiles here? (even though it's another computation)


class StatisticsResults(ComputationResult):
    """Results of a Statistics computation."""

    results: List[models.StatisticResult]

    def __init__(self, results: List[models.StatisticResult]):
        self.results = results

    def as_table(self) -> pd.DataFrame:
        """Returns a pandas DataFrame containing the statistics."""
        cols = ["name", "mean", "variance", "min", "median", "max", "IQR"]
        data = []
        for res in self.results:
            data.append(
                [
                    res.name,
                    res.mean,
                    res.variance,
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
        for res in self.results:
            tmp = res.name.split()
            var_name = tmp[len(tmp) - 1]
            boxes.append(
                {
                    "label": var_name,
                    "whislo": res.min_,  # Bottom whisker position
                    "q1": res.quantiles[1],  # First quartile (25th percentile)
                    "med": res.median,  # Median         (50th percentile)
                    "q3": res.quantiles[3],  # Third quartile (75th percentile)
                    "whishi": res.max_,  # Top whisker position
                    "fliers": [],  # Outliers
                }
            )
            names.append(var_name)
            means.append(res.mean)
            deviations.append(math.sqrt(res.variance))

        ax[0].errorbar(names, means, deviations, linestyle="None", marker="o", color=c)
        ax[1].bxp(boxes, showfliers=False, medianprops={"color": c})

        # Apply Tune Insight styling to the plots.
        style_plot(
            ax[0],
            fig,
            "Mean & Standard Deviation",
            None,
            y_label=metric,
            size=(3.5 + 3 * len(self.results), 5),
            local=local,
        )
        style_title(ax[1], title="Quantiles")
        plt.show()


class Statistics(ModelBasedComputation):
    """
    A computation of basic statistics about individual variables in a dataset.

    The statistics that can be computed include the mean, variance, and quantiles
    (min, 25%, median, 75%, max), as well as the IQR.

    For each variable, a min and max bound need to be specified for the encrypted
    computations. These bounds do not need to be very accurate. By default, each
    variable is assumed to have bounds [0, 200]. Variables can be specified either
    in the constructor, or using the `.add_variable` method.

    """

    _variables: Dict[str, models.StatisticDefinition] = {}

    def __init__(
        self,
        project,
        variables: List[Union[str, dict]] = None,
        quantities: List[models.StatisticalQuantity] = UNSET,
    ):
        """
        Create a Statistics Computation.

        Args
            project (client.Project): the project to which this computation belongs.
            variables (list of str or dict): the variables to which this computation
                should be applied. Each variable can be specified either as a string
                (its name), in which case default bounds [0, 200] apply, or as a
                dictionary with entry "name" and optional "min_bound" and "max_bound".
            quantities (list of StatisticalQuantity): if provided, only compute the
                restricted set of statistics. If not provided, all quantities (mean,
                variance, and quantiles) will be computed.
        """
        super().__init__(
            project,
            models.DatasetStatistics,
            type=models.ComputationType.DATASETSTATISTICS,
        )
        self.quantities = quantities
        # The computation expects a dict mapping strings to models.StatisticDefinition
        # as input containing min and max bounds. We implement a high-level interface
        # where users can call add_variable to instantiate the variables.
        self._variables = {}
        for var in variables or []:
            if isinstance(var, str):
                self.add_variable(var, var)
            elif isinstance(var, dict):
                if "variable" not in var:
                    var["variable"] = var["name"]
                self.add_variable(**var)

    # [Proposal]: Remove these two methods. We should encourage users to use preprocessing
    # operations directly. Maybe I don't understand how this differs from just applying
    # the filter operation of preprocessing directly.

    def create_subgroups(
        self, variable_name: str, column: str, values: List[str], numerical=False
    ):
        if variable_name not in self._variables:
            raise ValueError(f"no such variable: {variable_name}")

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
        comparator: models.ComparisonType,
        value: Any,
        numerical: bool = True,
    ):
        if variable_name not in self._variables:
            raise ValueError(f"no such variable: {variable_name}")
        f = models.Filter(
            type=models.PreprocessingOperationType.FILTER,
            col_name=column,
            comparator=comparator,
            value=str(value),
            numerical=numerical,
        )
        # Does this set a filter for the computation on one variable only? I.e. the filtering operation will be different on others?
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
        Returns the api model definition of this computation.

        Returns:
            models.DatasetStatistics: the computation definition
        """
        # Update the variables of this model.
        self.model.statistics = list(self._variables.values())
        return self.model

    def _pre_run_check(self):
        """Checks that the user provided at least one variable to compute stats for."""
        if len(self._variables) == 0:
            raise ValueError("at least one variable must be added to the computation")
        self.max_timeout = 30 * time_tools.MINUTE

    def _process_results(self, dataobjects):
        """Post-processes results by converting them to StatisticsResults."""
        return StatisticsResults(dataobjects[0].get_stats().results)
