from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerWireGuardClientsConfigVO")


@_attrs_define
class ServerWireGuardClientsConfigVO:
    """WireGuard clients.

    Attributes:
        name (str): Client name.
        interface_ip (str): IP address.
        private_key (str): The private key of WireGuard VPN must have 44 character of base64 and end with '='.
        pre_shared_key (str | Unset): The preSharedKey of WireGuard peer must have 44 character of base64 and end with
            '='.
        allowed_address_status (bool | Unset): When parameter [allowedAddressStatus] is false, server WireGuard peer
            allowed address is client interface IP.
        allowed_address (list[str] | Unset): IP/MASK address list of server WireGuard peer allowed.
    """

    name: str
    interface_ip: str
    private_key: str
    pre_shared_key: str | Unset = UNSET
    allowed_address_status: bool | Unset = UNSET
    allowed_address: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        interface_ip = self.interface_ip

        private_key = self.private_key

        pre_shared_key = self.pre_shared_key

        allowed_address_status = self.allowed_address_status

        allowed_address: list[str] | Unset = UNSET
        if not isinstance(self.allowed_address, Unset):
            allowed_address = self.allowed_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "interfaceIp": interface_ip,
                "privateKey": private_key,
            }
        )
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
        name = d.pop("name")

        interface_ip = d.pop("interfaceIp")

        private_key = d.pop("privateKey")

        pre_shared_key = d.pop("preSharedKey", UNSET)

        allowed_address_status = d.pop("allowedAddressStatus", UNSET)

        allowed_address = cast(list[str], d.pop("allowedAddress", UNSET))

        server_wire_guard_clients_config_vo = cls(
            name=name,
            interface_ip=interface_ip,
            private_key=private_key,
            pre_shared_key=pre_shared_key,
            allowed_address_status=allowed_address_status,
            allowed_address=allowed_address,
        )

        server_wire_guard_clients_config_vo.additional_properties = d
        return server_wire_guard_clients_config_vo

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
