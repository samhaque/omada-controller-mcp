from enum import StrEnum


class GemMappingModifyDTOPortMappingType(StrEnum):
    ETH = "ETH"
    POTS = "POTS"

    def __str__(self) -> str:
        return str(self.value)
