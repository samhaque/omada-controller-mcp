from enum import StrEnum


class EthUnit1PortDTODuplex(StrEnum):
    AUTO = "AUTO"
    FULL = "FULL"
    HALF = "HALF"

    def __str__(self) -> str:
        return str(self.value)
