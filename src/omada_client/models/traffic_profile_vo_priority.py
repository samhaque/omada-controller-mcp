from enum import StrEnum


class TrafficProfileVOPriority(StrEnum):
    ASSIGNED = "ASSIGNED"
    USER_COS = "USER_COS"

    def __str__(self) -> str:
        return str(self.value)
