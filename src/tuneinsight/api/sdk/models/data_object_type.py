from enum import Enum


class DataObjectType(str, Enum):
    RLWE_PUBLIC_KEY = "rlwe-public-key"
    RLWE_GALOIS_KEY = "rlwe-galois-key"
    RLWE_MEM_EVALUATION_KEY_SET = "rlwe-mem-evaluation-key-set"
    RLWE_RELINEARIZATION_KEY = "rlwe-relinearization-key"
    RLWE_SECRET_KEY = "rlwe-secret-key"
    HEFLOAT_CIPHERTEXT_SINGLE = "hefloat-ciphertext-single"
    HEFLOAT_CIPHERTEXT_MATRIX = "hefloat-ciphertext-matrix"
    HEINT_CIPHERTEXT_SINGLE = "heint-ciphertext-single"
    HEINT_CIPHERTEXT_MATRIX = "heint-ciphertext-matrix"
    ENCRYPTED_REG_MODEL = "encrypted-reg-model"
    ENCRYPTED_REG_PREDICTION = "encrypted-reg-prediction"
    DECRYPTED_PREDICTION = "decrypted-prediction"
    PLAINTEXT_REG_MODEL = "plaintext-reg-model"
    TABLE = "table"
    FLOAT_MATRIX = "float-matrix"
    ENCRYPTED_PREDICTION_DATASET = "encrypted-prediction-dataset"
    ENCRYPTED_REG_MODEL_COMPRESSED = "encrypted-reg-model-compressed"
    DISTRIBUTED_JOIN_MAPPING = "distributed-join-mapping"
    ENCRYPTED_BUFFER = "encrypted-buffer"
    COHORT = "cohort"
    GWAS_MODEL = "gwas-model"
    EXTERNAL_ML_MODEL = "external-ml-model"
    ENCRYPTED_STATISTICS = "encrypted-statistics"
    DECRYPTED_STATISTICS = "decrypted-statistics"
    PIR_DATASET = "pir-dataset"
    ENCRYPTED_PIR_SEARCH = "encrypted-pir-search"
    ENCRYPTED_PIR_RESULT = "encrypted-pir-result"
    ENCRYPTED_DATA_OBJECT = "encrypted-data-object"

    def __str__(self) -> str:
        return str(self.value)
