from enum import StrEnum


class EthUnit1PortDTODuplexLink(StrEnum):
    AUTO = "AUTO"
    FULL = "FULL"
    HALF = "HALF"

    def __str__(self) -> str:
        return str(self.value)
