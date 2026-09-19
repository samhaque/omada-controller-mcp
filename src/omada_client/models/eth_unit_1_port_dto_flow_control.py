from enum import StrEnum


class EthUnit1PortDTOFlowControl(StrEnum):
    DISABLE = "DISABLE"
    ENABLE = "ENABLE"

    def __str__(self) -> str:
        return str(self.value)
