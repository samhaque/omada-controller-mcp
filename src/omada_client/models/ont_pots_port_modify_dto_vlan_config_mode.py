from enum import StrEnum


class OntPotsPortModifyDTOVlanConfigMode(StrEnum):
    OTHERS = "OTHERS"
    TRANSPARENT = "TRANSPARENT"

    def __str__(self) -> str:
        return str(self.value)
