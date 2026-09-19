from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="VpnValueAvailableVO")


@_attrs_define
class VpnValueAvailableVO:
    """
    Attributes:
        type_ (int): Parameter [type] should be a value as follows: 0, name; 1, port.
        usage (int | Unset): Parameter [usage] should not be null when [type] is name. Parameter [usage] should be a
            value as follows: 0, server; 1, client; 2: site-to-site.
        name (str | Unset): VPN name. Parameter [name] should not be null when [type] is name.
        port (int | Unset): Parameter [port] should not be null when [type] is port.
        vpn_type (int | Unset): Vpn type should be a value as follows: 0: L2TP; 1: PPTP; 2: IPSec; 3: OpenVPN; 4:
            WireGuard; 5: SSL VPN.
        wan (str | Unset): WAN of the VPN.
        service_type (int | Unset): Service type of the Open VPN should be a value as follows: 0: UDP; 1: TCP.
        id (str | Unset): VPN ID.
    """

    type_: int
    usage: int | Unset = UNSET
    name: str | Unset = UNSET
    port: int | Unset = UNSET
    vpn_type: int | Unset = UNSET
    wan: str | Unset = UNSET
    service_type: int | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        usage = self.usage

        name = self.name

        port = self.port

        vpn_type = self.vpn_type

        wan = self.wan

        service_type = self.service_type

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if usage is not UNSET:
            field_dict["usage"] = usage
        if name is not UNSET:
            field_dict["name"] = name
        if port is not UNSET:
            field_dict["port"] = port
        if vpn_type is not UNSET:
            field_dict["vpnType"] = vpn_type
        if wan is not UNSET:
            field_dict["wan"] = wan
        if service_type is not UNSET:
            field_dict["serviceType"] = service_type
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type")

        usage = d.pop("usage", UNSET)

        name = d.pop("name", UNSET)

        port = d.pop("port", UNSET)

        vpn_type = d.pop("vpnType", UNSET)

        wan = d.pop("wan", UNSET)

        service_type = d.pop("serviceType", UNSET)

        id = d.pop("id", UNSET)

        vpn_value_available_vo = cls(
            type_=type_,
            usage=usage,
            name=name,
            port=port,
            vpn_type=vpn_type,
            wan=wan,
            service_type=service_type,
            id=id,
        )

        vpn_value_available_vo.additional_properties = d
        return vpn_value_available_vo

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
