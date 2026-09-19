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


T = TypeVar("T", bound="ClientToSiteVpnClient")


@_attrs_define
class ClientToSiteVpnClient:
    """
    Attributes:
        name (str): Name should contain 1 to 63 characters.
        wan (list[str]): WAN list of the VPN. WAN port ID can be obtained from 'Get internet basic info' interface.
        client_vpn_type (int): Client Vpn type should be a value as follows: 0: L2TP; 1: PPTP; 2: IPSec; 3: OpenVPN.
        id (str | Unset): ID of the VPN.
        status (bool | Unset): Status of the VPN.
        mode (int | Unset): Mode(only for server OpenVPN) should be a value as follows: 0: certification; 1:
            certification+account.
        remote_site (str | Unset): Remote site of the VPN.
        remote_ip (str | Unset): Remote IP of the VPN. Get whether supports domain from interface 'Get client-to-site
            VPN client list'.
        remote_subnet (list[IPSubnetsVO] | Unset): Remote subnet of the VPN.
        network_type (int | Unset): Network type should be a value as follows: 0: network list; 1: custom networks.
        network_list (list[str] | Unset): Network list of the VPN. Network can be created using 'Create LAN network'
            interface, and network ID can be obtained from 'Get LAN network list' interface.
        custom_network (list[IPSubnetsVO] | Unset): Custom networks of the VPN.
        pre_shared_key (str | Unset): Pre-shared key of the VPN.
        open_vpn_tunnel_mode (int | Unset): OpenVPN tunnel mode should be a value as follows: 0: split; 1: full.
        open_vpn_mode (int | Unset): OpenVPN mode should be a value as follows: 0: certification; 1:
            certification+account.
        service_type (int | Unset): Service type should be a value as follows: 0: UDP; 1: TCP.
        service_port (int | Unset): Service port should be within the range of 1–65535.
        encryption (int | Unset): Encryption should be a value as follows: 0: Encrypted; 1: Unencrypted.
        working_mode (int | Unset): Working mode should be a value as follows: 0: NAT; 1: Routing.
        client_user_name (str | Unset): Client username should contain 1 to 64 characters.
        client_password (str | Unset): Client password should contain 1 to 64 characters.
        vpn_configuration (VpnCertificateOpenApiVO | Unset): VPN configuration of the VPN.
    """

    name: str
    wan: list[str]
    client_vpn_type: int
    id: str | Unset = UNSET
    status: bool | Unset = UNSET
    mode: int | Unset = UNSET
    remote_site: str | Unset = UNSET
    remote_ip: str | Unset = UNSET
    remote_subnet: list[IPSubnetsVO] | Unset = UNSET
    network_type: int | Unset = UNSET
    network_list: list[str] | Unset = UNSET
    custom_network: list[IPSubnetsVO] | Unset = UNSET
    pre_shared_key: str | Unset = UNSET
    open_vpn_tunnel_mode: int | Unset = UNSET
    open_vpn_mode: int | Unset = UNSET
    service_type: int | Unset = UNSET
    service_port: int | Unset = UNSET
    encryption: int | Unset = UNSET
    working_mode: int | Unset = UNSET
    client_user_name: str | Unset = UNSET
    client_password: str | Unset = UNSET
    vpn_configuration: VpnCertificateOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        wan = self.wan

        client_vpn_type = self.client_vpn_type

        id = self.id

        status = self.status

        mode = self.mode

        remote_site = self.remote_site

        remote_ip = self.remote_ip

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

        pre_shared_key = self.pre_shared_key

        open_vpn_tunnel_mode = self.open_vpn_tunnel_mode

        open_vpn_mode = self.open_vpn_mode

        service_type = self.service_type

        service_port = self.service_port

        encryption = self.encryption

        working_mode = self.working_mode

        client_user_name = self.client_user_name

        client_password = self.client_password

        vpn_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vpn_configuration, Unset):
            vpn_configuration = self.vpn_configuration.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "wan": wan,
                "clientVpnType": client_vpn_type,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if mode is not UNSET:
            field_dict["mode"] = mode
        if remote_site is not UNSET:
            field_dict["remoteSite"] = remote_site
        if remote_ip is not UNSET:
            field_dict["remoteIp"] = remote_ip
        if remote_subnet is not UNSET:
            field_dict["remoteSubnet"] = remote_subnet
        if network_type is not UNSET:
            field_dict["networkType"] = network_type
        if network_list is not UNSET:
            field_dict["networkList"] = network_list
        if custom_network is not UNSET:
            field_dict["customNetwork"] = custom_network
        if pre_shared_key is not UNSET:
            field_dict["preSharedKey"] = pre_shared_key
        if open_vpn_tunnel_mode is not UNSET:
            field_dict["openVpnTunnelMode"] = open_vpn_tunnel_mode
        if open_vpn_mode is not UNSET:
            field_dict["openVpnMode"] = open_vpn_mode
        if service_type is not UNSET:
            field_dict["serviceType"] = service_type
        if service_port is not UNSET:
            field_dict["servicePort"] = service_port
        if encryption is not UNSET:
            field_dict["encryption"] = encryption
        if working_mode is not UNSET:
            field_dict["workingMode"] = working_mode
        if client_user_name is not UNSET:
            field_dict["clientUserName"] = client_user_name
        if client_password is not UNSET:
            field_dict["clientPassword"] = client_password
        if vpn_configuration is not UNSET:
            field_dict["vpnConfiguration"] = vpn_configuration

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ip_subnets_vo import IPSubnetsVO
        from ..models.vpn_certificate_open_api_vo import (
            VpnCertificateOpenApiVO,
        )

        d = dict(src_dict)
        name = d.pop("name")

        wan = cast(list[str], d.pop("wan"))

        client_vpn_type = d.pop("clientVpnType")

        id = d.pop("id", UNSET)

        status = d.pop("status", UNSET)

        mode = d.pop("mode", UNSET)

        remote_site = d.pop("remoteSite", UNSET)

        remote_ip = d.pop("remoteIp", UNSET)

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

        pre_shared_key = d.pop("preSharedKey", UNSET)

        open_vpn_tunnel_mode = d.pop("openVpnTunnelMode", UNSET)

        open_vpn_mode = d.pop("openVpnMode", UNSET)

        service_type = d.pop("serviceType", UNSET)

        service_port = d.pop("servicePort", UNSET)

        encryption = d.pop("encryption", UNSET)

        working_mode = d.pop("workingMode", UNSET)

        client_user_name = d.pop("clientUserName", UNSET)

        client_password = d.pop("clientPassword", UNSET)

        _vpn_configuration = d.pop("vpnConfiguration", UNSET)
        vpn_configuration: VpnCertificateOpenApiVO | Unset
        if isinstance(_vpn_configuration, Unset):
            vpn_configuration = UNSET
        else:
            vpn_configuration = VpnCertificateOpenApiVO.from_dict(_vpn_configuration)

        client_to_site_vpn_client = cls(
            name=name,
            wan=wan,
            client_vpn_type=client_vpn_type,
            id=id,
            status=status,
            mode=mode,
            remote_site=remote_site,
            remote_ip=remote_ip,
            remote_subnet=remote_subnet,
            network_type=network_type,
            network_list=network_list,
            custom_network=custom_network,
            pre_shared_key=pre_shared_key,
            open_vpn_tunnel_mode=open_vpn_tunnel_mode,
            open_vpn_mode=open_vpn_mode,
            service_type=service_type,
            service_port=service_port,
            encryption=encryption,
            working_mode=working_mode,
            client_user_name=client_user_name,
            client_password=client_password,
            vpn_configuration=vpn_configuration,
        )

        client_to_site_vpn_client.additional_properties = d
        return client_to_site_vpn_client

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
