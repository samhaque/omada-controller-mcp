from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PartnerLinkVO")


@_attrs_define
class PartnerLinkVO:
    """Mlo link Info

    Attributes:
        radio_id (int | Unset): radioId, 0:2.4G, 1:5G, 2:5G2, 3:6G
        channel (int | Unset): Uplink AP channel
        rssi (int | Unset): Uplink AP rssi
        snr (int | Unset): Uplink AP Signal-noise ratio
        tx_rate (str | Unset): Uplink AP txRate
        tx_rate_int (int | Unset): Uplink AP txRateInt; Unit: Mbps
        rx_rate (str | Unset): Uplink AP rxRate
        rx_rate_int (int | Unset): Uplink AP rxRateInt; Unit: Mbps
        up_bytes (int | Unset): Uplink AP upBytes; Unit: Byte
        down_bytes (int | Unset): Uplink AP downBytes; Unit:Byte
        up_packets (int | Unset): Uplink AP upPackets
        down_packets (int | Unset): Uplink AP downPackets
        activity (int | Unset): Uplink AP activity: (change of(downBytes+upBytes))/time
        up_rate (int | Unset): Uplink AP upRate: the txRate calculate by Controller
        down_rate (int | Unset): Uplink AP downRate: the rxRate calculate by Controller
    """

    radio_id: int | Unset = UNSET
    channel: int | Unset = UNSET
    rssi: int | Unset = UNSET
    snr: int | Unset = UNSET
    tx_rate: str | Unset = UNSET
    tx_rate_int: int | Unset = UNSET
    rx_rate: str | Unset = UNSET
    rx_rate_int: int | Unset = UNSET
    up_bytes: int | Unset = UNSET
    down_bytes: int | Unset = UNSET
    up_packets: int | Unset = UNSET
    down_packets: int | Unset = UNSET
    activity: int | Unset = UNSET
    up_rate: int | Unset = UNSET
    down_rate: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        radio_id = self.radio_id

        channel = self.channel

        rssi = self.rssi

        snr = self.snr

        tx_rate = self.tx_rate

        tx_rate_int = self.tx_rate_int

        rx_rate = self.rx_rate

        rx_rate_int = self.rx_rate_int

        up_bytes = self.up_bytes

        down_bytes = self.down_bytes

        up_packets = self.up_packets

        down_packets = self.down_packets

        activity = self.activity

        up_rate = self.up_rate

        down_rate = self.down_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if radio_id is not UNSET:
            field_dict["radioId"] = radio_id
        if channel is not UNSET:
            field_dict["channel"] = channel
        if rssi is not UNSET:
            field_dict["rssi"] = rssi
        if snr is not UNSET:
            field_dict["snr"] = snr
        if tx_rate is not UNSET:
            field_dict["txRate"] = tx_rate
        if tx_rate_int is not UNSET:
            field_dict["txRateInt"] = tx_rate_int
        if rx_rate is not UNSET:
            field_dict["rxRate"] = rx_rate
        if rx_rate_int is not UNSET:
            field_dict["rxRateInt"] = rx_rate_int
        if up_bytes is not UNSET:
            field_dict["upBytes"] = up_bytes
        if down_bytes is not UNSET:
            field_dict["downBytes"] = down_bytes
        if up_packets is not UNSET:
            field_dict["upPackets"] = up_packets
        if down_packets is not UNSET:
            field_dict["downPackets"] = down_packets
        if activity is not UNSET:
            field_dict["activity"] = activity
        if up_rate is not UNSET:
            field_dict["upRate"] = up_rate
        if down_rate is not UNSET:
            field_dict["downRate"] = down_rate

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        radio_id = d.pop("radioId", UNSET)

        channel = d.pop("channel", UNSET)

        rssi = d.pop("rssi", UNSET)

        snr = d.pop("snr", UNSET)

        tx_rate = d.pop("txRate", UNSET)

        tx_rate_int = d.pop("txRateInt", UNSET)

        rx_rate = d.pop("rxRate", UNSET)

        rx_rate_int = d.pop("rxRateInt", UNSET)

        up_bytes = d.pop("upBytes", UNSET)

        down_bytes = d.pop("downBytes", UNSET)

        up_packets = d.pop("upPackets", UNSET)

        down_packets = d.pop("downPackets", UNSET)

        activity = d.pop("activity", UNSET)

        up_rate = d.pop("upRate", UNSET)

        down_rate = d.pop("downRate", UNSET)

        partner_link_vo = cls(
            radio_id=radio_id,
            channel=channel,
            rssi=rssi,
            snr=snr,
            tx_rate=tx_rate,
            tx_rate_int=tx_rate_int,
            rx_rate=rx_rate,
            rx_rate_int=rx_rate_int,
            up_bytes=up_bytes,
            down_bytes=down_bytes,
            up_packets=up_packets,
            down_packets=down_packets,
            activity=activity,
            up_rate=up_rate,
            down_rate=down_rate,
        )

        partner_link_vo.additional_properties = d
        return partner_link_vo

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
