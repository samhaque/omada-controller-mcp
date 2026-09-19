from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SiteToSiteManualWgPeerConfigVO")


@_attrs_define
class SiteToSiteManualWgPeerConfigVO:
    """List of Site-To-Site manual WireGuard peer Configuration.

    Attributes:
        name (str): The name of WireGuard peer should contain 1 to 64 characters.
        status (bool): Status of the VPN.
        server_public_key (str): The public key of WireGuard VPN must have 44 character of base64 and end with '='.
        remote_subnet (list[str]): IP/MASK address list of client WireGuard peer allowed.
        keep_alive (int): The keepalive second of WireGuard peer should be within the range of 0-65535.
        remote_ip (str | Unset): Remote IP of the VPN
        service_port (int | Unset): Service port should be within the range of 1–65535.
        pre_shared_key (str | Unset): The preSharedKey of WireGuard peer must have 44 character of base64 and end with
            '='.
        comment (str | Unset): The comment of WireGuard peer should contain 0 to 128 characters.
    """

    name: str
    status: bool
    server_public_key: str
    remote_subnet: list[str]
    keep_alive: int
    remote_ip: str | Unset = UNSET
    service_port: int | Unset = UNSET
    pre_shared_key: str | Unset = UNSET
    comment: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status = self.status

        server_public_key = self.server_public_key

        remote_subnet = self.remote_subnet

        keep_alive = self.keep_alive

        remote_ip = self.remote_ip

        service_port = self.service_port

        pre_shared_key = self.pre_shared_key

        comment = self.comment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "status": status,
                "serverPublicKey": server_public_key,
                "remoteSubnet": remote_subnet,
                "keepAlive": keep_alive,
            }
        )
        if remote_ip is not UNSET:
            field_dict["remoteIp"] = remote_ip
        if service_port is not UNSET:
            field_dict["servicePort"] = service_port
        if pre_shared_key is not UNSET:
            field_dict["preSharedKey"] = pre_shared_key
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        status = d.pop("status")

        server_public_key = d.pop("serverPublicKey")

        remote_subnet = cast(list[str], d.pop("remoteSubnet"))

        keep_alive = d.pop("keepAlive")

        remote_ip = d.pop("remoteIp", UNSET)

        service_port = d.pop("servicePort", UNSET)

        pre_shared_key = d.pop("preSharedKey", UNSET)

        comment = d.pop("comment", UNSET)

        site_to_site_manual_wg_peer_config_vo = cls(
            name=name,
            status=status,
            server_public_key=server_public_key,
            remote_subnet=remote_subnet,
            keep_alive=keep_alive,
            remote_ip=remote_ip,
            service_port=service_port,
            pre_shared_key=pre_shared_key,
            comment=comment,
        )

        site_to_site_manual_wg_peer_config_vo.additional_properties = d
        return site_to_site_manual_wg_peer_config_vo

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
