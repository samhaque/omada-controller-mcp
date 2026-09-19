from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vpn_default_value_resp_vo_vpn_name import VpnDefaultValueRespVOVpnName


T = TypeVar("T", bound="VpnDefaultValueRespVO")


@_attrs_define
class VpnDefaultValueRespVO:
    """
    Attributes:
        vpn_name (VpnDefaultValueRespVOVpnName | Unset): Default VPN name for each VPN type.
        port (int | Unset): Default service port.
        tunnel_ip (str | Unset): Default tunnel IP for Wire Guard.
    """

    vpn_name: VpnDefaultValueRespVOVpnName | Unset = UNSET
    port: int | Unset = UNSET
    tunnel_ip: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vpn_name: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vpn_name, Unset):
            vpn_name = self.vpn_name.to_dict()

        port = self.port

        tunnel_ip = self.tunnel_ip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vpn_name is not UNSET:
            field_dict["vpnName"] = vpn_name
        if port is not UNSET:
            field_dict["port"] = port
        if tunnel_ip is not UNSET:
            field_dict["tunnelIp"] = tunnel_ip

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.vpn_default_value_resp_vo_vpn_name import (
            VpnDefaultValueRespVOVpnName,
        )

        d = dict(src_dict)
        _vpn_name = d.pop("vpnName", UNSET)
        vpn_name: VpnDefaultValueRespVOVpnName | Unset
        if isinstance(_vpn_name, Unset):
            vpn_name = UNSET
        else:
            vpn_name = VpnDefaultValueRespVOVpnName.from_dict(_vpn_name)

        port = d.pop("port", UNSET)

        tunnel_ip = d.pop("tunnelIp", UNSET)

        vpn_default_value_resp_vo = cls(
            vpn_name=vpn_name,
            port=port,
            tunnel_ip=tunnel_ip,
        )

        vpn_default_value_resp_vo.additional_properties = d
        return vpn_default_value_resp_vo

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
