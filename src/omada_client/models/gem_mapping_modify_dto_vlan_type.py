from enum import StrEnum


class GemMappingModifyDTOVlanType(StrEnum):
    TAGGED = "TAGGED"
    UNTAGGED = "UNTAGGED"
    VLAN_TRANSPARENT = "VLAN_TRANSPARENT"

    def __str__(self) -> str:
        return str(self.value)
