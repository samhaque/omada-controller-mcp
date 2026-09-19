from enum import StrEnum


class AuthenticationConfigDTOConfigStatus(StrEnum):
    FAILED = "FAILED"
    SUCCESS = "SUCCESS"

    def __str__(self) -> str:
        return str(self.value)
