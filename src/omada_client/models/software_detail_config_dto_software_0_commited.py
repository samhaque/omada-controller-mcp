from enum import StrEnum


class SoftwareDetailConfigDTOSoftware0Commited(StrEnum):
    COMMITTED = "COMMITTED"
    UNCOMMITTED = "UNCOMMITTED"

    def __str__(self) -> str:
        return str(self.value)
