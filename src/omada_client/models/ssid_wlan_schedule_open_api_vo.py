from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SsidWlanScheduleOpenApiVO")


@_attrs_define
class SsidWlanScheduleOpenApiVO:
    """SSID WLAN schedule config.

    Attributes:
        wlan_schedule_enable (bool | Unset): SSID WLAN schedule global config status. True: enable, false: disable.
        action (int | Unset): 0 means radio off, indicating the Wi-Fi function is off during the selected period; 1
            means radio on, indicating the Wi-Fi function is on during the selected period.
        schedule_id (str | Unset): This field represents Time Range Profile ID. Time Range Profile can be created using
            Create time range profile interface, and Time Range Profile ID can be obtained from Get time range profile list
            interface.
    """

    wlan_schedule_enable: bool | Unset = UNSET
    action: int | Unset = UNSET
    schedule_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wlan_schedule_enable = self.wlan_schedule_enable

        action = self.action

        schedule_id = self.schedule_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if wlan_schedule_enable is not UNSET:
            field_dict["wlanScheduleEnable"] = wlan_schedule_enable
        if action is not UNSET:
            field_dict["action"] = action
        if schedule_id is not UNSET:
            field_dict["scheduleId"] = schedule_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        wlan_schedule_enable = d.pop("wlanScheduleEnable", UNSET)

        action = d.pop("action", UNSET)

        schedule_id = d.pop("scheduleId", UNSET)

        ssid_wlan_schedule_open_api_vo = cls(
            wlan_schedule_enable=wlan_schedule_enable,
            action=action,
            schedule_id=schedule_id,
        )

        ssid_wlan_schedule_open_api_vo.additional_properties = d
        return ssid_wlan_schedule_open_api_vo

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
