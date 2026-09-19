from enum import StrEnum


class ServicePortProfileDetailDTOStatisticPerformance(StrEnum):
    DISABLE = "DISABLE"
    ENABLE = "ENABLE"

    def __str__(self) -> str:
        return str(self.value)
