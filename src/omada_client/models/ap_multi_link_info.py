from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="APMultiLinkInfo")


@_attrs_define
class APMultiLinkInfo:
    """Multi link info (MLO)

    Attributes:
        radio_id (int | Unset): Radio ID should be a value as follows: 0: 2.4GHz; 1: 5GHz-1; 2:5GHz-2; 3: 6GHz.
        channel (int | Unset): (Wireless)  Actual channel.
        rssi (int | Unset): Signal strength, unit: dBm.
        traffic_down (int | Unset): Downstream traffic (Byte).
        traffic_up (int | Unset): Upstream traffic (Byte).
        tx_rate (int | Unset): Downlink negotiation rate (Kbit/s)
        rx_rate (int | Unset): Uplink negotiation rate (Kbit/s)
    """

    radio_id: int | Unset = UNSET
    channel: int | Unset = UNSET
    rssi: int | Unset = UNSET
    traffic_down: int | Unset = UNSET
    traffic_up: int | Unset = UNSET
    tx_rate: int | Unset = UNSET
    rx_rate: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        radio_id = self.radio_id

        channel = self.channel

        rssi = self.rssi

        traffic_down = self.traffic_down

        traffic_up = self.traffic_up

        tx_rate = self.tx_rate

        rx_rate = self.rx_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if radio_id is not UNSET:
            field_dict["radioId"] = radio_id
        if channel is not UNSET:
            field_dict["channel"] = channel
        if rssi is not UNSET:
            field_dict["rssi"] = rssi
        if traffic_down is not UNSET:
            field_dict["trafficDown"] = traffic_down
        if traffic_up is not UNSET:
            field_dict["trafficUp"] = traffic_up
        if tx_rate is not UNSET:
            field_dict["txRate"] = tx_rate
        if rx_rate is not UNSET:
            field_dict["rxRate"] = rx_rate

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        radio_id = d.pop("radioId", UNSET)

        channel = d.pop("channel", UNSET)

        rssi = d.pop("rssi", UNSET)

        traffic_down = d.pop("trafficDown", UNSET)

        traffic_up = d.pop("trafficUp", UNSET)

        tx_rate = d.pop("txRate", UNSET)

        rx_rate = d.pop("rxRate", UNSET)

        ap_multi_link_info = cls(
            radio_id=radio_id,
            channel=channel,
            rssi=rssi,
            traffic_down=traffic_down,
            traffic_up=traffic_up,
            tx_rate=tx_rate,
            rx_rate=rx_rate,
        )

        ap_multi_link_info.additional_properties = d
        return ap_multi_link_info

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
