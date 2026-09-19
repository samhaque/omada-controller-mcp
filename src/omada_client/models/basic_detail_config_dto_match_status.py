from enum import StrEnum


class BasicDetailConfigDTOMatchStatus(StrEnum):
    MATCH = "MATCH"
    MISMATCH = "MISMATCH"

    def __str__(self) -> str:
        return str(self.value)
