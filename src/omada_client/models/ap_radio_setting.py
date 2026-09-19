from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApRadioSetting")


@_attrs_define
class ApRadioSetting:
    """Radio Setting

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
        auto_switch_off_wifi (bool | Unset): Enable auto Switch Off Wifi
        auto_switch_off_wifi_interval (int | Unset): Auto Switch Off Wifi Interval
        rrm_type (int | Unset):
        inter_time_stamp (int | Unset):
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
    auto_switch_off_wifi: bool | Unset = UNSET
    auto_switch_off_wifi_interval: int | Unset = UNSET
    rrm_type: int | Unset = UNSET
    inter_time_stamp: int | Unset = UNSET
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

        auto_switch_off_wifi = self.auto_switch_off_wifi

        auto_switch_off_wifi_interval = self.auto_switch_off_wifi_interval

        rrm_type = self.rrm_type

        inter_time_stamp = self.inter_time_stamp

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
        if auto_switch_off_wifi is not UNSET:
            field_dict["autoSwitchOffWifi"] = auto_switch_off_wifi
        if auto_switch_off_wifi_interval is not UNSET:
            field_dict["autoSwitchOffWifiInterval"] = auto_switch_off_wifi_interval
        if rrm_type is not UNSET:
            field_dict["rrmType"] = rrm_type
        if inter_time_stamp is not UNSET:
            field_dict["interTimeStamp"] = inter_time_stamp

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

        auto_switch_off_wifi = d.pop("autoSwitchOffWifi", UNSET)

        auto_switch_off_wifi_interval = d.pop("autoSwitchOffWifiInterval", UNSET)

        rrm_type = d.pop("rrmType", UNSET)

        inter_time_stamp = d.pop("interTimeStamp", UNSET)

        ap_radio_setting = cls(
            radio_enable=radio_enable,
            channel_range=channel_range,
            channel_width=channel_width,
            channel=channel,
            tx_power=tx_power,
            tx_power_level=tx_power_level,
            channel_limit_enable=channel_limit_enable,
            freq=freq,
            wireless_mode=wireless_mode,
            auto_switch_off_wifi=auto_switch_off_wifi,
            auto_switch_off_wifi_interval=auto_switch_off_wifi_interval,
            rrm_type=rrm_type,
            inter_time_stamp=inter_time_stamp,
        )

        ap_radio_setting.additional_properties = d
        return ap_radio_setting

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
