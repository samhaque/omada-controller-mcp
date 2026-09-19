from enum import StrEnum


class BasicDetailConfigDTOOnlineStatus(StrEnum):
    FAILED = "FAILED"
    OFFLINE = "OFFLINE"
    ONLINE = "ONLINE"
    SUCCESSFUL = "SUCCESSFUL"
    UPGRADING = "UPGRADING"
    WAITING_UPGRADE = "WAITING_UPGRADE"

    def __str__(self) -> str:
        return str(self.value)
