from enum import StrEnum


class ServiceProfileModifyDTOTaggedType(StrEnum):
    TRANSLATION = "TRANSLATION"
    TRANSPARENT = "TRANSPARENT"

    def __str__(self) -> str:
        return str(self.value)
