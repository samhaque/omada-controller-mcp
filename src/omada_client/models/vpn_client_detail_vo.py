from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feature_info_vo import FeatureInfoVO
    from ..models.vpn_certificate_open_api_vo import VpnCertificateOpenApiVO
    from ..models.vpn_ip_subnets_open_api_vo import VpnIPSubnetsOpenApiVO


T = TypeVar("T", bound="VpnClientDetailVO")


@_attrs_define
class VpnClientDetailVO:
    """
    Attributes:
        id (str | Unset): ID of the VPN.
        name (str | Unset): VPN name.
        status (bool | Unset): Status of the VPN.
        vpn_type (int | Unset): Client Vpn type. 0: L2TP; 1: PPTP; 3: OpenVPN; 4: WireGuard.
        wans (list[str] | Unset): WAN port ID.
        setup (int | Unset): Wire Guard setup should be a value as follows: 0: file; 1: manual.
        mtu (int | Unset): The MTU of WireGuard VPN should be within the range of 576-1440.
        keep_alive (int | Unset): The keepalive second of WireGuard peer should be within the range of 0-65535.
        private_key (str | Unset): The private key of WireGuard VPN must have 44 character of base64 and end with '='.
        public_key (str | Unset): The public key of WireGuard VPN must have 44 character of base64 and end with '='.
        server_public_key (str | Unset): The public key of WireGuard VPN must have 44 character of base64 and end with
            '='.
        tunnel_ip (str | Unset): The local IP address of WireGuard VPN.
        remote_ip (str | Unset): Remote IP of the VPN.
        remote_subnet (list[str] | Unset): Remote subnet of the VPN.
        service_port (int | Unset): Service port for VPN server.
        client_port (int | Unset): Client port for VPN client.
        dns1 (str | Unset): Primary DNS of the VPN.
        dns2 (str | Unset): Secondary DNS of the VPN.
        network_type (int | Unset): Network type. 0: network list; 1: custom networks.
        network_list (list[str] | Unset): Network list of the VPN.
        custom_network (list[VpnIPSubnetsOpenApiVO] | Unset): Custom networks of the VPN.
        open_vpn_mode (int | Unset): OpenVPN mode should be a value as follows: 0: certification; 1:
            certification+account.
        pre_shared_key (str | Unset): Pre-shared key of the VPN.
        encryption (int | Unset): Encryption should be a value as follows: 0: Encrypted; 1: Unencrypted.
        working_mode (int | Unset): Working mode should be a value as follows: 0: NAT; 1: Routing.
        client_username (str | Unset): Client username should contain 1 to 64 characters.
        client_password (str | Unset): Client password should contain 1 to 64 characters.
        vpn_configuration (VpnCertificateOpenApiVO | Unset): VPN configuration of the VPN.
        allowed_server_address (list[str] | Unset): Wire Guard allowed server address.
        feature_description (list[FeatureInfoVO] | Unset): Gateway Feature Description
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    status: bool | Unset = UNSET
    vpn_type: int | Unset = UNSET
    wans: list[str] | Unset = UNSET
    setup: int | Unset = UNSET
    mtu: int | Unset = UNSET
    keep_alive: int | Unset = UNSET
    private_key: str | Unset = UNSET
    public_key: str | Unset = UNSET
    server_public_key: str | Unset = UNSET
    tunnel_ip: str | Unset = UNSET
    remote_ip: str | Unset = UNSET
    remote_subnet: list[str] | Unset = UNSET
    service_port: int | Unset = UNSET
    client_port: int | Unset = UNSET
    dns1: str | Unset = UNSET
    dns2: str | Unset = UNSET
    network_type: int | Unset = UNSET
    network_list: list[str] | Unset = UNSET
    custom_network: list[VpnIPSubnetsOpenApiVO] | Unset = UNSET
    open_vpn_mode: int | Unset = UNSET
    pre_shared_key: str | Unset = UNSET
    encryption: int | Unset = UNSET
    working_mode: int | Unset = UNSET
    client_username: str | Unset = UNSET
    client_password: str | Unset = UNSET
    vpn_configuration: VpnCertificateOpenApiVO | Unset = UNSET
    allowed_server_address: list[str] | Unset = UNSET
    feature_description: list[FeatureInfoVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        status = self.status

        vpn_type = self.vpn_type

        wans: list[str] | Unset = UNSET
        if not isinstance(self.wans, Unset):
            wans = self.wans

        setup = self.setup

        mtu = self.mtu

        keep_alive = self.keep_alive

        private_key = self.private_key

        public_key = self.public_key

        server_public_key = self.server_public_key

        tunnel_ip = self.tunnel_ip

        remote_ip = self.remote_ip

        remote_subnet: list[str] | Unset = UNSET
        if not isinstance(self.remote_subnet, Unset):
            remote_subnet = self.remote_subnet

        service_port = self.service_port

        client_port = self.client_port

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

        open_vpn_mode = self.open_vpn_mode

        pre_shared_key = self.pre_shared_key

        encryption = self.encryption

        working_mode = self.working_mode

        client_username = self.client_username

        client_password = self.client_password

        vpn_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vpn_configuration, Unset):
            vpn_configuration = self.vpn_configuration.to_dict()

        allowed_server_address: list[str] | Unset = UNSET
        if not isinstance(self.allowed_server_address, Unset):
            allowed_server_address = self.allowed_server_address

        feature_description: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.feature_description, Unset):
            feature_description = []
            for feature_description_item_data in self.feature_description:
                feature_description_item = feature_description_item_data.to_dict()
                feature_description.append(feature_description_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if vpn_type is not UNSET:
            field_dict["vpnType"] = vpn_type
        if wans is not UNSET:
            field_dict["wans"] = wans
        if setup is not UNSET:
            field_dict["setup"] = setup
        if mtu is not UNSET:
            field_dict["mtu"] = mtu
        if keep_alive is not UNSET:
            field_dict["keepAlive"] = keep_alive
        if private_key is not UNSET:
            field_dict["privateKey"] = private_key
        if public_key is not UNSET:
            field_dict["publicKey"] = public_key
        if server_public_key is not UNSET:
            field_dict["serverPublicKey"] = server_public_key
        if tunnel_ip is not UNSET:
            field_dict["tunnelIp"] = tunnel_ip
        if remote_ip is not UNSET:
            field_dict["remoteIp"] = remote_ip
        if remote_subnet is not UNSET:
            field_dict["remoteSubnet"] = remote_subnet
        if service_port is not UNSET:
            field_dict["servicePort"] = service_port
        if client_port is not UNSET:
            field_dict["clientPort"] = client_port
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
        if open_vpn_mode is not UNSET:
            field_dict["openVpnMode"] = open_vpn_mode
        if pre_shared_key is not UNSET:
            field_dict["preSharedKey"] = pre_shared_key
        if encryption is not UNSET:
            field_dict["encryption"] = encryption
        if working_mode is not UNSET:
            field_dict["workingMode"] = working_mode
        if client_username is not UNSET:
            field_dict["clientUsername"] = client_username
        if client_password is not UNSET:
            field_dict["clientPassword"] = client_password
        if vpn_configuration is not UNSET:
            field_dict["vpnConfiguration"] = vpn_configuration
        if allowed_server_address is not UNSET:
            field_dict["allowedServerAddress"] = allowed_server_address
        if feature_description is not UNSET:
            field_dict["featureDescription"] = feature_description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.feature_info_vo import FeatureInfoVO
        from ..models.vpn_certificate_open_api_vo import (
            VpnCertificateOpenApiVO,
        )
        from ..models.vpn_ip_subnets_open_api_vo import (
            VpnIPSubnetsOpenApiVO,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        status = d.pop("status", UNSET)

        vpn_type = d.pop("vpnType", UNSET)

        wans = cast(list[str], d.pop("wans", UNSET))

        setup = d.pop("setup", UNSET)

        mtu = d.pop("mtu", UNSET)

        keep_alive = d.pop("keepAlive", UNSET)

        private_key = d.pop("privateKey", UNSET)

        public_key = d.pop("publicKey", UNSET)

        server_public_key = d.pop("serverPublicKey", UNSET)

        tunnel_ip = d.pop("tunnelIp", UNSET)

        remote_ip = d.pop("remoteIp", UNSET)

        remote_subnet = cast(list[str], d.pop("remoteSubnet", UNSET))

        service_port = d.pop("servicePort", UNSET)

        client_port = d.pop("clientPort", UNSET)

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

        open_vpn_mode = d.pop("openVpnMode", UNSET)

        pre_shared_key = d.pop("preSharedKey", UNSET)

        encryption = d.pop("encryption", UNSET)

        working_mode = d.pop("workingMode", UNSET)

        client_username = d.pop("clientUsername", UNSET)

        client_password = d.pop("clientPassword", UNSET)

        _vpn_configuration = d.pop("vpnConfiguration", UNSET)
        vpn_configuration: VpnCertificateOpenApiVO | Unset
        if isinstance(_vpn_configuration, Unset):
            vpn_configuration = UNSET
        else:
            vpn_configuration = VpnCertificateOpenApiVO.from_dict(_vpn_configuration)

        allowed_server_address = cast(list[str], d.pop("allowedServerAddress", UNSET))

        _feature_description = d.pop("featureDescription", UNSET)
        feature_description: list[FeatureInfoVO] | Unset = UNSET
        if _feature_description is not UNSET:
            feature_description = []
            for feature_description_item_data in _feature_description:
                feature_description_item = FeatureInfoVO.from_dict(
                    feature_description_item_data
                )

                feature_description.append(feature_description_item)

        vpn_client_detail_vo = cls(
            id=id,
            name=name,
            status=status,
            vpn_type=vpn_type,
            wans=wans,
            setup=setup,
            mtu=mtu,
            keep_alive=keep_alive,
            private_key=private_key,
            public_key=public_key,
            server_public_key=server_public_key,
            tunnel_ip=tunnel_ip,
            remote_ip=remote_ip,
            remote_subnet=remote_subnet,
            service_port=service_port,
            client_port=client_port,
            dns1=dns1,
            dns2=dns2,
            network_type=network_type,
            network_list=network_list,
            custom_network=custom_network,
            open_vpn_mode=open_vpn_mode,
            pre_shared_key=pre_shared_key,
            encryption=encryption,
            working_mode=working_mode,
            client_username=client_username,
            client_password=client_password,
            vpn_configuration=vpn_configuration,
            allowed_server_address=allowed_server_address,
            feature_description=feature_description,
        )

        vpn_client_detail_vo.additional_properties = d
        return vpn_client_detail_vo

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
