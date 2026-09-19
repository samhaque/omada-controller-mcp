from enum import StrEnum


class AuthenticationConfigDTODiscoveryMode(StrEnum):
    ALWAYS_ON = "ALWAYS_ON"
    ONCE_ON = "ONCE_ON"

    def __str__(self) -> str:
        return str(self.value)
