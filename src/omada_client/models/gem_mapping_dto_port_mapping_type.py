from enum import StrEnum


class GemMappingDTOPortMappingType(StrEnum):
    ETH = "ETH"
    POTS = "POTS"

    def __str__(self) -> str:
        return str(self.value)
