from enum import Enum
from tuneinsight.api.sdk.models import ComputationType as ct

class Type(Enum):
    '''
    Type Enumeration of all of the exposed distributed computations types
    '''

    AGGREGATION = ct.ENCRYPTEDAGGREGATION
    REGRESSION = ct.ENCRYPTEDREGRESSION
    PREDICTION = ct.ENCRYPTEDPREDICTION
    INTERSECTION =  ct.SETINTERSECTION
    STAT_AGGREGATION = ct.STATISTICALAGGREGATION
    JOIN = ct.DISTRIBUTEDJOIN
    SAMPLE_EXTRACTION = ct.SAMPLEEXTRACTION
    GWAS = ct.GWAS
    SURVIVAL_ANALYSIS = ct.SURVIVALAGGREGATION
    DATASET_STATISTICS = ct.DATASETSTATISTICS

    def to_computation_type(self) -> ct:
        return ct(self.value)



displayed_types = {
    Type.AGGREGATION : "Aggregation",
    Type.REGRESSION: "Regression",
    Type.PREDICTION: "Prediction",
    Type.INTERSECTION: 'Private Set Intersection',
    Type.STAT_AGGREGATION: 'Statistical Aggregation',
    Type.JOIN: "Secure Join",
    Type.SAMPLE_EXTRACTION: "Sample Extraction",
    Type.GWAS: 'GWAS',
    Type.SURVIVAL_ANALYSIS: "Survival Analysis",
    Type.DATASET_STATISTICS: "Secure Quantiles Computation",
}
