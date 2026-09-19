from enum import StrEnum


class ServicePortProfileListDetailDTOCreationMode(StrEnum):
    AUTO = "AUTO"
    MANUAL = "MANUAL"

    def __str__(self) -> str:
        return str(self.value)
