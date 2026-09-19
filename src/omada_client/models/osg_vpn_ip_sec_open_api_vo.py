from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OsgVpnIpSecOpenApiVO")


@_attrs_define
class OsgVpnIpSecOpenApiVO:
    """
    Attributes:
        vpn_id (int | Unset): VPN Item Id.
        spi (int | Unset): Security Parameter Index of SA.
        name (str | Unset): IPsec name.
        direction (str | Unset): SA direction, in/out.
        local_peer_ip (str | Unset): IP address of the local peer.
        remote_peer_ip (str | Unset): IP address of the remote peer.
        local_sa (str | Unset): Local network segment of SA cover.
        remote_sa (str | Unset): Remote network segment of SA cover.
        protocol (str | Unset): SA Authentication protocol and Encryption protocol.
        ah_authentication (str | Unset): AH Authentication Algorithm.
        esp_authentication (str | Unset): ESP Authentication Algorithm.
        esp_encryption (str | Unset): ESP Encryption Algorithm.
    """

    vpn_id: int | Unset = UNSET
    spi: int | Unset = UNSET
    name: str | Unset = UNSET
    direction: str | Unset = UNSET
    local_peer_ip: str | Unset = UNSET
    remote_peer_ip: str | Unset = UNSET
    local_sa: str | Unset = UNSET
    remote_sa: str | Unset = UNSET
    protocol: str | Unset = UNSET
    ah_authentication: str | Unset = UNSET
    esp_authentication: str | Unset = UNSET
    esp_encryption: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vpn_id = self.vpn_id

        spi = self.spi

        name = self.name

        direction = self.direction

        local_peer_ip = self.local_peer_ip

        remote_peer_ip = self.remote_peer_ip

        local_sa = self.local_sa

        remote_sa = self.remote_sa

        protocol = self.protocol

        ah_authentication = self.ah_authentication

        esp_authentication = self.esp_authentication

        esp_encryption = self.esp_encryption

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vpn_id is not UNSET:
            field_dict["vpnId"] = vpn_id
        if spi is not UNSET:
            field_dict["spi"] = spi
        if name is not UNSET:
            field_dict["name"] = name
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
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if ah_authentication is not UNSET:
            field_dict["ahAuthentication"] = ah_authentication
        if esp_authentication is not UNSET:
            field_dict["espAuthentication"] = esp_authentication
        if esp_encryption is not UNSET:
            field_dict["espEncryption"] = esp_encryption

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        vpn_id = d.pop("vpnId", UNSET)

        spi = d.pop("spi", UNSET)

        name = d.pop("name", UNSET)

        direction = d.pop("direction", UNSET)

        local_peer_ip = d.pop("localPeerIp", UNSET)

        remote_peer_ip = d.pop("remotePeerIp", UNSET)

        local_sa = d.pop("localSa", UNSET)

        remote_sa = d.pop("remoteSa", UNSET)

        protocol = d.pop("protocol", UNSET)

        ah_authentication = d.pop("ahAuthentication", UNSET)

        esp_authentication = d.pop("espAuthentication", UNSET)

        esp_encryption = d.pop("espEncryption", UNSET)

        osg_vpn_ip_sec_open_api_vo = cls(
            vpn_id=vpn_id,
            spi=spi,
            name=name,
            direction=direction,
            local_peer_ip=local_peer_ip,
            remote_peer_ip=remote_peer_ip,
            local_sa=local_sa,
            remote_sa=remote_sa,
            protocol=protocol,
            ah_authentication=ah_authentication,
            esp_authentication=esp_authentication,
            esp_encryption=esp_encryption,
        )

        osg_vpn_ip_sec_open_api_vo.additional_properties = d
        return osg_vpn_ip_sec_open_api_vo

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
