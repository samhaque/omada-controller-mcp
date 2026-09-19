from enum import StrEnum


class AuthenticationConfigDTOMatchStatus(StrEnum):
    MATCH = "MATCH"
    MISMATCH = "MISMATCH"

    def __str__(self) -> str:
        return str(self.value)
