from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.port_ip_open_api_vo import PortIpOpenApiVO


T = TypeVar("T", bound="PortForwardingInfoTemplate")


@_attrs_define
class PortForwardingInfoTemplate:
    """
    Attributes:
        name (str): Name, name should contain 1 to 64 characters.
        status (bool): Port-forwarding enable status.
        from_ (int): From corresponds with source IP in web. From should be a value as follows: 0: where; 1: limited
            address
        interface_wan_port_id (list[str]): This field represents WAN port ID. WAN port ID can be obtained from can be
            obtained from 'Get internet basic info' interface.
        forward_ip (str): Forward IP corresponds with destination IP in web. Forward IP
        d_mz (bool): With DMZ enabled, all ports are open and the traffic from external network will be forwarded to the
            specific destination IP in the LAN.
        id (str | Unset): Port-forwarding ID
        site_id (str | Unset): Site ID
        limited_addresses (list[str] | Unset): Only for limited address
        virtual_wan_id (list[str] | Unset): This field represents VirtualWan ID. VirtualWan ID can be obtained from
            'Query available virtual WAN list' interface
        wan_ips (list[PortIpOpenApiVO] | Unset): WAN IPs
        external_port (str | Unset): External port corresponds with source port in web. ExternalPort should be within
            the range of 1–65535.
        forward_port (str | Unset): Forward port corresponds with destination port in web. ForwardPort should be 1 or
            1-10, within the range of 1–65535.
        protocol (int | Unset): Protocol should be a value as follows: 0: ALL; 1: TCP; 2: UDP.
    """

    name: str
    status: bool
    from_: int
    interface_wan_port_id: list[str]
    forward_ip: str
    d_mz: bool
    id: str | Unset = UNSET
    site_id: str | Unset = UNSET
    limited_addresses: list[str] | Unset = UNSET
    virtual_wan_id: list[str] | Unset = UNSET
    wan_ips: list[PortIpOpenApiVO] | Unset = UNSET
    external_port: str | Unset = UNSET
    forward_port: str | Unset = UNSET
    protocol: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status = self.status

        from_ = self.from_

        interface_wan_port_id = self.interface_wan_port_id

        forward_ip = self.forward_ip

        d_mz = self.d_mz

        id = self.id

        site_id = self.site_id

        limited_addresses: list[str] | Unset = UNSET
        if not isinstance(self.limited_addresses, Unset):
            limited_addresses = self.limited_addresses

        virtual_wan_id: list[str] | Unset = UNSET
        if not isinstance(self.virtual_wan_id, Unset):
            virtual_wan_id = self.virtual_wan_id

        wan_ips: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.wan_ips, Unset):
            wan_ips = []
            for wan_ips_item_data in self.wan_ips:
                wan_ips_item = wan_ips_item_data.to_dict()
                wan_ips.append(wan_ips_item)

        external_port = self.external_port

        forward_port = self.forward_port

        protocol = self.protocol

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "status": status,
                "from": from_,
                "interfaceWanPortId": interface_wan_port_id,
                "forwardIp": forward_ip,
                "dMZ": d_mz,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if site_id is not UNSET:
            field_dict["site id"] = site_id
        if limited_addresses is not UNSET:
            field_dict["limitedAddresses"] = limited_addresses
        if virtual_wan_id is not UNSET:
            field_dict["virtualWanId"] = virtual_wan_id
        if wan_ips is not UNSET:
            field_dict["wanIps"] = wan_ips
        if external_port is not UNSET:
            field_dict["externalPort"] = external_port
        if forward_port is not UNSET:
            field_dict["forwardPort"] = forward_port
        if protocol is not UNSET:
            field_dict["protocol"] = protocol

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.port_ip_open_api_vo import PortIpOpenApiVO

        d = dict(src_dict)
        name = d.pop("name")

        status = d.pop("status")

        from_ = d.pop("from")

        interface_wan_port_id = cast(list[str], d.pop("interfaceWanPortId"))

        forward_ip = d.pop("forwardIp")

        d_mz = d.pop("dMZ")

        id = d.pop("id", UNSET)

        site_id = d.pop("site id", UNSET)

        limited_addresses = cast(list[str], d.pop("limitedAddresses", UNSET))

        virtual_wan_id = cast(list[str], d.pop("virtualWanId", UNSET))

        _wan_ips = d.pop("wanIps", UNSET)
        wan_ips: list[PortIpOpenApiVO] | Unset = UNSET
        if _wan_ips is not UNSET:
            wan_ips = []
            for wan_ips_item_data in _wan_ips:
                wan_ips_item = PortIpOpenApiVO.from_dict(wan_ips_item_data)

                wan_ips.append(wan_ips_item)

        external_port = d.pop("externalPort", UNSET)

        forward_port = d.pop("forwardPort", UNSET)

        protocol = d.pop("protocol", UNSET)

        port_forwarding_info_template = cls(
            name=name,
            status=status,
            from_=from_,
            interface_wan_port_id=interface_wan_port_id,
            forward_ip=forward_ip,
            d_mz=d_mz,
            id=id,
            site_id=site_id,
            limited_addresses=limited_addresses,
            virtual_wan_id=virtual_wan_id,
            wan_ips=wan_ips,
            external_port=external_port,
            forward_port=forward_port,
            protocol=protocol,
        )

        port_forwarding_info_template.additional_properties = d
        return port_forwarding_info_template

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
