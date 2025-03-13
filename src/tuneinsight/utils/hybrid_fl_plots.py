""" Plotting functions for hybrid federated learning metrics. """

from datetime import datetime
import matplotlib.pyplot as plt

from tuneinsight.utils.plots import (
    style_plot,
    style_suptitle,
    add_branded_text,
    TI_COLORS,
    FONT_LIGHT,
)


LIMITS = {
    "acc": (0, 110),
    "loss": (None, None),
    "f1": (0, 1.1),
    "auroc": (0, 1.1),
}


def plot_timeline(history, local_only, metrics_to_display=("acc",)):
    """
    Plot a timeline of training and validation metrics over epochs
    with Tune Insight branding.

    Parameters:
        history: object with required attributes:
            - init_timestamps
            - start_timestamps
            - end_timestamps
            - init_metrics (dict of metrics at initialization)
            - metrics (dict of metrics over epochs)
        local_only: bool, whether to exclude global aggregation results.
        metrics_to_display: tuple of str, metrics to plot (e.g., ("acc", "loss")).
    """

    # set grid background color to white
    plt.style.use("bmh")
    plt.rcParams.update({"axes.facecolor": "white", "figure.facecolor": "white"})

    # Determine last index based on local_only
    last_idx = -1 if local_only else None

    # Extract timestamps and metrics
    init_timestamps, start_timestamps, end_timestamps = _filter_none_timestamps(history)
    init_train_metrics, init_test_metrics, train_metrics, test_metrics = (
        _extract_metrics(history)
    )

    # Compute durations and epochs indexes
    agg_durations, local_epochs_durations = _compute_durations(
        init_timestamps, end_timestamps
    )
    epochs, x_points, aggregation_width = _compute_epochs_xpoints(start_timestamps)

    # Merge metrics
    merged_train_metrics, merged_test_metrics = _merge_metrics(
        init_train_metrics,
        train_metrics,
        init_test_metrics,
        test_metrics,
        metrics_to_display,
    )

    # Compute y-axis limits for each metric
    limits = _compute_metric_limits(
        merged_train_metrics, merged_test_metrics, metrics_to_display, last_idx
    )

    # Plot each metric
    for metric in metrics_to_display:
        fig = plt.figure()  # Optional: specify figure size
        ax = plt.gca()
        # Plot the metric
        _plot_metric_with_branding(
            fig,
            ax,
            metric,
            x_points[:last_idx],
            merged_train_metrics[metric][:last_idx],
            merged_test_metrics[metric][:last_idx],
            limits[metric],
            epochs,
            aggregation_width,
            local_only,
        )
        # Add text about epochs and aggregation durations
        _add_agg_durations(
            ax,
            epochs,
            aggregation_width,
            agg_durations,
            local_epochs_durations,
            local_only,
        )
        plt.show()


def _prepare_figure_axes(metrics_to_display):
    """
    Prepare figure and axes for the given number of metrics.
    This function may be used in the case we want to have multiple metrics in the same figure.
    But that would require smart adjustments to the plot and font sizes.
    """
    n_plots = len(metrics_to_display)
    fig, ax = plt.subplots(n_plots, 1, figsize=(15, 4 * n_plots))

    ## Add grid to all axes
    ax = [ax] if n_plots == 1 else ax
    # Style the figure title with branding
    style_suptitle(fig, title="Training and Validation Metrics")
    return fig, ax


def _filter_none_timestamps(history):
    """
    Filter out None values from timestamps.
    """
    init_timestamps = [ts for ts in history.init_timestamps if ts is not None]
    start_timestamps = [ts for ts in history.start_timestamps if ts is not None]
    end_timestamps = [ts for ts in history.end_timestamps if ts is not None]
    return init_timestamps, start_timestamps, end_timestamps


def _extract_metrics(history):
    """
    Extract train and test metrics from history.
    """
    init_train_metrics = history.init_metrics["train"]
    train_metrics = history.metrics["train"]
    init_test_metrics = history.init_metrics["val"]
    test_metrics = history.metrics["val"]
    return init_train_metrics, init_test_metrics, train_metrics, test_metrics


def _compute_durations(init_timestamps, end_timestamps):
    """
    Compute aggregation durations and local epoch durations.
    """
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
    return agg_durations, local_epochs_durations


def _compute_epochs_xpoints(start_timestamps):
    """
    Compute the epochs structure and corresponding x points for the plot.
    """
    aggregation_width = 1
    epochs = [list(range(len(x) + 1)) for x in start_timestamps]

    flat_epochs = [
        x + i * (len(sublist) - 1 + aggregation_width)
        for i, sublist in enumerate(epochs)
        for x in sublist
    ]
    flat_epochs.append(flat_epochs[-1] + aggregation_width)  # Add last aggregation

    return epochs, flat_epochs, aggregation_width


