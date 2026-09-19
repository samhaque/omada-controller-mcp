from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="BatchWifiInterferenceOpenApiVO")


@_attrs_define
class BatchWifiInterferenceOpenApiVO:
    """
    Attributes:
        id (str | Unset): id
        bssid (str | Unset): bssid
        ssid (str | Unset): ssid
        radio_id (int | Unset): radio id
        channel (int | Unset): channel
        mode (int | Unset): phyMode
        security (int | Unset): security type. Security should be a value as follows:0: None;1: WEP;2: WPA;3: WPA2;4:
            WPA/WPA2;5: WPE3-OWE;6: WPA3-EnterPrise;7: WPA2-PSK/WPA3-SAE;8: WPA/WPA2-PSK;9: WPA/WPA2-EnterPrise.
        beacon (int | Unset): beacon Interval
        signal (int | Unset): Signal strength
        last_seen (int | Unset): Last detect time.
        nearest_ap (str | Unset): MAC of the AP device closest to that wifi interference.
        band_width (int | Unset): Band Width
    """

    id: str | Unset = UNSET
    bssid: str | Unset = UNSET
    ssid: str | Unset = UNSET
    radio_id: int | Unset = UNSET
    channel: int | Unset = UNSET
    mode: int | Unset = UNSET
    security: int | Unset = UNSET
    beacon: int | Unset = UNSET
    signal: int | Unset = UNSET
    last_seen: int | Unset = UNSET
    nearest_ap: str | Unset = UNSET
    band_width: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        bssid = self.bssid

        ssid = self.ssid

        radio_id = self.radio_id

        channel = self.channel

        mode = self.mode

        security = self.security

        beacon = self.beacon

        signal = self.signal

        last_seen = self.last_seen

        nearest_ap = self.nearest_ap

        band_width = self.band_width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if bssid is not UNSET:
            field_dict["bssid"] = bssid
        if ssid is not UNSET:
            field_dict["ssid"] = ssid
        if radio_id is not UNSET:
            field_dict["radioId"] = radio_id
        if channel is not UNSET:
            field_dict["channel"] = channel
        if mode is not UNSET:
            field_dict["mode"] = mode
        if security is not UNSET:
            field_dict["security"] = security
        if beacon is not UNSET:
            field_dict["beacon"] = beacon
        if signal is not UNSET:
            field_dict["signal"] = signal
        if last_seen is not UNSET:
            field_dict["lastSeen"] = last_seen
        if nearest_ap is not UNSET:
            field_dict["nearestAp"] = nearest_ap
        if band_width is not UNSET:
            field_dict["bandWidth"] = band_width

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        bssid = d.pop("bssid", UNSET)

        ssid = d.pop("ssid", UNSET)

        radio_id = d.pop("radioId", UNSET)

        channel = d.pop("channel", UNSET)

        mode = d.pop("mode", UNSET)

        security = d.pop("security", UNSET)

        beacon = d.pop("beacon", UNSET)

        signal = d.pop("signal", UNSET)

        last_seen = d.pop("lastSeen", UNSET)

        nearest_ap = d.pop("nearestAp", UNSET)

        band_width = d.pop("bandWidth", UNSET)

        batch_wifi_interference_open_api_vo = cls(
            id=id,
            bssid=bssid,
            ssid=ssid,
            radio_id=radio_id,
            channel=channel,
            mode=mode,
            security=security,
            beacon=beacon,
            signal=signal,
            last_seen=last_seen,
            nearest_ap=nearest_ap,
            band_width=band_width,
        )

        batch_wifi_interference_open_api_vo.additional_properties = d
        return batch_wifi_interference_open_api_vo

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
