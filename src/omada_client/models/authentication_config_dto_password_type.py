from enum import StrEnum


class AuthenticationConfigDTOPasswordType(StrEnum):
    ASCII = "ASCII"
    HEX = "HEX"

    def __str__(self) -> str:
        return str(self.value)
