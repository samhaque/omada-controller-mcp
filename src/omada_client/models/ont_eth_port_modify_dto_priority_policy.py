from enum import StrEnum


class OntEthPortModifyDTOPriorityPolicy(StrEnum):
    ASSIGNED = "ASSIGNED"
    COPY_COS = "COPY_COS"
    UNCONCERN = "UNCONCERN"

    def __str__(self) -> str:
        return str(self.value)
