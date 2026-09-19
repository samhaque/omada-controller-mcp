from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="WireguardDetailOpenApiVO")


@_attrs_define
class WireguardDetailOpenApiVO:
    """
    Attributes:
        id (str | Unset): The ID of WireGuard VPN.
        name (str | Unset): The name of WireGuard VPN should contain 1 to 64 characters.
        status (bool | Unset): The status of WireGuard VPN.
        mtu (int | Unset): The MTU of WireGuard VPN should be within the range of 576-1440.
        listen_port (int | Unset): The listening port for WireGuard VPN should be within the range of 1-65535.
        private_key (str | Unset): The private key of WireGuard VPN must have 44 character of base64 and end with '='.
        public_key (str | Unset): The publicKey key of WireGuard VPN must have 44 character of base64 and end with '='.
        local_ip (str | Unset): The local IP address of WireGuard VPN.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    status: bool | Unset = UNSET
    mtu: int | Unset = UNSET
    listen_port: int | Unset = UNSET
    private_key: str | Unset = UNSET
    public_key: str | Unset = UNSET
    local_ip: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        status = self.status

        mtu = self.mtu

        listen_port = self.listen_port

        private_key = self.private_key

        public_key = self.public_key

        local_ip = self.local_ip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if mtu is not UNSET:
            field_dict["mtu"] = mtu
        if listen_port is not UNSET:
            field_dict["listenPort"] = listen_port
        if private_key is not UNSET:
            field_dict["privateKey"] = private_key
        if public_key is not UNSET:
            field_dict["publicKey"] = public_key
        if local_ip is not UNSET:
            field_dict["localIp"] = local_ip

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        status = d.pop("status", UNSET)

        mtu = d.pop("mtu", UNSET)

        listen_port = d.pop("listenPort", UNSET)

        private_key = d.pop("privateKey", UNSET)

        public_key = d.pop("publicKey", UNSET)

        local_ip = d.pop("localIp", UNSET)

        wireguard_detail_open_api_vo = cls(
            id=id,
            name=name,
            status=status,
            mtu=mtu,
            listen_port=listen_port,
            private_key=private_key,
            public_key=public_key,
            local_ip=local_ip,
        )

        wireguard_detail_open_api_vo.additional_properties = d
        return wireguard_detail_open_api_vo

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
