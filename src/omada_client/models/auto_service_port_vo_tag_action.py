from enum import StrEnum


class AutoServicePortVOTagAction(StrEnum):
    ADD_DOUBLE = "ADD_DOUBLE"
    DEFAULT = "DEFAULT"
    TRANSLATE = "TRANSLATE"
    TRANSLATE_AND_ADD = "TRANSLATE_AND_ADD"
    TRANSPARENT = "TRANSPARENT"

    def __str__(self) -> str:
        return str(self.value)
