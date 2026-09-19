from enum import StrEnum


class ServiceProfileVOTaggedType(StrEnum):
    TRANSLATION = "TRANSLATION"
    TRANSPARENT = "TRANSPARENT"

    def __str__(self) -> str:
        return str(self.value)
