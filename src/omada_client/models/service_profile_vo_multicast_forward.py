from enum import StrEnum


class ServiceProfileVOMulticastForward(StrEnum):
    TAGGED = "TAGGED"
    UNCONCERN = "UNCONCERN"
    UNTAGGED = "UNTAGGED"

    def __str__(self) -> str:
        return str(self.value)
