"""Utilities for benchmarking memory usage of and time taken by computations."""

from typing import List, Any, Dict, Tuple
from dateutil.parser import parse

import numpy as np
import matplotlib.pyplot as plt

from tuneinsight.api.sdk import models
from tuneinsight.utils import time_tools
from tuneinsight.utils.plots import style_title, style_suptitle


BIT = 1
BYTE = 8 * BIT
KILOBIT = 1024 * BIT
KILOBYTE = 1024 * BYTE
MEGABIT = 1024 * KILOBIT
MEGABYTE = 1024 * KILOBYTE
GIGABIT = 1024 * MEGABIT
GIGABYTE = 1024 * MEGABYTE

net_labels = {
    BIT: "b",
    BYTE: "B",
    KILOBIT: "Kb",
    KILOBYTE: "KB",
    MEGABIT: "Mb",
    MEGABYTE: "MB",
    GIGABIT: "Gb",
    GIGABYTE: "GB",
}

time_labels = {
    time_tools.MICROSECOND: "μs",
    time_tools.MILLISECOND: "ms",
    time_tools.SECOND: "s",
    time_tools.MINUTE: "min",
    time_tools.HOUR: "hour",
    time_tools.DAY: "day",
}


def get_total_time(comp: models.Computation) -> int:
    """
    Computes the total running time of the computation in microseconds.

    Args:
        comp (models.Computation): the computation schema returned by the agent

    Returns:
        int: the total running times in microseconds
    """
    start = parse(comp.started_at)
    end = parse(comp.ended_at)
    diff = end - start
    return int(round((diff).total_seconds() * time_tools.SECOND))


def get_total_communication(comp: models.Computation) -> int:
    """
    Returns the total egress plus ingress communication of the computation.

    This is recorded from the point of view of the node that returned the provided schema.

    Args:
        comp (models.Computation): the computation schema returned by the agent

    Returns:
        int: the total recorded communication in bits
    """
    return comp.egress * BYTE + comp.ingress * BYTE


def plot_benchmarks(
    x_values: List[Any],
    times: Dict[str, np.ndarray],
    nets: Dict[str, np.ndarray],
    time_unit: int = time_tools.MILLISECOND,
    net_unit: int = KILOBYTE,
    title: str = "",
    markers="",
    x_label="",
):
    """
    Plots the results of a benchmark.

    This uses matplotlib to draw the evolution of computation time and communication
    egress and ingress as a function of a free variable.

    Args:
        x_values (List[Any]): the x-axis variables/settings
        times (Dict[str,np.ndarray]): the benchmarked times, expects a dictionary from
            computation type to numpy array storing the time values for each x value.
        nets (Dict[str,np.ndarray]): the benchmarked communications, expects a dictionary
            from computation type to numpy array storing the communication values for each x value.
        time_unit (int, optional): the time unit used. Defaults to time_tools.second.
        net_unit (int, optional): the communication size unit used. Defaults to kilobyte.
        title (str, optional): optional title to provide to the plot. Defaults to "".
        markers (str, optional): optional marker values for plot points. Defaults to "".
    """
    fig, ax = plt.subplots(1, 2)
    style_suptitle(fig, title=title, fontsize=18)
    fig.tight_layout()
    for label in times.keys():
        ax[0].plot(x_values, times[label], label=label, marker=markers)
        ax[1].plot(x_values, nets[label], label=label, marker=markers)
        ax[1].set_ylabel(f"total communication ({net_labels[net_unit]})")
        ax[1].set_xlabel(x_label)
    style_title(ax[0], title=f"Time ({time_labels[time_unit]})")
    style_title(ax[1], title=f"Communication Cost ({net_labels[net_unit]})")
    plt.legend()
    plt.show()


def average_benchmarks(vals: List[Dict[str, np.ndarray]]) -> Dict[str, np.ndarray]:
    """
    Averages a list of benchmark values.

    Args:
        vals (List[Dict[str,np.ndarray]]): a list of benchmarks, expected to be a
            dictionary from computation type to numpy array of recorded values.

    Returns:
        Dict[str,np.ndarray]: the dictionary that averages the list given as argument
    """
    result = {}
    for benchmarks in vals:
        for key, values in benchmarks.items():
            if key not in result:
                result[key] = values
            else:
                result[key] += values
    final_res = result.copy()
    for k, v in result.items():
        final_res[k] = v / len(vals)
    return final_res


def compute_benchmarks(
    x_values: List[Any],
    recordings: List[List[models.Computation]],
    time_unit: int = time_tools.MILLISECOND,
    net_unit: int = KILOBYTE,
) -> Tuple[Dict[str, np.ndarray], Dict[str, np.ndarray]]:
    """
    Computes the time/communication benchmarking results of a set of computations.

    Args:
        x_values (List[Any]): the x axis values/settings used for the benchmarks
        recordings (List[List[models.Computation]]): the list of recordings with
            len(x_values) items (the list of recorded computations for each setting).
        time_unit (int, optional): the time unit to use for the benchmarking.
            Defaults to time_tools.second.
        net_unit (int, optional): the communication size unit to use for the benchmarking.
            Defaults to kilobyte.

    Returns:
        Tuple[Dict[str,np.ndarray],Dict[str,np.ndarray]]: a tuple (T,N) where T is the timings
            for each computation types and N is the communications for each computation types
    """
    all_comp_types = set()
    for recording in recordings:
        for computation in recording:
            all_comp_types.add(str(computation.definition.type))
    times = {}
    nets = {}
    for comp in all_comp_types:
        times[comp] = np.zeros(len(x_values))
        nets[comp] = np.zeros(len(x_values))
    total_time = np.zeros(len(x_values))
    total_net = np.zeros(len(x_values))
    for i, recording in enumerate(recordings):
        for comp in recording:
            time = get_total_time(comp) / time_unit
            net = get_total_communication(comp) / net_unit
            times[str(comp.definition.type)][i] = time
            total_time[i] += time
            nets[str(comp.definition.type)][i] = net
            total_net[i] += net
    times["total"] = total_time
    nets["total"] = total_net
    return times, nets
