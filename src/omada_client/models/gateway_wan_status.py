from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="GatewayWanStatus")


@_attrs_define
class GatewayWanStatus:
    """wan status infos.

    Attributes:
        port (int | Unset): Port serial number
        name (str | Unset): Port name
        type_ (int | Unset): Port type, 0:WAN,1:WAN/LAN,2:LAN,3:SFP WAN;
        physical_type (int | Unset): SFP port type, 0:normal,1:SFP,2:SFP+;
        mode (int | Unset): Port mode, 0:WAN,1:LAN;
        status (int | Unset): Port status should be a value as follows: 0: disconnected; 1: connected
        internet_state (int | Unset): Wan internet state should be a value as follows: 0: disconnected; 1: connected
        ip (str | Unset): WAN ip address.
        online_detection (int | Unset): online status, 0-offline, 1-online
        ip2 (str | Unset): Secondary ip address.
        speed (int | Unset): Port speed, 1-10M，2-100M，3-1000M
        duplex (int | Unset): Port duplex, 1-Half，2-Full
        rx (int | Unset): Port total rx bytes
        rx_pkt (int | Unset): Port total rx packets
        rx_pkt_rate (int | Unset): Port rx Packet rate, Unit: Pkt/s;
        rx_rate (int | Unset): Port rx rate, Unit: KB/s;
        tx (int | Unset): Port total tx bytes
        tx_pkt (int | Unset): Port total tx packets
        tx_pkt_rate (int | Unset): Port tx packet rate, Unit: Pkt/s;
        tx_rate (int | Unset): Port tx rate, Unit: KB/s;
        proto (str | Unset): Wan ipv4 proto type, use static，dhcp，pppoe，l2tp，pptp.
        health_level (int | Unset): Wan health level. 0-GOOD, 1-FAIR, 2-POOR, 3-NO_DATA, 4-OFFLINE, 5-DISABLE, 6-ONLINE
        latency (int | Unset): Wan latency, when mode is wan and device is connected, Unit: ms
        loss (float | Unset): Wan packet loss rate, Unit : %
        rx_error_pkts (int | Unset): rx error pkts.
        tx_error_pkts (int | Unset): tx error pkts.
    """

    port: int | Unset = UNSET
    name: str | Unset = UNSET
    type_: int | Unset = UNSET
    physical_type: int | Unset = UNSET
    mode: int | Unset = UNSET
    status: int | Unset = UNSET
    internet_state: int | Unset = UNSET
    ip: str | Unset = UNSET
    online_detection: int | Unset = UNSET
    ip2: str | Unset = UNSET
    speed: int | Unset = UNSET
    duplex: int | Unset = UNSET
    rx: int | Unset = UNSET
    rx_pkt: int | Unset = UNSET
    rx_pkt_rate: int | Unset = UNSET
    rx_rate: int | Unset = UNSET
    tx: int | Unset = UNSET
    tx_pkt: int | Unset = UNSET
    tx_pkt_rate: int | Unset = UNSET
    tx_rate: int | Unset = UNSET
    proto: str | Unset = UNSET
    health_level: int | Unset = UNSET
    latency: int | Unset = UNSET
    loss: float | Unset = UNSET
    rx_error_pkts: int | Unset = UNSET
    tx_error_pkts: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        name = self.name

        type_ = self.type_

        physical_type = self.physical_type

        mode = self.mode

        status = self.status

        internet_state = self.internet_state

        ip = self.ip

        online_detection = self.online_detection

        ip2 = self.ip2

        speed = self.speed

        duplex = self.duplex

        rx = self.rx

        rx_pkt = self.rx_pkt

        rx_pkt_rate = self.rx_pkt_rate

        rx_rate = self.rx_rate

        tx = self.tx

        tx_pkt = self.tx_pkt

        tx_pkt_rate = self.tx_pkt_rate

        tx_rate = self.tx_rate

        proto = self.proto

        health_level = self.health_level

        latency = self.latency

        loss = self.loss

        rx_error_pkts = self.rx_error_pkts

        tx_error_pkts = self.tx_error_pkts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if physical_type is not UNSET:
            field_dict["physicalType"] = physical_type
        if mode is not UNSET:
            field_dict["mode"] = mode
        if status is not UNSET:
            field_dict["status"] = status
        if internet_state is not UNSET:
            field_dict["internetState"] = internet_state
        if ip is not UNSET:
            field_dict["ip"] = ip
        if online_detection is not UNSET:
            field_dict["onlineDetection"] = online_detection
        if ip2 is not UNSET:
            field_dict["ip2"] = ip2
        if speed is not UNSET:
            field_dict["speed"] = speed
        if duplex is not UNSET:
            field_dict["duplex"] = duplex
        if rx is not UNSET:
            field_dict["rx"] = rx
        if rx_pkt is not UNSET:
            field_dict["rxPkt"] = rx_pkt
        if rx_pkt_rate is not UNSET:
            field_dict["rxPktRate"] = rx_pkt_rate
        if rx_rate is not UNSET:
            field_dict["rxRate"] = rx_rate
        if tx is not UNSET:
            field_dict["tx"] = tx
        if tx_pkt is not UNSET:
            field_dict["txPkt"] = tx_pkt
        if tx_pkt_rate is not UNSET:
            field_dict["txPktRate"] = tx_pkt_rate
        if tx_rate is not UNSET:
            field_dict["txRate"] = tx_rate
        if proto is not UNSET:
            field_dict["proto"] = proto
        if health_level is not UNSET:
            field_dict["healthLevel"] = health_level
        if latency is not UNSET:
            field_dict["latency"] = latency
        if loss is not UNSET:
            field_dict["loss"] = loss
        if rx_error_pkts is not UNSET:
            field_dict["rxErrorPkts"] = rx_error_pkts
        if tx_error_pkts is not UNSET:
            field_dict["txErrorPkts"] = tx_error_pkts

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port = d.pop("port", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        physical_type = d.pop("physicalType", UNSET)

        mode = d.pop("mode", UNSET)

        status = d.pop("status", UNSET)

        internet_state = d.pop("internetState", UNSET)

        ip = d.pop("ip", UNSET)

        online_detection = d.pop("onlineDetection", UNSET)

        ip2 = d.pop("ip2", UNSET)

        speed = d.pop("speed", UNSET)

        duplex = d.pop("duplex", UNSET)

        rx = d.pop("rx", UNSET)

        rx_pkt = d.pop("rxPkt", UNSET)

        rx_pkt_rate = d.pop("rxPktRate", UNSET)

        rx_rate = d.pop("rxRate", UNSET)

        tx = d.pop("tx", UNSET)

        tx_pkt = d.pop("txPkt", UNSET)

        tx_pkt_rate = d.pop("txPktRate", UNSET)

        tx_rate = d.pop("txRate", UNSET)

        proto = d.pop("proto", UNSET)

        health_level = d.pop("healthLevel", UNSET)

        latency = d.pop("latency", UNSET)

        loss = d.pop("loss", UNSET)

        rx_error_pkts = d.pop("rxErrorPkts", UNSET)

        tx_error_pkts = d.pop("txErrorPkts", UNSET)

        gateway_wan_status = cls(
            port=port,
            name=name,
            type_=type_,
            physical_type=physical_type,
            mode=mode,
            status=status,
            internet_state=internet_state,
            ip=ip,
            online_detection=online_detection,
            ip2=ip2,
            speed=speed,
            duplex=duplex,
            rx=rx,
            rx_pkt=rx_pkt,
            rx_pkt_rate=rx_pkt_rate,
            rx_rate=rx_rate,
            tx=tx,
            tx_pkt=tx_pkt,
            tx_pkt_rate=tx_pkt_rate,
            tx_rate=tx_rate,
            proto=proto,
            health_level=health_level,
            latency=latency,
            loss=loss,
            rx_error_pkts=rx_error_pkts,
            tx_error_pkts=tx_error_pkts,
        )

        gateway_wan_status.additional_properties = d
        return gateway_wan_status

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
