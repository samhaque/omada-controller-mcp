from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OltPortStatOpenApiVO")


@_attrs_define
class OltPortStatOpenApiVO:
    """Traffic information of ports

    Attributes:
        port (str | Unset): Port of OLT
        tx (int | Unset): Transmit traffic of the port, in bytes
        rx (int | Unset): Receive traffic of the port, in bytes
        tx_packets (int | Unset): Transmit packets of the port
        rx_packets (int | Unset): Receive receive packets of the port
        tx_broadcast_packets (int | Unset): Transmit broadcast packets
        rx_broadcast_packets (int | Unset): Receive broadcast packets
        tx_multicast_packets (int | Unset): Transmit multicast packets
        rx_multicast_packets (int | Unset): Receive multicast packets
        tx_rate (float | Unset): Transmit rate, byte/s
        rx_rate (float | Unset): Receive rate, byte/s
    """

    port: str | Unset = UNSET
    tx: int | Unset = UNSET
    rx: int | Unset = UNSET
    tx_packets: int | Unset = UNSET
    rx_packets: int | Unset = UNSET
    tx_broadcast_packets: int | Unset = UNSET
    rx_broadcast_packets: int | Unset = UNSET
    tx_multicast_packets: int | Unset = UNSET
    rx_multicast_packets: int | Unset = UNSET
    tx_rate: float | Unset = UNSET
    rx_rate: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        tx = self.tx

        rx = self.rx

        tx_packets = self.tx_packets

        rx_packets = self.rx_packets

        tx_broadcast_packets = self.tx_broadcast_packets

        rx_broadcast_packets = self.rx_broadcast_packets

        tx_multicast_packets = self.tx_multicast_packets

        rx_multicast_packets = self.rx_multicast_packets

        tx_rate = self.tx_rate

        rx_rate = self.rx_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if tx is not UNSET:
            field_dict["tx"] = tx
        if rx is not UNSET:
            field_dict["rx"] = rx
        if tx_packets is not UNSET:
            field_dict["txPackets"] = tx_packets
        if rx_packets is not UNSET:
            field_dict["rxPackets"] = rx_packets
        if tx_broadcast_packets is not UNSET:
            field_dict["txBroadcastPackets"] = tx_broadcast_packets
        if rx_broadcast_packets is not UNSET:
            field_dict["rxBroadcastPackets"] = rx_broadcast_packets
        if tx_multicast_packets is not UNSET:
            field_dict["txMulticastPackets"] = tx_multicast_packets
        if rx_multicast_packets is not UNSET:
            field_dict["rxMulticastPackets"] = rx_multicast_packets
        if tx_rate is not UNSET:
            field_dict["txRate"] = tx_rate
        if rx_rate is not UNSET:
            field_dict["rxRate"] = rx_rate

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port = d.pop("port", UNSET)

        tx = d.pop("tx", UNSET)

        rx = d.pop("rx", UNSET)

        tx_packets = d.pop("txPackets", UNSET)

        rx_packets = d.pop("rxPackets", UNSET)

        tx_broadcast_packets = d.pop("txBroadcastPackets", UNSET)

        rx_broadcast_packets = d.pop("rxBroadcastPackets", UNSET)

        tx_multicast_packets = d.pop("txMulticastPackets", UNSET)

        rx_multicast_packets = d.pop("rxMulticastPackets", UNSET)

        tx_rate = d.pop("txRate", UNSET)

        rx_rate = d.pop("rxRate", UNSET)

        olt_port_stat_open_api_vo = cls(
            port=port,
            tx=tx,
            rx=rx,
            tx_packets=tx_packets,
            rx_packets=rx_packets,
            tx_broadcast_packets=tx_broadcast_packets,
            rx_broadcast_packets=rx_broadcast_packets,
            tx_multicast_packets=tx_multicast_packets,
            rx_multicast_packets=rx_multicast_packets,
            tx_rate=tx_rate,
            rx_rate=rx_rate,
        )

        olt_port_stat_open_api_vo.additional_properties = d
        return olt_port_stat_open_api_vo

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
