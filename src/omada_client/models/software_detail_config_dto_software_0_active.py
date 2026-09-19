from enum import StrEnum


class SoftwareDetailConfigDTOSoftware0Active(StrEnum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

    def __str__(self) -> str:
        return str(self.value)
