from enum import StrEnum


class BasicDetailConfigDTOConfigStatus(StrEnum):
    FAILED = "FAILED"
    SUCCESS = "SUCCESS"

    def __str__(self) -> str:
        return str(self.value)
