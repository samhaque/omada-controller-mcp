from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SiteSettingCapVO")


@_attrs_define
class SiteSettingCapVO:
    """
    Attributes:
        firewall (bool | Unset):
        ssl_vpn (bool | Unset):
        vpn_user (bool | Unset):
        one_to_one_nat (bool | Unset):
        disable_nat (bool | Unset):
        ip_mac_binding (bool | Unset):
        qos (bool | Unset):
        wireguard (bool | Unset):
        dns_proxy (bool | Unset):
        ipsec_failover (bool | Unset):
        ldap_vpn (bool | Unset):
        service_type (bool | Unset):
        dns_cache (bool | Unset):
        ips_ids (bool | Unset):
        mac_filter (bool | Unset):
        app_control (bool | Unset):
        application_control (bool | Unset):
        sim (bool | Unset):
        client_rate_limit (bool | Unset):
        lock_to_ap (bool | Unset):
        voip (bool | Unset):
        olt_vlan (bool | Unset):
        p2p (bool | Unset):
        server_open_vpn_google_ldap (bool | Unset):
        google_ldap (bool | Unset):
        virtual_wan (bool | Unset):
        l_2tp (bool | Unset):
        ipsec (bool | Unset):
        open_vpn (bool | Unset):
        pptp (bool | Unset):
        ip_port_group (bool | Unset):
        support_es (bool | Unset):
        support_l2 (bool | Unset):
        support_l3 (bool | Unset):
        url_category (bool | Unset):
        custom_acl (bool | Unset):
        peer_endpoint_domain (bool | Unset):
        lan_dns (bool | Unset):
        isolation_settings (bool | Unset):
        dsl (bool | Unset):
        ldap_ssl (bool | Unset):
        package_capture_gateway (bool | Unset):
        cluster (bool | Unset):
        cluster_mode_on (bool | Unset):
        init_cluster_reminder (bool | Unset):
        cert_profile (bool | Unset):
        network_check_support (bool | Unset):
        ping_support (bool | Unset):
        traceroute_support (bool | Unset):
        dns_loop_up_support (bool | Unset):
        arp_table_support (bool | Unset):
        packet_capture_support (bool | Unset):
        terminal_support (bool | Unset):
        service_iptv (bool | Unset):
        sub_vpn (bool | Unset):
        vpn_status (bool | Unset):
        policy_routing (bool | Unset):
        internet (bool | Unset):
        wireless (bool | Unset):
        radios (bool | Unset):
        beacon_control (bool | Unset):
        wlans (bool | Unset):
        network_security (bool | Unset):
        attack_defense (bool | Unset):
        transmission (bool | Unset):
        ddns (bool | Unset):
        upnp (bool | Unset):
        iptv (bool | Unset):
        dhcp_reservation (bool | Unset):
        snmp_service_setting (bool | Unset):
        ssh (bool | Unset):
        statistics (bool | Unset):
        speed_test (bool | Unset):
        speed_test_schedule (bool | Unset):
        domain_no_port_group (bool | Unset):
        server_client_wireguard (bool | Unset):
        support_dpi (bool | Unset):
        vpn_server (bool | Unset):
        vpn_client (bool | Unset):
        site_to_site_vpn (bool | Unset):
        dpi_stat (bool | Unset):
        support_show_server_in_reservation (bool | Unset):
        dpi (bool | Unset):
        nat_traversal (bool | Unset):
        support_get_dhcp_lease_time (bool | Unset):
        cluster_hs_mode (bool | Unset):
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
    dns_cache: bool | Unset = UNSET
    ips_ids: bool | Unset = UNSET
    mac_filter: bool | Unset = UNSET
    app_control: bool | Unset = UNSET
    application_control: bool | Unset = UNSET
    sim: bool | Unset = UNSET
    client_rate_limit: bool | Unset = UNSET
    lock_to_ap: bool | Unset = UNSET
    voip: bool | Unset = UNSET
    olt_vlan: bool | Unset = UNSET
    p2p: bool | Unset = UNSET
    server_open_vpn_google_ldap: bool | Unset = UNSET
    google_ldap: bool | Unset = UNSET
    virtual_wan: bool | Unset = UNSET
    l_2tp: bool | Unset = UNSET
    ipsec: bool | Unset = UNSET
    open_vpn: bool | Unset = UNSET
    pptp: bool | Unset = UNSET
    ip_port_group: bool | Unset = UNSET
    support_es: bool | Unset = UNSET
    support_l2: bool | Unset = UNSET
    support_l3: bool | Unset = UNSET
    url_category: bool | Unset = UNSET
    custom_acl: bool | Unset = UNSET
    peer_endpoint_domain: bool | Unset = UNSET
    lan_dns: bool | Unset = UNSET
    isolation_settings: bool | Unset = UNSET
    dsl: bool | Unset = UNSET
    ldap_ssl: bool | Unset = UNSET
    package_capture_gateway: bool | Unset = UNSET
    cluster: bool | Unset = UNSET
    cluster_mode_on: bool | Unset = UNSET
    init_cluster_reminder: bool | Unset = UNSET
    cert_profile: bool | Unset = UNSET
    network_check_support: bool | Unset = UNSET
    ping_support: bool | Unset = UNSET
    traceroute_support: bool | Unset = UNSET
    dns_loop_up_support: bool | Unset = UNSET
    arp_table_support: bool | Unset = UNSET
    packet_capture_support: bool | Unset = UNSET
    terminal_support: bool | Unset = UNSET
    service_iptv: bool | Unset = UNSET
    sub_vpn: bool | Unset = UNSET
    vpn_status: bool | Unset = UNSET
    policy_routing: bool | Unset = UNSET
    internet: bool | Unset = UNSET
    wireless: bool | Unset = UNSET
    radios: bool | Unset = UNSET
    beacon_control: bool | Unset = UNSET
    wlans: bool | Unset = UNSET
    network_security: bool | Unset = UNSET
    attack_defense: bool | Unset = UNSET
    transmission: bool | Unset = UNSET
    ddns: bool | Unset = UNSET
    upnp: bool | Unset = UNSET
    iptv: bool | Unset = UNSET
    dhcp_reservation: bool | Unset = UNSET
    snmp_service_setting: bool | Unset = UNSET
    ssh: bool | Unset = UNSET
    statistics: bool | Unset = UNSET
    speed_test: bool | Unset = UNSET
    speed_test_schedule: bool | Unset = UNSET
    domain_no_port_group: bool | Unset = UNSET
    server_client_wireguard: bool | Unset = UNSET
    support_dpi: bool | Unset = UNSET
    vpn_server: bool | Unset = UNSET
    vpn_client: bool | Unset = UNSET
    site_to_site_vpn: bool | Unset = UNSET
    dpi_stat: bool | Unset = UNSET
    support_show_server_in_reservation: bool | Unset = UNSET
    dpi: bool | Unset = UNSET
    nat_traversal: bool | Unset = UNSET
    support_get_dhcp_lease_time: bool | Unset = UNSET
    cluster_hs_mode: bool | Unset = UNSET
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

        dns_cache = self.dns_cache

        ips_ids = self.ips_ids

        mac_filter = self.mac_filter

        app_control = self.app_control

        application_control = self.application_control

        sim = self.sim

        client_rate_limit = self.client_rate_limit

        lock_to_ap = self.lock_to_ap

        voip = self.voip

        olt_vlan = self.olt_vlan

        p2p = self.p2p

        server_open_vpn_google_ldap = self.server_open_vpn_google_ldap

        google_ldap = self.google_ldap

        virtual_wan = self.virtual_wan

        l_2tp = self.l_2tp

        ipsec = self.ipsec

        open_vpn = self.open_vpn

        pptp = self.pptp

        ip_port_group = self.ip_port_group

        support_es = self.support_es

        support_l2 = self.support_l2

        support_l3 = self.support_l3

        url_category = self.url_category

        custom_acl = self.custom_acl

        peer_endpoint_domain = self.peer_endpoint_domain

        lan_dns = self.lan_dns

        isolation_settings = self.isolation_settings

        dsl = self.dsl

        ldap_ssl = self.ldap_ssl

        package_capture_gateway = self.package_capture_gateway

        cluster = self.cluster

        cluster_mode_on = self.cluster_mode_on

        init_cluster_reminder = self.init_cluster_reminder

        cert_profile = self.cert_profile

        network_check_support = self.network_check_support

        ping_support = self.ping_support

        traceroute_support = self.traceroute_support

        dns_loop_up_support = self.dns_loop_up_support

        arp_table_support = self.arp_table_support

        packet_capture_support = self.packet_capture_support

        terminal_support = self.terminal_support

        service_iptv = self.service_iptv

        sub_vpn = self.sub_vpn

        vpn_status = self.vpn_status

        policy_routing = self.policy_routing

        internet = self.internet

        wireless = self.wireless

        radios = self.radios

        beacon_control = self.beacon_control

        wlans = self.wlans

        network_security = self.network_security

        attack_defense = self.attack_defense

        transmission = self.transmission

        ddns = self.ddns

        upnp = self.upnp

        iptv = self.iptv

        dhcp_reservation = self.dhcp_reservation

        snmp_service_setting = self.snmp_service_setting

        ssh = self.ssh

        statistics = self.statistics

        speed_test = self.speed_test

        speed_test_schedule = self.speed_test_schedule

        domain_no_port_group = self.domain_no_port_group

        server_client_wireguard = self.server_client_wireguard

        support_dpi = self.support_dpi

        vpn_server = self.vpn_server

        vpn_client = self.vpn_client

        site_to_site_vpn = self.site_to_site_vpn

        dpi_stat = self.dpi_stat

        support_show_server_in_reservation = self.support_show_server_in_reservation

        dpi = self.dpi

        nat_traversal = self.nat_traversal

        support_get_dhcp_lease_time = self.support_get_dhcp_lease_time

        cluster_hs_mode = self.cluster_hs_mode

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
        if dns_cache is not UNSET:
            field_dict["dnsCache"] = dns_cache
        if ips_ids is not UNSET:
            field_dict["ipsIds"] = ips_ids
        if mac_filter is not UNSET:
            field_dict["macFilter"] = mac_filter
        if app_control is not UNSET:
            field_dict["appControl"] = app_control
        if application_control is not UNSET:
            field_dict["applicationControl"] = application_control
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
        if google_ldap is not UNSET:
            field_dict["googleLdap"] = google_ldap
        if virtual_wan is not UNSET:
            field_dict["virtualWan"] = virtual_wan
        if l_2tp is not UNSET:
            field_dict["l2TP"] = l_2tp
        if ipsec is not UNSET:
            field_dict["ipsec"] = ipsec
        if open_vpn is not UNSET:
            field_dict["openVpn"] = open_vpn
        if pptp is not UNSET:
            field_dict["pptp"] = pptp
        if ip_port_group is not UNSET:
            field_dict["ipPortGroup"] = ip_port_group
        if support_es is not UNSET:
            field_dict["supportES"] = support_es
        if support_l2 is not UNSET:
            field_dict["supportL2"] = support_l2
        if support_l3 is not UNSET:
            field_dict["supportL3"] = support_l3
        if url_category is not UNSET:
            field_dict["urlCategory"] = url_category
        if custom_acl is not UNSET:
            field_dict["customAcl"] = custom_acl
        if peer_endpoint_domain is not UNSET:
            field_dict["peerEndpointDomain"] = peer_endpoint_domain
        if lan_dns is not UNSET:
            field_dict["lanDns"] = lan_dns
        if isolation_settings is not UNSET:
            field_dict["isolationSettings"] = isolation_settings
        if dsl is not UNSET:
            field_dict["dsl"] = dsl
        if ldap_ssl is not UNSET:
            field_dict["ldapSsl"] = ldap_ssl
        if package_capture_gateway is not UNSET:
            field_dict["packageCaptureGateway"] = package_capture_gateway
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if cluster_mode_on is not UNSET:
            field_dict["clusterModeOn"] = cluster_mode_on
        if init_cluster_reminder is not UNSET:
            field_dict["initClusterReminder"] = init_cluster_reminder
        if cert_profile is not UNSET:
            field_dict["certProfile"] = cert_profile
        if network_check_support is not UNSET:
            field_dict["networkCheckSupport"] = network_check_support
        if ping_support is not UNSET:
            field_dict["pingSupport"] = ping_support
        if traceroute_support is not UNSET:
            field_dict["tracerouteSupport"] = traceroute_support
        if dns_loop_up_support is not UNSET:
            field_dict["dnsLoopUpSupport"] = dns_loop_up_support
        if arp_table_support is not UNSET:
            field_dict["arpTableSupport"] = arp_table_support
        if packet_capture_support is not UNSET:
            field_dict["packetCaptureSupport"] = packet_capture_support
        if terminal_support is not UNSET:
            field_dict["terminalSupport"] = terminal_support
        if service_iptv is not UNSET:
            field_dict["serviceIptv"] = service_iptv
        if sub_vpn is not UNSET:
            field_dict["subVpn"] = sub_vpn
        if vpn_status is not UNSET:
            field_dict["vpnStatus"] = vpn_status
        if policy_routing is not UNSET:
            field_dict["policyRouting"] = policy_routing
        if internet is not UNSET:
            field_dict["internet"] = internet
        if wireless is not UNSET:
            field_dict["wireless"] = wireless
        if radios is not UNSET:
            field_dict["radios"] = radios
        if beacon_control is not UNSET:
            field_dict["beaconControl"] = beacon_control
        if wlans is not UNSET:
            field_dict["wlans"] = wlans
        if network_security is not UNSET:
            field_dict["networkSecurity"] = network_security
        if attack_defense is not UNSET:
            field_dict["attackDefense"] = attack_defense
        if transmission is not UNSET:
            field_dict["transmission"] = transmission
        if ddns is not UNSET:
            field_dict["ddns"] = ddns
        if upnp is not UNSET:
            field_dict["upnp"] = upnp
        if iptv is not UNSET:
            field_dict["iptv"] = iptv
        if dhcp_reservation is not UNSET:
            field_dict["dhcpReservation"] = dhcp_reservation
        if snmp_service_setting is not UNSET:
            field_dict["snmpServiceSetting"] = snmp_service_setting
        if ssh is not UNSET:
            field_dict["ssh"] = ssh
        if statistics is not UNSET:
            field_dict["statistics"] = statistics
        if speed_test is not UNSET:
            field_dict["speedTest"] = speed_test
        if speed_test_schedule is not UNSET:
            field_dict["speedTestSchedule"] = speed_test_schedule
        if domain_no_port_group is not UNSET:
            field_dict["domainNoPortGroup"] = domain_no_port_group
        if server_client_wireguard is not UNSET:
            field_dict["serverClientWireguard"] = server_client_wireguard
        if support_dpi is not UNSET:
            field_dict["supportDpi"] = support_dpi
        if vpn_server is not UNSET:
            field_dict["vpnServer"] = vpn_server
        if vpn_client is not UNSET:
            field_dict["vpnClient"] = vpn_client
        if site_to_site_vpn is not UNSET:
            field_dict["siteToSiteVpn"] = site_to_site_vpn
        if dpi_stat is not UNSET:
            field_dict["dpiStat"] = dpi_stat
        if support_show_server_in_reservation is not UNSET:
            field_dict["supportShowServerInReservation"] = (
                support_show_server_in_reservation
            )
        if dpi is not UNSET:
            field_dict["dpi"] = dpi
        if nat_traversal is not UNSET:
            field_dict["natTraversal"] = nat_traversal
        if support_get_dhcp_lease_time is not UNSET:
            field_dict["supportGetDhcpLeaseTime"] = support_get_dhcp_lease_time
        if cluster_hs_mode is not UNSET:
            field_dict["clusterHsMode"] = cluster_hs_mode

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

        dns_cache = d.pop("dnsCache", UNSET)

        ips_ids = d.pop("ipsIds", UNSET)

        mac_filter = d.pop("macFilter", UNSET)

        app_control = d.pop("appControl", UNSET)

        application_control = d.pop("applicationControl", UNSET)

        sim = d.pop("sim", UNSET)

        client_rate_limit = d.pop("clientRateLimit", UNSET)

        lock_to_ap = d.pop("lockToAp", UNSET)

        voip = d.pop("voip", UNSET)

        olt_vlan = d.pop("oltVlan", UNSET)

        p2p = d.pop("p2p", UNSET)

        server_open_vpn_google_ldap = d.pop("serverOpenVpnGoogleLdap", UNSET)

        google_ldap = d.pop("googleLdap", UNSET)

        virtual_wan = d.pop("virtualWan", UNSET)

        l_2tp = d.pop("l2TP", UNSET)

        ipsec = d.pop("ipsec", UNSET)

        open_vpn = d.pop("openVpn", UNSET)

        pptp = d.pop("pptp", UNSET)

        ip_port_group = d.pop("ipPortGroup", UNSET)

        support_es = d.pop("supportES", UNSET)

        support_l2 = d.pop("supportL2", UNSET)

        support_l3 = d.pop("supportL3", UNSET)

        url_category = d.pop("urlCategory", UNSET)

        custom_acl = d.pop("customAcl", UNSET)

        peer_endpoint_domain = d.pop("peerEndpointDomain", UNSET)

        lan_dns = d.pop("lanDns", UNSET)

        isolation_settings = d.pop("isolationSettings", UNSET)

        dsl = d.pop("dsl", UNSET)

        ldap_ssl = d.pop("ldapSsl", UNSET)

        package_capture_gateway = d.pop("packageCaptureGateway", UNSET)

        cluster = d.pop("cluster", UNSET)

        cluster_mode_on = d.pop("clusterModeOn", UNSET)

        init_cluster_reminder = d.pop("initClusterReminder", UNSET)

        cert_profile = d.pop("certProfile", UNSET)

        network_check_support = d.pop("networkCheckSupport", UNSET)

        ping_support = d.pop("pingSupport", UNSET)

        traceroute_support = d.pop("tracerouteSupport", UNSET)

        dns_loop_up_support = d.pop("dnsLoopUpSupport", UNSET)

        arp_table_support = d.pop("arpTableSupport", UNSET)

        packet_capture_support = d.pop("packetCaptureSupport", UNSET)

        terminal_support = d.pop("terminalSupport", UNSET)

        service_iptv = d.pop("serviceIptv", UNSET)

        sub_vpn = d.pop("subVpn", UNSET)

        vpn_status = d.pop("vpnStatus", UNSET)

        policy_routing = d.pop("policyRouting", UNSET)

        internet = d.pop("internet", UNSET)

        wireless = d.pop("wireless", UNSET)

        radios = d.pop("radios", UNSET)

        beacon_control = d.pop("beaconControl", UNSET)

        wlans = d.pop("wlans", UNSET)

        network_security = d.pop("networkSecurity", UNSET)

        attack_defense = d.pop("attackDefense", UNSET)

        transmission = d.pop("transmission", UNSET)

        ddns = d.pop("ddns", UNSET)

        upnp = d.pop("upnp", UNSET)

        iptv = d.pop("iptv", UNSET)

        dhcp_reservation = d.pop("dhcpReservation", UNSET)

        snmp_service_setting = d.pop("snmpServiceSetting", UNSET)

        ssh = d.pop("ssh", UNSET)

        statistics = d.pop("statistics", UNSET)

        speed_test = d.pop("speedTest", UNSET)

        speed_test_schedule = d.pop("speedTestSchedule", UNSET)

        domain_no_port_group = d.pop("domainNoPortGroup", UNSET)

        server_client_wireguard = d.pop("serverClientWireguard", UNSET)

        support_dpi = d.pop("supportDpi", UNSET)

        vpn_server = d.pop("vpnServer", UNSET)

        vpn_client = d.pop("vpnClient", UNSET)

        site_to_site_vpn = d.pop("siteToSiteVpn", UNSET)

        dpi_stat = d.pop("dpiStat", UNSET)

        support_show_server_in_reservation = d.pop(
            "supportShowServerInReservation", UNSET
        )

        dpi = d.pop("dpi", UNSET)

        nat_traversal = d.pop("natTraversal", UNSET)

        support_get_dhcp_lease_time = d.pop("supportGetDhcpLeaseTime", UNSET)

        cluster_hs_mode = d.pop("clusterHsMode", UNSET)

        site_setting_cap_vo = cls(
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
            dns_cache=dns_cache,
            ips_ids=ips_ids,
            mac_filter=mac_filter,
            app_control=app_control,
            application_control=application_control,
            sim=sim,
            client_rate_limit=client_rate_limit,
            lock_to_ap=lock_to_ap,
            voip=voip,
            olt_vlan=olt_vlan,
            p2p=p2p,
            server_open_vpn_google_ldap=server_open_vpn_google_ldap,
            google_ldap=google_ldap,
            virtual_wan=virtual_wan,
            l_2tp=l_2tp,
            ipsec=ipsec,
            open_vpn=open_vpn,
            pptp=pptp,
            ip_port_group=ip_port_group,
            support_es=support_es,
            support_l2=support_l2,
            support_l3=support_l3,
            url_category=url_category,
            custom_acl=custom_acl,
            peer_endpoint_domain=peer_endpoint_domain,
            lan_dns=lan_dns,
            isolation_settings=isolation_settings,
            dsl=dsl,
            ldap_ssl=ldap_ssl,
            package_capture_gateway=package_capture_gateway,
            cluster=cluster,
            cluster_mode_on=cluster_mode_on,
            init_cluster_reminder=init_cluster_reminder,
            cert_profile=cert_profile,
            network_check_support=network_check_support,
            ping_support=ping_support,
            traceroute_support=traceroute_support,
            dns_loop_up_support=dns_loop_up_support,
            arp_table_support=arp_table_support,
            packet_capture_support=packet_capture_support,
            terminal_support=terminal_support,
            service_iptv=service_iptv,
            sub_vpn=sub_vpn,
            vpn_status=vpn_status,
            policy_routing=policy_routing,
            internet=internet,
            wireless=wireless,
            radios=radios,
            beacon_control=beacon_control,
            wlans=wlans,
            network_security=network_security,
            attack_defense=attack_defense,
            transmission=transmission,
            ddns=ddns,
            upnp=upnp,
            iptv=iptv,
            dhcp_reservation=dhcp_reservation,
            snmp_service_setting=snmp_service_setting,
            ssh=ssh,
            statistics=statistics,
            speed_test=speed_test,
            speed_test_schedule=speed_test_schedule,
            domain_no_port_group=domain_no_port_group,
            server_client_wireguard=server_client_wireguard,
            support_dpi=support_dpi,
            vpn_server=vpn_server,
            vpn_client=vpn_client,
            site_to_site_vpn=site_to_site_vpn,
            dpi_stat=dpi_stat,
            support_show_server_in_reservation=support_show_server_in_reservation,
            dpi=dpi,
            nat_traversal=nat_traversal,
            support_get_dhcp_lease_time=support_get_dhcp_lease_time,
            cluster_hs_mode=cluster_hs_mode,
        )

        site_setting_cap_vo.additional_properties = d
        return site_setting_cap_vo

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
