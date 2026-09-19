from enum import StrEnum


class AuthenticationConfigDTOAuthenticationMethod(StrEnum):
    LOID_AND_PASSWORD_AUTH = "LOID_AND_PASSWORD_AUTH"
    LOID_AUTH = "LOID_AUTH"
    PASSWORD_AUTH = "PASSWORD_AUTH"
    SN_AND_PASSWORD_AUTH = "SN_AND_PASSWORD_AUTH"
    SN_AUTH = "SN_AUTH"

    def __str__(self) -> str:
        return str(self.value)
