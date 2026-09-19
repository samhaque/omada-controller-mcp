from enum import StrEnum


class OntEthPortIGMPForwardDTOIgmpForwardMode(StrEnum):
    DEFAULT = "DEFAULT"
    TRANSLATION = "TRANSLATION"
    TRANSPARENT = "TRANSPARENT"
    UNCONCERN = "UNCONCERN"

    def __str__(self) -> str:
        return str(self.value)
