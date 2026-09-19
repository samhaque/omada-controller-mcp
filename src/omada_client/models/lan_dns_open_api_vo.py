from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="LanDnsOpenApiVO")


@_attrs_define
class LanDnsOpenApiVO:
    """
    Attributes:
        enable (bool): off:false, on: true
        name (str): Name of Lan Dns Item
        domain (str): Enter the domain name.
        type_ (int): There are three options, IP:0, CNAME:1, and FORWARD:2.
        aliases (list[str] | Unset): If a server provides different services and has multiple domain names, you can
            configure them in the Alias Domain Name.
        ip_addresses (list[str] | Unset): When the Type is IP, it is the IPv4 address of the returned DNS response.
        ipv_6_addresses (list[str] | Unset): When the Type is IP, it is the IPv6 address of the returned DNS response.
        cname (str | Unset): When Type is CNAME, set the domain name to which Domain Name and Alias Domain Name need to
            be mapped.
        dns_servers (list[str] | Unset): When the Type is FORWARD, set the Domain Name and Alias Domain Name to be
            forwarded to a specific DNS Server, up to two DNS Servers can be configured.
        lan_network_ids (list[str] | Unset): The ids of Lan Network. When the Type is IP or CNAME, it is the LAN network
            to which the rule applies.
        custom_ttl (bool | Unset): When custom TTL is activated, TTL will take effect as custom value. Otherwise, TTL
            will take effect as default(3600).
        ttl (int | Unset): The amount of time DNS information is allowed to be cached. The range of TTL should be
            1-86400. It is recommended to use the default TTL for each record.
    """

    enable: bool
    name: str
    domain: str
    type_: int
    aliases: list[str] | Unset = UNSET
    ip_addresses: list[str] | Unset = UNSET
    ipv_6_addresses: list[str] | Unset = UNSET
    cname: str | Unset = UNSET
    dns_servers: list[str] | Unset = UNSET
    lan_network_ids: list[str] | Unset = UNSET
    custom_ttl: bool | Unset = UNSET
    ttl: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        name = self.name

        domain = self.domain

        type_ = self.type_

        aliases: list[str] | Unset = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = self.aliases

        ip_addresses: list[str] | Unset = UNSET
        if not isinstance(self.ip_addresses, Unset):
            ip_addresses = self.ip_addresses

        ipv_6_addresses: list[str] | Unset = UNSET
        if not isinstance(self.ipv_6_addresses, Unset):
            ipv_6_addresses = self.ipv_6_addresses

        cname = self.cname

        dns_servers: list[str] | Unset = UNSET
        if not isinstance(self.dns_servers, Unset):
            dns_servers = self.dns_servers

        lan_network_ids: list[str] | Unset = UNSET
        if not isinstance(self.lan_network_ids, Unset):
            lan_network_ids = self.lan_network_ids

        custom_ttl = self.custom_ttl

        ttl = self.ttl

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
                "name": name,
                "domain": domain,
                "type": type_,
            }
        )
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if ip_addresses is not UNSET:
            field_dict["ipAddresses"] = ip_addresses
        if ipv_6_addresses is not UNSET:
            field_dict["ipv6Addresses"] = ipv_6_addresses
        if cname is not UNSET:
            field_dict["cname"] = cname
        if dns_servers is not UNSET:
            field_dict["dnsServers"] = dns_servers
        if lan_network_ids is not UNSET:
            field_dict["lanNetworkIds"] = lan_network_ids
        if custom_ttl is not UNSET:
            field_dict["customTtl"] = custom_ttl
        if ttl is not UNSET:
            field_dict["ttl"] = ttl

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable = d.pop("enable")

        name = d.pop("name")

        domain = d.pop("domain")

        type_ = d.pop("type")

        aliases = cast(list[str], d.pop("aliases", UNSET))

        ip_addresses = cast(list[str], d.pop("ipAddresses", UNSET))

        ipv_6_addresses = cast(list[str], d.pop("ipv6Addresses", UNSET))

        cname = d.pop("cname", UNSET)

        dns_servers = cast(list[str], d.pop("dnsServers", UNSET))

        lan_network_ids = cast(list[str], d.pop("lanNetworkIds", UNSET))

        custom_ttl = d.pop("customTtl", UNSET)

        ttl = d.pop("ttl", UNSET)

        lan_dns_open_api_vo = cls(
            enable=enable,
            name=name,
            domain=domain,
            type_=type_,
            aliases=aliases,
            ip_addresses=ip_addresses,
            ipv_6_addresses=ipv_6_addresses,
            cname=cname,
            dns_servers=dns_servers,
            lan_network_ids=lan_network_ids,
            custom_ttl=custom_ttl,
            ttl=ttl,
        )

        lan_dns_open_api_vo.additional_properties = d
        return lan_dns_open_api_vo

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
