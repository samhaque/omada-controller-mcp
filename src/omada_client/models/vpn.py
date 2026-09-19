from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ip_subnets_vo import IPSubnetsVO
    from ..models.vpn_certificate_open_api_vo import VpnCertificateOpenApiVO


T = TypeVar("T", bound="VPN")


@_attrs_define
class VPN:
    """
    Attributes:
        name (str): Name should contain 1 to 63 characters.
        purpose (int): Purpose of the VPN.
        client_vpn_type_1 (int): Client to Site VPN : 0:VPN Server 1:VPN Client.
        client_vpn_type_2 (int): Client Vpn type should be a value as follows: 0: L2TP; 1: PPTP; 2: IPSec; 3: OpenVPN.
        ip_pool (IPSubnetsVO): User remote subnets of the VPN user.
        id (str | Unset): ID of the VPN.
        site_vpn_type (int | Unset): Site VPN type of the VPN.
        status (bool | Unset): Status of the VPN.
        account_auth (bool | Unset): Account auth of the VPN, only for server OpenVPN.
        exist_account_auth (bool | Unset): Whether Account Auth is configured.
        remote_site (str | Unset): Remote site of the VPN.
        remote_ip (str | Unset): Remote IP of the VPN.
        exist_open_vpn_domain (bool | Unset): Whether Open VPN Client Remote Server is Domain Name.
        remote_subnet (list[IPSubnetsVO] | Unset): Remote subnet of the VPN, only for Manual IPSec type.
        network_type (int | Unset): Network type should be a value as follows: 0: network list; 1: custom networks.
        network_list (list[str] | Unset): Network list of the VPN, only for Manual IPSec type. Network can be created
            using 'Create LAN network' interface, and network ID can be obtained from 'Get LAN network list' interface.
        custom_network (list[IPSubnetsVO] | Unset): Custom networks of the VPN, only for Manual IPSec type.
        exist_custom_network (bool | Unset): Whether Local Network Type is Custom.
        pre_shared_key (str | Unset): Pre-shared key of the VPN.
        wans (list[str] | Unset): WAN list of the VPN. WAN port ID can be obtained from 'Get internet basic info'
            interface.
        exist_l2tp (bool | Unset): Whether current VPN is L2TP type.
        exist_i_psec (bool | Unset): Whether current VPN is IPsec type.
        open_vpn_tunnel_mode (int | Unset): OpenVPN tunnel mode should be a value as follows: 0: split; 1: full.
        exist_tunnel_mode (bool | Unset): OpenVPN tunnel mode is Full.
        open_vpn_mode (int | Unset): OpenVPN mode should be a value as follows: 0: certification; 1:
            certification+account.
        service_type (int | Unset): Service type of the VPN.
        service_port (int | Unset): Service port should be within the range of 1–65535.
        encryption (int | Unset): Encryption should be a value as follows: 0: Encrypted; 1: Unencrypted.
        ip_pool_type (int | Unset): IP pool type should be a value as follows: 0: Ip Address/Mask; 1: Ip Address Range.
        exist_ip_range (bool | Unset): Whether IP pool type is Ip Address Range.
        ip_pool_start (str | Unset): The start IP of the IP pool.
        ip_pool_end (str | Unset): The end IP of the IP pool.
        primary_dns (str | Unset): Primary DNS of the VPN.
        secondary_dns (str | Unset): Secondary DNS of the VPN.
        exist_custom_dns (bool | Unset): Whether custom DNS Server has been configured in current VPN.
        auth_mode (int | Unset): Authentication mode should be a value as follows: 0: Local; 1: LDAP.
        ldap_profile (str | Unset): Ldap Profile.
        exist_ldap (bool | Unset): Whether Auth Mode is LDAP.
        exist_server_open_vpn_google_ldap (bool | Unset): Whether Auth Mode is Google LDAP.
        working_mode (int | Unset): Working Mode should be a value as follow: 0:NAT 1:Routing.
        client_user_name (str | Unset): Client username of the VPN.
        client_password (str | Unset): Client password of the VPN.
        vpn_configuration (VpnCertificateOpenApiVO | Unset): VPN configuration of the VPN.
        exist_pfs (bool | Unset): Whether current VPN has configured none-default option: dh14 or dh15.
        exist_phase_1_proposal_1 (bool | Unset): Whether current VPN has configured none-default Proposal option for IKE
            negotiation phase-1: SHA384 or SHA512.
        exist_phase_2_proposal_2 (bool | Unset): Whether current VPN has configured none-default Proposal option for IKE
            negotiation phase-2: SHA384 or SHA512.
    """

    name: str
    purpose: int
    client_vpn_type_1: int
    client_vpn_type_2: int
    ip_pool: IPSubnetsVO
    id: str | Unset = UNSET
    site_vpn_type: int | Unset = UNSET
    status: bool | Unset = UNSET
    account_auth: bool | Unset = UNSET
    exist_account_auth: bool | Unset = UNSET
    remote_site: str | Unset = UNSET
    remote_ip: str | Unset = UNSET
    exist_open_vpn_domain: bool | Unset = UNSET
    remote_subnet: list[IPSubnetsVO] | Unset = UNSET
    network_type: int | Unset = UNSET
    network_list: list[str] | Unset = UNSET
    custom_network: list[IPSubnetsVO] | Unset = UNSET
    exist_custom_network: bool | Unset = UNSET
    pre_shared_key: str | Unset = UNSET
    wans: list[str] | Unset = UNSET
    exist_l2tp: bool | Unset = UNSET
    exist_i_psec: bool | Unset = UNSET
    open_vpn_tunnel_mode: int | Unset = UNSET
    exist_tunnel_mode: bool | Unset = UNSET
    open_vpn_mode: int | Unset = UNSET
    service_type: int | Unset = UNSET
    service_port: int | Unset = UNSET
    encryption: int | Unset = UNSET
    ip_pool_type: int | Unset = UNSET
    exist_ip_range: bool | Unset = UNSET
    ip_pool_start: str | Unset = UNSET
    ip_pool_end: str | Unset = UNSET
    primary_dns: str | Unset = UNSET
    secondary_dns: str | Unset = UNSET
    exist_custom_dns: bool | Unset = UNSET
    auth_mode: int | Unset = UNSET
    ldap_profile: str | Unset = UNSET
    exist_ldap: bool | Unset = UNSET
    exist_server_open_vpn_google_ldap: bool | Unset = UNSET
    working_mode: int | Unset = UNSET
    client_user_name: str | Unset = UNSET
    client_password: str | Unset = UNSET
    vpn_configuration: VpnCertificateOpenApiVO | Unset = UNSET
    exist_pfs: bool | Unset = UNSET
    exist_phase_1_proposal_1: bool | Unset = UNSET
    exist_phase_2_proposal_2: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        purpose = self.purpose

        client_vpn_type_1 = self.client_vpn_type_1

        client_vpn_type_2 = self.client_vpn_type_2

        ip_pool = self.ip_pool.to_dict()

        id = self.id

        site_vpn_type = self.site_vpn_type

        status = self.status

        account_auth = self.account_auth

        exist_account_auth = self.exist_account_auth

        remote_site = self.remote_site

        remote_ip = self.remote_ip

        exist_open_vpn_domain = self.exist_open_vpn_domain

        remote_subnet: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.remote_subnet, Unset):
            remote_subnet = []
            for remote_subnet_item_data in self.remote_subnet:
                remote_subnet_item = remote_subnet_item_data.to_dict()
                remote_subnet.append(remote_subnet_item)

        network_type = self.network_type

        network_list: list[str] | Unset = UNSET
        if not isinstance(self.network_list, Unset):
            network_list = self.network_list

        custom_network: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom_network, Unset):
            custom_network = []
            for custom_network_item_data in self.custom_network:
                custom_network_item = custom_network_item_data.to_dict()
                custom_network.append(custom_network_item)

        exist_custom_network = self.exist_custom_network

        pre_shared_key = self.pre_shared_key

        wans: list[str] | Unset = UNSET
        if not isinstance(self.wans, Unset):
            wans = self.wans

        exist_l2tp = self.exist_l2tp

        exist_i_psec = self.exist_i_psec

        open_vpn_tunnel_mode = self.open_vpn_tunnel_mode

        exist_tunnel_mode = self.exist_tunnel_mode

        open_vpn_mode = self.open_vpn_mode

        service_type = self.service_type

        service_port = self.service_port

        encryption = self.encryption

        ip_pool_type = self.ip_pool_type

        exist_ip_range = self.exist_ip_range

        ip_pool_start = self.ip_pool_start

        ip_pool_end = self.ip_pool_end

        primary_dns = self.primary_dns

        secondary_dns = self.secondary_dns

        exist_custom_dns = self.exist_custom_dns

        auth_mode = self.auth_mode

        ldap_profile = self.ldap_profile

        exist_ldap = self.exist_ldap

        exist_server_open_vpn_google_ldap = self.exist_server_open_vpn_google_ldap

        working_mode = self.working_mode

        client_user_name = self.client_user_name

        client_password = self.client_password

        vpn_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vpn_configuration, Unset):
            vpn_configuration = self.vpn_configuration.to_dict()

        exist_pfs = self.exist_pfs

        exist_phase_1_proposal_1 = self.exist_phase_1_proposal_1

        exist_phase_2_proposal_2 = self.exist_phase_2_proposal_2

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "purpose": purpose,
                "clientVpnType1": client_vpn_type_1,
                "clientVpnType2": client_vpn_type_2,
                "ipPool": ip_pool,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if site_vpn_type is not UNSET:
            field_dict["siteVpnType"] = site_vpn_type
        if status is not UNSET:
            field_dict["status"] = status
        if account_auth is not UNSET:
            field_dict["accountAuth"] = account_auth
        if exist_account_auth is not UNSET:
            field_dict["existAccountAuth"] = exist_account_auth
        if remote_site is not UNSET:
            field_dict["remoteSite"] = remote_site
        if remote_ip is not UNSET:
            field_dict["remoteIp"] = remote_ip
        if exist_open_vpn_domain is not UNSET:
            field_dict["existOpenVpnDomain"] = exist_open_vpn_domain
        if remote_subnet is not UNSET:
            field_dict["remoteSubnet"] = remote_subnet
        if network_type is not UNSET:
            field_dict["networkType"] = network_type
        if network_list is not UNSET:
            field_dict["networkList"] = network_list
        if custom_network is not UNSET:
            field_dict["customNetwork"] = custom_network
        if exist_custom_network is not UNSET:
            field_dict["existCustomNetwork"] = exist_custom_network
        if pre_shared_key is not UNSET:
            field_dict["preSharedKey"] = pre_shared_key
        if wans is not UNSET:
            field_dict["wans"] = wans
        if exist_l2tp is not UNSET:
            field_dict["existL2TP"] = exist_l2tp
        if exist_i_psec is not UNSET:
            field_dict["existIPsec"] = exist_i_psec
        if open_vpn_tunnel_mode is not UNSET:
            field_dict["openVpnTunnelMode"] = open_vpn_tunnel_mode
        if exist_tunnel_mode is not UNSET:
            field_dict["existTunnelMode"] = exist_tunnel_mode
        if open_vpn_mode is not UNSET:
            field_dict["openVpnMode"] = open_vpn_mode
        if service_type is not UNSET:
            field_dict["serviceType"] = service_type
        if service_port is not UNSET:
            field_dict["servicePort"] = service_port
        if encryption is not UNSET:
            field_dict["encryption"] = encryption
        if ip_pool_type is not UNSET:
            field_dict["ipPoolType"] = ip_pool_type
        if exist_ip_range is not UNSET:
            field_dict["existIpRange"] = exist_ip_range
        if ip_pool_start is not UNSET:
            field_dict["ipPoolStart"] = ip_pool_start
        if ip_pool_end is not UNSET:
            field_dict["ipPoolEnd"] = ip_pool_end
        if primary_dns is not UNSET:
            field_dict["primaryDns"] = primary_dns
        if secondary_dns is not UNSET:
            field_dict["secondaryDns"] = secondary_dns
        if exist_custom_dns is not UNSET:
            field_dict["existCustomDns"] = exist_custom_dns
        if auth_mode is not UNSET:
            field_dict["authMode"] = auth_mode
        if ldap_profile is not UNSET:
            field_dict["ldapProfile"] = ldap_profile
        if exist_ldap is not UNSET:
            field_dict["existLdap"] = exist_ldap
        if exist_server_open_vpn_google_ldap is not UNSET:
            field_dict["existServerOpenVpnGoogleLdap"] = (
                exist_server_open_vpn_google_ldap
            )
        if working_mode is not UNSET:
            field_dict["workingMode"] = working_mode
        if client_user_name is not UNSET:
            field_dict["clientUserName"] = client_user_name
        if client_password is not UNSET:
            field_dict["clientPassword"] = client_password
        if vpn_configuration is not UNSET:
            field_dict["vpnConfiguration"] = vpn_configuration
        if exist_pfs is not UNSET:
            field_dict["existPfs"] = exist_pfs
        if exist_phase_1_proposal_1 is not UNSET:
            field_dict["existPhase1Proposal1"] = exist_phase_1_proposal_1
        if exist_phase_2_proposal_2 is not UNSET:
            field_dict["existPhase2Proposal2"] = exist_phase_2_proposal_2

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ip_subnets_vo import IPSubnetsVO
        from ..models.vpn_certificate_open_api_vo import (
            VpnCertificateOpenApiVO,
        )

        d = dict(src_dict)
        name = d.pop("name")

        purpose = d.pop("purpose")

        client_vpn_type_1 = d.pop("clientVpnType1")

        client_vpn_type_2 = d.pop("clientVpnType2")

        ip_pool = IPSubnetsVO.from_dict(d.pop("ipPool"))

        id = d.pop("id", UNSET)

        site_vpn_type = d.pop("siteVpnType", UNSET)

        status = d.pop("status", UNSET)

        account_auth = d.pop("accountAuth", UNSET)

        exist_account_auth = d.pop("existAccountAuth", UNSET)

        remote_site = d.pop("remoteSite", UNSET)

        remote_ip = d.pop("remoteIp", UNSET)

        exist_open_vpn_domain = d.pop("existOpenVpnDomain", UNSET)

        _remote_subnet = d.pop("remoteSubnet", UNSET)
        remote_subnet: list[IPSubnetsVO] | Unset = UNSET
        if _remote_subnet is not UNSET:
            remote_subnet = []
            for remote_subnet_item_data in _remote_subnet:
                remote_subnet_item = IPSubnetsVO.from_dict(remote_subnet_item_data)

                remote_subnet.append(remote_subnet_item)

        network_type = d.pop("networkType", UNSET)

        network_list = cast(list[str], d.pop("networkList", UNSET))

        _custom_network = d.pop("customNetwork", UNSET)
        custom_network: list[IPSubnetsVO] | Unset = UNSET
        if _custom_network is not UNSET:
            custom_network = []
            for custom_network_item_data in _custom_network:
                custom_network_item = IPSubnetsVO.from_dict(custom_network_item_data)

                custom_network.append(custom_network_item)

        exist_custom_network = d.pop("existCustomNetwork", UNSET)

        pre_shared_key = d.pop("preSharedKey", UNSET)

        wans = cast(list[str], d.pop("wans", UNSET))

        exist_l2tp = d.pop("existL2TP", UNSET)

        exist_i_psec = d.pop("existIPsec", UNSET)

        open_vpn_tunnel_mode = d.pop("openVpnTunnelMode", UNSET)

        exist_tunnel_mode = d.pop("existTunnelMode", UNSET)

        open_vpn_mode = d.pop("openVpnMode", UNSET)

        service_type = d.pop("serviceType", UNSET)

        service_port = d.pop("servicePort", UNSET)

        encryption = d.pop("encryption", UNSET)

        ip_pool_type = d.pop("ipPoolType", UNSET)

        exist_ip_range = d.pop("existIpRange", UNSET)

        ip_pool_start = d.pop("ipPoolStart", UNSET)

        ip_pool_end = d.pop("ipPoolEnd", UNSET)

        primary_dns = d.pop("primaryDns", UNSET)

        secondary_dns = d.pop("secondaryDns", UNSET)

        exist_custom_dns = d.pop("existCustomDns", UNSET)

        auth_mode = d.pop("authMode", UNSET)

        ldap_profile = d.pop("ldapProfile", UNSET)

        exist_ldap = d.pop("existLdap", UNSET)

        exist_server_open_vpn_google_ldap = d.pop("existServerOpenVpnGoogleLdap", UNSET)

        working_mode = d.pop("workingMode", UNSET)

        client_user_name = d.pop("clientUserName", UNSET)

        client_password = d.pop("clientPassword", UNSET)

        _vpn_configuration = d.pop("vpnConfiguration", UNSET)
        vpn_configuration: VpnCertificateOpenApiVO | Unset
        if isinstance(_vpn_configuration, Unset):
            vpn_configuration = UNSET
        else:
            vpn_configuration = VpnCertificateOpenApiVO.from_dict(_vpn_configuration)

        exist_pfs = d.pop("existPfs", UNSET)

        exist_phase_1_proposal_1 = d.pop("existPhase1Proposal1", UNSET)

        exist_phase_2_proposal_2 = d.pop("existPhase2Proposal2", UNSET)

        vpn = cls(
            name=name,
            purpose=purpose,
            client_vpn_type_1=client_vpn_type_1,
            client_vpn_type_2=client_vpn_type_2,
            ip_pool=ip_pool,
            id=id,
            site_vpn_type=site_vpn_type,
            status=status,
            account_auth=account_auth,
            exist_account_auth=exist_account_auth,
            remote_site=remote_site,
            remote_ip=remote_ip,
            exist_open_vpn_domain=exist_open_vpn_domain,
            remote_subnet=remote_subnet,
            network_type=network_type,
            network_list=network_list,
            custom_network=custom_network,
            exist_custom_network=exist_custom_network,
            pre_shared_key=pre_shared_key,
            wans=wans,
            exist_l2tp=exist_l2tp,
            exist_i_psec=exist_i_psec,
            open_vpn_tunnel_mode=open_vpn_tunnel_mode,
            exist_tunnel_mode=exist_tunnel_mode,
            open_vpn_mode=open_vpn_mode,
            service_type=service_type,
            service_port=service_port,
            encryption=encryption,
            ip_pool_type=ip_pool_type,
            exist_ip_range=exist_ip_range,
            ip_pool_start=ip_pool_start,
            ip_pool_end=ip_pool_end,
            primary_dns=primary_dns,
            secondary_dns=secondary_dns,
            exist_custom_dns=exist_custom_dns,
            auth_mode=auth_mode,
            ldap_profile=ldap_profile,
            exist_ldap=exist_ldap,
            exist_server_open_vpn_google_ldap=exist_server_open_vpn_google_ldap,
            working_mode=working_mode,
            client_user_name=client_user_name,
            client_password=client_password,
            vpn_configuration=vpn_configuration,
            exist_pfs=exist_pfs,
            exist_phase_1_proposal_1=exist_phase_1_proposal_1,
            exist_phase_2_proposal_2=exist_phase_2_proposal_2,
        )

        vpn.additional_properties = d
        return vpn

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
