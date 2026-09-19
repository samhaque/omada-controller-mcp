from enum import StrEnum


class ServiceProfileVONativeVlan(StrEnum):
    CONCERN = "CONCERN"
    UNCONCERN = "UNCONCERN"

    def __str__(self) -> str:
        return str(self.value)
