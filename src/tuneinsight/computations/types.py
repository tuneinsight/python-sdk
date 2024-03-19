"""
Types of computation available in the SDK.

This module is currently unused (except for one notebook), and will likely be
deprecated soon, or revamped.

"""

from enum import Enum
from tuneinsight.api.sdk.models import ComputationType as ct

from tuneinsight.utils import deprecation


class Type(Enum):
    """
    All of the exposed distributed computations types.
    """

    AGGREGATION = ct.ENCRYPTEDAGGREGATION
    REGRESSION = ct.ENCRYPTEDREGRESSION
    PREDICTION = ct.ENCRYPTEDPREDICTION
    INTERSECTION = ct.SETINTERSECTION
    STAT_AGGREGATION = ct.STATISTICALAGGREGATION
    JOIN = ct.DISTRIBUTEDJOIN
    SAMPLE_EXTRACTION = ct.SAMPLEEXTRACTION
    GWAS = ct.GWAS
    SURVIVAL_ANALYSIS = ct.SURVIVALAGGREGATION
    DATASET_STATISTICS = ct.DATASETSTATISTICS

    def to_computation_type(self) -> ct:
        # The warning is here, because putting it at top-level causes the diapason import to print a warning.
        deprecation.warn("computations.types.Type", "api.sdk.models.ComputationType")
        return ct(self.value)


displayed_types = {
    Type.AGGREGATION: "Aggregation",
    Type.REGRESSION: "Regression",
    Type.PREDICTION: "Prediction",
    Type.INTERSECTION: "Private Set Intersection",
    Type.STAT_AGGREGATION: "Statistical Aggregation",
    Type.JOIN: "Secure Join",
    Type.SAMPLE_EXTRACTION: "Sample Extraction",
    Type.GWAS: "GWAS",
    Type.SURVIVAL_ANALYSIS: "Survival Analysis",
    Type.DATASET_STATISTICS: "Secure Quantiles Computation",
}
"""Mapping from computation type to human-readable name."""
