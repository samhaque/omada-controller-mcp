from enum import StrEnum


class TrafficProfileDTOPriorityPolicy(StrEnum):
    LOCAL_SETTING = "LOCAL_SETTING"
    TAG_IN_INGRESS_PACKAGE = "TAG_IN_INGRESS_PACKAGE"
    TAG_IN_PACKAGE = "TAG_IN_PACKAGE"

    def __str__(self) -> str:
        return str(self.value)
