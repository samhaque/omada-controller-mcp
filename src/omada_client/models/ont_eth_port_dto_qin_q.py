from enum import StrEnum


class OntEthPortDTOQinQ(StrEnum):
    DISABLE = "DISABLE"
    ENABLE = "ENABLE"
    UNCONCERN = "UNCONCERN"

    def __str__(self) -> str:
        return str(self.value)
