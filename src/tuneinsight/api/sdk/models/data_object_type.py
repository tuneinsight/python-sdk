from enum import Enum


class DataObjectType(str, Enum):
    RLWE_PUBLIC_KEY = "rlwe-public-key"
    RLWE_ROTATION_KEY = "rlwe-rotation-key"
    RLWE_RELINEARIZATION_KEY = "rlwe-relinearization-key"
    RLWE_SECRET_KEY = "rlwe-secret-key"
    ENCRYPTED_REG_MODEL = "encrypted-reg-model"
    ENCRYPTED_REG_PREDICTION = "encrypted-reg-prediction"
    DECRYPTED_PREDICTION = "decrypted-prediction"
    PLAINTEXT_REG_MODEL = "plaintext-reg-model"
    CIPHERTABLE = "ciphertable"
    TABLE = "table"
    FLOAT_MATRIX = "float-matrix"
    ENCRYPTED_PREDICTION_DATASET = "encrypted-prediction-dataset"
    ENCRYPTED_REG_MODEL_COMPRESSED = "encrypted-reg-model-compressed"
    BFV_SINGLE_CIPHERTEXT = "bfv-single-ciphertext"
    BGV_CIPHERTEXT = "bgv-ciphertext"
    DISTRIBUTED_JOIN_MAPPING = "distributed-join-mapping"
    ENCRYPTED_BUFFER = "encrypted-buffer"
    COHORT = "cohort"
    GWAS_MODEL = "gwas-model"
    ENCRYPTED_STATISTICS = "encrypted-statistics"
    DECRYPTED_STATISTICS = "decrypted-statistics"

    def __str__(self) -> str:
        return str(self.value)
