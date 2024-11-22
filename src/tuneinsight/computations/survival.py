"""Classes for survival analysis."""

from typing import List, Dict
import pandas as pd
import matplotlib.pyplot as plt

from tuneinsight.client.dataobject import DataContent
from tuneinsight.computations.base import (
    ModelBasedComputation,
    ComputationResult,
)
from tuneinsight.utils.plots import style_plot

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
        self, survival_parameters: SurvivalParameters, results: Dict[str, pd.DataFrame]
    ):
        """
        Args
            survival_parameters: the parameters of the survival analysis.
            results: a dictionary mapping subgroup name to dataframe of results.
        """
        self.survival_parameters = survival_parameters
        self.results = results

    def as_table(self) -> pd.DataFrame:
        return self.results["all"]

    def plot(self):
        self.plot_survivals()

    def plot_survivals(
        self,
        size: tuple = (8, 4),
        duration_col: str = None,
        title="Survival curve",
    ):
        """
        Plots the survival curve of each subgroup.

        Args
            size (tuple): the size of the figure, defaults to (8, 4).
            duration_col (str, optional): the column giving the duration.
            title (str): title of the plot (defaults to "Survival curve").
        """
        if duration_col is None:
            duration_col = self.survival_parameters.get_duration_column()
        plt.style.use("bmh")
        fig, ax = plt.subplots()
        for label, df in self.results.items():
            x = df[duration_col]
            y = df["survival_probability"]
            ax.step(x, y, linewidth=2.5, label=label)
        ax.legend()
        style_plot(ax, fig, title, duration_col, "Survival Probability", size=size)
        plt.show()

    def plot_survival(
        self,
        subgroup="all",
        size: tuple = (8, 4),
        duration_col: str = None,
        title="Survival curve",
    ):
        """
        Plots the survival of a subgroup.

        Args
            subgroup (str): the group for which to plot the curve, defaults to "all".
            size (tuple): the size of the figure, defaults to (8, 4).
            duration_col (str, optional): the column giving the duration.
            title (str): title of the plot (defaults to "Survival curve").
        """
        if duration_col is None:
            duration_col = self.survival_parameters.duration_col

        plt.style.use("bmh")
        fig, ax = plt.subplots()
        df = self.results[subgroup]
        x = df[duration_col]
        y = df["survival_probability"]
        ax.step(x, y, linewidth=2.5, color="#DE5F5A")
        style_plot(ax, fig, title, duration_col, "Survival Probability", size=size)
        plt.show()


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
        fm = results[0].get_float_matrix()
        if len(fm.data) != len(self.model.subgroups) + 1:
            raise ValueError(
                f"Survival result dimensions mismatch (expected {len(self.model.subgroups) + 1} rows, got {len(fm.data)})."
            )
        result_mapping = {}
        for i, row in enumerate(fm.data):
            subgroup_name = "all"
            if i > 0:
                subgroup_name = self.model.subgroups[i - 1].name
            df = pd.DataFrame({"Column": fm.columns, "Total": row})
            result_mapping[subgroup_name] = (
                self.survival_parameters.post_process_survival(df)
            )
        return SurvivalResults(self.survival_parameters, result_mapping)

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
