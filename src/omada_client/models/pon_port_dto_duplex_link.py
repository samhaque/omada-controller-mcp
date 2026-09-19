from enum import StrEnum


class PonPortDTODuplexLink(StrEnum):
    FULL = "FULL"

    def __str__(self) -> str:
        return str(self.value)
