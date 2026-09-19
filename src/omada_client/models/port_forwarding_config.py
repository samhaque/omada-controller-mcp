from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.port_ip_open_api_vo import PortIpOpenApiVO


T = TypeVar("T", bound="PortForwardingConfig")


@_attrs_define
class PortForwardingConfig:
    """
    Attributes:
        name (str): Name, name should contain 1 to 64 characters.
        status (bool): Port-forwarding enable status.
        from_ (int): From corresponds with source IP in web. From should be a value as follows: 0: where; 1: limited
            address
        forward_ip (str): Forward IP corresponds with destination IP in web. Forward IP
        d_mz (bool): With DMZ enabled, all ports are open and the traffic from external network will be forwarded to the
            specific destination IP in the LAN.
        limited_addresses (list[str] | Unset): Only for limited address
        interface_wan_port_id (list[str] | Unset): This field represents WAN port ID. WAN port ID can be obtained from
            can be obtained from 'Get internet basic info' interface.
        virtual_wan_id (list[str] | Unset): This field represents Virtual Wan ID. Virtual Wan Id can be obtained from
            'Query available virtual WAN list'
        exist_virtual_wan (bool | Unset): Whether Virtual Wan has been configured in current Port Forwarding.
        wan_ips (list[PortIpOpenApiVO] | Unset): WAN IPs. Wan IPs can be obtained from 'Get internet ports config'
            interface
        exist_wan_ip (bool | Unset): Whether WAN IP has been configured in current Port Forwarding.
        external_port (str | Unset): External port corresponds with source port in web. External port should be within
            the range of 1–65535. Must be filled in when DMS is false.
        forward_port (str | Unset): Forward port corresponds with destination port in web. Forward port should be 1 or
            1-10, within the range of 1–65535. Must be filled in when DMS is false.
        protocol (int | Unset): Protocol should be a value as follows: 0: ALL; 1: TCP; 2: UDP. Must be filled in when
            DMS is false.
    """

    name: str
    status: bool
    from_: int
    forward_ip: str
    d_mz: bool
    limited_addresses: list[str] | Unset = UNSET
    interface_wan_port_id: list[str] | Unset = UNSET
    virtual_wan_id: list[str] | Unset = UNSET
    exist_virtual_wan: bool | Unset = UNSET
    wan_ips: list[PortIpOpenApiVO] | Unset = UNSET
    exist_wan_ip: bool | Unset = UNSET
    external_port: str | Unset = UNSET
    forward_port: str | Unset = UNSET
    protocol: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status = self.status

        from_ = self.from_

        forward_ip = self.forward_ip

        d_mz = self.d_mz

        limited_addresses: list[str] | Unset = UNSET
        if not isinstance(self.limited_addresses, Unset):
            limited_addresses = self.limited_addresses

        interface_wan_port_id: list[str] | Unset = UNSET
        if not isinstance(self.interface_wan_port_id, Unset):
            interface_wan_port_id = self.interface_wan_port_id

        virtual_wan_id: list[str] | Unset = UNSET
        if not isinstance(self.virtual_wan_id, Unset):
            virtual_wan_id = self.virtual_wan_id

        exist_virtual_wan = self.exist_virtual_wan

        wan_ips: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.wan_ips, Unset):
            wan_ips = []
            for wan_ips_item_data in self.wan_ips:
                wan_ips_item = wan_ips_item_data.to_dict()
                wan_ips.append(wan_ips_item)

        exist_wan_ip = self.exist_wan_ip

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
                "forwardIp": forward_ip,
                "dMZ": d_mz,
            }
        )
        if limited_addresses is not UNSET:
            field_dict["limitedAddresses"] = limited_addresses
        if interface_wan_port_id is not UNSET:
            field_dict["interfaceWanPortId"] = interface_wan_port_id
        if virtual_wan_id is not UNSET:
            field_dict["virtualWanId"] = virtual_wan_id
        if exist_virtual_wan is not UNSET:
            field_dict["existVirtualWan"] = exist_virtual_wan
        if wan_ips is not UNSET:
            field_dict["wanIps"] = wan_ips
        if exist_wan_ip is not UNSET:
            field_dict["existWanIp"] = exist_wan_ip
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

        forward_ip = d.pop("forwardIp")

        d_mz = d.pop("dMZ")

        limited_addresses = cast(list[str], d.pop("limitedAddresses", UNSET))

        interface_wan_port_id = cast(list[str], d.pop("interfaceWanPortId", UNSET))

        virtual_wan_id = cast(list[str], d.pop("virtualWanId", UNSET))

        exist_virtual_wan = d.pop("existVirtualWan", UNSET)

        _wan_ips = d.pop("wanIps", UNSET)
        wan_ips: list[PortIpOpenApiVO] | Unset = UNSET
        if _wan_ips is not UNSET:
            wan_ips = []
            for wan_ips_item_data in _wan_ips:
                wan_ips_item = PortIpOpenApiVO.from_dict(wan_ips_item_data)

                wan_ips.append(wan_ips_item)

        exist_wan_ip = d.pop("existWanIp", UNSET)

        external_port = d.pop("externalPort", UNSET)

        forward_port = d.pop("forwardPort", UNSET)

        protocol = d.pop("protocol", UNSET)

        port_forwarding_config = cls(
            name=name,
            status=status,
            from_=from_,
            forward_ip=forward_ip,
            d_mz=d_mz,
            limited_addresses=limited_addresses,
            interface_wan_port_id=interface_wan_port_id,
            virtual_wan_id=virtual_wan_id,
            exist_virtual_wan=exist_virtual_wan,
            wan_ips=wan_ips,
            exist_wan_ip=exist_wan_ip,
            external_port=external_port,
            forward_port=forward_port,
            protocol=protocol,
        )

        port_forwarding_config.additional_properties = d
        return port_forwarding_config

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
