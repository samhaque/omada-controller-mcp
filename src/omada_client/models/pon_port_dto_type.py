from enum import StrEnum


class PonPortDTOType(StrEnum):
    COMBO = "COMBO"
    COPPER = "COPPER"
    SFP = "SFP"

    def __str__(self) -> str:
        return str(self.value)
