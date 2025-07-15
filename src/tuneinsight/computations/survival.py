"""Classes for survival analysis."""

from typing import List, Dict
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from tuneinsight.client.dataobject import DataContent
from tuneinsight.computations.base import (
    ModelBasedComputation,
    ComputationResult,
)
from tuneinsight.cryptolib.postprocessing import (
    post_process_survival,
    kaplan_meier_confidence_interval,
)
from tuneinsight.utils.plots import style_plot, TI_COLORS

from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import UNSET, is_set


def _at_risk_column(i):
    """Formats a 'at risk' column name in a way expected by the backend."""
    return "risk_" + str(int(i))


def _event_column(i):
    """Formats a 'event' column name in a way expected by the backend."""
    return "event_" + str(int(i))


def _get_survival_prob_at(previous, num_at_risk, num_events):
    """Computes the survival probability at a specific point."""
    if num_at_risk == 0:
        return previous
    return previous * (1.0 - float(num_events) / float(num_at_risk))


class SurvivalParameters:
    """
    Data class defining the parameters of a survival analysis.

    This also contains utilities to format the results of the analysis and get preprocessing operations.

    """

    duration_col: str
    event_col: str
    event_val: str
    start_event: str
    end_event: str
    unit: models.TimeUnit
    unit_value: int
    num_frames: int

    def __init__(
        self,
        duration_col: str = UNSET,
        event_col: str = UNSET,
        event_val: str = UNSET,
        start_event: str = UNSET,
        end_event: str = UNSET,
        num_frames: int = UNSET,
        unit: models.TimeUnit = models.TimeUnit.WEEKS,
        unit_value: int = 1,
    ):
        """
        Creates the parameters of a survival analysis.

        Args
            duration_col (str): the name of the column that stores the duration
                for each sample, the values stored must be integers.
            event_col (str): the name of the column that stores the event status
                for each sample Default: 'event'.
            event_val (str): the event value indicating a survival event (e.g. death).
            start_event (Union[Unset, str]): the event column that must contain
                the timestamps of the start of the trial.
            end_event (Union[Unset, str]): the column that must contain the timestamps
                of the end event (can be empty if no event happened)
            num_frames (Union[Unset, int]): the number of time frames to take
                into account starting from the start of the survival.
            unit (models.TimeUnit): the unit to use to measure time.
            unit_value (int): number of time units to use as time frame.

        """
        self.duration_col = duration_col
        self.event_col = event_col
        self.event_val = event_val
        self.start_event = start_event
        self.num_frames = num_frames
        self.end_event = end_event
        self.unit = unit
        self.unit_value = unit_value

    def get_duration_column(self) -> str:
        """Finds the column to use as duration column."""
        if self.duration_col is not UNSET:
            return self.duration_col
        if str(self.unit) is not UNSET:
            return str(self.unit)
        return str(models.TimeUnit.WEEKS)

    def post_process_survival(self, aggregation_output: pd.DataFrame) -> pd.DataFrame:
        """Post-processes the dataframe from the computation based on the parameters."""
        aggregation_output = aggregation_output.round(0)
        tmp = pd.DataFrame(
            data=[aggregation_output["Total"].to_list()],
            columns=aggregation_output["Column"],
        )
        final = pd.DataFrame()

        duration_col = self.get_duration_column()
        final[duration_col] = range(self.num_frames)
        final["n_at_risk"] = final.apply(
            lambda x: tmp[_at_risk_column(x[duration_col])], axis=1
        )
        final["n_events"] = final.apply(
            lambda x: tmp[_event_column(x[duration_col])], axis=1
        )
        curr_prob = 1
        survival_probabilities = []
        for i in range(self.num_frames):
            curr_prob = _get_survival_prob_at(
                curr_prob, final.loc[i, "n_at_risk"], final.loc[i, "n_events"]
            )
            survival_probabilities.append(curr_prob)

        final["survival_probability"] = survival_probabilities
        return final

    def get_preprocessing_op(self) -> models.PreprocessingOperation:
        """Converts the parameters to an API model."""
        interval = models.Duration(unit=self.unit, value=self.unit_value)
        return models.Survival(
            models.PreprocessingOperationType.SURVIVAL,
            duration_column=self.duration_col,
            event_column=self.event_col,
            event_value=self.event_val,
            start_event_column=self.start_event,
            end_event_column=self.end_event,
            interval=interval,
            num_frames=self.num_frames,
        )

    @classmethod
    def from_model(cls, model: models.Survival):
        """Initializes a set of survival parameters from an API model."""
        unit, value = UNSET, UNSET
        if is_set(model.interval):
            interval = model.interval
            unit = interval.unit
            value = interval.value
        return cls(
            duration_col=model.duration_col,
            event_col=model.event_col,
            event_val=model.event_val,
            start_event=model.start_event,
            end_event=model.end_event,
            num_frames=model.num_frames,
            unit=unit,
            unit_value=value,
        )


