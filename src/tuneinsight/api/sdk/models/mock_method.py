from enum import Enum


class MockMethod(str, Enum):
    PATIENTS = "patients"
    ALERTS = "alerts"
    NEUROLOGY_OBSERVATIONS = "neurology_observations"
    GENERIC = "generic"
    PRICES = "prices"
    PERSONS = "persons"
    SKUS = "skus"
    CYBER_LOGS = "cyber_logs"
    CUSTOM_FUNCTION = "custom_function"

    def __str__(self) -> str:
        return str(self.value)
