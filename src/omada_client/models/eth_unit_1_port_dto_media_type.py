from enum import StrEnum


class EthUnit1PortDTOMediaType(StrEnum):
    COPPER = "COPPER"
    FIBER = "FIBER"

    def __str__(self) -> str:
        return str(self.value)
