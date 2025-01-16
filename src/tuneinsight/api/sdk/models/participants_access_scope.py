from enum import Enum


class ParticipantsAccessScope(str, Enum):
    ALL = "all"
    ONLYROOT = "onlyRoot"
    ONLYNONROOT = "onlyNonRoot"
    ONLYCREATOR = "onlyCreator"
    ONLYCONTRIBUTORS = "onlyContributors"
    SPECIFIED = "specified"

    def __str__(self) -> str:
        return str(self.value)
