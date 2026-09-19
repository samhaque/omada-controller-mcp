from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_to_site_vpn_server import ClientToSiteVpnServer


T = TypeVar("T", bound="VpnOpenApiGridVOClientToSiteVpnServer")


@_attrs_define
class VpnOpenApiGridVOClientToSiteVpnServer:
    """
    Attributes:
        total_rows (int | Unset): Total rows of all items.
        current_page (int | Unset): Current page number.
        current_size (int | Unset): Number of entries per page.
        data (list[ClientToSiteVpnServer] | Unset):
        support_vpn_user_tab (bool | Unset): Whether user tab configuration is supported of the VPN
        support_custom_dns (bool | Unset): Whether custom dns configuration is supported of the VPN
        support_ip_range (bool | Unset): Whether ip range configuration is supported of the VPN
        support_account_auth (bool | Unset): Whether account auth configuration is supported of the VPN
        support_custom_network (bool | Unset): Whether custom network configuration is supported of the VPN
        support_tunnel_mode (bool | Unset): Whether tunnel mode configuration is supported of the VPN
        support_ldap (bool | Unset): Whether LDAP authentication mode is supported of the VPN server
        pfs_cap (list[int] | Unset): All PFS configuration types supported by the device, 1:dh1; 2:dh2; 3:dh3; 14:dh14;
            15:dh15. Default: dh1、dh2、dh5
        support_open_vpn_domain (bool | Unset): Whether OpenVPN supports inputting domain
        support_l2tp (bool | Unset): Whether L2TP VPN is supported.
        support_i_psec (bool | Unset): Whether IPsec VPN is supported.
        phase_1_proposal_1_cap (list[int] | Unset): Proposal options for IKE negotiation phase-1. 0: MD5, 1: SHA1,
            2:SHA256, 3:SHA384, 4:SHA512. Default: MD5, SHA1 and SHA256
        phase_2_proposal_2_cap (list[int] | Unset): Proposal options for IKE negotiation phase-2. 0: MD5, 1: SHA1,
            2:SHA256, 3:SHA384, 4:SHA512.+ Default: MD5, SHA1 and SHA256
        support_by_ds_lite_and_map_e (bool | Unset): Whether this feature is supported for the DS-Lite or Map-E WAN
            connection types.
        subnets_limit_size (int | Unset): The limit on the number of entries for remote subnets and local network.
    """

    total_rows: int | Unset = UNSET
    current_page: int | Unset = UNSET
    current_size: int | Unset = UNSET
    data: list[ClientToSiteVpnServer] | Unset = UNSET
    support_vpn_user_tab: bool | Unset = UNSET
    support_custom_dns: bool | Unset = UNSET
    support_ip_range: bool | Unset = UNSET
    support_account_auth: bool | Unset = UNSET
    support_custom_network: bool | Unset = UNSET
    support_tunnel_mode: bool | Unset = UNSET
    support_ldap: bool | Unset = UNSET
    pfs_cap: list[int] | Unset = UNSET
    support_open_vpn_domain: bool | Unset = UNSET
    support_l2tp: bool | Unset = UNSET
    support_i_psec: bool | Unset = UNSET
    phase_1_proposal_1_cap: list[int] | Unset = UNSET
    phase_2_proposal_2_cap: list[int] | Unset = UNSET
    support_by_ds_lite_and_map_e: bool | Unset = UNSET
    subnets_limit_size: int | Unset = UNSET
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

        support_ip_range = self.support_ip_range

        support_account_auth = self.support_account_auth

        support_custom_network = self.support_custom_network

        support_tunnel_mode = self.support_tunnel_mode

        support_ldap = self.support_ldap

        pfs_cap: list[int] | Unset = UNSET
        if not isinstance(self.pfs_cap, Unset):
            pfs_cap = self.pfs_cap

        support_open_vpn_domain = self.support_open_vpn_domain

        support_l2tp = self.support_l2tp

        support_i_psec = self.support_i_psec

        phase_1_proposal_1_cap: list[int] | Unset = UNSET
        if not isinstance(self.phase_1_proposal_1_cap, Unset):
            phase_1_proposal_1_cap = self.phase_1_proposal_1_cap

        phase_2_proposal_2_cap: list[int] | Unset = UNSET
        if not isinstance(self.phase_2_proposal_2_cap, Unset):
            phase_2_proposal_2_cap = self.phase_2_proposal_2_cap

        support_by_ds_lite_and_map_e = self.support_by_ds_lite_and_map_e

        subnets_limit_size = self.subnets_limit_size

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
        if support_ip_range is not UNSET:
            field_dict["supportIpRange"] = support_ip_range
        if support_account_auth is not UNSET:
            field_dict["supportAccountAuth"] = support_account_auth
        if support_custom_network is not UNSET:
            field_dict["supportCustomNetwork"] = support_custom_network
        if support_tunnel_mode is not UNSET:
            field_dict["supportTunnelMode"] = support_tunnel_mode
        if support_ldap is not UNSET:
            field_dict["supportLdap"] = support_ldap
        if pfs_cap is not UNSET:
            field_dict["pfsCap"] = pfs_cap
        if support_open_vpn_domain is not UNSET:
            field_dict["supportOpenVpnDomain"] = support_open_vpn_domain
        if support_l2tp is not UNSET:
            field_dict["supportL2TP"] = support_l2tp
        if support_i_psec is not UNSET:
            field_dict["supportIPsec"] = support_i_psec
        if phase_1_proposal_1_cap is not UNSET:
            field_dict["phase1Proposal1Cap"] = phase_1_proposal_1_cap
        if phase_2_proposal_2_cap is not UNSET:
            field_dict["phase2Proposal2Cap"] = phase_2_proposal_2_cap
        if support_by_ds_lite_and_map_e is not UNSET:
            field_dict["supportByDsLiteAndMapE"] = support_by_ds_lite_and_map_e
        if subnets_limit_size is not UNSET:
            field_dict["subnetsLimitSize"] = subnets_limit_size

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.client_to_site_vpn_server import (
            ClientToSiteVpnServer,
        )

        d = dict(src_dict)
        total_rows = d.pop("totalRows", UNSET)

        current_page = d.pop("currentPage", UNSET)

        current_size = d.pop("currentSize", UNSET)

        _data = d.pop("data", UNSET)
        data: list[ClientToSiteVpnServer] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = ClientToSiteVpnServer.from_dict(data_item_data)

                data.append(data_item)

        support_vpn_user_tab = d.pop("supportVpnUserTab", UNSET)

        support_custom_dns = d.pop("supportCustomDns", UNSET)

        support_ip_range = d.pop("supportIpRange", UNSET)

        support_account_auth = d.pop("supportAccountAuth", UNSET)

        support_custom_network = d.pop("supportCustomNetwork", UNSET)

        support_tunnel_mode = d.pop("supportTunnelMode", UNSET)

        support_ldap = d.pop("supportLdap", UNSET)

        pfs_cap = cast(list[int], d.pop("pfsCap", UNSET))

        support_open_vpn_domain = d.pop("supportOpenVpnDomain", UNSET)

        support_l2tp = d.pop("supportL2TP", UNSET)

        support_i_psec = d.pop("supportIPsec", UNSET)

        phase_1_proposal_1_cap = cast(list[int], d.pop("phase1Proposal1Cap", UNSET))

        phase_2_proposal_2_cap = cast(list[int], d.pop("phase2Proposal2Cap", UNSET))

        support_by_ds_lite_and_map_e = d.pop("supportByDsLiteAndMapE", UNSET)

        subnets_limit_size = d.pop("subnetsLimitSize", UNSET)

        vpn_open_api_grid_vo_client_to_site_vpn_server = cls(
            total_rows=total_rows,
            current_page=current_page,
            current_size=current_size,
            data=data,
            support_vpn_user_tab=support_vpn_user_tab,
            support_custom_dns=support_custom_dns,
            support_ip_range=support_ip_range,
            support_account_auth=support_account_auth,
            support_custom_network=support_custom_network,
            support_tunnel_mode=support_tunnel_mode,
            support_ldap=support_ldap,
            pfs_cap=pfs_cap,
            support_open_vpn_domain=support_open_vpn_domain,
            support_l2tp=support_l2tp,
            support_i_psec=support_i_psec,
            phase_1_proposal_1_cap=phase_1_proposal_1_cap,
            phase_2_proposal_2_cap=phase_2_proposal_2_cap,
            support_by_ds_lite_and_map_e=support_by_ds_lite_and_map_e,
            subnets_limit_size=subnets_limit_size,
        )

        vpn_open_api_grid_vo_client_to_site_vpn_server.additional_properties = d
        return vpn_open_api_grid_vo_client_to_site_vpn_server

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
