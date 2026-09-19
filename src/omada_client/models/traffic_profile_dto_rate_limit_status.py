from enum import StrEnum


class TrafficProfileDTORateLimitStatus(StrEnum):
    DISABLE = "DISABLE"
    ENABLE = "ENABLE"

    def __str__(self) -> str:
        return str(self.value)
