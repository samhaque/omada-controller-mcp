from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExistSiteSettingVO")


@_attrs_define
class ExistSiteSettingVO:
    """
    Attributes:
        virtual_wan (bool | Unset):
        dns_proxy (bool | Unset):
        lan_dns (bool | Unset):
        ipsec_failover (bool | Unset):
        wireguard (bool | Unset):
        ssl_vpn (bool | Unset):
        google_ldap (bool | Unset):
        ip_mac_binding (bool | Unset):
        url_category (bool | Unset):
        dns_cache (bool | Unset):
        mac_filter (bool | Unset):
        ips_ids (bool | Unset):
        vpn_user (bool | Unset):
        one_to_one_nat (bool | Unset):
        disable_nat (bool | Unset):
        qos (bool | Unset):
        service_type (bool | Unset):
        policy_routing (bool | Unset):
        sub_vpn (bool | Unset):
        service_iptv (bool | Unset):
        vpn_server (bool | Unset):
        vpn_client (bool | Unset):
        site_to_site_vpn (bool | Unset):
    """

    virtual_wan: bool | Unset = UNSET
    dns_proxy: bool | Unset = UNSET
    lan_dns: bool | Unset = UNSET
    ipsec_failover: bool | Unset = UNSET
    wireguard: bool | Unset = UNSET
    ssl_vpn: bool | Unset = UNSET
    google_ldap: bool | Unset = UNSET
    ip_mac_binding: bool | Unset = UNSET
    url_category: bool | Unset = UNSET
    dns_cache: bool | Unset = UNSET
    mac_filter: bool | Unset = UNSET
    ips_ids: bool | Unset = UNSET
    vpn_user: bool | Unset = UNSET
    one_to_one_nat: bool | Unset = UNSET
    disable_nat: bool | Unset = UNSET
    qos: bool | Unset = UNSET
    service_type: bool | Unset = UNSET
    policy_routing: bool | Unset = UNSET
    sub_vpn: bool | Unset = UNSET
    service_iptv: bool | Unset = UNSET
    vpn_server: bool | Unset = UNSET
    vpn_client: bool | Unset = UNSET
    site_to_site_vpn: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        virtual_wan = self.virtual_wan

        dns_proxy = self.dns_proxy

        lan_dns = self.lan_dns

        ipsec_failover = self.ipsec_failover

        wireguard = self.wireguard

        ssl_vpn = self.ssl_vpn

        google_ldap = self.google_ldap

        ip_mac_binding = self.ip_mac_binding

        url_category = self.url_category

        dns_cache = self.dns_cache

        mac_filter = self.mac_filter

        ips_ids = self.ips_ids

        vpn_user = self.vpn_user

        one_to_one_nat = self.one_to_one_nat

        disable_nat = self.disable_nat

        qos = self.qos

        service_type = self.service_type

        policy_routing = self.policy_routing

        sub_vpn = self.sub_vpn

        service_iptv = self.service_iptv

        vpn_server = self.vpn_server

        vpn_client = self.vpn_client

        site_to_site_vpn = self.site_to_site_vpn

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
        if ip_mac_binding is not UNSET:
            field_dict["ipMacBinding"] = ip_mac_binding
        if url_category is not UNSET:
            field_dict["urlCategory"] = url_category
        if dns_cache is not UNSET:
            field_dict["dnsCache"] = dns_cache
        if mac_filter is not UNSET:
            field_dict["macFilter"] = mac_filter
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
        if sub_vpn is not UNSET:
            field_dict["subVpn"] = sub_vpn
        if service_iptv is not UNSET:
            field_dict["serviceIptv"] = service_iptv
        if vpn_server is not UNSET:
            field_dict["vpnServer"] = vpn_server
        if vpn_client is not UNSET:
            field_dict["vpnClient"] = vpn_client
        if site_to_site_vpn is not UNSET:
            field_dict["siteToSiteVpn"] = site_to_site_vpn

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

        ip_mac_binding = d.pop("ipMacBinding", UNSET)

        url_category = d.pop("urlCategory", UNSET)

        dns_cache = d.pop("dnsCache", UNSET)

        mac_filter = d.pop("macFilter", UNSET)

        ips_ids = d.pop("ipsIds", UNSET)

        vpn_user = d.pop("vpnUser", UNSET)

        one_to_one_nat = d.pop("oneToOneNat", UNSET)

        disable_nat = d.pop("disableNat", UNSET)

        qos = d.pop("qos", UNSET)

        service_type = d.pop("serviceType", UNSET)

        policy_routing = d.pop("policyRouting", UNSET)

        sub_vpn = d.pop("subVpn", UNSET)

        service_iptv = d.pop("serviceIptv", UNSET)

        vpn_server = d.pop("vpnServer", UNSET)

        vpn_client = d.pop("vpnClient", UNSET)

        site_to_site_vpn = d.pop("siteToSiteVpn", UNSET)

        exist_site_setting_vo = cls(
            virtual_wan=virtual_wan,
            dns_proxy=dns_proxy,
            lan_dns=lan_dns,
            ipsec_failover=ipsec_failover,
            wireguard=wireguard,
            ssl_vpn=ssl_vpn,
            google_ldap=google_ldap,
            ip_mac_binding=ip_mac_binding,
            url_category=url_category,
            dns_cache=dns_cache,
            mac_filter=mac_filter,
            ips_ids=ips_ids,
            vpn_user=vpn_user,
            one_to_one_nat=one_to_one_nat,
            disable_nat=disable_nat,
            qos=qos,
            service_type=service_type,
            policy_routing=policy_routing,
            sub_vpn=sub_vpn,
            service_iptv=service_iptv,
            vpn_server=vpn_server,
            vpn_client=vpn_client,
            site_to_site_vpn=site_to_site_vpn,
        )

        exist_site_setting_vo.additional_properties = d
        return exist_site_setting_vo

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
