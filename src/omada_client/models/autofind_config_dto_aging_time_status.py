from enum import StrEnum


class AutofindConfigDTOAgingTimeStatus(StrEnum):
    NO_AGING = "NO_AGING"
    TIMEOUT = "TIMEOUT"

    def __str__(self) -> str:
        return str(self.value)
