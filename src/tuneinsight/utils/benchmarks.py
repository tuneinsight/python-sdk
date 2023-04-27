from typing import List,Any,Dict,Tuple
from dateutil.parser import parse

import numpy as np
import matplotlib.pyplot as plt

from tuneinsight.api.sdk import models
from tuneinsight.utils import time_tools
from tuneinsight.utils.plots import style_title, style_suptitle



bit = 1
byte = 8 * bit
kilobit = 1024 * bit
kilobyte = 1024 * byte
megabit = 1024 * kilobit
megabyte = 1024 * kilobyte
gigabit = 1024 * megabit
gigabyte = 1024 * megabyte

net_labels = {
    bit: "b",
    byte: 'B',
    kilobit: 'Kb',
    kilobyte: 'KB',
    megabit: 'Mb',
    megabyte: 'MB',
    gigabit: 'Gb',
    gigabyte: 'GB',
}

time_labels = {
    time_tools.microsecond: 'μs',
    time_tools.millisecond: 'ms',
    time_tools.second: 's',
    time_tools.minute: 'min',
    time_tools.hour: 'hour',
    time_tools.day: 'day',
}


def get_total_time(comp: models.Computation) -> int:
    '''
    get_total_time returns the total running time of the computation in microseconds

    Args:
        comp (models.Computation): the computation schema returned by the agent

    Returns:
        int: the total running times in microseconds
    '''
    start = parse(comp.started_at)
    end = parse(comp.ended_at)
    diff = end - start
    return int(round((diff).total_seconds() * time_tools.second))


def get_total_communication(comp: models.Computation) ->int:
    '''
    get_total_communication returns the total egress + ingress communication of the computation (recorded from the point of view of the node that returned the provided schema)

    Args:
        comp (models.Computation): the computation schema returned by the agent

    Returns:
        int: the total recorded communication in bits
    '''
    return comp.egress * byte + comp.ingress * byte


def plot_benchmarks(x_values: List[Any],times: Dict[str,np.ndarray],nets: Dict[str,np.ndarray],time_unit: int = time_tools.millisecond,net_unit: int = kilobyte,title:str = "",markers="",x_label=""):
    '''
    plot_benchmarks plots the benchmarks results

    Args:
        x_values (List[Any]): the x-axis variables/settings
        times (Dict[str,np.ndarray]): the benchmarked times, expects a dictionary from computation type to numpy array storing the time values for each x value
        nets (Dict[str,np.ndarray]): the benchmarked communications, expects a dictionary from computation type to numpy array storing the communication values for each x value
        time_unit (int, optional): the time unit used. Defaults to time_tools.second.
        net_unit (int, optional): the communication size unit used. Defaults to kilobyte.
        title (str, optional): optional title to provide to the plot. Defaults to "".
        markers (str, optional): optional marker values for plot points. Defaults to "".
    '''
    fig, ax = plt.subplots(1, 2)
    style_suptitle(fig,title=title,fontsize=18)
    fig.tight_layout()
    for label in times.keys():
        ax[0].plot(x_values,times[label],label=label,marker=markers)
        ax[1].plot(x_values,nets[label],label=label,marker=markers)
        ax[1].set_ylabel(f'total communication ({net_labels[net_unit]})')
        ax[1].set_xlabel(x_label)
    style_title(ax[0], title=f"Time ({time_labels[time_unit]})")
    style_title(ax[1], title=f"Communication Cost ({net_labels[net_unit]})")
    plt.legend()
    plt.show()


def average_benchmarks(vals: List[Dict[str,np.ndarray]]) ->Dict[str,np.ndarray]:
    '''
    average_benchmarks averages a list of benchmark values

    Args:
        vals (List[Dict[str,np.ndarray]]): a list of benchmarks, expected to be a dictionary from computation type to numpy array of recorded values

    Returns:
        Dict[str,np.ndarray]: the dictionary that averages the list given as argument
    '''
    result = {}
    for benchmarks in vals:
        for key,values in benchmarks.items():
            if key not in result:
                result[key] = values
            else:
                result[key] += values
    for k in result:
        result[k] = result[k] / len(vals)
    return result



def compute_benchmarks(x_values: List[Any],recordings: List[List[models.Computation]],time_unit: int = time_tools.millisecond,net_unit: int = kilobyte) -> Tuple[Dict[str,np.ndarray],Dict[str,np.ndarray]]:
    '''
    compute_benchmarks computes the time/communication benchmarking results given a set of computation recordings

    Args:
        x_values (List[Any]): the x axis values/settings used for the benchmarks
        recordings (List[List[models.Computation]]): the list of recordings with len(x_values) items (the list of recorded computations for each setting)
        time_unit (int, optional): the time unit to use for the benchmarking. Defaults to time_tools.second.
        net_unit (int, optional): the communication size unit to use for the benchmarking. Defaults to kilobyte.

    Returns:
        Tuple[Dict[str,np.ndarray],Dict[str,np.ndarray]]: a tuple (T,N) where T is the timings for each computation types and N is the communications for each computation types
    '''
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
    for i,recording in enumerate(recordings):
        for comp in recording:
            time = get_total_time(comp) / time_unit
            net = get_total_communication(comp) / net_unit
            times[str(comp.definition.type)][i] = time
            total_time[i] += time
            nets[str(comp.definition.type)][i] = net
            total_net[i] += net
    times['total'] = total_time
    nets['total'] = total_net
    return times,nets
