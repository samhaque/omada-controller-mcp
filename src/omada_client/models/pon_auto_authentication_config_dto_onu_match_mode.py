from enum import StrEnum


class PonAutoAuthenticationConfigDTOOnuMatchMode(StrEnum):
    ALL_ONU = "ALL_ONU"
    EQUID_AUTH = "EQUID_AUTH"
    EQUID_SWVER_AUTH = "EQUID_SWVER_AUTH"
    VENDOR_AUTH = "VENDOR_AUTH"

    def __str__(self) -> str:
        return str(self.value)
