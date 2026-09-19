from enum import StrEnum


class LineProfileVOMappingMode(StrEnum):
    PORT = "PORT"
    PORT_PRIORITY = "PORT_PRIORITY"
    PORT_VLAN = "PORT_VLAN"
    PORT_VLAN_PRIORITY = "PORT_VLAN_PRIORITY"
    PRIORITY = "PRIORITY"
    VLAN = "VLAN"
    VLAN_PRIORITY = "VLAN_PRIORITY"

    def __str__(self) -> str:
        return str(self.value)
