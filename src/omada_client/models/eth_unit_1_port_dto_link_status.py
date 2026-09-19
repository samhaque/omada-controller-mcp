from enum import StrEnum


class EthUnit1PortDTOLinkStatus(StrEnum):
    LINK_DOWN = "LINK_DOWN"
    LINK_UP = "LINK_UP"

    def __str__(self) -> str:
        return str(self.value)
