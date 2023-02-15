from enum import Enum


class BinningParametersMethod(str, Enum):
    AUTOMATIC = "automatic"
    RANGEBINS = "rangeBins"
    SPECIFIEDCATEGORIES = "specifiedCategories"

    def __str__(self) -> str:
        return str(self.value)
