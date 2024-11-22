"""
Classes for Hybrid Federated Learning.

🧪 This is an experimental feature. If your use case involves HybridFL on
   a large scale dataset, contact us at contact@tuneinsight.com.

🚧 This module is in active development, and likely to change dramatically in the next
   few releases. Use with caution.
"""

from typing import Optional, Dict, Union, List
from datetime import datetime
import json
from copy import deepcopy
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from tuneinsight.client.dataobject import DataContent
from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import UNSET
from tuneinsight.computations.base import ModelBasedComputation
from tuneinsight.utils import deprecation


class HybridFL(ModelBasedComputation):
    """
    Hybrid Federated Learning to train models collaboratively.

    In Hybrid Federated Learning, each party first performs local updates of a
    shared model, using their own data. Then, these models are aggregated
    together under encryption to obtain a new version of the shared model.

    All the computation and sharing is performed in the backend: this class
    only provides a high-level interface to start a computation and fetch
    results.

    This computation is configured by a data class defined by the API, that
    you should use directly.

    """

    def __init__(
        self,
        project,
        task_id: str,
        dp_epsilon: Optional[float] = UNSET,
        learning_params: models.HybridFLLearningParams = UNSET,
        task_def: Optional[Dict[str, Union[str, int, float]]] = None,
    ):
        """
        Creates a HybridFL Computation.

        Args:
            project (`Project`): The project to run the computation with.
            task_id (str): a unique identifier for this learning task.
            dp_epsilon (float, optional):
                The privacy budget to use with this workflow. Defaults to UNSET, in which case differential privacy is not used.
            learning_params (models.HybridFLLearningParams): Machine Learning specific parameters of the computation.
            task_def (dict): task definition dictionary. See documentation for more details.

        """
        super().__init__(
            project,
            models.HybridFL,
            type=models.ComputationType.HYBRIDFL,
            task_id=task_id,
            dp_epsilon=dp_epsilon,
            learning_params=learning_params,
            task_def=json.dumps(task_def) if task_def is not None else UNSET,
        )

    def create_from_params(
        self,
        task_id: str,
        learning_params: models.HybridFLLearningParams,
        task_def: Optional[Dict[str, Union[str, int, float]]] = None,
    ):
        deprecation.warn("create_from_params", "HybridFL.__init__")
        model = models.HybridFL(type=models.ComputationType.HYBRIDFL)
        model.task_id = task_id
        model.learning_params = learning_params

        if task_def is not None:
            model.task_def = json.dumps(task_def)

        model.project_id = self.project.get_id()

        dataobjects = super().run(local=False, release=False)

        return dataobjects

    @classmethod
    def from_model(cls, project: "Project", model: models.HybridFL) -> "HybridFL":
        model = models.HybridFL.from_dict(model.to_dict())
        with project.disable_patch():
            comp = cls(
                project,
                task_id=model.task_id,
                learning_params=model.learning_params,
                task_def=model.task_def,
                dp_epsilon=model.dp_epsilon,
            )
        comp._adapt(model)
        return comp

    @staticmethod
    def get_results(history, local_only=False):
        """Extracts results from a history dictionary."""
        history = deepcopy(history)
        _format_history(history)
        train_metrics = (
            history.metrics["train"] if local_only else history.init_metrics["train"]
        )
        test_metrics = (
            history.metrics["val"] if local_only else history.init_metrics["val"]
        )

        for key, value in train_metrics.items():
            train_metrics[key] = (
                round(value[-1][-1] or -1, 4)
                if local_only
                else round(value[-1] or -1, 4)
            )
        for key, value in test_metrics.items():
            test_metrics[key] = (
                round(value[-1][-1] or -1, 4)
                if local_only
                else round(value[-1] or -1, 4)
            )

        return train_metrics, test_metrics

    def display_results(self, history, local_only=False, metrics_to_display=("acc",)):
        """Displays the results of this computation, given its history."""
        history = deepcopy(history)
        _format_history(history)

        _plot_timeline(
            history, local_only=local_only, metrics_to_display=metrics_to_display
        )

    def _process_results(self, results: List[DataContent]) -> pd.DataFrame:
        return results[0].get_ml_result()


