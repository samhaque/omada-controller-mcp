from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vpn_summary_vo import VpnSummaryVO


T = TypeVar("T", bound="VpnSummaryOpenApiGridVOVpnSummaryVO")


@_attrs_define
class VpnSummaryOpenApiGridVOVpnSummaryVO:
    """
    Attributes:
        total_rows (int | Unset): Total rows of all items.
        current_page (int | Unset): Current page number.
        current_size (int | Unset): Number of entries per page.
        data (list[VpnSummaryVO] | Unset):
        support_vpn_user_tab (bool | Unset): Whether user tab configuration is supported of the VPN
        support_custom_dns (bool | Unset): Whether custom dns configuration is supported of the VPN
        support_custom_network (bool | Unset): Whether custom network configuration is supported of the VPN
        support_account_auth (bool | Unset): Whether account auth configuration is supported of the VPN
        support_ip_range (bool | Unset): Whether ip range configuration is supported of the VPN
        support_tunnel_mode (bool | Unset): Whether tunnel mode configuration is supported of the VPN
        support_ldap (bool | Unset): Whether LDAP authentication mode is supported of the VPN server
        support_ssl_vpn_ldap (bool | Unset): Whether LDAP authentication mode is supported of the SSl VPN server
        support_ssl_vpn_radius (bool | Unset): Whether radius authentication mode is supported of the SSl VPN server
        support_l2tp (bool | Unset): Whether L2TP VPN is supported.
        support_i_psec (bool | Unset): Whether IPsec VPN is supported.
        support_i_psec_ip_range (bool | Unset): Whether IP range is supported of IPSec VPN Server.
        support_open_vpn_domain (bool | Unset): Whether OpenVPN supports inputting domain.
        support_wg_domain (bool | Unset): Whether peer supports inputting domain.
        pfs_cap (list[int] | Unset): All PFS configuration types supported by the device, 1:dh1; 2:dh2; 3:dh3; 14:dh14;
            15:dh15. Default: dh1、dh2、dh5
        support_server_client_wire_guard (bool | Unset): Whether Server/Client Wire Guard is supported.
        support_custom_server (bool | Unset): Whether custom server is supported.
        phase_1_proposal_1_cap (list[int] | Unset): Proposal options for IKE negotiation phase-1. 0: MD5, 1: SHA1,
            2:SHA256, 3:SHA384, 4:SHA512. Default: MD5, SHA1 and SHA256
        phase_2_proposal_2_cap (list[int] | Unset): Proposal options for IKE negotiation phase-2. 0: MD5, 1: SHA1,
            2:SHA256, 3:SHA384, 4:SHA512. Default: MD5, SHA1 and SHA256
        support_by_ds_lite_and_map_e (bool | Unset): Whether this feature is supported for the DS-Lite or Map-E WAN
            connection types.
        support_server_open_vpn_google_ldap (bool | Unset): Whether Open VPN Server supports Google LDAP.
        support_dns_status (bool | Unset): Whether supports dns auto.
        subnets_limit_size (int | Unset): The limit on the number of entries for remote subnets and local network.
        wg_peer_limit_size (int | Unset): The limit on the number of entries for peer in WireGuard.
        support_manual_wg_local_network (bool | Unset): Whether manual Wire Guard in site to site supports local
            network.
        support_auto_wire_guard (bool | Unset): Whether auto Wire Guard in site to site is supported.
        support_i_psec_failover (bool | Unset): Whether supports IPSec failover in manual IPSec.
        ssl_vpn_num (int | Unset): The number of SSLVPN servers.
    """

    total_rows: int | Unset = UNSET
    current_page: int | Unset = UNSET
    current_size: int | Unset = UNSET
    data: list[VpnSummaryVO] | Unset = UNSET
    support_vpn_user_tab: bool | Unset = UNSET
    support_custom_dns: bool | Unset = UNSET
    support_custom_network: bool | Unset = UNSET
    support_account_auth: bool | Unset = UNSET
    support_ip_range: bool | Unset = UNSET
    support_tunnel_mode: bool | Unset = UNSET
    support_ldap: bool | Unset = UNSET
    support_ssl_vpn_ldap: bool | Unset = UNSET
    support_ssl_vpn_radius: bool | Unset = UNSET
    support_l2tp: bool | Unset = UNSET
    support_i_psec: bool | Unset = UNSET
    support_i_psec_ip_range: bool | Unset = UNSET
    support_open_vpn_domain: bool | Unset = UNSET
    support_wg_domain: bool | Unset = UNSET
    pfs_cap: list[int] | Unset = UNSET
    support_server_client_wire_guard: bool | Unset = UNSET
    support_custom_server: bool | Unset = UNSET
    phase_1_proposal_1_cap: list[int] | Unset = UNSET
    phase_2_proposal_2_cap: list[int] | Unset = UNSET
    support_by_ds_lite_and_map_e: bool | Unset = UNSET
    support_server_open_vpn_google_ldap: bool | Unset = UNSET
    support_dns_status: bool | Unset = UNSET
    subnets_limit_size: int | Unset = UNSET
    wg_peer_limit_size: int | Unset = UNSET
    support_manual_wg_local_network: bool | Unset = UNSET
    support_auto_wire_guard: bool | Unset = UNSET
    support_i_psec_failover: bool | Unset = UNSET
    ssl_vpn_num: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_rows = self.total_rows

        current_page = self.current_page

        current_size = self.current_size

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        support_vpn_user_tab = self.support_vpn_user_tab

        support_custom_dns = self.support_custom_dns

        support_custom_network = self.support_custom_network

        support_account_auth = self.support_account_auth

        support_ip_range = self.support_ip_range

        support_tunnel_mode = self.support_tunnel_mode

        support_ldap = self.support_ldap

        support_ssl_vpn_ldap = self.support_ssl_vpn_ldap

        support_ssl_vpn_radius = self.support_ssl_vpn_radius

        support_l2tp = self.support_l2tp

        support_i_psec = self.support_i_psec

        support_i_psec_ip_range = self.support_i_psec_ip_range

        support_open_vpn_domain = self.support_open_vpn_domain

        support_wg_domain = self.support_wg_domain

        pfs_cap: list[int] | Unset = UNSET
        if not isinstance(self.pfs_cap, Unset):
            pfs_cap = self.pfs_cap

        support_server_client_wire_guard = self.support_server_client_wire_guard

        support_custom_server = self.support_custom_server

        phase_1_proposal_1_cap: list[int] | Unset = UNSET
        if not isinstance(self.phase_1_proposal_1_cap, Unset):
            phase_1_proposal_1_cap = self.phase_1_proposal_1_cap

        phase_2_proposal_2_cap: list[int] | Unset = UNSET
        if not isinstance(self.phase_2_proposal_2_cap, Unset):
            phase_2_proposal_2_cap = self.phase_2_proposal_2_cap

        support_by_ds_lite_and_map_e = self.support_by_ds_lite_and_map_e

        support_server_open_vpn_google_ldap = self.support_server_open_vpn_google_ldap

        support_dns_status = self.support_dns_status

        subnets_limit_size = self.subnets_limit_size

        wg_peer_limit_size = self.wg_peer_limit_size

        support_manual_wg_local_network = self.support_manual_wg_local_network

        support_auto_wire_guard = self.support_auto_wire_guard

        support_i_psec_failover = self.support_i_psec_failover

        ssl_vpn_num = self.ssl_vpn_num

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_rows is not UNSET:
            field_dict["totalRows"] = total_rows
        if current_page is not UNSET:
            field_dict["currentPage"] = current_page
        if current_size is not UNSET:
            field_dict["currentSize"] = current_size
        if data is not UNSET:
            field_dict["data"] = data
        if support_vpn_user_tab is not UNSET:
            field_dict["supportVpnUserTab"] = support_vpn_user_tab
        if support_custom_dns is not UNSET:
            field_dict["supportCustomDns"] = support_custom_dns
        if support_custom_network is not UNSET:
            field_dict["supportCustomNetwork"] = support_custom_network
        if support_account_auth is not UNSET:
            field_dict["supportAccountAuth"] = support_account_auth
        if support_ip_range is not UNSET:
            field_dict["supportIpRange"] = support_ip_range
        if support_tunnel_mode is not UNSET:
            field_dict["supportTunnelMode"] = support_tunnel_mode
        if support_ldap is not UNSET:
            field_dict["supportLdap"] = support_ldap
        if support_ssl_vpn_ldap is not UNSET:
            field_dict["supportSslVpnLdap"] = support_ssl_vpn_ldap
        if support_ssl_vpn_radius is not UNSET:
            field_dict["supportSslVpnRadius"] = support_ssl_vpn_radius
        if support_l2tp is not UNSET:
            field_dict["supportL2TP"] = support_l2tp
        if support_i_psec is not UNSET:
            field_dict["supportIPsec"] = support_i_psec
        if support_i_psec_ip_range is not UNSET:
            field_dict["supportIPsecIpRange"] = support_i_psec_ip_range
        if support_open_vpn_domain is not UNSET:
            field_dict["supportOpenVpnDomain"] = support_open_vpn_domain
        if support_wg_domain is not UNSET:
            field_dict["supportWgDomain"] = support_wg_domain
        if pfs_cap is not UNSET:
            field_dict["pfsCap"] = pfs_cap
        if support_server_client_wire_guard is not UNSET:
            field_dict["supportServerClientWireGuard"] = (
                support_server_client_wire_guard
            )
        if support_custom_server is not UNSET:
            field_dict["supportCustomServer"] = support_custom_server
        if phase_1_proposal_1_cap is not UNSET:
            field_dict["phase1Proposal1Cap"] = phase_1_proposal_1_cap
        if phase_2_proposal_2_cap is not UNSET:
            field_dict["phase2Proposal2Cap"] = phase_2_proposal_2_cap
        if support_by_ds_lite_and_map_e is not UNSET:
            field_dict["supportByDsLiteAndMapE"] = support_by_ds_lite_and_map_e
        if support_server_open_vpn_google_ldap is not UNSET:
            field_dict["supportServerOpenVpnGoogleLdap"] = (
                support_server_open_vpn_google_ldap
            )
        if support_dns_status is not UNSET:
            field_dict["supportDnsStatus"] = support_dns_status
        if subnets_limit_size is not UNSET:
            field_dict["subnetsLimitSize"] = subnets_limit_size
        if wg_peer_limit_size is not UNSET:
            field_dict["wgPeerLimitSize"] = wg_peer_limit_size
        if support_manual_wg_local_network is not UNSET:
            field_dict["supportManualWgLocalNetwork"] = support_manual_wg_local_network
        if support_auto_wire_guard is not UNSET:
            field_dict["supportAutoWireGuard"] = support_auto_wire_guard
        if support_i_psec_failover is not UNSET:
            field_dict["supportIPsecFailover"] = support_i_psec_failover
        if ssl_vpn_num is not UNSET:
            field_dict["sslVpnNum"] = ssl_vpn_num

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.vpn_summary_vo import VpnSummaryVO

        d = dict(src_dict)
        total_rows = d.pop("totalRows", UNSET)

        current_page = d.pop("currentPage", UNSET)

        current_size = d.pop("currentSize", UNSET)

        _data = d.pop("data", UNSET)
        data: list[VpnSummaryVO] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = VpnSummaryVO.from_dict(data_item_data)

                data.append(data_item)

        support_vpn_user_tab = d.pop("supportVpnUserTab", UNSET)

        support_custom_dns = d.pop("supportCustomDns", UNSET)

        support_custom_network = d.pop("supportCustomNetwork", UNSET)

        support_account_auth = d.pop("supportAccountAuth", UNSET)

        support_ip_range = d.pop("supportIpRange", UNSET)

        support_tunnel_mode = d.pop("supportTunnelMode", UNSET)

        support_ldap = d.pop("supportLdap", UNSET)

        support_ssl_vpn_ldap = d.pop("supportSslVpnLdap", UNSET)

        support_ssl_vpn_radius = d.pop("supportSslVpnRadius", UNSET)

        support_l2tp = d.pop("supportL2TP", UNSET)

        support_i_psec = d.pop("supportIPsec", UNSET)

        support_i_psec_ip_range = d.pop("supportIPsecIpRange", UNSET)

        support_open_vpn_domain = d.pop("supportOpenVpnDomain", UNSET)

        support_wg_domain = d.pop("supportWgDomain", UNSET)

        pfs_cap = cast(list[int], d.pop("pfsCap", UNSET))

        support_server_client_wire_guard = d.pop("supportServerClientWireGuard", UNSET)

        support_custom_server = d.pop("supportCustomServer", UNSET)

        phase_1_proposal_1_cap = cast(list[int], d.pop("phase1Proposal1Cap", UNSET))

        phase_2_proposal_2_cap = cast(list[int], d.pop("phase2Proposal2Cap", UNSET))

        support_by_ds_lite_and_map_e = d.pop("supportByDsLiteAndMapE", UNSET)

        support_server_open_vpn_google_ldap = d.pop(
            "supportServerOpenVpnGoogleLdap", UNSET
        )

        support_dns_status = d.pop("supportDnsStatus", UNSET)

        subnets_limit_size = d.pop("subnetsLimitSize", UNSET)

        wg_peer_limit_size = d.pop("wgPeerLimitSize", UNSET)

        support_manual_wg_local_network = d.pop("supportManualWgLocalNetwork", UNSET)

        support_auto_wire_guard = d.pop("supportAutoWireGuard", UNSET)

        support_i_psec_failover = d.pop("supportIPsecFailover", UNSET)

        ssl_vpn_num = d.pop("sslVpnNum", UNSET)

        vpn_summary_open_api_grid_vo_vpn_summary_vo = cls(
            total_rows=total_rows,
            current_page=current_page,
            current_size=current_size,
            data=data,
            support_vpn_user_tab=support_vpn_user_tab,
            support_custom_dns=support_custom_dns,
            support_custom_network=support_custom_network,
            support_account_auth=support_account_auth,
            support_ip_range=support_ip_range,
            support_tunnel_mode=support_tunnel_mode,
            support_ldap=support_ldap,
            support_ssl_vpn_ldap=support_ssl_vpn_ldap,
            support_ssl_vpn_radius=support_ssl_vpn_radius,
            support_l2tp=support_l2tp,
            support_i_psec=support_i_psec,
            support_i_psec_ip_range=support_i_psec_ip_range,
            support_open_vpn_domain=support_open_vpn_domain,
            support_wg_domain=support_wg_domain,
            pfs_cap=pfs_cap,
            support_server_client_wire_guard=support_server_client_wire_guard,
            support_custom_server=support_custom_server,
            phase_1_proposal_1_cap=phase_1_proposal_1_cap,
            phase_2_proposal_2_cap=phase_2_proposal_2_cap,
            support_by_ds_lite_and_map_e=support_by_ds_lite_and_map_e,
            support_server_open_vpn_google_ldap=support_server_open_vpn_google_ldap,
            support_dns_status=support_dns_status,
            subnets_limit_size=subnets_limit_size,
            wg_peer_limit_size=wg_peer_limit_size,
            support_manual_wg_local_network=support_manual_wg_local_network,
            support_auto_wire_guard=support_auto_wire_guard,
            support_i_psec_failover=support_i_psec_failover,
            ssl_vpn_num=ssl_vpn_num,
        )

        vpn_summary_open_api_grid_vo_vpn_summary_vo.additional_properties = d
        return vpn_summary_open_api_grid_vo_vpn_summary_vo

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
