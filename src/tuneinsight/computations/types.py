"""
Types of computation available in the SDK.

This module defines wrappers for the API computation types, including human-friendly computation names.

"""

from enum import Enum
from tuneinsight.api.sdk.models import ComputationType as ct

from tuneinsight.computations import (
    Aggregation,
    DatasetLength,
    Distribution,
    EncryptedMean,
    Feasibility,
    GWAS,
    HybridFL,
    Matching,
    Statistics,
    SurvivalAnalysis,
)


class Type(Enum):
    """
    All of the exposed distributed computations types.
    """

    AGGREGATION = ct.ENCRYPTEDAGGREGATION
    DATASET_LENGTH = ct.AGGREGATEDDATASETLENGTH
    DATASET_STATISTICS = ct.DATASETSTATISTICS
    FEASIBILITY = ct.FEASIBILITY
    GWAS = ct.GWAS
    HYBRIDFL = ct.HYBRIDFL
    INTERSECTION = ct.SETINTERSECTION
    MEAN = ct.ENCRYPTEDMEAN
    PREDICTION = ct.ENCRYPTEDPREDICTION
    REGRESSION = ct.ENCRYPTEDREGRESSION
    SURVIVAL_ANALYSIS = ct.SURVIVALAGGREGATION
    VALUE_DISTRIBUTION = ct.VALUEDISTRIBUTION

    def to_computation_type(self) -> ct:
        # The warning is here, because putting it at top-level causes the diapason import to print a warning.
        return ct(self.value)


displayed_types = {
    Type.AGGREGATION: "Aggregation",
    Type.DATASET_LENGTH: "Dataset Length",
    Type.DATASET_STATISTICS: "Secure Quantiles Computation",
    Type.FEASIBILITY: "Feasibility",
    Type.GWAS: "GWAS",
    Type.HYBRIDFL: "Hybrid Federated Learning",
    Type.INTERSECTION: "Private Set Intersection",
    Type.MEAN: "Mean",
    Type.PREDICTION: "Prediction",
    Type.REGRESSION: "Regression",
    Type.SURVIVAL_ANALYSIS: "Survival Analysis",
    Type.VALUE_DISTRIBUTION: "Value Distribution",
}
"""Mapping from computation type to human-readable name."""


type_to_class = {
    Type.AGGREGATION: Aggregation,
    Type.DATASET_LENGTH: DatasetLength,
    Type.DATASET_STATISTICS: Statistics,
    Type.FEASIBILITY: Feasibility,
    Type.GWAS: GWAS,
    Type.HYBRIDFL: HybridFL,
    Type.INTERSECTION: Matching,
    Type.MEAN: EncryptedMean,
    Type.SURVIVAL_ANALYSIS: SurvivalAnalysis,
    Type.VALUE_DISTRIBUTION: Distribution,
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
