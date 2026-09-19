from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.onu_information_reboot_status_config_dto_online_status import (
    OnuInformationRebootStatusConfigDTOOnlineStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="OnuInformationRebootStatusConfigDTO")


@_attrs_define
class OnuInformationRebootStatusConfigDTO:
    """
    Attributes:
        key (str | Unset): Identifier of ONU
        online_status (OnuInformationRebootStatusConfigDTOOnlineStatus | Unset): Online status should be a value as
            follows:ONLINE,OFFLINE,UPGRADING
    """

    key: str | Unset = UNSET
    online_status: OnuInformationRebootStatusConfigDTOOnlineStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        online_status: str | Unset = UNSET
        if not isinstance(self.online_status, Unset):
            online_status = self.online_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if online_status is not UNSET:
            field_dict["onlineStatus"] = online_status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        key = d.pop("key", UNSET)

        _online_status = d.pop("onlineStatus", UNSET)
        online_status: OnuInformationRebootStatusConfigDTOOnlineStatus | Unset
        if isinstance(_online_status, Unset):
            online_status = UNSET
        else:
            online_status = OnuInformationRebootStatusConfigDTOOnlineStatus(
                _online_status
            )

        onu_information_reboot_status_config_dto = cls(
            key=key,
            online_status=online_status,
        )

        onu_information_reboot_status_config_dto.additional_properties = d
        return onu_information_reboot_status_config_dto

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
