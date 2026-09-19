from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApRadioSettingopenApiVO")


@_attrs_define
class ApRadioSettingopenApiVO:
    """Radio setting of 6 GHz.

    Attributes:
        radio_enable (bool | Unset): Enable/Disable radio setting(if false, other params is not required)
        channel_range (list[int] | Unset): Custom optional channel freq collection.
        channel_width (str | Unset): RADIO_20 = 2; RADIO_40 = 3; RADIO_40_20 = 4(corresponding 2G Auto); RADIO_80 = 5;
            RADIO_80_40_20 = 6(corresponding 5G Auto); RADIO_160= 7; RADIO_160_80_40_20 = 8; RADIO_240 = 9; RADIO_320 = 10
        channel (str | Unset): Channel Index; The channel index list supported by device can be obtained from interface
            : Get available channel list of ap; If select auto configuration need to enter 0.
        tx_power (int | Unset): TX Power
        tx_power_level (int | Unset): It should be a value as follows: 0: Low; 1: Medium; 2: High; 3: Custom; 4: Auto
        channel_limit_enable (bool | Unset): Enable channel limit(site level)
        freq (int | Unset): Frequency;The frequency list supported by device can be obtained from interface : Get
            available channel list of ap.The freq and channel fields should be corresponding, otherwise the channel will be
            corrected based on the freq field.
        wireless_mode (int | Unset): Wireless mode config status of the device; -2 : Auto; 3 : 802.11b/g mixed(Only for
            2.4G); 4 : 802.11b/g/n mixed(Only for 2.4G); 13 : 802.11b/g/n/ax mixed(Only for 2.4G); 17 : 802.11b/g/n/ax/be
            mixed(Only for 2.4G); 7 : 802.11a/n mixed(Only for 5G); 10 : 802.11a/n/ac mixed(Only for 5G); 16 :
            802.11a/n/ac/ax mixed(Only for 5G); 18 : 802.11a/n/ac/ax/be mixed(Only for 5G); 11 : 802.11ax only(Only for 6G);
            19 : 802.11ax/be mixed(Only for 6G).
        non_psc_enable (bool | Unset): APP 6G Radio Setting
        auto_switch_off_wifi (bool | Unset): Whether enable to auto switch off wifi
        auto_switch_off_wifi_interval (int | Unset): The interval of auto switch off wifi
    """

    radio_enable: bool | Unset = UNSET
    channel_range: list[int] | Unset = UNSET
    channel_width: str | Unset = UNSET
    channel: str | Unset = UNSET
    tx_power: int | Unset = UNSET
    tx_power_level: int | Unset = UNSET
    channel_limit_enable: bool | Unset = UNSET
    freq: int | Unset = UNSET
    wireless_mode: int | Unset = UNSET
    non_psc_enable: bool | Unset = UNSET
    auto_switch_off_wifi: bool | Unset = UNSET
    auto_switch_off_wifi_interval: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        radio_enable = self.radio_enable

        channel_range: list[int] | Unset = UNSET
        if not isinstance(self.channel_range, Unset):
            channel_range = self.channel_range

        channel_width = self.channel_width

        channel = self.channel

        tx_power = self.tx_power

        tx_power_level = self.tx_power_level

        channel_limit_enable = self.channel_limit_enable

        freq = self.freq

        wireless_mode = self.wireless_mode

        non_psc_enable = self.non_psc_enable

        auto_switch_off_wifi = self.auto_switch_off_wifi

        auto_switch_off_wifi_interval = self.auto_switch_off_wifi_interval

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if radio_enable is not UNSET:
            field_dict["radioEnable"] = radio_enable
        if channel_range is not UNSET:
            field_dict["channelRange"] = channel_range
        if channel_width is not UNSET:
            field_dict["channelWidth"] = channel_width
        if channel is not UNSET:
            field_dict["channel"] = channel
        if tx_power is not UNSET:
            field_dict["txPower"] = tx_power
        if tx_power_level is not UNSET:
            field_dict["txPowerLevel"] = tx_power_level
        if channel_limit_enable is not UNSET:
            field_dict["channelLimitEnable"] = channel_limit_enable
        if freq is not UNSET:
            field_dict["freq"] = freq
        if wireless_mode is not UNSET:
            field_dict["wirelessMode"] = wireless_mode
        if non_psc_enable is not UNSET:
            field_dict["nonPscEnable"] = non_psc_enable
        if auto_switch_off_wifi is not UNSET:
            field_dict["autoSwitchOffWifi"] = auto_switch_off_wifi
        if auto_switch_off_wifi_interval is not UNSET:
            field_dict["autoSwitchOffWifiInterval"] = auto_switch_off_wifi_interval

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        radio_enable = d.pop("radioEnable", UNSET)

        channel_range = cast(list[int], d.pop("channelRange", UNSET))

        channel_width = d.pop("channelWidth", UNSET)

        channel = d.pop("channel", UNSET)

        tx_power = d.pop("txPower", UNSET)

        tx_power_level = d.pop("txPowerLevel", UNSET)

        channel_limit_enable = d.pop("channelLimitEnable", UNSET)

        freq = d.pop("freq", UNSET)

        wireless_mode = d.pop("wirelessMode", UNSET)

        non_psc_enable = d.pop("nonPscEnable", UNSET)

        auto_switch_off_wifi = d.pop("autoSwitchOffWifi", UNSET)

        auto_switch_off_wifi_interval = d.pop("autoSwitchOffWifiInterval", UNSET)

        ap_radio_settingopen_api_vo = cls(
            radio_enable=radio_enable,
            channel_range=channel_range,
            channel_width=channel_width,
            channel=channel,
            tx_power=tx_power,
            tx_power_level=tx_power_level,
            channel_limit_enable=channel_limit_enable,
            freq=freq,
            wireless_mode=wireless_mode,
            non_psc_enable=non_psc_enable,
            auto_switch_off_wifi=auto_switch_off_wifi,
            auto_switch_off_wifi_interval=auto_switch_off_wifi_interval,
        )

        ap_radio_settingopen_api_vo.additional_properties = d
        return ap_radio_settingopen_api_vo

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
