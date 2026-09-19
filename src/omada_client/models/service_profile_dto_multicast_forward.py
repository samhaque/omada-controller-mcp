from enum import StrEnum


class ServiceProfileDTOMulticastForward(StrEnum):
    TAGGED = "TAGGED"
    UNCONCERN = "UNCONCERN"
    UNTAGGED = "UNTAGGED"

    def __str__(self) -> str:
        return str(self.value)
