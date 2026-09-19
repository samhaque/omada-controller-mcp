from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SiteSettingCapOpenApiVO")


@_attrs_define
class SiteSettingCapOpenApiVO:
    """
    Attributes:
        firewall (bool | Unset): Whether support firewall configuration.
        ssl_vpn (bool | Unset): Whether support SSL VPN configuration.
        vpn_user (bool | Unset): Whether support VPN User configuration.
        one_to_one_nat (bool | Unset): Whether support one-to-one NAT configuration.
        disable_nat (bool | Unset): Whether support disable NAT configuration.
        ip_mac_binding (bool | Unset): Whether support ipMacBinding configuration.
        qos (bool | Unset): Whether support QOS configuration.
        wireguard (bool | Unset): Whether support wireguard VPN configuration.
        dns_proxy (bool | Unset): Whether support dnsProxy configuration.
        ipsec_failover (bool | Unset): Whether support IPsec failover configuration.
        ldap_vpn (bool | Unset): Whether support VPN configuration with LDAP.
        service_type (bool | Unset): Whether support serviceType configuration.
        ips_ids (bool | Unset): Whether support IPS configuration.
        mac_filter (bool | Unset): Whether support network security-mac filter configuration.
        sim (bool | Unset): Whether support SIM configuration.
        client_rate_limit (bool | Unset): false: there is a wireless route device that does not support
            ClientRateLimit.true or null: all devices support ClientRateLimit
        lock_to_ap (bool | Unset): false: there is a wireless route device that does not support LockToAp.true or null:
            all devices support LockToAp
        voip (bool | Unset): Whether support voip configuration.
        olt_vlan (bool | Unset): An OLT device exists.
        p2p (bool | Unset): An P2P device exists.
        server_open_vpn_google_ldap (bool | Unset): Whether server-openvpn support Google LDAP.
        virtual_wan (bool | Unset): Whether support virtual WAN configuration.
        l_2tp (bool | Unset): Whether support L2TP VPN configuration.
        ipsec (bool | Unset): Whether support Ipsec VPN configuration.
        ip_port_group (bool | Unset): Whether support IP-Port Group configuration.
        support_es (bool | Unset): Whether the site supports adopting Agile Series Switches
        support_l2 (bool | Unset): Whether the site supports adopting Non-Agile Series Switches
        url_category (bool | Unset): Whether Url Filter support category mode.
        custom_acl (bool | Unset): Whether ACL support custom mode.
        peer_endpoint_domain (bool | Unset): Whether peer-endpoint support entering domain names.
        lan_dns (bool | Unset): Whether support LAN DNS configuration.
        isolation_settings (bool | Unset): Whether support Network Isolation.
        dsl (bool | Unset): Whether support DSL configuration.
        ldap_ssl (bool | Unset): Whether SSL VPN support ldap.
        google_ldap (bool | Unset): Whether support Google LDAP configuration.
        dpi (bool | Unset): Whether support DPI configuration. Deprecated.
        package_capture_gateway (bool | Unset): Whether the gateway can be selected in the packet capture page.
        cluster (bool | Unset): Whether support cluster mode.
        cluster_mode_on (bool | Unset): Whether the current software is running in cluster mode.
        init_cluster_reminder (bool | Unset): Whether the current cluster prompts that it has not been restarted after
            configuration initialization.
        dpi_stat (bool | Unset): Whether support dpi stat.Deprecated, same as dpi. Deprecated.
        service_iptv (bool | Unset): Whether support IGMP or IPTV.
        sub_vpn (bool | Unset): Whether support VPN menu in VPN module.
        vpn_status (bool | Unset): Whether support vpnStatus.
        policy_routing (bool | Unset): Whether support policyRouting.
        support_dpi (bool | Unset): Whether support Dpi.
        support_show_server_in_reservation (bool | Unset): Whether support show server in DHCP Reservation.
        speed_test (bool | Unset): Whether support speedTest.
        nat_traversal (bool | Unset): Whether support natTraversal.
    """

    firewall: bool | Unset = UNSET
    ssl_vpn: bool | Unset = UNSET
    vpn_user: bool | Unset = UNSET
    one_to_one_nat: bool | Unset = UNSET
    disable_nat: bool | Unset = UNSET
    ip_mac_binding: bool | Unset = UNSET
    qos: bool | Unset = UNSET
    wireguard: bool | Unset = UNSET
    dns_proxy: bool | Unset = UNSET
    ipsec_failover: bool | Unset = UNSET
    ldap_vpn: bool | Unset = UNSET
    service_type: bool | Unset = UNSET
    ips_ids: bool | Unset = UNSET
    mac_filter: bool | Unset = UNSET
    sim: bool | Unset = UNSET
    client_rate_limit: bool | Unset = UNSET
    lock_to_ap: bool | Unset = UNSET
    voip: bool | Unset = UNSET
    olt_vlan: bool | Unset = UNSET
    p2p: bool | Unset = UNSET
    server_open_vpn_google_ldap: bool | Unset = UNSET
    virtual_wan: bool | Unset = UNSET
    l_2tp: bool | Unset = UNSET
    ipsec: bool | Unset = UNSET
    ip_port_group: bool | Unset = UNSET
    support_es: bool | Unset = UNSET
    support_l2: bool | Unset = UNSET
    url_category: bool | Unset = UNSET
    custom_acl: bool | Unset = UNSET
    peer_endpoint_domain: bool | Unset = UNSET
    lan_dns: bool | Unset = UNSET
    isolation_settings: bool | Unset = UNSET
    dsl: bool | Unset = UNSET
    ldap_ssl: bool | Unset = UNSET
    google_ldap: bool | Unset = UNSET
    dpi: bool | Unset = UNSET
    package_capture_gateway: bool | Unset = UNSET
    cluster: bool | Unset = UNSET
    cluster_mode_on: bool | Unset = UNSET
    init_cluster_reminder: bool | Unset = UNSET
    dpi_stat: bool | Unset = UNSET
    service_iptv: bool | Unset = UNSET
    sub_vpn: bool | Unset = UNSET
    vpn_status: bool | Unset = UNSET
    policy_routing: bool | Unset = UNSET
    support_dpi: bool | Unset = UNSET
    support_show_server_in_reservation: bool | Unset = UNSET
    speed_test: bool | Unset = UNSET
    nat_traversal: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        firewall = self.firewall

        ssl_vpn = self.ssl_vpn

        vpn_user = self.vpn_user

        one_to_one_nat = self.one_to_one_nat

        disable_nat = self.disable_nat

        ip_mac_binding = self.ip_mac_binding

        qos = self.qos

        wireguard = self.wireguard

        dns_proxy = self.dns_proxy

        ipsec_failover = self.ipsec_failover

        ldap_vpn = self.ldap_vpn

        service_type = self.service_type

        ips_ids = self.ips_ids

        mac_filter = self.mac_filter

        sim = self.sim

        client_rate_limit = self.client_rate_limit

        lock_to_ap = self.lock_to_ap

        voip = self.voip

        olt_vlan = self.olt_vlan

        p2p = self.p2p

        server_open_vpn_google_ldap = self.server_open_vpn_google_ldap

        virtual_wan = self.virtual_wan

        l_2tp = self.l_2tp

        ipsec = self.ipsec

        ip_port_group = self.ip_port_group

        support_es = self.support_es

        support_l2 = self.support_l2

        url_category = self.url_category

        custom_acl = self.custom_acl

        peer_endpoint_domain = self.peer_endpoint_domain

        lan_dns = self.lan_dns

        isolation_settings = self.isolation_settings

        dsl = self.dsl

        ldap_ssl = self.ldap_ssl

        google_ldap = self.google_ldap

        dpi = self.dpi

        package_capture_gateway = self.package_capture_gateway

        cluster = self.cluster

        cluster_mode_on = self.cluster_mode_on

        init_cluster_reminder = self.init_cluster_reminder

        dpi_stat = self.dpi_stat

        service_iptv = self.service_iptv

        sub_vpn = self.sub_vpn

        vpn_status = self.vpn_status

        policy_routing = self.policy_routing

        support_dpi = self.support_dpi

        support_show_server_in_reservation = self.support_show_server_in_reservation

        speed_test = self.speed_test

        nat_traversal = self.nat_traversal

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if firewall is not UNSET:
            field_dict["firewall"] = firewall
        if ssl_vpn is not UNSET:
            field_dict["sslVpn"] = ssl_vpn
        if vpn_user is not UNSET:
            field_dict["vpnUser"] = vpn_user
        if one_to_one_nat is not UNSET:
            field_dict["oneToOneNat"] = one_to_one_nat
        if disable_nat is not UNSET:
            field_dict["disableNat"] = disable_nat
        if ip_mac_binding is not UNSET:
            field_dict["ipMacBinding"] = ip_mac_binding
        if qos is not UNSET:
            field_dict["qos"] = qos
        if wireguard is not UNSET:
            field_dict["wireguard"] = wireguard
        if dns_proxy is not UNSET:
            field_dict["dnsProxy"] = dns_proxy
        if ipsec_failover is not UNSET:
            field_dict["ipsecFailover"] = ipsec_failover
        if ldap_vpn is not UNSET:
            field_dict["ldapVpn"] = ldap_vpn
        if service_type is not UNSET:
            field_dict["serviceType"] = service_type
        if ips_ids is not UNSET:
            field_dict["ipsIds"] = ips_ids
        if mac_filter is not UNSET:
            field_dict["macFilter"] = mac_filter
        if sim is not UNSET:
            field_dict["sim"] = sim
        if client_rate_limit is not UNSET:
            field_dict["clientRateLimit"] = client_rate_limit
        if lock_to_ap is not UNSET:
            field_dict["lockToAp"] = lock_to_ap
        if voip is not UNSET:
            field_dict["voip"] = voip
        if olt_vlan is not UNSET:
            field_dict["oltVlan"] = olt_vlan
        if p2p is not UNSET:
            field_dict["p2p"] = p2p
        if server_open_vpn_google_ldap is not UNSET:
            field_dict["serverOpenVpnGoogleLdap"] = server_open_vpn_google_ldap
        if virtual_wan is not UNSET:
            field_dict["virtualWan"] = virtual_wan
        if l_2tp is not UNSET:
            field_dict["l2TP"] = l_2tp
        if ipsec is not UNSET:
            field_dict["ipsec"] = ipsec
        if ip_port_group is not UNSET:
            field_dict["ipPortGroup"] = ip_port_group
        if support_es is not UNSET:
            field_dict["supportES"] = support_es
        if support_l2 is not UNSET:
            field_dict["supportL2"] = support_l2
        if url_category is not UNSET:
            field_dict["urlCategory"] = url_category
        if custom_acl is not UNSET:
            field_dict["customAcl"] = custom_acl
        if peer_endpoint_domain is not UNSET:
            field_dict["peerEndpointDomain"] = peer_endpoint_domain
        if lan_dns is not UNSET:
            field_dict["lanDns"] = lan_dns
        if isolation_settings is not UNSET:
            field_dict["IsolationSettings"] = isolation_settings
        if dsl is not UNSET:
            field_dict["dsl"] = dsl
        if ldap_ssl is not UNSET:
            field_dict["ldapSsl"] = ldap_ssl
        if google_ldap is not UNSET:
            field_dict["googleLdap"] = google_ldap
        if dpi is not UNSET:
            field_dict["dpi"] = dpi
        if package_capture_gateway is not UNSET:
            field_dict["packageCaptureGateway"] = package_capture_gateway
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if cluster_mode_on is not UNSET:
            field_dict["clusterModeOn"] = cluster_mode_on
        if init_cluster_reminder is not UNSET:
            field_dict["initClusterReminder"] = init_cluster_reminder
        if dpi_stat is not UNSET:
            field_dict["dpiStat"] = dpi_stat
        if service_iptv is not UNSET:
            field_dict["serviceIptv"] = service_iptv
        if sub_vpn is not UNSET:
            field_dict["subVpn"] = sub_vpn
        if vpn_status is not UNSET:
            field_dict["vpnStatus"] = vpn_status
        if policy_routing is not UNSET:
            field_dict["policyRouting"] = policy_routing
        if support_dpi is not UNSET:
            field_dict["supportDpi"] = support_dpi
        if support_show_server_in_reservation is not UNSET:
            field_dict["supportShowServerInReservation"] = (
                support_show_server_in_reservation
            )
        if speed_test is not UNSET:
            field_dict["speedTest"] = speed_test
        if nat_traversal is not UNSET:
            field_dict["natTraversal"] = nat_traversal

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        firewall = d.pop("firewall", UNSET)

        ssl_vpn = d.pop("sslVpn", UNSET)

        vpn_user = d.pop("vpnUser", UNSET)

        one_to_one_nat = d.pop("oneToOneNat", UNSET)

        disable_nat = d.pop("disableNat", UNSET)

        ip_mac_binding = d.pop("ipMacBinding", UNSET)

        qos = d.pop("qos", UNSET)

        wireguard = d.pop("wireguard", UNSET)

        dns_proxy = d.pop("dnsProxy", UNSET)

        ipsec_failover = d.pop("ipsecFailover", UNSET)

        ldap_vpn = d.pop("ldapVpn", UNSET)

        service_type = d.pop("serviceType", UNSET)

        ips_ids = d.pop("ipsIds", UNSET)

        mac_filter = d.pop("macFilter", UNSET)

        sim = d.pop("sim", UNSET)

        client_rate_limit = d.pop("clientRateLimit", UNSET)

        lock_to_ap = d.pop("lockToAp", UNSET)

        voip = d.pop("voip", UNSET)

        olt_vlan = d.pop("oltVlan", UNSET)

        p2p = d.pop("p2p", UNSET)

        server_open_vpn_google_ldap = d.pop("serverOpenVpnGoogleLdap", UNSET)

        virtual_wan = d.pop("virtualWan", UNSET)

        l_2tp = d.pop("l2TP", UNSET)

        ipsec = d.pop("ipsec", UNSET)

        ip_port_group = d.pop("ipPortGroup", UNSET)

        support_es = d.pop("supportES", UNSET)

        support_l2 = d.pop("supportL2", UNSET)

        url_category = d.pop("urlCategory", UNSET)

        custom_acl = d.pop("customAcl", UNSET)

        peer_endpoint_domain = d.pop("peerEndpointDomain", UNSET)

        lan_dns = d.pop("lanDns", UNSET)

        isolation_settings = d.pop("IsolationSettings", UNSET)

        dsl = d.pop("dsl", UNSET)

        ldap_ssl = d.pop("ldapSsl", UNSET)

        google_ldap = d.pop("googleLdap", UNSET)

        dpi = d.pop("dpi", UNSET)

        package_capture_gateway = d.pop("packageCaptureGateway", UNSET)

        cluster = d.pop("cluster", UNSET)

        cluster_mode_on = d.pop("clusterModeOn", UNSET)

        init_cluster_reminder = d.pop("initClusterReminder", UNSET)

        dpi_stat = d.pop("dpiStat", UNSET)

        service_iptv = d.pop("serviceIptv", UNSET)

        sub_vpn = d.pop("subVpn", UNSET)

        vpn_status = d.pop("vpnStatus", UNSET)

        policy_routing = d.pop("policyRouting", UNSET)

        support_dpi = d.pop("supportDpi", UNSET)

        support_show_server_in_reservation = d.pop(
            "supportShowServerInReservation", UNSET
        )

        speed_test = d.pop("speedTest", UNSET)

        nat_traversal = d.pop("natTraversal", UNSET)

        site_setting_cap_open_api_vo = cls(
            firewall=firewall,
            ssl_vpn=ssl_vpn,
            vpn_user=vpn_user,
            one_to_one_nat=one_to_one_nat,
            disable_nat=disable_nat,
            ip_mac_binding=ip_mac_binding,
            qos=qos,
            wireguard=wireguard,
            dns_proxy=dns_proxy,
            ipsec_failover=ipsec_failover,
            ldap_vpn=ldap_vpn,
            service_type=service_type,
            ips_ids=ips_ids,
            mac_filter=mac_filter,
            sim=sim,
            client_rate_limit=client_rate_limit,
            lock_to_ap=lock_to_ap,
            voip=voip,
            olt_vlan=olt_vlan,
            p2p=p2p,
            server_open_vpn_google_ldap=server_open_vpn_google_ldap,
            virtual_wan=virtual_wan,
            l_2tp=l_2tp,
            ipsec=ipsec,
            ip_port_group=ip_port_group,
            support_es=support_es,
            support_l2=support_l2,
            url_category=url_category,
            custom_acl=custom_acl,
            peer_endpoint_domain=peer_endpoint_domain,
            lan_dns=lan_dns,
            isolation_settings=isolation_settings,
            dsl=dsl,
            ldap_ssl=ldap_ssl,
            google_ldap=google_ldap,
            dpi=dpi,
            package_capture_gateway=package_capture_gateway,
            cluster=cluster,
            cluster_mode_on=cluster_mode_on,
            init_cluster_reminder=init_cluster_reminder,
            dpi_stat=dpi_stat,
            service_iptv=service_iptv,
            sub_vpn=sub_vpn,
            vpn_status=vpn_status,
            policy_routing=policy_routing,
            support_dpi=support_dpi,
            support_show_server_in_reservation=support_show_server_in_reservation,
            speed_test=speed_test,
            nat_traversal=nat_traversal,
        )

        site_setting_cap_open_api_vo.additional_properties = d
        return site_setting_cap_open_api_vo

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
