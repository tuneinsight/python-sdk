"""Utilities for Differential Privacy post-analysis."""

from typing import List

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from tuneinsight.utils.plots import style_plot


class RatioEstimator:
    """
    Compute confidence intervals for the ratio of two values computed with differential privacy.

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
        Create simulated samples of the ratio under DP.

        Args
            numerator: the numerator of the ratio, observed with Laplace noise.
            denominator: the denominator of the ratio, observer with Laplace noise.
            noise_scale: the scale of the Laplace noise added to the numerator (and the denominator, if not specified).
            noise_scale_denominator: the scale of the Laplace noise added to the denominator (if None, noise_scale is used).
            num_samples (int, default 1e6): number of samples to use in the Monte-Carlo estimation.
        """

        laplace_noises = np.random.laplace(loc=0, scale=1, size=(2, num_samples))

        numerators = numerator + noise_scale * laplace_noises[0, :]
        if noise_scale_denominator is None:
            noise_scale_denominator = noise_scale
        denominators = denominator + noise_scale_denominator * laplace_noises[1, :]

        self.observed = numerator / denominator
        self.samples = numerators / denominators

    def confidence_intervals(self, p: List[float] = (95, 99)):
        """
        Estimate confidence intervals for the ratio.

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

    def draw_distribution(self, ci_color="k"):
        """Display the shape of this distribution in a matplotlib figure.

        Args
            ci_color: if not None, the 95% and 99% confidence intervals are displayed in this color.

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
        )
