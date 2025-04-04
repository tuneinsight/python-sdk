"""Module accessing the utilities in the cryptolib dedicated to post-processing results."""

import ctypes
from io import StringIO
import json
import math
from typing import List
import pandas as pd

from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import is_unset

from .cryptolib import so, LOADED


def post_process_survival(results: pd.DataFrame) -> pd.DataFrame:
    """
    Post-processes noisy results from a survival analysis with differential privacy.

    The output of the post-processing uses only nonnegative integer values, and leads
    to a nonincreasing Kaplan-Meier curve. Both input and output should be Pandas
    DataFrame extracted from the FloatMatrix result of a survival computation.

    Fails gracefully: if the cryptolib could not load, this returns the input unchanged.

    """
    if not LOADED:
        return results
    csv_data = results.to_csv(index=False).encode("UTF-8")
    post_process = so.PostProcessSurvivalDP
    post_process.restype = ctypes.c_char_p
    csv_result = post_process(csv_data)
    csv_result = csv_result.decode("utf8")
    return pd.read_csv(StringIO(csv_result), names=results.columns)


def kaplan_meier_confidence_interval(
    results: pd.DataFrame, epsilon: float
) -> pd.DataFrame:
    """
    Estimates the 95%-confidence interval of the Kaplan-Meier curve for each group of a survival analysis.

    Args:
        results (pd.DataFrame): the results of a survival analysis (noisy frames data).
        epsilon (float): the epsilon privacy parameter used to compute the results.

    """
    csv_data = results.to_csv(index=False).encode("UTF-8")
    estimate = so.KaplanMeierConfidenceInterval
    estimate.restype = ctypes.c_char_p
    csv_result = estimate(csv_data, str(epsilon).encode("UTF-8"))
    csv_result = csv_result.decode("utf8")
    return pd.read_csv(StringIO(csv_result), header=None)


def post_process_statistics(
    comp: models.DatasetStatistics, results: List[List[float]]
) -> models.Statistics:
    """
    Post-processes the raw results of a statistics computation under differential privacy.

    Args:
        comp (models.DatasetStatistics): the computation definition.
        results (pd.DataFrame): the raw results (a list of aggregated values).

    Returns:
        models.Statistics: A DataContent of the right type.
    """
    csv_data = ",".join([str(x) for x in results[0]])
    post_process = so.PostProcessStatistics
    post_process.restype = ctypes.c_char_p
    json_result = post_process(csv_data.encode("UTF-8"))
    results = []
    for i, stat in enumerate(json.loads(json_result)):
        stat_def = comp.statistics[i]
        stat_result = models.StatisticResult.from_dict(stat_def.to_dict())
        use_default = is_unset(stat_def.quantities) or len(stat_def.quantities) < 1
        if use_default or models.StatisticalQuantity.MEAN in stat_def.quantities:
            stat_result.mean = stat["mean"]
        if use_default or models.StatisticalQuantity.VARIANCE in stat_def.quantities:
            stat_result.variance = stat["variance"]
            stat_result.stddev = math.sqrt(stat_result.variance)
        results.append(stat_result)
    return models.Statistics(
        type=models.ContentType.STATISTICS, results=results, raw_dp_results=results[0]
    )


def statistics_confidence_interval(
    comp: models.DatasetStatistics,
    raw_results: List[List[float]],
    noise_parameters: models.ResultMetadata,
) -> pd.DataFrame:
    """Estimates 95% confidence intervals on the mean and variance computed with differential privacy.

    Args:
        comp (models.DatasetStatistics): the computation definition.
        raw_results (List[List[float]]): the raw results (a list of aggregated values).
        noise_parameters (models.ResultMetadata): the metadata on the noise added to each result.
    """
    csv_data = ",".join([str(x) for x in raw_results[0]])
    # Flatten the noise parameters to a single matrix.
    if is_unset(noise_parameters.dp_noise):
        raise ValueError("No DP noise metadata available.")
    dp_metadata: List[List[float]] = []
    # Concatenate the scaling matrices for the noise added to the different variables.
    for metadata in noise_parameters.dp_noise:
        if is_unset(metadata.sum_parameters):
            continue
        # Noise on [count, sum, sum_squares]
        dp_metadata += metadata.sum_parameters
    csv_metadata = ",".join([str(x) for x in dp_metadata])
    estimate = so.StatisticsConfidenceInterval
    estimate.restype = ctypes.c_char_p
    csv_result = estimate(csv_data.encode("utf-8"), csv_metadata.encode("utf-8"))
    # Parse the result:
    csv_result = csv_result.decode("utf8")
    matrix = pd.read_csv(StringIO(csv_result), header=None).values
    columns = ["variable", "name", "quantity", "min", "max"]
    results = []
    for i, stat_def in enumerate(comp.statistics):
        stat_def: models.StatisticDefinition
        header = (stat_def.name, stat_def.variable)
        use_default = is_unset(stat_def.quantities) or len(stat_def.quantities) < 1
        if use_default or models.StatisticalQuantity.MEAN in stat_def.quantities:
            results.append(header + ("mean",) + tuple(matrix[2 * i, :]))
        if use_default or models.StatisticalQuantity.VARIANCE in stat_def.quantities:
            results.append(header + ("variance",) + tuple(matrix[2 * i + 1, :]))
    return pd.DataFrame(results, columns=columns)