def _merge_metrics(
    init_train_metrics,
    train_metrics,
    init_test_metrics,
    test_metrics,
    metrics_to_display,
):
    """
    Merge initial and epoch-wise metrics into a single list for train and test.
    """
    merged_train_metrics = {}
    merged_test_metrics = {}

    for key in metrics_to_display:
        merged_train_metrics[key] = [
            x
            for init, sub in zip(init_train_metrics[key], train_metrics[key])
            for x in [init] + sub
        ] + [init_train_metrics[key][-1]]

        merged_test_metrics[key] = [
            x
            for init, sub in zip(init_test_metrics[key], test_metrics[key])
            for x in [init] + sub
        ] + [init_test_metrics[key][-1]]

        if key == "acc":
            merged_train_metrics[key] = [100 * x for x in merged_train_metrics[key]]
            merged_test_metrics[key] = [100 * x for x in merged_test_metrics[key]]

    return merged_train_metrics, merged_test_metrics


def _compute_metric_limits(
    merged_train_metrics, merged_test_metrics, metrics_to_display, last_idx
):
    """
    Compute y-limits for each metric plot.
    """
    limits = {}
    for key in metrics_to_display:
        all_values = (
            merged_train_metrics[key][:last_idx] + merged_test_metrics[key][:last_idx]
        )

        if key == "loss":
            max_val = max((x or 0) for x in all_values)
            margin = abs(max_val) * 0.1
            limits[key] = (-margin, max_val + margin)

        elif key in LIMITS:
            limits[key] = LIMITS[key]

        else:
            min_val = min(all_values)
            max_val = max(all_values)
            margin = max(abs(max_val), abs(min_val)) * 0.1
            limits[key] = (min_val - margin, max_val + margin)

    return limits


def _plot_metric_with_branding(
    fig,
    axis,
    metric,
    x_points,
    y_train,
    y_test,
    ylims,
    epochs,
    aggregation_width,
    local_only,
):
    """
    Plot a single metric with Tune Insight branding.
    """
    axis.set_ylim(ylims[0], ylims[1])
    axis.plot(x_points, y_train, marker=".", label="Train", color=TI_COLORS[0])
    axis.plot(x_points, y_test, marker=".", label="Validation", color=TI_COLORS[1])

    last_idx = -1 if local_only else None

    for i, epoch in enumerate(epochs[:last_idx]):
        agg_start = len(epoch) - 1 + i * (len(epoch) - 1 + aggregation_width)
        agg_end = (i + 1) * (len(epoch) - 1 + aggregation_width)
        axis.axvspan(agg_start, agg_end, alpha=0.2, color="grey")

    style_plot(
        axis=axis,
        fig=fig,
        title=f"{_format_metric_name(metric)}",
        x_label=None,
        y_label=_format_metric_name(metric),
        size=(12, 6),
        local=local_only,
    )
    # set grid to true
    axis.grid(True)

    # build x ticks label array
    x_ticks = []
    x_labels = []
    for i, epoch in enumerate(epochs):
        epoch_start = i * (len(epoch) - 1 + aggregation_width)
        agg_start = len(epoch) - 1 + i * (len(epoch) - 1 + aggregation_width)
        agg_end = (i + 1) * (len(epoch) - 1 + aggregation_width)
        for j in range(len(epoch)):
            x_ticks.append(epoch_start + j + 0.5)
            x_labels.append(f"Epoch {i * len(epoch) + j + 1}")
        if not local_only:
            x_ticks.append((agg_start + agg_end) / 2)
            x_labels.append(f"Agg {i + 1}")

    axis.set_xticks(x_ticks, minor=True)
    axis.set_xticklabels(
        x_labels, rotation=25, minor=True, fontdict={"font": FONT_LIGHT, "fontsize": 8}
    )
    axis.set_xticks([], minor=False)
    axis.set_xticklabels([], minor=False)
    axis.tick_params(axis="x", which="both", length=0)  # Set tick length to 0

    # Add legend
    axis.legend(loc="upper right", fontsize=10)


def _add_agg_durations(
    ax, epochs, aggregation_width, agg_durations, local_epochs_durations, local_only
):
    """
    Add textual information about epochs and aggregation durations above the plots.
    """
    aggregation_width = 1
    for i, epoch in enumerate(epochs):
        n_epochs = len(epoch) - 1
        epoch_start = i * (n_epochs + aggregation_width)
        epoch_end = i * (n_epochs + aggregation_width) + n_epochs
        agg_start = len(epoch) - 1 + i * (len(epoch) - 1 + aggregation_width)
        agg_end = (i + 1) * (len(epoch) - 1 + aggregation_width)
        # Find the y position for the text under/ above the x-axis
        y0, y1 = ax.get_ylim()
        y1 = y1 - 0.025 * (y1 - y0)

        # Add epoch durations
        if i < len(local_epochs_durations):
            epoch_duration = local_epochs_durations[i]
            add_branded_text(
                ax,
                f"{epoch_duration} s",
                x=(epoch_start + epoch_end) / 2,
                y=y1,
                fontsize=8,
            )

        # Add aggregation durations
        if not local_only and i < len(agg_durations):
            agg_duration = agg_durations[i]
            add_branded_text(
                ax, f"{agg_duration} s", x=(agg_start + agg_end) / 2, y=y1, fontsize=8
            )


def _format_metric_name(metric_name):
    """
    Format metric names for display in the plot's y-label.
    """
    name_map = {
        "acc": "Accuracy",
        "loss": "Loss",
        "f1": "F1 Score",
        "auroc": "AUROC",
        "modularity": "Modularity",
    }
    return name_map.get(metric_name, metric_name.capitalize())
