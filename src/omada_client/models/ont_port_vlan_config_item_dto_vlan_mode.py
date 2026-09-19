from enum import StrEnum


class OntPortVlanConfigItemDTOVlanMode(StrEnum):
    QINQ = "QINQ"
    TRANSLATION = "TRANSLATION"
    TRUNK = "TRUNK"

    def __str__(self) -> str:
        return str(self.value)
