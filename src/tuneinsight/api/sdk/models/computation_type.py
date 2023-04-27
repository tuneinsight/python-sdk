from enum import Enum


class ComputationType(str, Enum):
    DUMMY = "dummy"
    COLLECTIVEKEYGEN = "collectiveKeyGen"
    RELINKEYGEN = "relinKeyGen"
    ROTKEYGEN = "rotKeyGen"
    BOOTSTRAP = "bootstrap"
    COLLECTIVEKEYSWITCH = "collectiveKeySwitch"
    ENCRYPTEDAGGREGATION = "encryptedAggregation"
    AGGREGATEDDATASETLENGTH = "aggregatedDatasetLength"
    ENCRYPTEDREGRESSION = "encryptedRegression"
    ENCRYPTEDPREDICTION = "encryptedPrediction"
    SETINTERSECTION = "setIntersection"
    KEYSWITCHEDCOMPUTATION = "keySwitchedComputation"
    VBINNEDAGGREGATION = "vBinnedAggregation"
    STATISTICALAGGREGATION = "statisticalAggregation"
    SETUPSESSION = "setupSession"
    DISTRIBUTEDJOIN = "distributedJoin"
    SAMPLEEXTRACTION = "sampleExtraction"
    GWAS = "GWAS"
    SURVIVALAGGREGATION = "survivalAggregation"
    HYBRIDFL = "hybridFL"
    DATASETSTATISTICS = "datasetStatistics"
    PRIVATESEARCH = "privateSearch"

    def __str__(self) -> str:
        return str(self.value)
