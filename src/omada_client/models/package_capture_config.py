from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PackageCaptureConfig")


@_attrs_define
class PackageCaptureConfig:
    """
    Attributes:
        duration (int | Unset): Packet capture duration, in seconds.
        interface_type (int | Unset): Interface type. 0: Wired; 1: Wireless; 2: LAN Network.
        single_package_size (int | Unset): Single package size, in bytes.
        channel (int | Unset): (Wireless)  0: 2.4GHz  1: 5GHz-1  2:5GHz-2 3: 6GHz
        interface_name (str | Unset): Interface name.
        interface_id (str | Unset): Interface ID, for example: if interfaceType is network, interfaceId should be LAN
            network ID. LAN Network can be created using 'Create LAN network' interface, and LAN Network ID can be obtained
            from 'Get LAN network list' interface.
        filter_rules (str | Unset): Filter rules.
        capture_mode (int | Unset): Capture mode. 0: Local packet capture; 1: Flow-mode packet capture.
        ar_channel (int | Unset): Channel.
        ota_filter_rules (str | Unset): Filter rules of air interface packet capture.
        src_mac (int | Unset): Source L4 port of the packet.
        dest_mac (str | Unset): Destination MAC address of the packet.
        dest_port (int | Unset): Destination L4 port of the packet.
        src_ip (str | Unset): IP address of the message sender.
        dest_ip (str | Unset): Destination IP address of the packet.
        protocol (int | Unset): Packet type/protocol. It's required when a Switch captures packets.
        stack (bool | Unset): Whether the device supports stacking.
        unit (int | Unset): Equipment unit ID.
    """

    duration: int | Unset = UNSET
    interface_type: int | Unset = UNSET
    single_package_size: int | Unset = UNSET
    channel: int | Unset = UNSET
    interface_name: str | Unset = UNSET
    interface_id: str | Unset = UNSET
    filter_rules: str | Unset = UNSET
    capture_mode: int | Unset = UNSET
    ar_channel: int | Unset = UNSET
    ota_filter_rules: str | Unset = UNSET
    src_mac: int | Unset = UNSET
    dest_mac: str | Unset = UNSET
    dest_port: int | Unset = UNSET
    src_ip: str | Unset = UNSET
    dest_ip: str | Unset = UNSET
    protocol: int | Unset = UNSET
    stack: bool | Unset = UNSET
    unit: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duration = self.duration

        interface_type = self.interface_type

        single_package_size = self.single_package_size

        channel = self.channel

        interface_name = self.interface_name

        interface_id = self.interface_id

        filter_rules = self.filter_rules

        capture_mode = self.capture_mode

        ar_channel = self.ar_channel

        ota_filter_rules = self.ota_filter_rules

        src_mac = self.src_mac

        dest_mac = self.dest_mac

        dest_port = self.dest_port

        src_ip = self.src_ip

        dest_ip = self.dest_ip

        protocol = self.protocol

        stack = self.stack

        unit = self.unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if duration is not UNSET:
            field_dict["duration"] = duration
        if interface_type is not UNSET:
            field_dict["interfaceType"] = interface_type
        if single_package_size is not UNSET:
            field_dict["singlePackageSize"] = single_package_size
        if channel is not UNSET:
            field_dict["channel"] = channel
        if interface_name is not UNSET:
            field_dict["interfaceName"] = interface_name
        if interface_id is not UNSET:
            field_dict["interfaceId"] = interface_id
        if filter_rules is not UNSET:
            field_dict["filterRules"] = filter_rules
        if capture_mode is not UNSET:
            field_dict["captureMode"] = capture_mode
        if ar_channel is not UNSET:
            field_dict["arChannel"] = ar_channel
        if ota_filter_rules is not UNSET:
            field_dict["otaFilterRules"] = ota_filter_rules
        if src_mac is not UNSET:
            field_dict["srcMac"] = src_mac
        if dest_mac is not UNSET:
            field_dict["destMac"] = dest_mac
        if dest_port is not UNSET:
            field_dict["destPort"] = dest_port
        if src_ip is not UNSET:
            field_dict["srcIp"] = src_ip
        if dest_ip is not UNSET:
            field_dict["destIp"] = dest_ip
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if stack is not UNSET:
            field_dict["stack"] = stack
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        duration = d.pop("duration", UNSET)

        interface_type = d.pop("interfaceType", UNSET)

        single_package_size = d.pop("singlePackageSize", UNSET)

        channel = d.pop("channel", UNSET)

        interface_name = d.pop("interfaceName", UNSET)

        interface_id = d.pop("interfaceId", UNSET)

        filter_rules = d.pop("filterRules", UNSET)

        capture_mode = d.pop("captureMode", UNSET)

        ar_channel = d.pop("arChannel", UNSET)

        ota_filter_rules = d.pop("otaFilterRules", UNSET)

        src_mac = d.pop("srcMac", UNSET)

        dest_mac = d.pop("destMac", UNSET)

        dest_port = d.pop("destPort", UNSET)

        src_ip = d.pop("srcIp", UNSET)

        dest_ip = d.pop("destIp", UNSET)

        protocol = d.pop("protocol", UNSET)

        stack = d.pop("stack", UNSET)

        unit = d.pop("unit", UNSET)

        package_capture_config = cls(
            duration=duration,
            interface_type=interface_type,
            single_package_size=single_package_size,
            channel=channel,
            interface_name=interface_name,
            interface_id=interface_id,
            filter_rules=filter_rules,
            capture_mode=capture_mode,
            ar_channel=ar_channel,
            ota_filter_rules=ota_filter_rules,
            src_mac=src_mac,
            dest_mac=dest_mac,
            dest_port=dest_port,
            src_ip=src_ip,
            dest_ip=dest_ip,
            protocol=protocol,
            stack=stack,
            unit=unit,
        )

        package_capture_config.additional_properties = d
        return package_capture_config

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
