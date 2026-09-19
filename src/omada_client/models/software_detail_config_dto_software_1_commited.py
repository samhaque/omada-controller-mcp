from enum import StrEnum


class SoftwareDetailConfigDTOSoftware1Commited(StrEnum):
    COMMITTED = "COMMITTED"
    UNCOMMITTED = "UNCOMMITTED"

    def __str__(self) -> str:
        return str(self.value)
