from enum import StrEnum


class PonPortDTOSpeed(StrEnum):
    GPON = "GPON"
    NONE = "NONE"
    XGS_PON = "XGS_PON"
    XG_PON = "XG_PON"

    def __str__(self) -> str:
        return str(self.value)
