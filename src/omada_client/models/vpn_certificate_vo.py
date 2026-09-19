from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="VpnCertificateVO")


@_attrs_define
class VpnCertificateVO:
    """
    Attributes:
        id (str | Unset):
        file_name (str | Unset):
        remote_ip (str | Unset):
        service_port (int | Unset):
        open_vpn_mode (int | Unset):
        private_key (str | Unset):
        public_key (str | Unset):
        server_public_key (str | Unset):
        pre_shared_key (str | Unset):
        local_ip (str | Unset):
        dns1 (str | Unset):
        dns2 (str | Unset):
        allowed_server_address (list[str] | Unset):
        keep_alive (int | Unset):
    """

    id: str | Unset = UNSET
    file_name: str | Unset = UNSET
    remote_ip: str | Unset = UNSET
    service_port: int | Unset = UNSET
    open_vpn_mode: int | Unset = UNSET
    private_key: str | Unset = UNSET
    public_key: str | Unset = UNSET
    server_public_key: str | Unset = UNSET
    pre_shared_key: str | Unset = UNSET
    local_ip: str | Unset = UNSET
    dns1: str | Unset = UNSET
    dns2: str | Unset = UNSET
    allowed_server_address: list[str] | Unset = UNSET
    keep_alive: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        file_name = self.file_name

        remote_ip = self.remote_ip

        service_port = self.service_port

        open_vpn_mode = self.open_vpn_mode

        private_key = self.private_key

        public_key = self.public_key

        server_public_key = self.server_public_key

        pre_shared_key = self.pre_shared_key

        local_ip = self.local_ip

        dns1 = self.dns1

        dns2 = self.dns2

        allowed_server_address: list[str] | Unset = UNSET
        if not isinstance(self.allowed_server_address, Unset):
            allowed_server_address = self.allowed_server_address

        keep_alive = self.keep_alive

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if remote_ip is not UNSET:
            field_dict["remoteIp"] = remote_ip
        if service_port is not UNSET:
            field_dict["servicePort"] = service_port
        if open_vpn_mode is not UNSET:
            field_dict["openVpnMode"] = open_vpn_mode
        if private_key is not UNSET:
            field_dict["privateKey"] = private_key
        if public_key is not UNSET:
            field_dict["publicKey"] = public_key
        if server_public_key is not UNSET:
            field_dict["serverPublicKey"] = server_public_key
        if pre_shared_key is not UNSET:
            field_dict["preSharedKey"] = pre_shared_key
        if local_ip is not UNSET:
            field_dict["localIp"] = local_ip
        if dns1 is not UNSET:
            field_dict["dns1"] = dns1
        if dns2 is not UNSET:
            field_dict["dns2"] = dns2
        if allowed_server_address is not UNSET:
            field_dict["allowedServerAddress"] = allowed_server_address
        if keep_alive is not UNSET:
            field_dict["keepAlive"] = keep_alive

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        file_name = d.pop("fileName", UNSET)

        remote_ip = d.pop("remoteIp", UNSET)

        service_port = d.pop("servicePort", UNSET)

        open_vpn_mode = d.pop("openVpnMode", UNSET)

        private_key = d.pop("privateKey", UNSET)

        public_key = d.pop("publicKey", UNSET)

        server_public_key = d.pop("serverPublicKey", UNSET)

        pre_shared_key = d.pop("preSharedKey", UNSET)

        local_ip = d.pop("localIp", UNSET)

        dns1 = d.pop("dns1", UNSET)

        dns2 = d.pop("dns2", UNSET)

        allowed_server_address = cast(list[str], d.pop("allowedServerAddress", UNSET))

        keep_alive = d.pop("keepAlive", UNSET)

        vpn_certificate_vo = cls(
            id=id,
            file_name=file_name,
            remote_ip=remote_ip,
            service_port=service_port,
            open_vpn_mode=open_vpn_mode,
            private_key=private_key,
            public_key=public_key,
            server_public_key=server_public_key,
            pre_shared_key=pre_shared_key,
            local_ip=local_ip,
            dns1=dns1,
            dns2=dns2,
            allowed_server_address=allowed_server_address,
            keep_alive=keep_alive,
        )

        vpn_certificate_vo.additional_properties = d
        return vpn_certificate_vo

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
