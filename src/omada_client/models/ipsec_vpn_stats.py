from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="IpsecVpnStats")


@_attrs_define
class IpsecVpnStats:
    """
    Attributes:
        site (str | Unset):
        name (str | Unset): VPN name
        id (int | Unset): VPN ID
        status (bool | Unset): VPN status, whether to enable VPN
        direction (str | Unset): SA direction should be a value as follows: in; out
        local_peer_ip (str | Unset): IP address of the local peer
        remote_peer_ip (str | Unset): IP address of the remote peer
        local_sa (str | Unset): Local network segment of SA Cover
        remote_sa (str | Unset): Remote network segment of SA Cover
    """

    site: str | Unset = UNSET
    name: str | Unset = UNSET
    id: int | Unset = UNSET
    status: bool | Unset = UNSET
    direction: str | Unset = UNSET
    local_peer_ip: str | Unset = UNSET
    remote_peer_ip: str | Unset = UNSET
    local_sa: str | Unset = UNSET
    remote_sa: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site = self.site

        name = self.name

        id = self.id

        status = self.status

        direction = self.direction

        local_peer_ip = self.local_peer_ip

        remote_peer_ip = self.remote_peer_ip

        local_sa = self.local_sa

        remote_sa = self.remote_sa

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site is not UNSET:
            field_dict["site"] = site
        if name is not UNSET:
            field_dict["name"] = name
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if direction is not UNSET:
            field_dict["direction"] = direction
        if local_peer_ip is not UNSET:
            field_dict["localPeerIp"] = local_peer_ip
        if remote_peer_ip is not UNSET:
            field_dict["remotePeerIp"] = remote_peer_ip
        if local_sa is not UNSET:
            field_dict["localSa"] = local_sa
        if remote_sa is not UNSET:
            field_dict["remoteSa"] = remote_sa

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        site = d.pop("site", UNSET)

        name = d.pop("name", UNSET)

        id = d.pop("id", UNSET)

        status = d.pop("status", UNSET)

        direction = d.pop("direction", UNSET)

        local_peer_ip = d.pop("localPeerIp", UNSET)

        remote_peer_ip = d.pop("remotePeerIp", UNSET)

        local_sa = d.pop("localSa", UNSET)

        remote_sa = d.pop("remoteSa", UNSET)

        ipsec_vpn_stats = cls(
            site=site,
            name=name,
            id=id,
            status=status,
            direction=direction,
            local_peer_ip=local_peer_ip,
            remote_peer_ip=remote_peer_ip,
            local_sa=local_sa,
            remote_sa=remote_sa,
        )

        ipsec_vpn_stats.additional_properties = d
        return ipsec_vpn_stats

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
