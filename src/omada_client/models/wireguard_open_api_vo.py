from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="WireguardOpenApiVO")


@_attrs_define
class WireguardOpenApiVO:
    """
    Attributes:
        name (str): The name of WireGuard VPN should contain 1 to 64 characters.
        status (bool): The status of WireGuard VPN. Valid value is true or false.
        mtu (int): The MTU of WireGuard VPN should be within the range of 576-1440.
        listen_port (int): The listening port for WireGuard VPN should be within the range of 1-65535.
        private_key (str): The private key of WireGuard VPN must have 44 character of base64 and end with '='.
        local_ip (str): The local IP address of WireGuard VPN.
    """

    name: str
    status: bool
    mtu: int
    listen_port: int
    private_key: str
    local_ip: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status = self.status

        mtu = self.mtu

        listen_port = self.listen_port

        private_key = self.private_key

        local_ip = self.local_ip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "status": status,
                "mtu": mtu,
                "listenPort": listen_port,
                "privateKey": private_key,
                "localIp": local_ip,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        status = d.pop("status")

        mtu = d.pop("mtu")

        listen_port = d.pop("listenPort")

        private_key = d.pop("privateKey")

        local_ip = d.pop("localIp")

        wireguard_open_api_vo = cls(
            name=name,
            status=status,
            mtu=mtu,
            listen_port=listen_port,
            private_key=private_key,
            local_ip=local_ip,
        )

        wireguard_open_api_vo.additional_properties = d
        return wireguard_open_api_vo

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
