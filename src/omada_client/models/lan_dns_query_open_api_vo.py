from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feature_info_vo import FeatureInfoVO


T = TypeVar("T", bound="LanDnsQueryOpenApiVO")


@_attrs_define
class LanDnsQueryOpenApiVO:
    """
    Attributes:
        enable (bool): off:false, on: true
        name (str): Name of Lan Dns Item
        domain (str): Enter the domain name.
        type_ (int): There are three options, IP:0, CNAME:1, and FORWARD:2.
        id (str | Unset): The ID of current Lan Dns entry.
        aliases (list[str] | Unset): Name of Lan Dns Item
        ip_addresses (list[str] | Unset): When the Type is IP, it is the IPv4 address of the returned DNS response.
        ipv_6_addresses (list[str] | Unset): When the Type is IP, it is the IPv6 address of the returned DNS response.
        cname (str | Unset): When Type is CNAME, set the domain name to which Domain Name and Alias Domain Name need to
            be mapped.
        dns_servers (list[str] | Unset): When the Type is FORWARD, set the Domain Name and Alias Domain Name to be
            forwarded to a specific DNS Server, up to two DNS Servers can be configured.
        lan_network_ids (list[str] | Unset): The ids of Lan Network.
        custom_ttl (bool | Unset): When custom TTL is activated, TTL will take effect as custom. Otherwise, TTL will
            take effect as default(3600).
        ttl (int | Unset): The amount of time DNS information is allowed to be cached before it expires and needs to be
            refreshed. It is recommended to use the default TTL (3600) for each record. The range of TTL is between 1 and
            86400.
        feature_description (list[FeatureInfoVO] | Unset): Gateway Feature Description.
    """

    enable: bool
    name: str
    domain: str
    type_: int
    id: str | Unset = UNSET
    aliases: list[str] | Unset = UNSET
    ip_addresses: list[str] | Unset = UNSET
    ipv_6_addresses: list[str] | Unset = UNSET
    cname: str | Unset = UNSET
    dns_servers: list[str] | Unset = UNSET
    lan_network_ids: list[str] | Unset = UNSET
    custom_ttl: bool | Unset = UNSET
    ttl: int | Unset = UNSET
    feature_description: list[FeatureInfoVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        name = self.name

        domain = self.domain

        type_ = self.type_

        id = self.id

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

        feature_description: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.feature_description, Unset):
            feature_description = []
            for feature_description_item_data in self.feature_description:
                feature_description_item = feature_description_item_data.to_dict()
                feature_description.append(feature_description_item)

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
        if id is not UNSET:
            field_dict["id"] = id
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
        if feature_description is not UNSET:
            field_dict["featureDescription"] = feature_description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.feature_info_vo import FeatureInfoVO

        d = dict(src_dict)
        enable = d.pop("enable")

        name = d.pop("name")

        domain = d.pop("domain")

        type_ = d.pop("type")

        id = d.pop("id", UNSET)

        aliases = cast(list[str], d.pop("aliases", UNSET))

        ip_addresses = cast(list[str], d.pop("ipAddresses", UNSET))

        ipv_6_addresses = cast(list[str], d.pop("ipv6Addresses", UNSET))

        cname = d.pop("cname", UNSET)

        dns_servers = cast(list[str], d.pop("dnsServers", UNSET))

        lan_network_ids = cast(list[str], d.pop("lanNetworkIds", UNSET))

        custom_ttl = d.pop("customTtl", UNSET)

        ttl = d.pop("ttl", UNSET)

        _feature_description = d.pop("featureDescription", UNSET)
        feature_description: list[FeatureInfoVO] | Unset = UNSET
        if _feature_description is not UNSET:
            feature_description = []
            for feature_description_item_data in _feature_description:
                feature_description_item = FeatureInfoVO.from_dict(
                    feature_description_item_data
                )

                feature_description.append(feature_description_item)

        lan_dns_query_open_api_vo = cls(
            enable=enable,
            name=name,
            domain=domain,
            type_=type_,
            id=id,
            aliases=aliases,
            ip_addresses=ip_addresses,
            ipv_6_addresses=ipv_6_addresses,
            cname=cname,
            dns_servers=dns_servers,
            lan_network_ids=lan_network_ids,
            custom_ttl=custom_ttl,
            ttl=ttl,
            feature_description=feature_description,
        )

        lan_dns_query_open_api_vo.additional_properties = d
        return lan_dns_query_open_api_vo

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
