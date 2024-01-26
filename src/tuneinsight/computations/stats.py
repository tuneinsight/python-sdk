from typing import List, Dict, Any
import math
import pandas as pd
import matplotlib.pyplot as plt
from tuneinsight.api.sdk import models
from tuneinsight.client.computations import ComputationRunner
import tuneinsight.utils.time_tools as time
from tuneinsight.utils.plots import style_title, style_ylabel, add_ti_branding


class Statistics:
    results: List[models.StatisticResult]

    def __init__(self, results: List[models.StatisticResult]):
        self.results = results

    def as_table(self) -> pd.DataFrame:
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
        plt.style.use("bmh")
        boxes = []
        fig, ax = plt.subplots(1, 2, sharey=True)
        names = []
        means = []
        deviations = []
        fig.set_figheight(5)
        fig.set_figwidth(3.5 + 3 * len(self.results))
        fig.tight_layout()
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
        style_title(ax[0], title="Mean & Standard Deviation")
        style_title(ax[1], title="Quantiles")
        style_ylabel(ax[0], y_label=metric)
        add_ti_branding(ax[0], ha="right", local=local)
        plt.show()


class DatasetStatistics(ComputationRunner):
    variables: Dict[str, models.StatisticDefinition] = {}

    def create_subgroups(
        self, variable_name: str, column: str, values: List[str], numerical=False
    ):
        if variable_name not in self.variables:
            raise Exception(f"no such variable: {variable_name}")

        variable = self.variables[variable_name]
        for v in values:
            new_var_name = str(column) + "=" + str(v)
            self.new_variable(
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
        if variable_name not in self.variables:
            raise Exception(f"no such variable: {variable_name}")
        f = models.Filter(
            type=models.PreprocessingOperationType.FILTER,
            col_name=column,
            comparator=comparator,
            value=str(value),
            numerical=numerical,
        )
        self.variables[variable_name].filter_ = f

    def new_variable(
        self, name: str, variable: str, min_bound: float = 0.0, max_bound: float = 200.0
    ):
        """
        new_variable adds a new variable for the statistics computation.

        Args:
            name (str): The name of the variable.
            variable (str): The variable to compute statistics for.
            min_bound (float, optional): The minimum bound for the variable. Defaults to 0.0.
            max_bound (float, optional): The maximum bound for the variable. Defaults to 200.0.
        """
        self.variables[name] = models.StatisticDefinition(
            name=name,
            variable=variable,
            min_bound=min_bound,
            max_bound=max_bound,
            quantiles_k_value=1,
        )

    def get_model(self) -> models.DatasetStatistics:
        """
        get_model returns the api model definition of this computation

        Returns:
            models.DatasetStatistics: the computation definition
        """
        model = models.DatasetStatistics(type=models.ComputationType.DATASETSTATISTICS)
        model.statistics = list(self.variables.values())
        model.project_id = self.project_id
        return model

    def compute(self, local: bool = False) -> Statistics:
        """
        Computes the statistics for the variables added to the computation.

        Args:
            local (bool, optional): Whether to run the computation locally or collectively. Defaults to False.

        Returns:
            Statistics: A Statistics object representing the computed statistics.
        """
        if len(self.variables) == 0:
            raise Exception("at least one variable must be added to the computation")
        model = self.get_model()
        self.max_timeout = 30 * time.minute
        results = super().run_computation(comp=model, local=local, release=True)
        return Statistics(results[0].get_stats().results)

    def display_workflow(self):
        """
        display_workflow displays a documentation of the computation workflow
        """
        return super().display_documentation(self.get_model())
