"""Utilities for Differential Privacy post-analysis."""

from typing import List

from typing import Callable

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from tuneinsight.utils.plots import style_plot


# TO DO: use noise scales from results metadata.


class ConfidenceIntervalEstimator:
    """
    Computes confidence intervals for a function of Differentially Private outputs.

    This uses Monte-Carlo sampling to simulate multiple runs of the Laplace mechanism
    on a multi-dimensional query that is then aggregated to one number using an
    arbitrary function.

    This assumes that the outputs are computed with Laplace noise.
    """

    def __init__(
        self,
        noisy_answers: np.array,
        noise_scales: np.array,
        function: Callable[[np.array], float],
        num_samples: int = int(1e6),
    ):
        """
        Creates simulated samples of a function of the outputs of the Laplace mechanism.

        Args
            noisy_answers (np.array): the observed output of the mechanism, typically the
                result of several queries with added noise.
            noise_scales (np.array): the scale of the noise added on each answer. If an array
                of length 1 is provided, the noise is assumed to be of the same scale on each.
            function: a callable function that maps an array of answers to a single float. The
                input array will be one-dimensional.
            num_samples (int, default 1e6): number of samples to use in Monte-Carlo estimation.
                Only change this number if the code takes too long to run.
        """
        # Convert the inputs to 1-dimensional arrays of same dimension (hopefully).
        noisy_answers = np.array(noisy_answers).flatten()
        noise_scales = np.array(noise_scales).flatten()
        if len(noise_scales) == 1:
            noise_scales = np.full(noisy_answers.shape, noise_scales[0])
        assert (
            noise_scales.shape == noisy_answers.shape
        ), "Mismatching input dimensions for noise_scales and noisy_answers."
        # Simulate the Laplace mechanism multiple times.
        laplace_noises = np.random.laplace(
            loc=0, scale=noise_scales, size=(num_samples, len(noise_scales))
        )
        samples = np.tile(noisy_answers, (num_samples, 1)) + laplace_noises
        # Compute the function on each of these samples.
        self.observed = function(noisy_answers)
        self.samples = np.array([function(row) for row in samples])

    def confidence_intervals(self, p: List[float] = (95, 99)):
        """
        Estimates confidence intervals for the function result.

        Args
            p: the probabilities of the confidence interval (in percentages, in [0, 100]).
        """
        results = []
        for perc in p:
            d = (
                100 - perc
            ) / 2  # The fraction to "remove" on either side of the interval.
            v_low, v_hi = np.percentile(self.samples, [d, (100 - d)])
            results.append([perc, v_low, v_hi])

        return pd.DataFrame(results, columns=["Percentage", "CI (min)", "CI (max)"])

    def draw_distribution(self, ci_color="k", local=False):
        """
        Displays the shape of the distribution of function results in a matplotlib figure.

        Args
            ci_color: if not None, the 95% and 99% confidence intervals are displayed in this color.
            local: whether the results are from a local or collective computation.

        """
        plt.style.use("bmh")
        fig, axis = plt.subplots()

        # Extract a normalizes histogram.
        hist, bin_edges = np.histogram(self.samples, bins=100)
        hist_norm = hist / hist.sum()
        bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
        bin_width = bin_edges[1:] - bin_edges[:-1]
        # Several plots for good effects.
        max_height = hist_norm.max()
        axis.bar(
            bin_centers,
            hist_norm,
            width=bin_width,
            alpha=0.8,
            color="#D05F5C",
            edgecolor="black",
        )
        axis.plot(
            [self.observed, self.observed],
            [0, 1.2 * max_height],
            "k--",
            lw=1,
            alpha=0.8,
        )
        # Plot confidence intervals.
        if ci_color is not None:
            for p, w in zip([95, 99], [0.1, 0.05]):
                ci = self.confidence_intervals([p]).iloc[0]
                cmin = ci["CI (min)"]
                cmax = ci["CI (max)"]
                axis.plot([cmin] * 2, [0, w * max_height], c=ci_color)
                axis.plot([cmax] * 2, [0, w * max_height], c=ci_color)
                axis.plot(
                    [cmin, cmax], [0.99 * w * max_height] * 2, c=ci_color, alpha=0.3
                )
                axis.text(cmax, w * max_height * 1.1, f"{p}%  ")
        # Adjust visibility window.
        plt.xlim([bin_edges.min(), bin_edges.max()])
        plt.ylim([0, 1.2 * max_height])

        style_plot(
            axis,
            fig,
            title="Distribution of true values",
            x_label="Possible values",
            y_label="Likelihood",
            size=(8, 6),
            local=local,
        )


class RatioEstimator(ConfidenceIntervalEstimator):
    """
    Computes confidence intervals for the ratio of two values computed with differential privacy.

    This class uses simulated samples to estimate various properties of the observed values.

    """

    def __init__(
        self,
        numerator: float,
        denominator: float,
        noise_scale: float,
        noise_scale_denominator: float = None,
        num_samples: int = int(1e6),
    ):
        """
        Createds simulated samples of the ratio under DP.

        Args
            numerator: the numerator of the ratio, observed with Laplace noise.
            denominator: the denominator of the ratio, observer with Laplace noise.
            noise_scale: the scale of the Laplace noise added to the numerator (and the denominator, if not specified).
            noise_scale_denominator: the scale of the Laplace noise added to the denominator (if None, noise_scale is used).
            num_samples (int, default 1e6): number of samples to use in the Monte-Carlo estimation.
        """
        noise_scales = [noise_scale]
        if noise_scale_denominator is not None:
            noise_scales.append(noise_scale_denominator)
        super().__init__(
            [numerator, denominator], noise_scales, lambda x: x[0] / x[1], num_samples
        )


class CountEstimator(ConfidenceIntervalEstimator):
    """Confidence intervals for a counting query."""

    def __init__(self, noisy_count: float, noise_scale: float):
        """
        Args
            noisy_count (float): the observed noisy count.
            noise_scale (float): the scale of the Laplace noise added to the count.
        """
        super().__init__([noisy_count], [noise_scale], lambda x: x[0])
