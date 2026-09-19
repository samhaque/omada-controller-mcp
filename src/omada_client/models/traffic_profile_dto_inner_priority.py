from enum import StrEnum


class TrafficProfileDTOInnerPriority(StrEnum):
    ASSIGNED = "ASSIGNED"
    NONE = "NONE"
    USER_COS = "USER_COS"
    USER_INNER_COS = "USER_INNER_COS"

    def __str__(self) -> str:
        return str(self.value)
