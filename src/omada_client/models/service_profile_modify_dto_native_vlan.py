from enum import StrEnum


class ServiceProfileModifyDTONativeVlan(StrEnum):
    CONCERN = "CONCERN"
    UNCONCERN = "UNCONCERN"

    def __str__(self) -> str:
        return str(self.value)
