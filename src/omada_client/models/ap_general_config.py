from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_rssi_led_setting_vo import ApRssiLedSettingVO
    from ..models.device_location_detail_vo import DeviceLocationDetailVO


T = TypeVar("T", bound="ApGeneralConfig")


@_attrs_define
class ApGeneralConfig:
    """
    Attributes:
        name (str | Unset): Device name should contain 1 to 128 characters.
        led_setting (int | Unset): Led setting should be a value as follows: 0:off; 1:on; 2:Use Site Settings.
        remote_reset (bool | Unset): Whether the remote reset function is enabled.
        wifi_control_enable (bool | Unset): Whether the wifi Control function is enabled.
        rssi_led_settings (list[ApRssiLedSettingVO] | Unset): Rssi Led Setting.
        tag_ids (list[str] | Unset): Tag IDs.
        gps_enable (bool | Unset): gps Enable only for ap which support gps function.
        location (DeviceLocationDetailVO | Unset): Device location
        remember_device (int | Unset): Parameter [rememberDevice] should be a value as follows: 0:off; 1:on; 2:Use Site
            Settings.
        disable_hw_reset (bool | Unset): When this value is [true], the device's hardware reset is invalid.(Only some
            specific devices support this feature)
    """

    name: str | Unset = UNSET
    led_setting: int | Unset = UNSET
    remote_reset: bool | Unset = UNSET
    wifi_control_enable: bool | Unset = UNSET
    rssi_led_settings: list[ApRssiLedSettingVO] | Unset = UNSET
    tag_ids: list[str] | Unset = UNSET
    gps_enable: bool | Unset = UNSET
    location: DeviceLocationDetailVO | Unset = UNSET
    remember_device: int | Unset = UNSET
    disable_hw_reset: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        led_setting = self.led_setting

        remote_reset = self.remote_reset

        wifi_control_enable = self.wifi_control_enable

        rssi_led_settings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rssi_led_settings, Unset):
            rssi_led_settings = []
            for rssi_led_settings_item_data in self.rssi_led_settings:
                rssi_led_settings_item = rssi_led_settings_item_data.to_dict()
                rssi_led_settings.append(rssi_led_settings_item)

        tag_ids: list[str] | Unset = UNSET
        if not isinstance(self.tag_ids, Unset):
            tag_ids = self.tag_ids

        gps_enable = self.gps_enable

        location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        remember_device = self.remember_device

        disable_hw_reset = self.disable_hw_reset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if led_setting is not UNSET:
            field_dict["ledSetting"] = led_setting
        if remote_reset is not UNSET:
            field_dict["remoteReset"] = remote_reset
        if wifi_control_enable is not UNSET:
            field_dict["wifiControlEnable"] = wifi_control_enable
        if rssi_led_settings is not UNSET:
            field_dict["rssiLedSettings"] = rssi_led_settings
        if tag_ids is not UNSET:
            field_dict["tagIds"] = tag_ids
        if gps_enable is not UNSET:
            field_dict["gpsEnable"] = gps_enable
        if location is not UNSET:
            field_dict["location"] = location
        if remember_device is not UNSET:
            field_dict["rememberDevice"] = remember_device
        if disable_hw_reset is not UNSET:
            field_dict["disableHwReset"] = disable_hw_reset

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_rssi_led_setting_vo import ApRssiLedSettingVO
        from ..models.device_location_detail_vo import (
            DeviceLocationDetailVO,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        led_setting = d.pop("ledSetting", UNSET)

        remote_reset = d.pop("remoteReset", UNSET)

        wifi_control_enable = d.pop("wifiControlEnable", UNSET)

        _rssi_led_settings = d.pop("rssiLedSettings", UNSET)
        rssi_led_settings: list[ApRssiLedSettingVO] | Unset = UNSET
        if _rssi_led_settings is not UNSET:
            rssi_led_settings = []
            for rssi_led_settings_item_data in _rssi_led_settings:
                rssi_led_settings_item = ApRssiLedSettingVO.from_dict(
                    rssi_led_settings_item_data
                )

                rssi_led_settings.append(rssi_led_settings_item)

        tag_ids = cast(list[str], d.pop("tagIds", UNSET))

        gps_enable = d.pop("gpsEnable", UNSET)

        _location = d.pop("location", UNSET)
        location: DeviceLocationDetailVO | Unset
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = DeviceLocationDetailVO.from_dict(_location)

        remember_device = d.pop("rememberDevice", UNSET)

        disable_hw_reset = d.pop("disableHwReset", UNSET)

        ap_general_config = cls(
            name=name,
            led_setting=led_setting,
            remote_reset=remote_reset,
            wifi_control_enable=wifi_control_enable,
            rssi_led_settings=rssi_led_settings,
            tag_ids=tag_ids,
            gps_enable=gps_enable,
            location=location,
            remember_device=remember_device,
            disable_hw_reset=disable_hw_reset,
        )

        ap_general_config.additional_properties = d
        return ap_general_config

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
