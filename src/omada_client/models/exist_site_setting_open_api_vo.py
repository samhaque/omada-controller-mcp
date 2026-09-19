from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExistSiteSettingOpenApiVO")


@_attrs_define
class ExistSiteSettingOpenApiVO:
    """
    Attributes:
        virtual_wan (bool | Unset): Whether the current site has Virtual WAN configured.
        dns_proxy (bool | Unset): Whether the current site has DNS proxy configured.
        lan_dns (bool | Unset): Whether the current site has LAN DNS configured.
        ipsec_failover (bool | Unset): Whether the current site has IPsec failover configured.
        wireguard (bool | Unset): Whether the current site has WireGuard VPN configured.
        ssl_vpn (bool | Unset): Whether the current site has SSL VPN configured.
        google_ldap (bool | Unset): Whether the current site has Google LDAP configured.
        ips_ids (bool | Unset): Whether the current site has IDS/IPS configured.
        vpn_user (bool | Unset): Whether the current site has VPN User configured.
        one_to_one_nat (bool | Unset): Whether the current site has One-to-One NAT configured.
        disable_nat (bool | Unset): Whether the current site has Disable NAT configured.
        qos (bool | Unset): Whether the current site has QoS configured.
        service_type (bool | Unset): Whether the current site has Gateway QoS service configured.
        policy_routing (bool | Unset): Whether the current site has Policy Routing configured.
        ip_mac_binding (bool | Unset): Whether the current site has IP-MAC Binding configured.
        url_category (bool | Unset): Whether the General Config of URL Filtering has been configured.
        dns_cache (bool | Unset): Whether the current site has DNS Cache configured.
        mac_filter (bool | Unset): Whether the current site has MAC Filtering configured.
    """

    virtual_wan: bool | Unset = UNSET
    dns_proxy: bool | Unset = UNSET
    lan_dns: bool | Unset = UNSET
    ipsec_failover: bool | Unset = UNSET
    wireguard: bool | Unset = UNSET
    ssl_vpn: bool | Unset = UNSET
    google_ldap: bool | Unset = UNSET
    ips_ids: bool | Unset = UNSET
    vpn_user: bool | Unset = UNSET
    one_to_one_nat: bool | Unset = UNSET
    disable_nat: bool | Unset = UNSET
    qos: bool | Unset = UNSET
    service_type: bool | Unset = UNSET
    policy_routing: bool | Unset = UNSET
    ip_mac_binding: bool | Unset = UNSET
    url_category: bool | Unset = UNSET
    dns_cache: bool | Unset = UNSET
    mac_filter: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        virtual_wan = self.virtual_wan

        dns_proxy = self.dns_proxy

        lan_dns = self.lan_dns

        ipsec_failover = self.ipsec_failover

        wireguard = self.wireguard

        ssl_vpn = self.ssl_vpn

        google_ldap = self.google_ldap

        ips_ids = self.ips_ids

        vpn_user = self.vpn_user

        one_to_one_nat = self.one_to_one_nat

        disable_nat = self.disable_nat

        qos = self.qos

        service_type = self.service_type

        policy_routing = self.policy_routing

        ip_mac_binding = self.ip_mac_binding

        url_category = self.url_category

        dns_cache = self.dns_cache

        mac_filter = self.mac_filter

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if virtual_wan is not UNSET:
            field_dict["virtualWan"] = virtual_wan
        if dns_proxy is not UNSET:
            field_dict["dnsProxy"] = dns_proxy
        if lan_dns is not UNSET:
            field_dict["lanDns"] = lan_dns
        if ipsec_failover is not UNSET:
            field_dict["ipsecFailover"] = ipsec_failover
        if wireguard is not UNSET:
            field_dict["wireguard"] = wireguard
        if ssl_vpn is not UNSET:
            field_dict["sslVpn"] = ssl_vpn
        if google_ldap is not UNSET:
            field_dict["googleLdap"] = google_ldap
        if ips_ids is not UNSET:
            field_dict["ipsIds"] = ips_ids
        if vpn_user is not UNSET:
            field_dict["vpnUser"] = vpn_user
        if one_to_one_nat is not UNSET:
            field_dict["oneToOneNat"] = one_to_one_nat
        if disable_nat is not UNSET:
            field_dict["disableNat"] = disable_nat
        if qos is not UNSET:
            field_dict["qos"] = qos
        if service_type is not UNSET:
            field_dict["serviceType"] = service_type
        if policy_routing is not UNSET:
            field_dict["policyRouting"] = policy_routing
        if ip_mac_binding is not UNSET:
            field_dict["ipMacBinding"] = ip_mac_binding
        if url_category is not UNSET:
            field_dict["urlCategory"] = url_category
        if dns_cache is not UNSET:
            field_dict["dnsCache"] = dns_cache
        if mac_filter is not UNSET:
            field_dict["macFilter"] = mac_filter

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        virtual_wan = d.pop("virtualWan", UNSET)

        dns_proxy = d.pop("dnsProxy", UNSET)

        lan_dns = d.pop("lanDns", UNSET)

        ipsec_failover = d.pop("ipsecFailover", UNSET)

        wireguard = d.pop("wireguard", UNSET)

        ssl_vpn = d.pop("sslVpn", UNSET)

        google_ldap = d.pop("googleLdap", UNSET)

        ips_ids = d.pop("ipsIds", UNSET)

        vpn_user = d.pop("vpnUser", UNSET)

        one_to_one_nat = d.pop("oneToOneNat", UNSET)

        disable_nat = d.pop("disableNat", UNSET)

        qos = d.pop("qos", UNSET)

        service_type = d.pop("serviceType", UNSET)

        policy_routing = d.pop("policyRouting", UNSET)

        ip_mac_binding = d.pop("ipMacBinding", UNSET)

        url_category = d.pop("urlCategory", UNSET)

        dns_cache = d.pop("dnsCache", UNSET)

        mac_filter = d.pop("macFilter", UNSET)

        exist_site_setting_open_api_vo = cls(
            virtual_wan=virtual_wan,
            dns_proxy=dns_proxy,
            lan_dns=lan_dns,
            ipsec_failover=ipsec_failover,
            wireguard=wireguard,
            ssl_vpn=ssl_vpn,
            google_ldap=google_ldap,
            ips_ids=ips_ids,
            vpn_user=vpn_user,
            one_to_one_nat=one_to_one_nat,
            disable_nat=disable_nat,
            qos=qos,
            service_type=service_type,
            policy_routing=policy_routing,
            ip_mac_binding=ip_mac_binding,
            url_category=url_category,
            dns_cache=dns_cache,
            mac_filter=mac_filter,
        )

        exist_site_setting_open_api_vo.additional_properties = d
        return exist_site_setting_open_api_vo

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
