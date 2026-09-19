from enum import StrEnum


class DBAProfileModifyDTOType(StrEnum):
    ASSURE = "ASSURE"
    ASSURE_MAX = "ASSURE_MAX"
    FIX = "FIX"
    FIX_ASSURE_MAX = "FIX_ASSURE_MAX"
    MAX = "MAX"

    def __str__(self) -> str:
        return str(self.value)
