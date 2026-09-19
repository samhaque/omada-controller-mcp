from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="WireguardPeerDetailOpenApiVO")


@_attrs_define
class WireguardPeerDetailOpenApiVO:
    """
    Attributes:
        id (str | Unset): The ID of WireGuard peer.
        name (str | Unset): The name of WireGuard peer should contain 1 to 64 characters.
        status (bool | Unset): The status of WireGuard peer.
        interface_id (str | Unset): The ID of WireGuard VPN to which this WireGuard peer binds. The ID can be obtained
            from 'Get all wireguard's id and name info' interface.
        interface_name (str | Unset): The name of WireGuard VPN to which this WireGuard peer binds.
        public_key (str | Unset): The public key of WireGuard peer must have 44 character of base64 and end with '='.
        end_point (str | Unset): The end point of WireGuard peer.
        end_point_port (int | Unset): The end point port of WireGuard peer should be within the range of 1-65535.
        exist_domain (bool | Unset): Whether a domain name has been configured in Endpoint.
        allow_address (list[str] | Unset): IP address list of WireGuard peer allowed.
        preshared_key (str | Unset): The presharedKey of WireGuard peer must have 44 character of base64 and end with
            '='.
        keep_alive (int | Unset): The keepalive second of WireGuard peer should be within the range of 0-65535.
        comment (str | Unset): The comment of WireGuard peer should contain 0 to 128 characters.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    status: bool | Unset = UNSET
    interface_id: str | Unset = UNSET
    interface_name: str | Unset = UNSET
    public_key: str | Unset = UNSET
    end_point: str | Unset = UNSET
    end_point_port: int | Unset = UNSET
    exist_domain: bool | Unset = UNSET
    allow_address: list[str] | Unset = UNSET
    preshared_key: str | Unset = UNSET
    keep_alive: int | Unset = UNSET
    comment: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        status = self.status

        interface_id = self.interface_id

        interface_name = self.interface_name

        public_key = self.public_key

        end_point = self.end_point

        end_point_port = self.end_point_port

        exist_domain = self.exist_domain

        allow_address: list[str] | Unset = UNSET
        if not isinstance(self.allow_address, Unset):
            allow_address = self.allow_address

        preshared_key = self.preshared_key

        keep_alive = self.keep_alive

        comment = self.comment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if interface_id is not UNSET:
            field_dict["interfaceId"] = interface_id
        if interface_name is not UNSET:
            field_dict["interfaceName"] = interface_name
        if public_key is not UNSET:
            field_dict["publicKey"] = public_key
        if end_point is not UNSET:
            field_dict["endPoint"] = end_point
        if end_point_port is not UNSET:
            field_dict["endPointPort"] = end_point_port
        if exist_domain is not UNSET:
            field_dict["existDomain"] = exist_domain
        if allow_address is not UNSET:
            field_dict["allowAddress"] = allow_address
        if preshared_key is not UNSET:
            field_dict["presharedKey"] = preshared_key
        if keep_alive is not UNSET:
            field_dict["keepAlive"] = keep_alive
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        status = d.pop("status", UNSET)

        interface_id = d.pop("interfaceId", UNSET)

        interface_name = d.pop("interfaceName", UNSET)

        public_key = d.pop("publicKey", UNSET)

        end_point = d.pop("endPoint", UNSET)

        end_point_port = d.pop("endPointPort", UNSET)

        exist_domain = d.pop("existDomain", UNSET)

        allow_address = cast(list[str], d.pop("allowAddress", UNSET))

        preshared_key = d.pop("presharedKey", UNSET)

        keep_alive = d.pop("keepAlive", UNSET)

        comment = d.pop("comment", UNSET)

        wireguard_peer_detail_open_api_vo = cls(
            id=id,
            name=name,
            status=status,
            interface_id=interface_id,
            interface_name=interface_name,
            public_key=public_key,
            end_point=end_point,
            end_point_port=end_point_port,
            exist_domain=exist_domain,
            allow_address=allow_address,
            preshared_key=preshared_key,
            keep_alive=keep_alive,
            comment=comment,
        )

        wireguard_peer_detail_open_api_vo.additional_properties = d
        return wireguard_peer_detail_open_api_vo

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