class SurvivalResults(ComputationResult):
    """Result from a survival analysis."""

    def __init__(
        self,
        survival_parameters: SurvivalParameters,
        raw_results: pd.DataFrame,
        group_parameters: List[models.SurvivalAggregationSubgroupsItem],
        dp_epsilon: float = None,
    ):
        """
        Args
            survival_parameters: the parameters of the survival analysis.
            raw_results: a pandas DataFrame with the full survival data for each group (one row per group).
            group_parameters: the grouping parameters used in the survival analysis.
            dp_noise: if differentially private, epsilon parameter of the DP noise added (Defaults None). Used for confidence intervals.
        """
        self.survival_parameters = survival_parameters
        self.raw_results = raw_results
        self.group_parameters = group_parameters
        self.dp_noise = dp_epsilon
        self.results = self._process_raw(raw_results)

    def _process_raw(self, raw_results: pd.DataFrame) -> Dict[str, pd.DataFrame]:
        """Processes raw results to a dictionary of user-friendly dataframes (per group).

        Args:
            raw_results (pd.DataFrame): raw results from the floatmatrix result.

        Returns:
            Dict[str, pd.DataFrame]: dictionary mapping each group name to its result.
        """
        result_mapping = {}
        for i, row in raw_results.iterrows():
            subgroup_name = "all"
            if i > 0:
                subgroup_name = self.group_parameters[i - 1].name
            df = pd.DataFrame({"Column": raw_results.columns, "Total": row})
            result_mapping[subgroup_name] = (
                self.survival_parameters.post_process_survival(df)
            )
        return result_mapping

    def as_table(self) -> pd.DataFrame:
        return self.results["all"]

    def plot(self):
        self.plot_survivals()

    def plot_survivals(
        self,
        size: tuple = (6, 4),
        duration_col: str = None,
        title: str = "Survival curve",
        ci: bool = True,
    ):
        """
        Plots the survival curve of each subgroup.

        Args
            size (tuple): the size of the figure, defaults to (8, 4).
            duration_col (str, optional): the column giving the duration.
            title (str): title of the plot (defaults to "Survival curve").
            ci (bool): whether to plot a confidence interval.
        """
        if duration_col is None:
            duration_col = self.survival_parameters.get_duration_column()
        if ci:
            confidence_intervals = self.confidence_interval()
        plt.style.use("bmh")
        fig, ax = plt.subplots()
        x_max = 0
        for i, (label, df) in enumerate(self.results.items()):
            # We add a point at the beginning to start with a plateau of 1 on the first frame,
            # and a last point that duplicates the previous one to have a last step.
            x = np.array(df[duration_col])
            x = np.concat(([0], x + 1, [x[-1] + 2]))
            x_max = max(x_max, *x)
            y = np.array(df["survival_probability"])
            y = np.concat(([1], y, [y[-1]]))
            color = TI_COLORS[i % len(TI_COLORS)]
            ax.step(x, y, "-", linewidth=2, label=label, where="post", color=color)
            # Add big points for all the data points (the end of each time frame).
            ax.plot(x[1:-1], y[1:-1], ".", ms=5, color=color)
            if ci:
                this_ci = confidence_intervals[label]
                # Duplicate the last point of CIs as well.
                lower = np.array(this_ci["lower"])
                upper = np.array(this_ci["upper"])
                ax.fill_between(
                    x,
                    np.concat([lower, [lower[-1]]]),
                    np.concat([upper, [upper[-1]]]),
                    alpha=0.2,
                    step="post",
                    color=color,
                )
        ax.legend()
        # We add margin in the topleft so as to show the starting point (0,1).
        ax.set_ylim([0, 1.01])
        # Set "clever" xticks: we should have about 8 integer-valued ticks.
        space = x_max // 8
        x_max = int(space * np.ceil(x_max / space))
        ax.set_xlim([0, x_max])
        ticks = list(range(0, x_max + space, space))
        ax.set_xticks(ticks)
        style_plot(ax, fig, title, duration_col, "Survival Probability", size=size)
        plt.show()

    def plot_survival(
        self,
        subgroup="all",
        size: tuple = (6, 4),
        duration_col: str = None,
        title="Survival curve",
        ci: bool = False,
        color: str = "#DE5F5A",
    ):
        """
        Plots the survival of a subgroup.

        Args
            subgroup (str): the group for which to plot the curve, defaults to "all".
            size (tuple): the size of the figure, defaults to (8, 4).
            duration_col (str, optional): the column giving the duration.
            title (str): title of the plot (defaults to "Survival curve").
            ci (bool): whether to plot a confidence interval.
            color (str): the color of the curve and confidence interval.
        """
        if duration_col is None:
            duration_col = self.survival_parameters.get_duration_column()

        plt.style.use("bmh")
        fig, ax = plt.subplots()
        df = self.results[subgroup]
        x = df[duration_col]
        y = df["survival_probability"]
        ax.set_ylim([0, 1.01])
        ax.step(x, y, linewidth=2.5, color=color)
        if ci:
            cis = self.confidence_interval()
            ax.fill_between(
                x, cis[subgroup]["lower"], cis[subgroup]["upper"], fc=color, alpha=0.2
            )
        style_plot(ax, fig, title, duration_col, "Survival Probability", size=size)
        plt.show()

    def confidence_interval(self) -> Dict[str, pd.DataFrame]:
        """Estimates 95% confidence intervals for the Kaplan-Meier survival curve."""
        all_cis = kaplan_meier_confidence_interval(self.raw_results, self.dp_noise)
        grouped_cis = {}
        for i in range(len(self.raw_results)):
            subgroup_name = "all"
            if i > 0:
                subgroup_name = self.group_parameters[i - 1].name
            grouped_cis[subgroup_name] = {
                "lower": all_cis.iloc[2 * i],
                "upper": all_cis.iloc[2 * i + 1],
            }
        return grouped_cis

    def post_process(self) -> "SurvivalResults":
        """
        Post-processes a survival curve obtained with differential privacy.

        When differential privacy is used, noise is added to the survival results,
        which means that the counts obtained are not integer-valued and the survival
        curve is not guaranteed to be non-increasing. This function processes the
        noisy results and returns a new SurvivalResults object with integer values
        and a non-increasing survival curve.

        A caveat: while the post-processed curve looks more "correct", it is _less_
        accurate than the noisy result. Post-processing may introduce biases and lead
        to imprecise conclusions. These issues can be mitigated by changing the survival
        parameters and the privacy budget -- always validate results on toy use cases
        before running a mission-critical analysis.

        Returns:
            SurvivalResults: post-processed results.
        """
        # Post-process the *raw* results (as expected by the method).
        post_processed_results = post_process_survival(self.raw_results)
        return SurvivalResults(
            self.survival_parameters,
            post_processed_results,
            self.group_parameters,
        )


