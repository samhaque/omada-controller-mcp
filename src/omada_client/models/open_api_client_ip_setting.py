from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenApiClientIpSetting")


@_attrs_define
class OpenApiClientIpSetting:
    """
    Attributes:
        use_fixed_addr (bool): Whether to use the specified IP
        net_id (str | Unset): Lan network ID
        ip (str | Unset): Client IP
        server_type (str | Unset): DHCP Server Type
        server_mac (str | Unset): DHCP Server Mac
        server_stack_id (str | Unset): DHCP Server Stack ID
    """

    use_fixed_addr: bool
    net_id: str | Unset = UNSET
    ip: str | Unset = UNSET
    server_type: str | Unset = UNSET
    server_mac: str | Unset = UNSET
    server_stack_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        use_fixed_addr = self.use_fixed_addr

        net_id = self.net_id

        ip = self.ip

        server_type = self.server_type

        server_mac = self.server_mac

        server_stack_id = self.server_stack_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "useFixedAddr": use_fixed_addr,
            }
        )
        if net_id is not UNSET:
            field_dict["netId"] = net_id
        if ip is not UNSET:
            field_dict["ip"] = ip
        if server_type is not UNSET:
            field_dict["serverType"] = server_type
        if server_mac is not UNSET:
            field_dict["serverMac"] = server_mac
        if server_stack_id is not UNSET:
            field_dict["serverStackId"] = server_stack_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        use_fixed_addr = d.pop("useFixedAddr")

        net_id = d.pop("netId", UNSET)

        ip = d.pop("ip", UNSET)

        server_type = d.pop("serverType", UNSET)

        server_mac = d.pop("serverMac", UNSET)

        server_stack_id = d.pop("serverStackId", UNSET)

        open_api_client_ip_setting = cls(
            use_fixed_addr=use_fixed_addr,
            net_id=net_id,
            ip=ip,
            server_type=server_type,
            server_mac=server_mac,
            server_stack_id=server_stack_id,
        )

        open_api_client_ip_setting.additional_properties = d
        return open_api_client_ip_setting

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
