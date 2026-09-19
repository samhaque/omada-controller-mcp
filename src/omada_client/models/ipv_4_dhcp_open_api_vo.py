from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wan_dhcp_option_open_api_vo import WanDhcpOptionOpenApiVO
    from ..models.wan_multiple_ip_open_api_vo import WanMultipleIpOpenApiVO


T = TypeVar("T", bound="Ipv4DhcpOpenApiVO")


@_attrs_define
class Ipv4DhcpOpenApiVO:
    """It is required when [protoType] is 1.

    Attributes:
        mtu (int): 576-1500, default:1500.
        unicast_dhcp (bool | Unset): Unicast DHCP
        primary_dns (str | Unset): Primary DNS
        secondary_dns (str | Unset): Secondary DNS
        hostname (str | Unset): Host name
        wan_multiple_ips (list[WanMultipleIpOpenApiVO] | Unset):
        dhcp_options (list[WanDhcpOptionOpenApiVO] | Unset):
    """

    mtu: int
    unicast_dhcp: bool | Unset = UNSET
    primary_dns: str | Unset = UNSET
    secondary_dns: str | Unset = UNSET
    hostname: str | Unset = UNSET
    wan_multiple_ips: list[WanMultipleIpOpenApiVO] | Unset = UNSET
    dhcp_options: list[WanDhcpOptionOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mtu = self.mtu

        unicast_dhcp = self.unicast_dhcp

        primary_dns = self.primary_dns

        secondary_dns = self.secondary_dns

        hostname = self.hostname

        wan_multiple_ips: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.wan_multiple_ips, Unset):
            wan_multiple_ips = []
            for wan_multiple_ips_item_data in self.wan_multiple_ips:
                wan_multiple_ips_item = wan_multiple_ips_item_data.to_dict()
                wan_multiple_ips.append(wan_multiple_ips_item)

        dhcp_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dhcp_options, Unset):
            dhcp_options = []
            for dhcp_options_item_data in self.dhcp_options:
                dhcp_options_item = dhcp_options_item_data.to_dict()
                dhcp_options.append(dhcp_options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mtu": mtu,
            }
        )
        if unicast_dhcp is not UNSET:
            field_dict["unicastDhcp"] = unicast_dhcp
        if primary_dns is not UNSET:
            field_dict["primaryDns"] = primary_dns
        if secondary_dns is not UNSET:
            field_dict["secondaryDns"] = secondary_dns
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if wan_multiple_ips is not UNSET:
            field_dict["wanMultipleIps"] = wan_multiple_ips
        if dhcp_options is not UNSET:
            field_dict["dhcpOptions"] = dhcp_options

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.wan_dhcp_option_open_api_vo import (
            WanDhcpOptionOpenApiVO,
        )
        from ..models.wan_multiple_ip_open_api_vo import (
            WanMultipleIpOpenApiVO,
        )

        d = dict(src_dict)
        mtu = d.pop("mtu")

        unicast_dhcp = d.pop("unicastDhcp", UNSET)

        primary_dns = d.pop("primaryDns", UNSET)

        secondary_dns = d.pop("secondaryDns", UNSET)

        hostname = d.pop("hostname", UNSET)

        _wan_multiple_ips = d.pop("wanMultipleIps", UNSET)
        wan_multiple_ips: list[WanMultipleIpOpenApiVO] | Unset = UNSET
        if _wan_multiple_ips is not UNSET:
            wan_multiple_ips = []
            for wan_multiple_ips_item_data in _wan_multiple_ips:
                wan_multiple_ips_item = WanMultipleIpOpenApiVO.from_dict(
                    wan_multiple_ips_item_data
                )

                wan_multiple_ips.append(wan_multiple_ips_item)

        _dhcp_options = d.pop("dhcpOptions", UNSET)
        dhcp_options: list[WanDhcpOptionOpenApiVO] | Unset = UNSET
        if _dhcp_options is not UNSET:
            dhcp_options = []
            for dhcp_options_item_data in _dhcp_options:
                dhcp_options_item = WanDhcpOptionOpenApiVO.from_dict(
                    dhcp_options_item_data
                )

                dhcp_options.append(dhcp_options_item)

        ipv_4_dhcp_open_api_vo = cls(
            mtu=mtu,
            unicast_dhcp=unicast_dhcp,
            primary_dns=primary_dns,
            secondary_dns=secondary_dns,
            hostname=hostname,
            wan_multiple_ips=wan_multiple_ips,
            dhcp_options=dhcp_options,
        )

        ipv_4_dhcp_open_api_vo.additional_properties = d
        return ipv_4_dhcp_open_api_vo

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
