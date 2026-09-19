from enum import StrEnum


class EthUnit1PortDTOType(StrEnum):
    COMBO = "COMBO"
    COPPER = "COPPER"
    RJ45 = "RJ45"
    SFP = "SFP+"

    def __str__(self) -> str:
        return str(self.value)
