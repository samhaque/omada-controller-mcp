from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ip_subnets_vo import IPSubnetsVO


T = TypeVar("T", bound="VpnUserRequest")


@_attrs_define
class VpnUserRequest:
    """
    Attributes:
        username (str): Username of the VPN user.
        password (str): Password of the VPN user.
        servers (list[str]): Servers of the VPN user. Server can be created using 'Create client-to-site VPN server'
            interface, and server ID can be obtained from 'Get client-to-site VPN server list' interface.
        protocol (int | Unset): Protocol should be a value as follows: 0: L2TP or PPTP; 1: openVPN.
        client_mode (int | Unset): Client mode should be a value as follows: 0: Client-To-Site, 1: Site-To-Site.
        max_connections (int | Unset): Max connections should be within the range of 1–100.
        user_remote_subnets (list[IPSubnetsVO] | Unset): User remote subnets of the VPN user.
        local_ip (str | Unset): Local IP of the VPN user.
    """

    username: str
    password: str
    servers: list[str]
    protocol: int | Unset = UNSET
    client_mode: int | Unset = UNSET
    max_connections: int | Unset = UNSET
    user_remote_subnets: list[IPSubnetsVO] | Unset = UNSET
    local_ip: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        password = self.password

        servers = self.servers

        protocol = self.protocol

        client_mode = self.client_mode

        max_connections = self.max_connections

        user_remote_subnets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.user_remote_subnets, Unset):
            user_remote_subnets = []
            for user_remote_subnets_item_data in self.user_remote_subnets:
                user_remote_subnets_item = user_remote_subnets_item_data.to_dict()
                user_remote_subnets.append(user_remote_subnets_item)

        local_ip = self.local_ip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
                "password": password,
                "servers": servers,
            }
        )
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if client_mode is not UNSET:
            field_dict["clientMode"] = client_mode
        if max_connections is not UNSET:
            field_dict["maxConnections"] = max_connections
        if user_remote_subnets is not UNSET:
            field_dict["userRemoteSubnets"] = user_remote_subnets
        if local_ip is not UNSET:
            field_dict["localIp"] = local_ip

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ip_subnets_vo import IPSubnetsVO

        d = dict(src_dict)
        username = d.pop("username")

        password = d.pop("password")

        servers = cast(list[str], d.pop("servers"))

        protocol = d.pop("protocol", UNSET)

        client_mode = d.pop("clientMode", UNSET)

        max_connections = d.pop("maxConnections", UNSET)

        _user_remote_subnets = d.pop("userRemoteSubnets", UNSET)
        user_remote_subnets: list[IPSubnetsVO] | Unset = UNSET
        if _user_remote_subnets is not UNSET:
            user_remote_subnets = []
            for user_remote_subnets_item_data in _user_remote_subnets:
                user_remote_subnets_item = IPSubnetsVO.from_dict(
                    user_remote_subnets_item_data
                )

                user_remote_subnets.append(user_remote_subnets_item)

        local_ip = d.pop("localIp", UNSET)

        vpn_user_request = cls(
            username=username,
            password=password,
            servers=servers,
            protocol=protocol,
            client_mode=client_mode,
            max_connections=max_connections,
            user_remote_subnets=user_remote_subnets,
            local_ip=local_ip,
        )

        vpn_user_request.additional_properties = d
        return vpn_user_request

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
