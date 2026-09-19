from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vpn_certificate_open_api_vo import VpnCertificateOpenApiVO
    from ..models.vpn_ip_subnets_open_api_vo import VpnIPSubnetsOpenApiVO


T = TypeVar("T", bound="VpnClientConfigOpenApiVO")


@_attrs_define
class VpnClientConfigOpenApiVO:
    """
    Attributes:
        name (str): Name should contain 1 to 63 characters.
        status (bool): Status of the VPN.
        vpn_type (int): Vpn type should be a value as follows: 0: L2TP; 1: PPTP; 3: OpenVPN; 4: WireGuard.
        wans (list[str]): WAN list of the VPN. WAN port ID can be obtained from 'Get internet basic info' interface.
        setup (int): Wire Guard setup should be a value as follows: 0: file; 1: manual.
        service_port (int): Service port should be within the range of 1–65535.
        server_public_key (str): The public key of WireGuard VPN must have 44 character of base64 and end with '='.
        remote_ip (str): Remote IP of the VPN
        vpn_configuration (VpnCertificateOpenApiVO): VPN configuration of the VPN.
        tunnel_ip (str | Unset): The local IP address of WireGuard VPN.
        mtu (int | Unset): The MTU of WireGuard VPN should be within the range of 576-1440.
        keep_alive (int | Unset): The keepalive second of WireGuard peer should be within the range of 0-65535.
        client_port (int | Unset): Client port should be within the range of 1–65535.
        private_key (str | Unset): The private key of WireGuard VPN must have 44 character of base64 and end with '='.
        dns1 (str | Unset): Primary DNS of the VPN.
        dns2 (str | Unset): Secondary DNS of the VPN.
        network_type (int | Unset): Network type should be a value as follows: 0: network list; 1: custom networks.
        network_list (list[str] | Unset): Network list of the VPN. Network can be created using 'Create LAN network'
            interface, and network ID can be obtained from 'Get LAN network list' interface.
        custom_network (list[VpnIPSubnetsOpenApiVO] | Unset): Custom networks of the VPN.
        remote_subnet (list[str] | Unset): Remote subnet of the VPN.
        encryption (int | Unset): Encryption should be a value as follows: 0: Encrypted; 1: Unencrypted; 2: Auto.
        pre_shared_key (str | Unset): Pre-shared key of the VPN.
        working_mode (int | Unset): Working Mode should be a value as follow: 0:NAT 1:Routing.
        open_vpn_mode (int | Unset): OpenVPN mode should be a value as follows: 0: certification; 1:
            certification+account.
        client_username (str | Unset): Client username of the VPN.
        client_password (str | Unset): Client password of the VPN.
        allowed_server_address (list[str] | Unset): Wire Guard allowed server address.
    """

    name: str
    status: bool
    vpn_type: int
    wans: list[str]
    setup: int
    service_port: int
    server_public_key: str
    remote_ip: str
    vpn_configuration: VpnCertificateOpenApiVO
    tunnel_ip: str | Unset = UNSET
    mtu: int | Unset = UNSET
    keep_alive: int | Unset = UNSET
    client_port: int | Unset = UNSET
    private_key: str | Unset = UNSET
    dns1: str | Unset = UNSET
    dns2: str | Unset = UNSET
    network_type: int | Unset = UNSET
    network_list: list[str] | Unset = UNSET
    custom_network: list[VpnIPSubnetsOpenApiVO] | Unset = UNSET
    remote_subnet: list[str] | Unset = UNSET
    encryption: int | Unset = UNSET
    pre_shared_key: str | Unset = UNSET
    working_mode: int | Unset = UNSET
    open_vpn_mode: int | Unset = UNSET
    client_username: str | Unset = UNSET
    client_password: str | Unset = UNSET
    allowed_server_address: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status = self.status

        vpn_type = self.vpn_type

        wans = self.wans

        setup = self.setup

        service_port = self.service_port

        server_public_key = self.server_public_key

        remote_ip = self.remote_ip

        vpn_configuration = self.vpn_configuration.to_dict()

        tunnel_ip = self.tunnel_ip

        mtu = self.mtu

        keep_alive = self.keep_alive

        client_port = self.client_port

        private_key = self.private_key

        dns1 = self.dns1

        dns2 = self.dns2

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

        remote_subnet: list[str] | Unset = UNSET
        if not isinstance(self.remote_subnet, Unset):
            remote_subnet = self.remote_subnet

        encryption = self.encryption

        pre_shared_key = self.pre_shared_key

        working_mode = self.working_mode

        open_vpn_mode = self.open_vpn_mode

        client_username = self.client_username

        client_password = self.client_password

        allowed_server_address: list[str] | Unset = UNSET
        if not isinstance(self.allowed_server_address, Unset):
            allowed_server_address = self.allowed_server_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "status": status,
                "vpnType": vpn_type,
                "wans": wans,
                "setup": setup,
                "servicePort": service_port,
                "serverPublicKey": server_public_key,
                "remoteIp": remote_ip,
                "vpnConfiguration": vpn_configuration,
            }
        )
        if tunnel_ip is not UNSET:
            field_dict["tunnelIp"] = tunnel_ip
        if mtu is not UNSET:
            field_dict["mtu"] = mtu
        if keep_alive is not UNSET:
            field_dict["keepAlive"] = keep_alive
        if client_port is not UNSET:
            field_dict["clientPort"] = client_port
        if private_key is not UNSET:
            field_dict["privateKey"] = private_key
        if dns1 is not UNSET:
            field_dict["dns1"] = dns1
        if dns2 is not UNSET:
            field_dict["dns2"] = dns2
        if network_type is not UNSET:
            field_dict["networkType"] = network_type
        if network_list is not UNSET:
            field_dict["networkList"] = network_list
        if custom_network is not UNSET:
            field_dict["customNetwork"] = custom_network
        if remote_subnet is not UNSET:
            field_dict["remoteSubnet"] = remote_subnet
        if encryption is not UNSET:
            field_dict["encryption"] = encryption
        if pre_shared_key is not UNSET:
            field_dict["preSharedKey"] = pre_shared_key
        if working_mode is not UNSET:
            field_dict["workingMode"] = working_mode
        if open_vpn_mode is not UNSET:
            field_dict["openVpnMode"] = open_vpn_mode
        if client_username is not UNSET:
            field_dict["clientUsername"] = client_username
        if client_password is not UNSET:
            field_dict["clientPassword"] = client_password
        if allowed_server_address is not UNSET:
            field_dict["allowedServerAddress"] = allowed_server_address

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.vpn_certificate_open_api_vo import (
            VpnCertificateOpenApiVO,
        )
        from ..models.vpn_ip_subnets_open_api_vo import (
            VpnIPSubnetsOpenApiVO,
        )

        d = dict(src_dict)
        name = d.pop("name")

        status = d.pop("status")

        vpn_type = d.pop("vpnType")

        wans = cast(list[str], d.pop("wans"))

        setup = d.pop("setup")

        service_port = d.pop("servicePort")

        server_public_key = d.pop("serverPublicKey")

        remote_ip = d.pop("remoteIp")

        vpn_configuration = VpnCertificateOpenApiVO.from_dict(d.pop("vpnConfiguration"))

        tunnel_ip = d.pop("tunnelIp", UNSET)

        mtu = d.pop("mtu", UNSET)

        keep_alive = d.pop("keepAlive", UNSET)

        client_port = d.pop("clientPort", UNSET)

        private_key = d.pop("privateKey", UNSET)

        dns1 = d.pop("dns1", UNSET)

        dns2 = d.pop("dns2", UNSET)

        network_type = d.pop("networkType", UNSET)

        network_list = cast(list[str], d.pop("networkList", UNSET))

        _custom_network = d.pop("customNetwork", UNSET)
        custom_network: list[VpnIPSubnetsOpenApiVO] | Unset = UNSET
        if _custom_network is not UNSET:
            custom_network = []
            for custom_network_item_data in _custom_network:
                custom_network_item = VpnIPSubnetsOpenApiVO.from_dict(
                    custom_network_item_data
                )

                custom_network.append(custom_network_item)

        remote_subnet = cast(list[str], d.pop("remoteSubnet", UNSET))

        encryption = d.pop("encryption", UNSET)

        pre_shared_key = d.pop("preSharedKey", UNSET)

        working_mode = d.pop("workingMode", UNSET)

        open_vpn_mode = d.pop("openVpnMode", UNSET)

        client_username = d.pop("clientUsername", UNSET)

        client_password = d.pop("clientPassword", UNSET)

        allowed_server_address = cast(list[str], d.pop("allowedServerAddress", UNSET))

        vpn_client_config_open_api_vo = cls(
            name=name,
            status=status,
            vpn_type=vpn_type,
            wans=wans,
            setup=setup,
            service_port=service_port,
            server_public_key=server_public_key,
            remote_ip=remote_ip,
            vpn_configuration=vpn_configuration,
            tunnel_ip=tunnel_ip,
            mtu=mtu,
            keep_alive=keep_alive,
            client_port=client_port,
            private_key=private_key,
            dns1=dns1,
            dns2=dns2,
            network_type=network_type,
            network_list=network_list,
            custom_network=custom_network,
            remote_subnet=remote_subnet,
            encryption=encryption,
            pre_shared_key=pre_shared_key,
            working_mode=working_mode,
            open_vpn_mode=open_vpn_mode,
            client_username=client_username,
            client_password=client_password,
            allowed_server_address=allowed_server_address,
        )

        vpn_client_config_open_api_vo.additional_properties = d
        return vpn_client_config_open_api_vo

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
