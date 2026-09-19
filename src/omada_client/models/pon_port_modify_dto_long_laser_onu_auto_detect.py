from enum import StrEnum


class PonPortModifyDTOLongLaserOnuAutoDetect(StrEnum):
    DISABLE = "DISABLE"
    ENABLE = "ENABLE"

    def __str__(self) -> str:
        return str(self.value)
