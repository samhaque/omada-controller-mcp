from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="Ipv4Connection2OpenApiVO")


@_attrs_define
class Ipv4Connection2OpenApiVO:
    """
    Attributes:
        secondary_proto_type (int): It should be a value as follows: 0:Static IP; 1:Dynamic IP; 2: None(Only for PPPoE).
        server (str | Unset): (Optional) VPN Server/Domain Name. It is required for L2TP/PPTP.
        ip_address (str | Unset): (Optional) It is required when [secondaryProtoType] is 0.
        subnet_mask (str | Unset): (Optional) It is required when [secondaryProtoType] is 0.
        default_gateway (str | Unset): (Optional) It is required when [secondaryProtoType] is 0.
        primary_dns (str | Unset): (Optional) It is required when [secondaryProtoType] is 0.
        secondary_dns (str | Unset): (Optional) It is required when [secondaryProtoType] is 0.
    """

    secondary_proto_type: int
    server: str | Unset = UNSET
    ip_address: str | Unset = UNSET
    subnet_mask: str | Unset = UNSET
    default_gateway: str | Unset = UNSET
    primary_dns: str | Unset = UNSET
    secondary_dns: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        secondary_proto_type = self.secondary_proto_type

        server = self.server

        ip_address = self.ip_address

        subnet_mask = self.subnet_mask

        default_gateway = self.default_gateway

        primary_dns = self.primary_dns

        secondary_dns = self.secondary_dns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "secondaryProtoType": secondary_proto_type,
            }
        )
        if server is not UNSET:
            field_dict["server"] = server
        if ip_address is not UNSET:
            field_dict["ipAddress"] = ip_address
        if subnet_mask is not UNSET:
            field_dict["subnetMask"] = subnet_mask
        if default_gateway is not UNSET:
            field_dict["defaultGateway"] = default_gateway
        if primary_dns is not UNSET:
            field_dict["primaryDns"] = primary_dns
        if secondary_dns is not UNSET:
            field_dict["secondaryDns"] = secondary_dns

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        secondary_proto_type = d.pop("secondaryProtoType")

        server = d.pop("server", UNSET)

        ip_address = d.pop("ipAddress", UNSET)

        subnet_mask = d.pop("subnetMask", UNSET)

        default_gateway = d.pop("defaultGateway", UNSET)

        primary_dns = d.pop("primaryDns", UNSET)

        secondary_dns = d.pop("secondaryDns", UNSET)

        ipv_4_connection_2_open_api_vo = cls(
            secondary_proto_type=secondary_proto_type,
            server=server,
            ip_address=ip_address,
            subnet_mask=subnet_mask,
            default_gateway=default_gateway,
            primary_dns=primary_dns,
            secondary_dns=secondary_dns,
        )

        ipv_4_connection_2_open_api_vo.additional_properties = d
        return ipv_4_connection_2_open_api_vo

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
