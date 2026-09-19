from enum import StrEnum


class AuthenticationConfigDTOOnlineStatus(StrEnum):
    OFFLINE = "OFFLINE"
    ONLINE = "ONLINE"

    def __str__(self) -> str:
        return str(self.value)
