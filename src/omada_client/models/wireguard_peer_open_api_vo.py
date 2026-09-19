from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="WireguardPeerOpenApiVO")


@_attrs_define
class WireguardPeerOpenApiVO:
    """
    Attributes:
        name (str): The name of WireGuard peer should contain 1 to 64 characters.
        status (bool): The status of WireGuard peer. Valid value is true or false.
        interface_id (str): The ID of WireGuard VPN to which this WireGuard peer binds. The ID can be obtained from 'Get
            all wireguard's id and name info' interface.
        public_key (str): The public key of WireGuard peer must have 44 character of base64 and end with '='.
        allow_address (list[str]): IP/MASK address list of WireGuard peer allowed.
        keep_alive (int): The keepalive second of WireGuard peer should be within the range of 0-65535.
        end_point (str | Unset): The end point IP of WireGuard peer. Get whether supports domain from interface 'Get
            wireguard peer list'.
        end_point_port (int | Unset): The end point port of WireGuard peer should be within the range of 1-65535.
        preshared_key (str | Unset): The presharedKey of WireGuard peer must have 44 character of base64 and end with
            '='.
        comment (str | Unset): The comment of WireGuard peer should contain 0 to 128 characters.
    """

    name: str
    status: bool
    interface_id: str
    public_key: str
    allow_address: list[str]
    keep_alive: int
    end_point: str | Unset = UNSET
    end_point_port: int | Unset = UNSET
    preshared_key: str | Unset = UNSET
    comment: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status = self.status

        interface_id = self.interface_id

        public_key = self.public_key

        allow_address = self.allow_address

        keep_alive = self.keep_alive

        end_point = self.end_point

        end_point_port = self.end_point_port

        preshared_key = self.preshared_key

        comment = self.comment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "status": status,
                "interfaceId": interface_id,
                "publicKey": public_key,
                "allowAddress": allow_address,
                "keepAlive": keep_alive,
            }
        )
        if end_point is not UNSET:
            field_dict["endPoint"] = end_point
        if end_point_port is not UNSET:
            field_dict["endPointPort"] = end_point_port
        if preshared_key is not UNSET:
            field_dict["presharedKey"] = preshared_key
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        status = d.pop("status")

        interface_id = d.pop("interfaceId")

        public_key = d.pop("publicKey")

        allow_address = cast(list[str], d.pop("allowAddress"))

        keep_alive = d.pop("keepAlive")

        end_point = d.pop("endPoint", UNSET)

        end_point_port = d.pop("endPointPort", UNSET)

        preshared_key = d.pop("presharedKey", UNSET)

        comment = d.pop("comment", UNSET)

        wireguard_peer_open_api_vo = cls(
            name=name,
            status=status,
            interface_id=interface_id,
            public_key=public_key,
            allow_address=allow_address,
            keep_alive=keep_alive,
            end_point=end_point,
            end_point_port=end_point_port,
            preshared_key=preshared_key,
            comment=comment,
        )

        wireguard_peer_open_api_vo.additional_properties = d
        return wireguard_peer_open_api_vo

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
