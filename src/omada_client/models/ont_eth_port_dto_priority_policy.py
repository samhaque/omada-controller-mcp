from enum import StrEnum


class OntEthPortDTOPriorityPolicy(StrEnum):
    ASSIGNED = "ASSIGNED"
    COPY_COS = "COPY_COS"
    UNCONCERN = "UNCONCERN"

    def __str__(self) -> str:
        return str(self.value)
