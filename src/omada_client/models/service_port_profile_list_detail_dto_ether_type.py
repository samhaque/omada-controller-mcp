from enum import StrEnum


class ServicePortProfileListDetailDTOEtherType(StrEnum):
    IPV4OE = "IPV4OE"
    IPV6OE = "IPV6OE"
    NONE = "NONE"
    PPPOE = "PPPOE"

    def __str__(self) -> str:
        return str(self.value)
