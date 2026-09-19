from enum import StrEnum


class SoftwareDetailConfigDTOSoftware0Valid(StrEnum):
    INVALID = "INVALID"
    VALID = "VALID"

    def __str__(self) -> str:
        return str(self.value)
