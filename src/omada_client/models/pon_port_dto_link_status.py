from enum import StrEnum


class PonPortDTOLinkStatus(StrEnum):
    ACTIVE_STANDBY = "ACTIVE_STANDBY"
    ACTIVE_WORKING = "ACTIVE_WORKING"
    ACTIVE_WORKING_NONE = "ACTIVE_WORKING_NONE"
    INACTIVE = "INACTIVE"

    def __str__(self) -> str:
        return str(self.value)
