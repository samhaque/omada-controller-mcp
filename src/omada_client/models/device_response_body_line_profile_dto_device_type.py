from enum import StrEnum


class DeviceResponseBodyLineProfileDTODeviceType(StrEnum):
    AP = "ap"
    EMS = "ems"
    FESTA_AP = "festa ap"
    FESTA_GATEWAY = "festa gateway"
    FESTA_SWITCH = "festa switch"
    GATEWAY = "gateway"
    OLT = "olt"
    ONU = "onu"
    PRO_AP = "pro ap"
    PRO_GATEWAY = "pro gateway"
    PRO_SWITCH = "pro switch"
    SWITCH = "switch"

    def __str__(self) -> str:
        return str(self.value)
