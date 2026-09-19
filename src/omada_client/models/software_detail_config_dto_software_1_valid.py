from enum import StrEnum


class SoftwareDetailConfigDTOSoftware1Valid(StrEnum):
    INVALID = "INVALID"
    VALID = "VALID"

    def __str__(self) -> str:
        return str(self.value)
