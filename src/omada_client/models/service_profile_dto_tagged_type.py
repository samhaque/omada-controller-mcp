from enum import StrEnum


class ServiceProfileDTOTaggedType(StrEnum):
    TRANSLATION = "TRANSLATION"
    TRANSPARENT = "TRANSPARENT"

    def __str__(self) -> str:
        return str(self.value)
