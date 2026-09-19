from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerWireGuardClientsVO")


@_attrs_define
class ServerWireGuardClientsVO:
    """WireGuard clients.

    Attributes:
        id (str | Unset): ID of the client.
        name (str | Unset): Client name.
        interface_ip (str | Unset): IP address.
        public_key (str | Unset): The public key of WireGuard VPN must have 44 character of base64 and end with '='.
        private_key (str | Unset): The privateKey key of WireGuard VPN must have 44 character of base64 and end with
            '='.
        pre_shared_key (str | Unset): The preSharedKey of WireGuard peer must have 44 character of base64 and end with
            '='.
        allowed_address_status (bool | Unset): When parameter [allowedAddressStatus] is false, server WireGuard peer
            allowed address is client interface IP.
        allowed_address (list[str] | Unset): IP/MASK address list of server WireGuard peer allowed.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    interface_ip: str | Unset = UNSET
    public_key: str | Unset = UNSET
    private_key: str | Unset = UNSET
    pre_shared_key: str | Unset = UNSET
    allowed_address_status: bool | Unset = UNSET
    allowed_address: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        interface_ip = self.interface_ip

        public_key = self.public_key

        private_key = self.private_key

        pre_shared_key = self.pre_shared_key

        allowed_address_status = self.allowed_address_status

        allowed_address: list[str] | Unset = UNSET
        if not isinstance(self.allowed_address, Unset):
            allowed_address = self.allowed_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if interface_ip is not UNSET:
            field_dict["interfaceIp"] = interface_ip
        if public_key is not UNSET:
            field_dict["publicKey"] = public_key
        if private_key is not UNSET:
            field_dict["privateKey"] = private_key
        if pre_shared_key is not UNSET:
            field_dict["preSharedKey"] = pre_shared_key
        if allowed_address_status is not UNSET:
            field_dict["allowedAddressStatus"] = allowed_address_status
        if allowed_address is not UNSET:
            field_dict["allowedAddress"] = allowed_address

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        interface_ip = d.pop("interfaceIp", UNSET)

        public_key = d.pop("publicKey", UNSET)

        private_key = d.pop("privateKey", UNSET)

        pre_shared_key = d.pop("preSharedKey", UNSET)

        allowed_address_status = d.pop("allowedAddressStatus", UNSET)

        allowed_address = cast(list[str], d.pop("allowedAddress", UNSET))

        server_wire_guard_clients_vo = cls(
            id=id,
            name=name,
            interface_ip=interface_ip,
            public_key=public_key,
            private_key=private_key,
            pre_shared_key=pre_shared_key,
            allowed_address_status=allowed_address_status,
            allowed_address=allowed_address,
        )

        server_wire_guard_clients_vo.additional_properties = d
        return server_wire_guard_clients_vo

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
