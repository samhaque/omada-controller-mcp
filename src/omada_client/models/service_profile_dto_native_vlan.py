from enum import StrEnum


class ServiceProfileDTONativeVlan(StrEnum):
    CONCERN = "CONCERN"
    UNCONCERN = "UNCONCERN"

    def __str__(self) -> str:
        return str(self.value)
