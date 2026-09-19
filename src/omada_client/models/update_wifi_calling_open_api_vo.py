from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateWifiCallingOpenApiVO")


@_attrs_define
class UpdateWifiCallingOpenApiVO:
    """
    Attributes:
        wifi_calling_enable (bool): SSID Wi-Fi Calling global config status. True: enable, false: disable.
        wifi_calling_id (str | Unset): This field represents Wi-Fi Calling Profile ID. Wi-Fi Calling Profile can be
            created using Create a new wifi calling profile.
    """

    wifi_calling_enable: bool
    wifi_calling_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wifi_calling_enable = self.wifi_calling_enable

        wifi_calling_id = self.wifi_calling_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "wifiCallingEnable": wifi_calling_enable,
            }
        )
        if wifi_calling_id is not UNSET:
            field_dict["wifiCallingId"] = wifi_calling_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        wifi_calling_enable = d.pop("wifiCallingEnable")

        wifi_calling_id = d.pop("wifiCallingId", UNSET)

        update_wifi_calling_open_api_vo = cls(
            wifi_calling_enable=wifi_calling_enable,
            wifi_calling_id=wifi_calling_id,
        )

        update_wifi_calling_open_api_vo.additional_properties = d
        return update_wifi_calling_open_api_vo

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
