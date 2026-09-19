from enum import StrEnum


class OnuAutofindConfigDTOPasswordType(StrEnum):
    ASCII = "ASCII"
    HEX = "HEX"

    def __str__(self) -> str:
        return str(self.value)
