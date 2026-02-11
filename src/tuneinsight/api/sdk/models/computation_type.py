from enum import Enum


class ComputationType(str, Enum):
    DUMMY = "dummy"
    UNDEFINED = "undefined"
    COLLECTIVEKEYSWITCH = "collectiveKeySwitch"
    ENCRYPTEDAGGREGATION = "encryptedAggregation"
    AGGREGATEDDATASETLENGTH = "aggregatedDatasetLength"
    COMBINE = "combine"
    ENCRYPTEDREGRESSION = "encryptedRegression"
    ENCRYPTEDPREDICTION = "encryptedPrediction"
    SETINTERSECTION = "setIntersection"
    SETUPSESSION = "setupSession"
    SURVIVALAGGREGATION = "survivalAggregation"
    HYBRIDFL = "hybridFL"
    SECUREINFERENCE = "secureInference"
    DATASETSTATISTICS = "datasetStatistics"
    ENCRYPTEDMEAN = "encryptedMean"
    FEASIBILITY = "feasibility"
    FILTEREDAGGREGATION = "filteredAggregation"
    VALUEDISTRIBUTION = "valueDistribution"

    def __str__(self) -> str:
        return str(self.value)