def _plot_timeline(history, local_only, metrics_to_display=("acc",)):
    n_plots = len(metrics_to_display)
    _, ax = plt.subplots(n_plots, 1, figsize=(20, 4 * n_plots))
    ax = [ax] if n_plots == 1 else ax

    last_idx = -1 if local_only else None

    init_timestamps = [x for x in history.init_timestamps if x is not None]
    start_timestamps = [x for x in history.start_timestamps if x is not None]
    end_timestamps = [x for x in history.end_timestamps if x is not None]

    init_train_metrics = history.init_metrics["train"]
    train_metrics = history.metrics["train"]
    init_test_metrics = history.init_metrics["val"]
    test_metrics = history.metrics["val"]

    agg_durations = [
        datetime.fromtimestamp(end / 1000.0)
        - datetime.fromtimestamp(starts[0] / 1000.0)
        for (starts, end) in zip(end_timestamps, init_timestamps[1:])
    ]
    local_epochs_durations = [
        datetime.fromtimestamp(ends[-1] / 1000.0)
        - datetime.fromtimestamp(start / 1000.0)
        for (start, ends) in zip(init_timestamps, end_timestamps)
    ]

    aggregation_width = 1
    epochs = [list(range(len(x) + 1)) for x in start_timestamps]

    flat_epochs = [
        x + i * (len(sublist) - 1 + aggregation_width)
        for i, sublist in enumerate(epochs)
        for x in sublist
    ]
    flat_epochs = flat_epochs + [
        flat_epochs[-1] + aggregation_width
    ]  # adds last aggregation

    x_points = flat_epochs

    merged_train_metrics = {}
    merged_test_metrics = {}
    for key in metrics_to_display:
        merged_train_metrics[key] = [
            x
            for init, sub in zip(init_train_metrics[key], train_metrics[key])
            for x in [init] + sub
        ] + [init_train_metrics[key][-1]]
        if key == "acc":
            merged_train_metrics[key] = [100 * x for x in merged_train_metrics[key]]
    for key in metrics_to_display:
        merged_test_metrics[key] = [
            x
            for init, sub in zip(init_test_metrics[key], test_metrics[key])
            for x in [init] + sub
        ] + [init_test_metrics[key][-1]]
        if key == "acc":
            merged_test_metrics[key] = [100 * x for x in merged_test_metrics[key]]

    limits = {}
    for key in metrics_to_display:
        if key == "loss":
            max_val = max(
                x or 0
                for x in merged_train_metrics[key][:last_idx]
                + merged_test_metrics[key][:last_idx]
            )
            margin = abs(max_val) * 1 / 10
            limits[key] = (-margin, max_val + margin)
        elif key == "acc":
            limits[key] = (-10, 110)
        elif key in ["f1", "auroc"]:
            limits[key] = (-0.1, 1.1)
        else:
            min_val = min(
                merged_train_metrics[key][:last_idx]
                + merged_test_metrics[key][:last_idx]
            )
            max_val = max(
                merged_train_metrics[key][:last_idx]
                + merged_test_metrics[key][:last_idx]
            )
            margin = max(abs(max_val), abs(min_val)) * 1 / 10
            limits[key] = (min_val - margin, max_val + margin)

    for i, metric in enumerate(metrics_to_display):
        _plot_axis(
            ax[i],
            x_points[:last_idx],
            merged_train_metrics[metric][:last_idx],
            merged_test_metrics[metric][:last_idx],
            limits[metric],
            epochs,
            aggregation_width,
            _format_metric_name(metric),
            local_only,
        )

    # Display time information below graph
    _add_text(
        epochs, aggregation_width, agg_durations, local_epochs_durations, local_only
    )


## Utility functions.


def _add_text(
    epochs, aggregation_width, agg_durations, local_epochs_durations, local_only
):
    text_margin = -0.2

    for i, epoch in enumerate(epochs):
        n_epochs = len(epoch) - 1
        epoch_start = i * (n_epochs + aggregation_width)
        epoch_end = i * (n_epochs + aggregation_width) + n_epochs
        epochs_list = ", ".join(
            list(map(str, range(i * n_epochs + 1, i * n_epochs + n_epochs + 1)))
        )
        text = f"Epochs {epochs_list}\n{local_epochs_durations[i].seconds} sec."
        plt.text(
            (epoch_start + epoch_end) / 2 + 0.2,
            text_margin,
            text,
            rotation=90,
            fontsize=14,
            ha="right",
            va="top",
        )

        if len(agg_durations) > i and not local_only:
            agg_start = len(epoch) - 1 + i * (len(epoch) - 1 + aggregation_width)
            agg_seconds = agg_durations[i].seconds
            text = f"Aggregation: {agg_seconds} sec."
            if agg_seconds < 2:
                agg_millis = agg_durations[i].total_seconds()
                text += f" ({agg_millis})"
            plt.text(
                agg_start + aggregation_width * 0.5,
                text_margin,
                text,
                rotation=90,
                fontsize=14,
                ha="right",
                va="top",
            )


def _plot_axis(
    axis, x, y_train, y_test, ylims, epochs, aggregation_width, label, local_only
):
    last_idx = -1 if local_only else None

    axis.set_ylim(ylims[0], ylims[1])
    axis.yaxis.tick_right()
    axis.plot(x, y_train, marker=".", label="Train")
    axis.plot(x, y_test, marker=".", label="Validation")
    axis.grid(axis="y", linewidth=0.5)
    axis.xaxis.set_major_locator(MaxNLocator(integer=True))
    axis.set_ylabel(label)
    for i, epoch in enumerate(epochs[:last_idx]):
        agg_start = len(epoch) - 1 + i * (len(epoch) - 1 + aggregation_width)
        agg_end = (i + 1) * (len(epoch) - 1 + aggregation_width)
        axis.axvspan(agg_start, agg_end, alpha=0.2, color="grey")
    axis.get_xaxis().set_ticks([])
    axis.legend()


def _format_history(history):
    metrics = {}
    for json_metrics in history.metrics:
        round_metrics = json.loads(json_metrics)
        for split, metrics_split in round_metrics.items():
            if split not in metrics:
                metrics[split] = {}
            for key, metrics_array in metrics_split.items():
                if key in metrics[split]:
                    metrics[split][key].append(metrics_array)
                else:
                    metrics[split][key] = [metrics_array]
    history.metrics = metrics

    init_metrics = {}
    for json_metrics in history.init_metrics:
        round_metrics = json.loads(json_metrics)
        for split, metrics_split in round_metrics.items():
            if split not in init_metrics:
                init_metrics[split] = {}
            for key, metrics_array in metrics_split.items():
                if key in init_metrics[split]:
                    init_metrics[split][key].append(metrics_array)
                else:
                    init_metrics[split][key] = [metrics_array]
    history.init_metrics = init_metrics


def _format_metric_name(metric_name: str) -> str:
    if metric_name == "loss":
        return "Loss"
    if metric_name == "acc":
        return "Accuracy (%)"
    if metric_name == "f1":
        return "F1-Score"
    if metric_name == "auroc":
        return "AUROC"
    return metric_name
