from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PortForwardingOpenApiVO")


@_attrs_define
class PortForwardingOpenApiVO:
    """
    Attributes:
        omadac_id (str | Unset): Omada ID
        site_id (str | Unset): Site ID
        entry_id (int | Unset): Port Forwarding entry id.
        name (str | Unset): Port Forwarding rule name.
        from_ (int | Unset): 0:Anywhere 1:Limited Address.
        limited_addresses (list[str] | Unset): If the field from is 1,limitedAddresses includes limited addresses.
        interface_wan_port_id (list[str] | Unset): Port Forwarding item id.
        protocol (int | Unset): 0:ALL, 1:TCP, 2:UDP.
        external_port (str | Unset): External Port.
        internal_ip (str | Unset): Internal IP.
        internal_port (str | Unset): Internal Port.
        packets (int | Unset): Packet quantity.
        bytes_ (int | Unset): Total flow in byte.
        lease_duration (int | Unset): Displays the duration of the UPnP port forwarding in seconds.
    """

    omadac_id: str | Unset = UNSET
    site_id: str | Unset = UNSET
    entry_id: int | Unset = UNSET
    name: str | Unset = UNSET
    from_: int | Unset = UNSET
    limited_addresses: list[str] | Unset = UNSET
    interface_wan_port_id: list[str] | Unset = UNSET
    protocol: int | Unset = UNSET
    external_port: str | Unset = UNSET
    internal_ip: str | Unset = UNSET
    internal_port: str | Unset = UNSET
    packets: int | Unset = UNSET
    bytes_: int | Unset = UNSET
    lease_duration: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        omadac_id = self.omadac_id

        site_id = self.site_id

        entry_id = self.entry_id

        name = self.name

        from_ = self.from_

        limited_addresses: list[str] | Unset = UNSET
        if not isinstance(self.limited_addresses, Unset):
            limited_addresses = self.limited_addresses

        interface_wan_port_id: list[str] | Unset = UNSET
        if not isinstance(self.interface_wan_port_id, Unset):
            interface_wan_port_id = self.interface_wan_port_id

        protocol = self.protocol

        external_port = self.external_port

        internal_ip = self.internal_ip

        internal_port = self.internal_port

        packets = self.packets

        bytes_ = self.bytes_

        lease_duration = self.lease_duration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if omadac_id is not UNSET:
            field_dict["omadacId"] = omadac_id
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if entry_id is not UNSET:
            field_dict["entryId"] = entry_id
        if name is not UNSET:
            field_dict["name"] = name
        if from_ is not UNSET:
            field_dict["from"] = from_
        if limited_addresses is not UNSET:
            field_dict["limitedAddresses"] = limited_addresses
        if interface_wan_port_id is not UNSET:
            field_dict["interfaceWanPortId"] = interface_wan_port_id
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if external_port is not UNSET:
            field_dict["externalPort"] = external_port
        if internal_ip is not UNSET:
            field_dict["internalIp"] = internal_ip
        if internal_port is not UNSET:
            field_dict["internalPort"] = internal_port
        if packets is not UNSET:
            field_dict["packets"] = packets
        if bytes_ is not UNSET:
            field_dict["bytes"] = bytes_
        if lease_duration is not UNSET:
            field_dict["leaseDuration"] = lease_duration

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        omadac_id = d.pop("omadacId", UNSET)

        site_id = d.pop("siteId", UNSET)

        entry_id = d.pop("entryId", UNSET)

        name = d.pop("name", UNSET)

        from_ = d.pop("from", UNSET)

        limited_addresses = cast(list[str], d.pop("limitedAddresses", UNSET))

        interface_wan_port_id = cast(list[str], d.pop("interfaceWanPortId", UNSET))

        protocol = d.pop("protocol", UNSET)

        external_port = d.pop("externalPort", UNSET)

        internal_ip = d.pop("internalIp", UNSET)

        internal_port = d.pop("internalPort", UNSET)

        packets = d.pop("packets", UNSET)

        bytes_ = d.pop("bytes", UNSET)

        lease_duration = d.pop("leaseDuration", UNSET)

        port_forwarding_open_api_vo = cls(
            omadac_id=omadac_id,
            site_id=site_id,
            entry_id=entry_id,
            name=name,
            from_=from_,
            limited_addresses=limited_addresses,
            interface_wan_port_id=interface_wan_port_id,
            protocol=protocol,
            external_port=external_port,
            internal_ip=internal_ip,
            internal_port=internal_port,
            packets=packets,
            bytes_=bytes_,
            lease_duration=lease_duration,
        )

        port_forwarding_open_api_vo.additional_properties = d
        return port_forwarding_open_api_vo

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
