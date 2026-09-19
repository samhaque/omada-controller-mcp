from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RogueAPScanResultEntry")


@_attrs_define
class RogueAPScanResultEntry:
    """
    Attributes:
        id (str | Unset): ID of the entry
        ssid (str | Unset): Name of SSID
        bssid (str | Unset): The MAC address of the network device, used as the unique identifier of the network
        radio_id (int | Unset): (Wireless) Radio ID should be a value as follows: 0: 2.4GHz; 1: 5GHz-1; 2:5GHz-2; 3:
            6GHz
        security (int | Unset): The encryption method of the network. 0: None  1: WEP  2: WPA-Enterprise  3: WPA-
            Personal  4:WPA3-SAE , 15:Unknown, the other unspecified return values are also displayed as Unknown
        beacon (int | Unset): The time interval for the network device to send Beacon frames
        channel (int | Unset): Channel
        nearest_ap_mac (str | Unset): The AP that scanned the network device
        nearest_ap (str | Unset): The AP name
        mode (int | Unset): 0: 11a  1: 11b  2: 11g  3: 11na  4: 11ng  5: 11ac  6: 11axa  7: 11axg
        signal (int | Unset): The signal strength of the network device, unit: dBm
        last_seen (int | Unset): The timestamp corresponding to the time when the network device was last scanned, unit:
            ms
    """

    id: str | Unset = UNSET
    ssid: str | Unset = UNSET
    bssid: str | Unset = UNSET
    radio_id: int | Unset = UNSET
    security: int | Unset = UNSET
    beacon: int | Unset = UNSET
    channel: int | Unset = UNSET
    nearest_ap_mac: str | Unset = UNSET
    nearest_ap: str | Unset = UNSET
    mode: int | Unset = UNSET
    signal: int | Unset = UNSET
    last_seen: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        ssid = self.ssid

        bssid = self.bssid

        radio_id = self.radio_id

        security = self.security

        beacon = self.beacon

        channel = self.channel

        nearest_ap_mac = self.nearest_ap_mac

        nearest_ap = self.nearest_ap

        mode = self.mode

        signal = self.signal

        last_seen = self.last_seen

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if ssid is not UNSET:
            field_dict["ssid"] = ssid
        if bssid is not UNSET:
            field_dict["bssid"] = bssid
        if radio_id is not UNSET:
            field_dict["radioId"] = radio_id
        if security is not UNSET:
            field_dict["security"] = security
        if beacon is not UNSET:
            field_dict["beacon"] = beacon
        if channel is not UNSET:
            field_dict["channel"] = channel
        if nearest_ap_mac is not UNSET:
            field_dict["nearestApMac"] = nearest_ap_mac
        if nearest_ap is not UNSET:
            field_dict["nearestAp"] = nearest_ap
        if mode is not UNSET:
            field_dict["mode"] = mode
        if signal is not UNSET:
            field_dict["signal"] = signal
        if last_seen is not UNSET:
            field_dict["lastSeen"] = last_seen

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        ssid = d.pop("ssid", UNSET)

        bssid = d.pop("bssid", UNSET)

        radio_id = d.pop("radioId", UNSET)

        security = d.pop("security", UNSET)

        beacon = d.pop("beacon", UNSET)

        channel = d.pop("channel", UNSET)

        nearest_ap_mac = d.pop("nearestApMac", UNSET)

        nearest_ap = d.pop("nearestAp", UNSET)

        mode = d.pop("mode", UNSET)

        signal = d.pop("signal", UNSET)

        last_seen = d.pop("lastSeen", UNSET)

        rogue_ap_scan_result_entry = cls(
            id=id,
            ssid=ssid,
            bssid=bssid,
            radio_id=radio_id,
            security=security,
            beacon=beacon,
            channel=channel,
            nearest_ap_mac=nearest_ap_mac,
            nearest_ap=nearest_ap,
            mode=mode,
            signal=signal,
            last_seen=last_seen,
        )

        rogue_ap_scan_result_entry.additional_properties = d
        return rogue_ap_scan_result_entry

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
