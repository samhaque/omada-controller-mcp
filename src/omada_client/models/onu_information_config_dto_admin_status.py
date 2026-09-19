from enum import StrEnum


class OnuInformationConfigDTOAdminStatus(StrEnum):
    ACTIVATE = "ACTIVATE"
    ACTIVATED = "ACTIVATED"
    DEACTIVATE = "DEACTIVATE"
    DEACTIVATED = "DEACTIVATED"

    def __str__(self) -> str:
        return str(self.value)
