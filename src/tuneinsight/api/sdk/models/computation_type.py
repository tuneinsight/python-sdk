from enum import Enum


class ComputationType(str, Enum):
    DUMMY = "dummy"
    UNDEFINED = "undefined"
    COLLECTIVEKEYSWITCH = "collectiveKeySwitch"
    ENCRYPTEDAGGREGATION = "encryptedAggregation"
    AGGREGATEDDATASETLENGTH = "aggregatedDatasetLength"
    ENCRYPTEDREGRESSION = "encryptedRegression"
    ENCRYPTEDPREDICTION = "encryptedPrediction"
    SETINTERSECTION = "setIntersection"
    VBINNEDAGGREGATION = "vBinnedAggregation"
    SETUPSESSION = "setupSession"
    GWAS = "GWAS"
    SURVIVALAGGREGATION = "survivalAggregation"
    HYBRIDFL = "hybridFL"
    DATASETSTATISTICS = "datasetStatistics"
    PRIVATESEARCH = "privateSearch"
    PRIVATESEARCHSETUP = "privateSearchSetup"
    ENCRYPTEDMEAN = "encryptedMean"
    FEASIBILITY = "feasibility"
    FILTEREDAGGREGATION = "filteredAggregation"
    VALUEDISTRIBUTION = "valueDistribution"

    def __str__(self) -> str:
        return str(self.value)
