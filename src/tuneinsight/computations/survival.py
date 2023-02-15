from typing import List
import pandas as pd
import matplotlib.pyplot as plt
from tuneinsight.api.sdk import models
from tuneinsight.utils.plots import style_plot
from tuneinsight.api.sdk.types import UNSET

def at_risk_column(i):
    return 'risk_' + str(int(i))

def event_column(i):
    return 'event_' + str(int(i))


def get_survival_prob_at(previous,num_at_risk,num_events):
    if num_at_risk == 0:
        return previous
    return previous * (1.0 - float(num_events) / float(num_at_risk))


class SurvivalParameters:


    duration_col: str
    event_col: str
    event_val: str
    start_event: str
    end_event: str
    unit: models.TimeUnit
    num_frames: int

    def __init__(self, duration_col: str = UNSET, event_col: str = UNSET, event_val: str = UNSET, start_event: str = UNSET, end_event: str = UNSET, num_frames: int = UNSET, unit: models.TimeUnit = models.TimeUnit.MONTHS):
        self.duration_col = duration_col
        self.event_col = event_col
        self.event_val = event_val
        self.start_event = start_event
        self.num_frames = num_frames
        self.end_event = end_event
        self.unit = unit


    def _resolve_duration_column(self) -> str:
        if self.duration_col is not UNSET:
            return self.duration_col
        if str(self.unit) is not UNSET:
            return str(self.unit)
        return str(models.TimeUnit.MONTHS)


    def compute_survival(self,aggregation_output: pd.DataFrame) -> pd.DataFrame:

        aggregation_output = aggregation_output.round(0)
        tmp = pd.DataFrame(data=[aggregation_output["Total"].to_list()],columns=aggregation_output["Column"])
        final = pd.DataFrame()

        duration_col = self._resolve_duration_column()
        final[duration_col] = range(self.num_frames)
        final['n_at_risk'] = final.apply(lambda x: tmp[at_risk_column(x[duration_col])],axis=1)
        final['n_events'] = final.apply(lambda x: tmp[event_column(x[duration_col])],axis=1)
        curr_prob = 1
        survival_probabilities = []
        for i in range(self.num_frames):
            curr_prob = get_survival_prob_at(curr_prob,final.loc[i,"n_at_risk"],final.loc[i,"n_events"])
            survival_probabilities.append(curr_prob)

        final['survival_probability'] = survival_probabilities
        return final

    def get_preprocessing_op(self) -> models.PreprocessingOperation:
        return models.Survival(models.PreprocessingOperationType.SURVIVAL,
                               duration_col=self.duration_col,
                               event_col=self.event_col,
                               event_val=self.event_val,
                               start_event=self.start_event,
                               end_event=self.end_event,
                               unit=self.unit,
                               num_frames=self.num_frames)

    def get_target_columns(self) -> List[str]:
        res = []
        for i in range(self.num_frames):
            res.append(at_risk_column(i))
            res.append(event_column(i))
        return res

    def plot_survivals(self, results: dict[str, pd.DataFrame], size:tuple=(8,4), duration_col: str = None, title="Survival curve"):
        if duration_col is None:
            duration_col = self._resolve_duration_column()
        plt.style.use("bmh")

        # plot
        fig, ax = plt.subplots()

        for label, df in results.items():
            x = df[duration_col]
            y = df['survival_probability']

            ax.step(x, y, linewidth=2.5, label=label)

        ax.legend()

        style_plot(ax, fig, title, duration_col, "Survival Probability", size=size)

        plt.show()

    def plot_survival(self, df: pd.DataFrame, size:tuple=(8,4), duration_col: str = None, title="Survival curve"):
        if duration_col is None:
            duration_col = self.duration_col

        plt.style.use("bmh")

        # plot
        fig, ax = plt.subplots()


        x = df[duration_col]
        y = df['survival_probability']

        ax.step(x, y, linewidth=2.5, color="#DE5F5A")


        style_plot(ax, fig, title, duration_col, "Survival Probability", size=size)

        plt.show()

    # def get_categorical_survival(self, target_column:str, values:List[str], nodes:List[str], cohort:Cohort):
    #     result = {}
    #     for value in values:
    #         aggregation = cohort.new_aggregation()
    #         aggregation.preprocessing.filter(target_column=target_column, comparator=models.ComparisonType.EQUAL, value=value, nodes=nodes)
    #         survival = aggregation.get_aggregated_survival(params=self,survival_nodes=nodes)
    #         result.update({value: survival})

    #     return result
