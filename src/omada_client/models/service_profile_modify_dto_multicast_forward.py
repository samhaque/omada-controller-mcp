from enum import StrEnum


class ServiceProfileModifyDTOMulticastForward(StrEnum):
    TAGGED = "TAGGED"
    UNCONCERN = "UNCONCERN"
    UNTAGGED = "UNTAGGED"

    def __str__(self) -> str:
        return str(self.value)
