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
    HybridFL,
    Matching,
    GWAS,
    SurvivalAnalysis,
    Statistics,
    Feasibility,
)


class Type(Enum):
    """
    All of the exposed distributed computations types.
    """

    AGGREGATION = ct.ENCRYPTEDAGGREGATION
    DATASETLENGTH = ct.AGGREGATEDDATASETLENGTH
    HYBRIDFL = ct.HYBRIDFL
    MEAN = ct.ENCRYPTEDMEAN
    REGRESSION = ct.ENCRYPTEDREGRESSION
    PREDICTION = ct.ENCRYPTEDPREDICTION
    INTERSECTION = ct.SETINTERSECTION
    GWAS = ct.GWAS
    SURVIVAL_ANALYSIS = ct.SURVIVALAGGREGATION
    DATASET_STATISTICS = ct.DATASETSTATISTICS
    FEASIBILITY = ct.FEASIBILITY

    def to_computation_type(self) -> ct:
        # The warning is here, because putting it at top-level causes the diapason import to print a warning.
        return ct(self.value)


displayed_types = {
    Type.AGGREGATION: "Aggregation",
    Type.DATASETLENGTH: "Dataset Length",
    Type.HYBRIDFL: "Hybrid Federated Learning",
    Type.MEAN: "Mean",
    Type.REGRESSION: "Regression",
    Type.PREDICTION: "Prediction",
    Type.INTERSECTION: "Private Set Intersection",
    Type.GWAS: "GWAS",
    Type.SURVIVAL_ANALYSIS: "Survival Analysis",
    Type.DATASET_STATISTICS: "Secure Quantiles Computation",
    Type.FEASIBILITY: "Feasibility",
}
"""Mapping from computation type to human-readable name."""


type_to_class = {
    Type.AGGREGATION: Aggregation,
    Type.DATASETLENGTH: DatasetLength,
    Type.HYBRIDFL: HybridFL,
    Type.MEAN: EncryptedMean,
    Type.INTERSECTION: Matching,
    Type.GWAS: GWAS,
    Type.SURVIVAL_ANALYSIS: SurvivalAnalysis,
    Type.DATASET_STATISTICS: Statistics,
    Type.FEASIBILITY: Feasibility,
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
