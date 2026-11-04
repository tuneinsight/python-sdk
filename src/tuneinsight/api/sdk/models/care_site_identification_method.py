from enum import Enum


class CareSiteIdentificationMethod(str, Enum):
    FR_FINESS = "fr_finess"
    NAME = "name"
    NAME_GROUP = "name_group"

    def __str__(self) -> str:
        return str(self.value)
