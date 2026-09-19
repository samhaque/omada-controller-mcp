from enum import StrEnum


class OnuInformationConfigDTOMatchStatus(StrEnum):
    MATCH = "MATCH"
    MISMATCH = "MISMATCH"

    def __str__(self) -> str:
        return str(self.value)
