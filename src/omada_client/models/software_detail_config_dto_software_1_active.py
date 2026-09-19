from enum import StrEnum


class SoftwareDetailConfigDTOSoftware1Active(StrEnum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

    def __str__(self) -> str:
        return str(self.value)
