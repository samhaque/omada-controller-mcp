from enum import StrEnum


class PonPortDTOLongLaserOnuAutoIsolate(StrEnum):
    DISABLE = "DISABLE"
    ENABLE = "ENABLE"

    def __str__(self) -> str:
        return str(self.value)
