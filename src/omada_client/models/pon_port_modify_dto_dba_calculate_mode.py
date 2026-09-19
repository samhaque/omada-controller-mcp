from enum import StrEnum


class PonPortModifyDTODbaCalculateMode(StrEnum):
    MAX_BW = "MAX_BW"
    MIN_DELAY = "MIN_DELAY"

    def __str__(self) -> str:
        return str(self.value)
