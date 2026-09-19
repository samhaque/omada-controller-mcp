from enum import StrEnum


class OntPotsPortDTOVlanConfigMode(StrEnum):
    OTHERS = "OTHERS"
    TRANSPARENT = "TRANSPARENT"

    def __str__(self) -> str:
        return str(self.value)
