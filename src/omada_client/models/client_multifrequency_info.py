from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientMultifrequencyInfo")


@_attrs_define
class ClientMultifrequencyInfo:
    """(Wireless) Client multifrequency info list.

    Attributes:
        radio_id (int | Unset): Radio ID should be a value as follows: 0: 2.4GHz; 1: 5GHz-1; 2:5GHz-2; 3: 6GHz.
        wifi_mode (int | Unset): Wi-Fi mode should be a value as follows: 0: 11a; 1: 11b; 2: 11g; 3: 11na; 4: 11ng; 5:
            11ac; 6: 11axa; 7: 11axg.
        channel (int | Unset): (Wireless)  Actual channel.
        rx_rate (int | Unset): (Wireless) Uplink negotiation rate (Kbit/s).
        tx_rate (int | Unset): (Wireless) Downlink negotiation rate (Kbit/s).
        power_save (bool | Unset): (Wireless)  true: Power save mode enabled.
        rssi (int | Unset): (Wireless) Signal strength, unit: dBm.
        snr (int | Unset): (Wireless) Signal Noise Ratio.
        signal_level (int | Unset): (Wireless) Signal strength percentage should be within the range of 0-100.
        signal_rank (int | Unset): (Wireless) Signal strength level should be within the range of 0-5.
        up_packet (int | Unset): Number of upstream packets.
        down_packet (int | Unset): Number of downstream packets.
        traffic_down (int | Unset): Downstream traffic (Byte).
        traffic_up (int | Unset): Upstream traffic (Byte).
        activity (int | Unset): Real-time downlink rate (Byte/s).
        signal_level_and_rank (int | Unset):
    """

    radio_id: int | Unset = UNSET
    wifi_mode: int | Unset = UNSET
    channel: int | Unset = UNSET
    rx_rate: int | Unset = UNSET
    tx_rate: int | Unset = UNSET
    power_save: bool | Unset = UNSET
    rssi: int | Unset = UNSET
    snr: int | Unset = UNSET
    signal_level: int | Unset = UNSET
    signal_rank: int | Unset = UNSET
    up_packet: int | Unset = UNSET
    down_packet: int | Unset = UNSET
    traffic_down: int | Unset = UNSET
    traffic_up: int | Unset = UNSET
    activity: int | Unset = UNSET
    signal_level_and_rank: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        radio_id = self.radio_id

        wifi_mode = self.wifi_mode

        channel = self.channel

        rx_rate = self.rx_rate

        tx_rate = self.tx_rate

        power_save = self.power_save

        rssi = self.rssi

        snr = self.snr

        signal_level = self.signal_level

        signal_rank = self.signal_rank

        up_packet = self.up_packet

        down_packet = self.down_packet

        traffic_down = self.traffic_down

        traffic_up = self.traffic_up

        activity = self.activity

        signal_level_and_rank = self.signal_level_and_rank

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if radio_id is not UNSET:
            field_dict["radioId"] = radio_id
        if wifi_mode is not UNSET:
            field_dict["wifiMode"] = wifi_mode
        if channel is not UNSET:
            field_dict["channel"] = channel
        if rx_rate is not UNSET:
            field_dict["rxRate"] = rx_rate
        if tx_rate is not UNSET:
            field_dict["txRate"] = tx_rate
        if power_save is not UNSET:
            field_dict["powerSave"] = power_save
        if rssi is not UNSET:
            field_dict["rssi"] = rssi
        if snr is not UNSET:
            field_dict["snr"] = snr
        if signal_level is not UNSET:
            field_dict["signalLevel"] = signal_level
        if signal_rank is not UNSET:
            field_dict["signalRank"] = signal_rank
        if up_packet is not UNSET:
            field_dict["upPacket"] = up_packet
        if down_packet is not UNSET:
            field_dict["downPacket"] = down_packet
        if traffic_down is not UNSET:
            field_dict["trafficDown"] = traffic_down
        if traffic_up is not UNSET:
            field_dict["trafficUp"] = traffic_up
        if activity is not UNSET:
            field_dict["activity"] = activity
        if signal_level_and_rank is not UNSET:
            field_dict["signalLevelAndRank"] = signal_level_and_rank

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        radio_id = d.pop("radioId", UNSET)

        wifi_mode = d.pop("wifiMode", UNSET)

        channel = d.pop("channel", UNSET)

        rx_rate = d.pop("rxRate", UNSET)

        tx_rate = d.pop("txRate", UNSET)

        power_save = d.pop("powerSave", UNSET)

        rssi = d.pop("rssi", UNSET)

        snr = d.pop("snr", UNSET)

        signal_level = d.pop("signalLevel", UNSET)

        signal_rank = d.pop("signalRank", UNSET)

        up_packet = d.pop("upPacket", UNSET)

        down_packet = d.pop("downPacket", UNSET)

        traffic_down = d.pop("trafficDown", UNSET)

        traffic_up = d.pop("trafficUp", UNSET)

        activity = d.pop("activity", UNSET)

        signal_level_and_rank = d.pop("signalLevelAndRank", UNSET)

        client_multifrequency_info = cls(
            radio_id=radio_id,
            wifi_mode=wifi_mode,
            channel=channel,
            rx_rate=rx_rate,
            tx_rate=tx_rate,
            power_save=power_save,
            rssi=rssi,
            snr=snr,
            signal_level=signal_level,
            signal_rank=signal_rank,
            up_packet=up_packet,
            down_packet=down_packet,
            traffic_down=traffic_down,
            traffic_up=traffic_up,
            activity=activity,
            signal_level_and_rank=signal_level_and_rank,
        )

        client_multifrequency_info.additional_properties = d
        return client_multifrequency_info

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
