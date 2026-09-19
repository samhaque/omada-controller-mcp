from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ip_subnets_vo import IPSubnetsVO


T = TypeVar("T", bound="VpnUser")


@_attrs_define
class VpnUser:
    """
    Attributes:
        id (str | Unset): ID of the VPN user.
        username (str | Unset): Username of the VPN user.
        password (str | Unset): Password of the VPN user.
        protocol (int | Unset): Protocol should be a value as follows: 0: L2TP or PPTP; 1: openVPN.
        client_mode (int | Unset): Client mode should be a value as follows: 0: Client-To-Site, 1: Site-To-Site.
        max_connections (int | Unset): Max connections should be within the range of 1–100.
        user_remote_subnets (list[IPSubnetsVO] | Unset): User remote subnets of the VPN user.
        servers (list[str] | Unset): Servers of the VPN user. Server can be created using 'Create client-to-site VPN
            server' interface, and server ID can be obtained from 'Get client-to-site VPN server list' interface.
        local_ip (str | Unset): Local IP of the VPN user.
        server_names (str | Unset): Server names of the VPN user.
    """

    id: str | Unset = UNSET
    username: str | Unset = UNSET
    password: str | Unset = UNSET
    protocol: int | Unset = UNSET
    client_mode: int | Unset = UNSET
    max_connections: int | Unset = UNSET
    user_remote_subnets: list[IPSubnetsVO] | Unset = UNSET
    servers: list[str] | Unset = UNSET
    local_ip: str | Unset = UNSET
    server_names: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        username = self.username

        password = self.password

        protocol = self.protocol

        client_mode = self.client_mode

        max_connections = self.max_connections

        user_remote_subnets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.user_remote_subnets, Unset):
            user_remote_subnets = []
            for user_remote_subnets_item_data in self.user_remote_subnets:
                user_remote_subnets_item = user_remote_subnets_item_data.to_dict()
                user_remote_subnets.append(user_remote_subnets_item)

        servers: list[str] | Unset = UNSET
        if not isinstance(self.servers, Unset):
            servers = self.servers

        local_ip = self.local_ip

        server_names = self.server_names

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if client_mode is not UNSET:
            field_dict["clientMode"] = client_mode
        if max_connections is not UNSET:
            field_dict["maxConnections"] = max_connections
        if user_remote_subnets is not UNSET:
            field_dict["userRemoteSubnets"] = user_remote_subnets
        if servers is not UNSET:
            field_dict["servers"] = servers
        if local_ip is not UNSET:
            field_dict["localIp"] = local_ip
        if server_names is not UNSET:
            field_dict["serverNames"] = server_names

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ip_subnets_vo import IPSubnetsVO

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

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

        servers = cast(list[str], d.pop("servers", UNSET))

        local_ip = d.pop("localIp", UNSET)

        server_names = d.pop("serverNames", UNSET)

        vpn_user = cls(
            id=id,
            username=username,
            password=password,
            protocol=protocol,
            client_mode=client_mode,
            max_connections=max_connections,
            user_remote_subnets=user_remote_subnets,
            servers=servers,
            local_ip=local_ip,
            server_names=server_names,
        )

        vpn_user.additional_properties = d
        return vpn_user

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