class SurvivalAnalysis(ModelBasedComputation):
    """
    Survival analysis computation.

    This computes collective survival curves using an encrypted aggregation.
    It is recommended to use specific submethods to configure this operation,
    rather than the constructor.

    """

    def __init__(
        self,
        project: "Project",
        survival_parameters: SurvivalParameters,
        matching_organization: str = "",
        matching_columns: List[str] = None,
        fuzzy_matching: bool = False,
        dp_epsilon: float = UNSET,
    ):
        """
        Initializes a Survival Analysis.

        Args
            project (client.Project): the project to which this computation belongs.
            survival_parameter (SurvivalParameters): the parameters for this operation.
            matching_organization (str): the organization with whom to match records.
            matching_columns (list of str): the columns to use for the matching.
            fuzzy_matching (bool, default False): whether to match approximately (fuzzy).
            dp_epsilon (float, optional): The privacy budget to use with this workflow.
                Defaults to UNSET, in which case differential privacy is not used.
        """
        super().__init__(
            project,
            models.SurvivalAggregation,
            type=models.ComputationType.SURVIVALAGGREGATION,
            survival_parameters=survival_parameters.get_preprocessing_op(),
            subgroups=[],
            secure_matching=len(matching_organization) > 0,
            matching_organization=matching_organization,
            matching_columns=(
                [
                    models.MatchingColumn(name=c, fuzzy=fuzzy_matching)
                    for c in matching_columns
                ]
                if matching_columns is not None
                else []
            ),
            dp_epsilon=dp_epsilon,
        )
        # Also save the survival parameters for post-processing.
        self.survival_parameters = survival_parameters

    @classmethod
    def from_model(
        cls, project: "Project", model: models.SurvivalAggregation
    ) -> "SurvivalAnalysis":
        """Initializes a SurvivalAnalysis computation from its API model."""
        model = models.SurvivalAggregation.from_dict(model.to_dict())
        # Convert model.matching_columns to parameters.
        fuzzy = False
        matching_columns = []
        if is_set(model.matching_columns):
            for mc in model.matching_columns:
                if is_set(mc.fuzzy) and mc.fuzzy:
                    # All variables should have the same fuzzy value.
                    fuzzy = True
                matching_columns.append(mc.name)
        with project.disable_patch():
            comp = SurvivalAnalysis(
                project,
                survival_parameters=SurvivalParameters.from_model(
                    model.survival_parameters
                ),
                matching_columns=matching_columns,
                fuzzy_matching=fuzzy,
                dp_epsilon=model.dp_epsilon,
            )
        comp._adapt(model)
        return comp

    def _process_results(self, results: List[DataContent]) -> Dict[str, pd.DataFrame]:
        """Converts raw results to a dictionary mapping subgroup name to a dataframe."""
        result = results[0]
        fm = result.get_float_matrix()
        if len(fm.data) != len(self.model.subgroups) + 1:
            raise ValueError(
                f"Survival result dimensions mismatch (expected {len(self.model.subgroups) + 1} rows, got {len(fm.data)})."
            )
        raw_results = pd.DataFrame(fm.data, columns=fm.columns)
        return SurvivalResults(
            self.survival_parameters,
            raw_results,
            self.model.subgroups,
            dp_epsilon=self.model.dp_epsilon,
        )

    def add_categories(self, column: str, values: List[str]):
        """
        Creates subgroups of the data to study independently.

        This will make the survival analysis output one survival curve for
        each group, created by grouping records by the value of the specified
        column (restricting to the values specified by `values`).

        Args
            column (str): the column to create the groups from.
            values (list[str]): value of the column for each group.
        """
        for v in values:
            self.add_subgroup(v, column, models.ComparisonType.EQUAL, v)

    def add_subgroup(
        self,
        name: str,
        target_column: str,
        comparator: models.ComparisonType,
        value: str,
        numerical: bool = False,
    ):
        """
        Creates a subgroup in the data for which to plot a survival curve.

        This group is obtained by filtering records that satisfy a condition
        of the type `column` `comparator` `value` (e.g. age >= 18).

        Args
            name (str): name of the subgroup.
            target_column (str): column to condition on.
            comparator (models.ComparisonType): comparator of the condition.
            value (str): value that the condition uses. Should be converted to string.
            numerical (bool, default False): whether to convert values to numbers
                when evaluating the condition.
        """
        filter_operation = models.Filter(
            type=models.PreprocessingOperationType.FILTER,
            column=target_column,
            comparator=comparator,
            value=str(value),
            numerical=numerical,
        )
        # Update the model with this subgroup.
        self.model.subgroups.append(
            models.SurvivalAggregationSubgroupsItem(filter_=filter_operation, name=name)
        )
        # Update the computation with this subgroup (and broadcast changes).
        self.project.set_computation(self)
