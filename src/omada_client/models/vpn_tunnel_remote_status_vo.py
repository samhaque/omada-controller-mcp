from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="VpnTunnelRemoteStatusVO")


@_attrs_define
class VpnTunnelRemoteStatusVO:
    """
    Attributes:
        id (str | Unset):
        vpn_id (str | Unset):
        name (str | Unset):
        remote_ip (str | Unset):
        local_ip (str | Unset):
        down_pkts (int | Unset):
        down_bytes (int | Unset):
        up_pkts (int | Unset):
        up_bytes (int | Unset):
        login_time (int | Unset):
        port (int | Unset):
        status (int | Unset):
    """

    id: str | Unset = UNSET
    vpn_id: str | Unset = UNSET
    name: str | Unset = UNSET
    remote_ip: str | Unset = UNSET
    local_ip: str | Unset = UNSET
    down_pkts: int | Unset = UNSET
    down_bytes: int | Unset = UNSET
    up_pkts: int | Unset = UNSET
    up_bytes: int | Unset = UNSET
    login_time: int | Unset = UNSET
    port: int | Unset = UNSET
    status: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        vpn_id = self.vpn_id

        name = self.name

        remote_ip = self.remote_ip

        local_ip = self.local_ip

        down_pkts = self.down_pkts

        down_bytes = self.down_bytes

        up_pkts = self.up_pkts

        up_bytes = self.up_bytes

        login_time = self.login_time

        port = self.port

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if vpn_id is not UNSET:
            field_dict["vpnId"] = vpn_id
        if name is not UNSET:
            field_dict["name"] = name
        if remote_ip is not UNSET:
            field_dict["remoteIp"] = remote_ip
        if local_ip is not UNSET:
            field_dict["localIp"] = local_ip
        if down_pkts is not UNSET:
            field_dict["downPkts"] = down_pkts
        if down_bytes is not UNSET:
            field_dict["downBytes"] = down_bytes
        if up_pkts is not UNSET:
            field_dict["upPkts"] = up_pkts
        if up_bytes is not UNSET:
            field_dict["upBytes"] = up_bytes
        if login_time is not UNSET:
            field_dict["loginTime"] = login_time
        if port is not UNSET:
            field_dict["port"] = port
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        vpn_id = d.pop("vpnId", UNSET)

        name = d.pop("name", UNSET)

        remote_ip = d.pop("remoteIp", UNSET)

        local_ip = d.pop("localIp", UNSET)

        down_pkts = d.pop("downPkts", UNSET)

        down_bytes = d.pop("downBytes", UNSET)

        up_pkts = d.pop("upPkts", UNSET)

        up_bytes = d.pop("upBytes", UNSET)

        login_time = d.pop("loginTime", UNSET)

        port = d.pop("port", UNSET)

        status = d.pop("status", UNSET)

        vpn_tunnel_remote_status_vo = cls(
            id=id,
            vpn_id=vpn_id,
            name=name,
            remote_ip=remote_ip,
            local_ip=local_ip,
            down_pkts=down_pkts,
            down_bytes=down_bytes,
            up_pkts=up_pkts,
            up_bytes=up_bytes,
            login_time=login_time,
            port=port,
            status=status,
        )

        vpn_tunnel_remote_status_vo.additional_properties = d
        return vpn_tunnel_remote_status_vo

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
