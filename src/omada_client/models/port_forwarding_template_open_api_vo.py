from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PortForwardingTemplateOpenApiVO")


@_attrs_define
class PortForwardingTemplateOpenApiVO:
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
        limited_addresses (list[str] | Unset): Only for limited address
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
    interface_wan_port_id: list[str]
    forward_ip: str
    d_mz: bool
    limited_addresses: list[str] | Unset = UNSET
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

        limited_addresses: list[str] | Unset = UNSET
        if not isinstance(self.limited_addresses, Unset):
            limited_addresses = self.limited_addresses

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
        if limited_addresses is not UNSET:
            field_dict["limitedAddresses"] = limited_addresses
        if external_port is not UNSET:
            field_dict["externalPort"] = external_port
        if forward_port is not UNSET:
            field_dict["forwardPort"] = forward_port
        if protocol is not UNSET:
            field_dict["protocol"] = protocol

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        status = d.pop("status")

        from_ = d.pop("from")

        interface_wan_port_id = cast(list[str], d.pop("interfaceWanPortId"))

        forward_ip = d.pop("forwardIp")

        d_mz = d.pop("dMZ")

        limited_addresses = cast(list[str], d.pop("limitedAddresses", UNSET))

        external_port = d.pop("externalPort", UNSET)

        forward_port = d.pop("forwardPort", UNSET)

        protocol = d.pop("protocol", UNSET)

        port_forwarding_template_open_api_vo = cls(
            name=name,
            status=status,
            from_=from_,
            interface_wan_port_id=interface_wan_port_id,
            forward_ip=forward_ip,
            d_mz=d_mz,
            limited_addresses=limited_addresses,
            external_port=external_port,
            forward_port=forward_port,
            protocol=protocol,
        )

        port_forwarding_template_open_api_vo.additional_properties = d
        return port_forwarding_template_open_api_vo

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
