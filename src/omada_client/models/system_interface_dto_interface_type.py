from enum import StrEnum


class SystemInterfaceDTOInterfaceType(StrEnum):
    MANAGEMENT = "MANAGEMENT"
    NONE = "NONE"
    PORT_CHANNEL = "PORT_CHANNEL"
    ROUTED_PORT = "ROUTED_PORT"
    VLAN = "VLAN"

    def __str__(self) -> str:
        return str(self.value)
