from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApWiredUplinkInfo")


@_attrs_define
class ApWiredUplinkInfo:
    """Wired uplink info

    Attributes:
        uplink_mac (str | Unset): Uplink device MAC address
        stack_id (str | Unset):
        type_ (str | Unset): Uplink device type
        name (str | Unset): Uplink device name
        rate (str | Unset): Negotiation rate, LAN(connected): 10,100,1000,2500,10000, LAN(disconnected):0, Unit:Mbps
        duplex (int | Unset): Duplex should be a value as follows: 0: LAN disconnected; 1: half; 2: full
        up_bytes (int | Unset): Unit: Byte
        down_bytes (int | Unset): Unit: Byte
        up_packets (int | Unset): Uplink Device upPackets
        down_packets (int | Unset): Uplink Device downPackets
        up_drop_packets (int | Unset): Uplink Device upDropPackets
        down_drop_packets (int | Unset): Uplink Device downDropPackets
        up_errors_packets (int | Unset): Uplink Device upErrorsPackets
        down_errors_packets (int | Unset): Uplink Device downErrorsPackets
        activity (int | Unset): (Change of( downBytes+upBytes))/ time, Unit: Bytes/s
        port (str | Unset): Uplink port ID, only supported by some devices.
        ip (str | Unset): Uplink device ip.
        port_type (int | Unset): Port Type, 0:ETH, 1:POTS, 2:SFP
        tx_power (float | Unset): Tx power, only supported by some devices.
        rx_power (float | Unset): Rx Power, only supported by some devices.
        temp (float | Unset): Temperature, only supported by some devices.
        voltage (float | Unset): Voltage, only supported by some devices.
        current (float | Unset): Current, only supported by some devices.
        model (str | Unset): Uplink device model
        model_version (str | Unset): Uplink device modelVersion
        uplink_port (str | Unset): Uplink device port
        link_status (int | Unset): Uplink port link status
        link_speed (int | Unset): Uplink port link speed
        poe_state (int | Unset): PoE state, 0: powering, 1: not powering
        voip_state (int | Unset): VoIP state, 0: off-hook, 1: on-hook
    """

    uplink_mac: str | Unset = UNSET
    stack_id: str | Unset = UNSET
    type_: str | Unset = UNSET
    name: str | Unset = UNSET
    rate: str | Unset = UNSET
    duplex: int | Unset = UNSET
    up_bytes: int | Unset = UNSET
    down_bytes: int | Unset = UNSET
    up_packets: int | Unset = UNSET
    down_packets: int | Unset = UNSET
    up_drop_packets: int | Unset = UNSET
    down_drop_packets: int | Unset = UNSET
    up_errors_packets: int | Unset = UNSET
    down_errors_packets: int | Unset = UNSET
    activity: int | Unset = UNSET
    port: str | Unset = UNSET
    ip: str | Unset = UNSET
    port_type: int | Unset = UNSET
    tx_power: float | Unset = UNSET
    rx_power: float | Unset = UNSET
    temp: float | Unset = UNSET
    voltage: float | Unset = UNSET
    current: float | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    uplink_port: str | Unset = UNSET
    link_status: int | Unset = UNSET
    link_speed: int | Unset = UNSET
    poe_state: int | Unset = UNSET
    voip_state: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uplink_mac = self.uplink_mac

        stack_id = self.stack_id

        type_ = self.type_

        name = self.name

        rate = self.rate

        duplex = self.duplex

        up_bytes = self.up_bytes

        down_bytes = self.down_bytes

        up_packets = self.up_packets

        down_packets = self.down_packets

        up_drop_packets = self.up_drop_packets

        down_drop_packets = self.down_drop_packets

        up_errors_packets = self.up_errors_packets

        down_errors_packets = self.down_errors_packets

        activity = self.activity

        port = self.port

        ip = self.ip

        port_type = self.port_type

        tx_power = self.tx_power

        rx_power = self.rx_power

        temp = self.temp

        voltage = self.voltage

        current = self.current

        model = self.model

        model_version = self.model_version

        uplink_port = self.uplink_port

        link_status = self.link_status

        link_speed = self.link_speed

        poe_state = self.poe_state

        voip_state = self.voip_state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uplink_mac is not UNSET:
            field_dict["uplinkMac"] = uplink_mac
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if name is not UNSET:
            field_dict["name"] = name
        if rate is not UNSET:
            field_dict["rate"] = rate
        if duplex is not UNSET:
            field_dict["duplex"] = duplex
        if up_bytes is not UNSET:
            field_dict["upBytes"] = up_bytes
        if down_bytes is not UNSET:
            field_dict["downBytes"] = down_bytes
        if up_packets is not UNSET:
            field_dict["upPackets"] = up_packets
        if down_packets is not UNSET:
            field_dict["downPackets"] = down_packets
        if up_drop_packets is not UNSET:
            field_dict["upDropPackets"] = up_drop_packets
        if down_drop_packets is not UNSET:
            field_dict["downDropPackets"] = down_drop_packets
        if up_errors_packets is not UNSET:
            field_dict["upErrorsPackets"] = up_errors_packets
        if down_errors_packets is not UNSET:
            field_dict["downErrorsPackets"] = down_errors_packets
        if activity is not UNSET:
            field_dict["activity"] = activity
        if port is not UNSET:
            field_dict["port"] = port
        if ip is not UNSET:
            field_dict["ip"] = ip
        if port_type is not UNSET:
            field_dict["portType"] = port_type
        if tx_power is not UNSET:
            field_dict["txPower"] = tx_power
        if rx_power is not UNSET:
            field_dict["rxPower"] = rx_power
        if temp is not UNSET:
            field_dict["temp"] = temp
        if voltage is not UNSET:
            field_dict["voltage"] = voltage
        if current is not UNSET:
            field_dict["current"] = current
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if uplink_port is not UNSET:
            field_dict["uplinkPort"] = uplink_port
        if link_status is not UNSET:
            field_dict["linkStatus"] = link_status
        if link_speed is not UNSET:
            field_dict["linkSpeed"] = link_speed
        if poe_state is not UNSET:
            field_dict["poeState"] = poe_state
        if voip_state is not UNSET:
            field_dict["voipState"] = voip_state

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        uplink_mac = d.pop("uplinkMac", UNSET)

        stack_id = d.pop("stackId", UNSET)

        type_ = d.pop("type", UNSET)

        name = d.pop("name", UNSET)

        rate = d.pop("rate", UNSET)

        duplex = d.pop("duplex", UNSET)

        up_bytes = d.pop("upBytes", UNSET)

        down_bytes = d.pop("downBytes", UNSET)

        up_packets = d.pop("upPackets", UNSET)

        down_packets = d.pop("downPackets", UNSET)

        up_drop_packets = d.pop("upDropPackets", UNSET)

        down_drop_packets = d.pop("downDropPackets", UNSET)

        up_errors_packets = d.pop("upErrorsPackets", UNSET)

        down_errors_packets = d.pop("downErrorsPackets", UNSET)

        activity = d.pop("activity", UNSET)

        port = d.pop("port", UNSET)

        ip = d.pop("ip", UNSET)

        port_type = d.pop("portType", UNSET)

        tx_power = d.pop("txPower", UNSET)

        rx_power = d.pop("rxPower", UNSET)

        temp = d.pop("temp", UNSET)

        voltage = d.pop("voltage", UNSET)

        current = d.pop("current", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        uplink_port = d.pop("uplinkPort", UNSET)

        link_status = d.pop("linkStatus", UNSET)

        link_speed = d.pop("linkSpeed", UNSET)

        poe_state = d.pop("poeState", UNSET)

        voip_state = d.pop("voipState", UNSET)

        ap_wired_uplink_info = cls(
            uplink_mac=uplink_mac,
            stack_id=stack_id,
            type_=type_,
            name=name,
            rate=rate,
            duplex=duplex,
            up_bytes=up_bytes,
            down_bytes=down_bytes,
            up_packets=up_packets,
            down_packets=down_packets,
            up_drop_packets=up_drop_packets,
            down_drop_packets=down_drop_packets,
            up_errors_packets=up_errors_packets,
            down_errors_packets=down_errors_packets,
            activity=activity,
            port=port,
            ip=ip,
            port_type=port_type,
            tx_power=tx_power,
            rx_power=rx_power,
            temp=temp,
            voltage=voltage,
            current=current,
            model=model,
            model_version=model_version,
            uplink_port=uplink_port,
            link_status=link_status,
            link_speed=link_speed,
            poe_state=poe_state,
            voip_state=voip_state,
        )

        ap_wired_uplink_info.additional_properties = d
        return ap_wired_uplink_info

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
