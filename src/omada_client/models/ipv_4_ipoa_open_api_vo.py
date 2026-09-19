from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wan_multiple_ip_open_api_vo import WanMultipleIpOpenApiVO


T = TypeVar("T", bound="Ipv4IpoaOpenApiVO")


@_attrs_define
class Ipv4IpoaOpenApiVO:
    """It is required when [protoType] is 8.

    Attributes:
        ip_address (str): IP address
        subnet_mask (str):
        default_gateway (str):
        mtu (int): 576-1500, default:1500
        primary_dns (str | Unset): Primary DNS
        secondary_dns (str | Unset): Secondary DNS
        wan_multiple_ips (list[WanMultipleIpOpenApiVO] | Unset):
    """

    ip_address: str
    subnet_mask: str
    default_gateway: str
    mtu: int
    primary_dns: str | Unset = UNSET
    secondary_dns: str | Unset = UNSET
    wan_multiple_ips: list[WanMultipleIpOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ip_address = self.ip_address

        subnet_mask = self.subnet_mask

        default_gateway = self.default_gateway

        mtu = self.mtu

        primary_dns = self.primary_dns

        secondary_dns = self.secondary_dns

        wan_multiple_ips: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.wan_multiple_ips, Unset):
            wan_multiple_ips = []
            for wan_multiple_ips_item_data in self.wan_multiple_ips:
                wan_multiple_ips_item = wan_multiple_ips_item_data.to_dict()
                wan_multiple_ips.append(wan_multiple_ips_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ipAddress": ip_address,
                "subnetMask": subnet_mask,
                "defaultGateway": default_gateway,
                "mtu": mtu,
            }
        )
        if primary_dns is not UNSET:
            field_dict["primaryDns"] = primary_dns
        if secondary_dns is not UNSET:
            field_dict["secondaryDns"] = secondary_dns
        if wan_multiple_ips is not UNSET:
            field_dict["wanMultipleIps"] = wan_multiple_ips

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.wan_multiple_ip_open_api_vo import (
            WanMultipleIpOpenApiVO,
        )

        d = dict(src_dict)
        ip_address = d.pop("ipAddress")

        subnet_mask = d.pop("subnetMask")

        default_gateway = d.pop("defaultGateway")

        mtu = d.pop("mtu")

        primary_dns = d.pop("primaryDns", UNSET)

        secondary_dns = d.pop("secondaryDns", UNSET)

        _wan_multiple_ips = d.pop("wanMultipleIps", UNSET)
        wan_multiple_ips: list[WanMultipleIpOpenApiVO] | Unset = UNSET
        if _wan_multiple_ips is not UNSET:
            wan_multiple_ips = []
            for wan_multiple_ips_item_data in _wan_multiple_ips:
                wan_multiple_ips_item = WanMultipleIpOpenApiVO.from_dict(
                    wan_multiple_ips_item_data
                )

                wan_multiple_ips.append(wan_multiple_ips_item)

        ipv_4_ipoa_open_api_vo = cls(
            ip_address=ip_address,
            subnet_mask=subnet_mask,
            default_gateway=default_gateway,
            mtu=mtu,
            primary_dns=primary_dns,
            secondary_dns=secondary_dns,
            wan_multiple_ips=wan_multiple_ips,
        )

        ipv_4_ipoa_open_api_vo.additional_properties = d
        return ipv_4_ipoa_open_api_vo

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
