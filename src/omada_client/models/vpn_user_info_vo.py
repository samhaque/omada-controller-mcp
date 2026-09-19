from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feature_info_vo import FeatureInfoVO
    from ..models.ip_subnets_vo import IPSubnetsVO


T = TypeVar("T", bound="VpnUserInfoVO")


@_attrs_define
class VpnUserInfoVO:
    """
    Attributes:
        id (str | Unset): ID of the VPN user.
        username (str | Unset): Username of the VPN user.
        password (str | Unset): Password of the VPN user.
        protocol (int | Unset): Protocol should be a value as follows: 0: L2TP or PPTP; 1: openVPN; 2: SSL VPN.
        servers (list[str] | Unset): Servers of the VPN user. Server can be created using 'Create client-to-site VPN
            server' interface, and server ID can be obtained from 'Get client-to-site VPN server list' interface.
        client_mode (int | Unset): Client mode should be a value as follows: 0: Client-To-Site, 1: Site-To-Site.
        max_connections (int | Unset): Max connections should be within the range of 1–100.
        user_remote_subnets (list[IPSubnetsVO] | Unset): User remote subnets of the VPN user.
        server_names (str | Unset): Server names of the VPN user.
        local_ip (str | Unset): Local IP of the VPN user.
        group_id (str | Unset): Group ID of the SSL VPN user. User group can be created using 'Create SSL VPN user
            group' interface, and User Group ID can be obtained from 'Get user group list for SSL VPN server' interface.
        group_name (str | Unset):
        status (bool | Unset): Status of the SSL VPN user.
        validity (str | Unset): Validity of the SSL VPN user. The format is Month/Day/Year, for example 08/20/2022.
        available (bool | Unset):
        feature_description (list[FeatureInfoVO] | Unset): Gateway Feature Description.
    """

    id: str | Unset = UNSET
    username: str | Unset = UNSET
    password: str | Unset = UNSET
    protocol: int | Unset = UNSET
    servers: list[str] | Unset = UNSET
    client_mode: int | Unset = UNSET
    max_connections: int | Unset = UNSET
    user_remote_subnets: list[IPSubnetsVO] | Unset = UNSET
    server_names: str | Unset = UNSET
    local_ip: str | Unset = UNSET
    group_id: str | Unset = UNSET
    group_name: str | Unset = UNSET
    status: bool | Unset = UNSET
    validity: str | Unset = UNSET
    available: bool | Unset = UNSET
    feature_description: list[FeatureInfoVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        username = self.username

        password = self.password

        protocol = self.protocol

        servers: list[str] | Unset = UNSET
        if not isinstance(self.servers, Unset):
            servers = self.servers

        client_mode = self.client_mode

        max_connections = self.max_connections

        user_remote_subnets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.user_remote_subnets, Unset):
            user_remote_subnets = []
            for user_remote_subnets_item_data in self.user_remote_subnets:
                user_remote_subnets_item = user_remote_subnets_item_data.to_dict()
                user_remote_subnets.append(user_remote_subnets_item)

        server_names = self.server_names

        local_ip = self.local_ip

        group_id = self.group_id

        group_name = self.group_name

        status = self.status

        validity = self.validity

        available = self.available

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
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if servers is not UNSET:
            field_dict["servers"] = servers
        if client_mode is not UNSET:
            field_dict["clientMode"] = client_mode
        if max_connections is not UNSET:
            field_dict["maxConnections"] = max_connections
        if user_remote_subnets is not UNSET:
            field_dict["userRemoteSubnets"] = user_remote_subnets
        if server_names is not UNSET:
            field_dict["serverNames"] = server_names
        if local_ip is not UNSET:
            field_dict["localIp"] = local_ip
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if group_name is not UNSET:
            field_dict["groupName"] = group_name
        if status is not UNSET:
            field_dict["status"] = status
        if validity is not UNSET:
            field_dict["validity"] = validity
        if available is not UNSET:
            field_dict["available"] = available
        if feature_description is not UNSET:
            field_dict["featureDescription"] = feature_description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.feature_info_vo import FeatureInfoVO
        from ..models.ip_subnets_vo import IPSubnetsVO

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        protocol = d.pop("protocol", UNSET)

        servers = cast(list[str], d.pop("servers", UNSET))

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

        server_names = d.pop("serverNames", UNSET)

        local_ip = d.pop("localIp", UNSET)

        group_id = d.pop("groupId", UNSET)

        group_name = d.pop("groupName", UNSET)

        status = d.pop("status", UNSET)

        validity = d.pop("validity", UNSET)

        available = d.pop("available", UNSET)

        _feature_description = d.pop("featureDescription", UNSET)
        feature_description: list[FeatureInfoVO] | Unset = UNSET
        if _feature_description is not UNSET:
            feature_description = []
            for feature_description_item_data in _feature_description:
                feature_description_item = FeatureInfoVO.from_dict(
                    feature_description_item_data
                )

                feature_description.append(feature_description_item)

        vpn_user_info_vo = cls(
            id=id,
            username=username,
            password=password,
            protocol=protocol,
            servers=servers,
            client_mode=client_mode,
            max_connections=max_connections,
            user_remote_subnets=user_remote_subnets,
            server_names=server_names,
            local_ip=local_ip,
            group_id=group_id,
            group_name=group_name,
            status=status,
            validity=validity,
            available=available,
            feature_description=feature_description,
        )

        vpn_user_info_vo.additional_properties = d
        return vpn_user_info_vo

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
