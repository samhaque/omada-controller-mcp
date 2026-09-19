from enum import StrEnum


class ServiceProfileDTOMulticastMode(StrEnum):
    IGMP_SNOOPING = "IGMP_SNOOPING"
    OLT_CONTROL = "OLT_CONTROL"
    UNCONCERN = "UNCONCERN"

    def __str__(self) -> str:
        return str(self.value)
