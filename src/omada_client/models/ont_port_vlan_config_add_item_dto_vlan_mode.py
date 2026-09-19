from enum import StrEnum


class OntPortVlanConfigAddItemDTOVlanMode(StrEnum):
    QINQ = "QINQ"
    TRANSLATION = "TRANSLATION"
    TRUNK = "TRUNK"

    def __str__(self) -> str:
        return str(self.value)
