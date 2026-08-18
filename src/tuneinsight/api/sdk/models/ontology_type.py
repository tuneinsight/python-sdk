from enum import Enum


class OntologyType(str, Enum):
    ICD10 = "ICD10"
    OMOPGENERATED = "OMOPGenerated"
    ICD10GM = "ICD10GM"
    CIM10 = "CIM10"
    ATC = "ATC"
    LOINC = "LOINC"
    CHOP = "CHOP"
    SNOMED = "SNOMED"
    CCAM = "CCAM"
    RXNORM = "RxNorm"
    RXNORM_EXTENSION = "RxNorm Extension"
    UCUM = "UCUM"
    CMS_PLACE_OF_SERVICE = "CMS Place of Service"
    CANCER_MODIFIER = "Cancer Modifier"
    CONDITION_STATUS = "Condition Status"
    CONDITION_TYPE = "Condition Type"
    DEATH_TYPE = "Death Type"
    DRUG_TYPE = "Drug Type"
    ETHNICITY = "Ethnicity"
    GENDER = "Gender"
    MEAS_TYPE = "Meas Type"
    OBS_PERIOD_TYPE = "Obs Period Type"
    OBSERVATION_TYPE = "Observation Type"
    PROCEDURE_TYPE = "Procedure Type"
    RACE = "Race"
    SPECIMEN_TYPE = "Specimen Type"
    VISIT_TYPE = "Visit Type"
    OMOP_EXTENSION = "OMOP Extension"

    def __str__(self) -> str:
        return str(self.value)
