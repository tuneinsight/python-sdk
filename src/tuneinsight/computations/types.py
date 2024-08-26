"""
Types of computation available in the SDK.

This module defines wrappers for the API computation types, including human-friendly computation names.

"""

from enum import Enum
from tuneinsight.api.sdk.models import ComputationType as ct

from tuneinsight.computations import (
    Aggregation,
    DatasetLength,
    EncryptedMean,
    Matching,
    GWAS,
    SurvivalAnalysis,
    Statistics,
)


class Type(Enum):
    """
    All of the exposed distributed computations types.
    """

    AGGREGATION = ct.ENCRYPTEDAGGREGATION
    DATASETLENGTH = ct.AGGREGATEDDATASETLENGTH
    MEAN = ct.ENCRYPTEDMEAN
    REGRESSION = ct.ENCRYPTEDREGRESSION
    PREDICTION = ct.ENCRYPTEDPREDICTION
    INTERSECTION = ct.SETINTERSECTION
    GWAS = ct.GWAS
    SURVIVAL_ANALYSIS = ct.SURVIVALAGGREGATION
    DATASET_STATISTICS = ct.DATASETSTATISTICS

    def to_computation_type(self) -> ct:
        # The warning is here, because putting it at top-level causes the diapason import to print a warning.
        return ct(self.value)


displayed_types = {
    Type.AGGREGATION: "Aggregation",
    Type.DATASETLENGTH: "Dataset Length",
    Type.MEAN: "Mean",
    Type.REGRESSION: "Regression",
    Type.PREDICTION: "Prediction",
    Type.INTERSECTION: "Private Set Intersection",
    Type.GWAS: "GWAS",
    Type.SURVIVAL_ANALYSIS: "Survival Analysis",
    Type.DATASET_STATISTICS: "Secure Quantiles Computation",
}
"""Mapping from computation type to human-readable name."""


type_to_class = {
    Type.AGGREGATION: Aggregation,
    Type.DATASETLENGTH: DatasetLength,
    Type.MEAN: EncryptedMean,
    Type.INTERSECTION: Matching,
    Type.GWAS: GWAS,
    Type.SURVIVAL_ANALYSIS: SurvivalAnalysis,
    Type.DATASET_STATISTICS: Statistics,
}
"""Mapping from computation type to SDK class."""


# pylint: disable=raise-missing-from
def model_type_to_class(model_type: ct):
    """Maps an API model type to a Computation class."""
    try:
        return type_to_class[Type(model_type)]
    except ValueError:
        raise ValueError(f"Unknown computation type: {model_type}")
    except KeyError:
        raise ValueError(
            f"Cannot fetch backend computation for type {Type(model_type)}."
        )
