from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ipv_6_dynamic_open_api_vo import Ipv6DynamicOpenApiVO
    from ..models.ipv_6_pppoe_open_api_vo import Ipv6PppoeOpenApiVO
    from ..models.ipv_6_static_open_api_vo import Ipv6StaticOpenApiVO
    from ..models.ipv_6_tunnel_open_api_vo import Ipv6TunnelOpenApiVO


T = TypeVar("T", bound="WanPortIpv6SettingOpenApiVO")


@_attrs_define
class WanPortIpv6SettingOpenApiVO:
    """Port IPv6 setting

    Attributes:
        enable (bool): IPv6 enable.
        proto_type (int | Unset): IPv6 connection type should be a value as follows: 0: static; 1: dynamic; 2: PPPoE; 3:
            6to4Tunnel; 4: bridge.
        ipv_6_dynamic (Ipv6DynamicOpenApiVO | Unset): It is required when protoType is dynamic
        ipv_6_pppoe (Ipv6PppoeOpenApiVO | Unset): It is required when protoType is PPPoE
        ipv_6_tunnel (Ipv6TunnelOpenApiVO | Unset): It is required when protoType is 6to4Tunnel
        ipv_6_static (Ipv6StaticOpenApiVO | Unset): It is required when protoType is static
    """

    enable: bool
    proto_type: int | Unset = UNSET
    ipv_6_dynamic: Ipv6DynamicOpenApiVO | Unset = UNSET
    ipv_6_pppoe: Ipv6PppoeOpenApiVO | Unset = UNSET
    ipv_6_tunnel: Ipv6TunnelOpenApiVO | Unset = UNSET
    ipv_6_static: Ipv6StaticOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        proto_type = self.proto_type

        ipv_6_dynamic: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ipv_6_dynamic, Unset):
            ipv_6_dynamic = self.ipv_6_dynamic.to_dict()

        ipv_6_pppoe: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ipv_6_pppoe, Unset):
            ipv_6_pppoe = self.ipv_6_pppoe.to_dict()

        ipv_6_tunnel: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ipv_6_tunnel, Unset):
            ipv_6_tunnel = self.ipv_6_tunnel.to_dict()

        ipv_6_static: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ipv_6_static, Unset):
            ipv_6_static = self.ipv_6_static.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
            }
        )
        if proto_type is not UNSET:
            field_dict["protoType"] = proto_type
        if ipv_6_dynamic is not UNSET:
            field_dict["ipv6Dynamic"] = ipv_6_dynamic
        if ipv_6_pppoe is not UNSET:
            field_dict["ipv6Pppoe"] = ipv_6_pppoe
        if ipv_6_tunnel is not UNSET:
            field_dict["ipv6Tunnel"] = ipv_6_tunnel
        if ipv_6_static is not UNSET:
            field_dict["ipv6Static"] = ipv_6_static

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ipv_6_dynamic_open_api_vo import (
            Ipv6DynamicOpenApiVO,
        )
        from ..models.ipv_6_pppoe_open_api_vo import Ipv6PppoeOpenApiVO
        from ..models.ipv_6_static_open_api_vo import (
            Ipv6StaticOpenApiVO,
        )
        from ..models.ipv_6_tunnel_open_api_vo import (
            Ipv6TunnelOpenApiVO,
        )

        d = dict(src_dict)
        enable = d.pop("enable")

        proto_type = d.pop("protoType", UNSET)

        _ipv_6_dynamic = d.pop("ipv6Dynamic", UNSET)
        ipv_6_dynamic: Ipv6DynamicOpenApiVO | Unset
        if isinstance(_ipv_6_dynamic, Unset):
            ipv_6_dynamic = UNSET
        else:
            ipv_6_dynamic = Ipv6DynamicOpenApiVO.from_dict(_ipv_6_dynamic)

        _ipv_6_pppoe = d.pop("ipv6Pppoe", UNSET)
        ipv_6_pppoe: Ipv6PppoeOpenApiVO | Unset
        if isinstance(_ipv_6_pppoe, Unset):
            ipv_6_pppoe = UNSET
        else:
            ipv_6_pppoe = Ipv6PppoeOpenApiVO.from_dict(_ipv_6_pppoe)

        _ipv_6_tunnel = d.pop("ipv6Tunnel", UNSET)
        ipv_6_tunnel: Ipv6TunnelOpenApiVO | Unset
        if isinstance(_ipv_6_tunnel, Unset):
            ipv_6_tunnel = UNSET
        else:
            ipv_6_tunnel = Ipv6TunnelOpenApiVO.from_dict(_ipv_6_tunnel)

        _ipv_6_static = d.pop("ipv6Static", UNSET)
        ipv_6_static: Ipv6StaticOpenApiVO | Unset
        if isinstance(_ipv_6_static, Unset):
            ipv_6_static = UNSET
        else:
            ipv_6_static = Ipv6StaticOpenApiVO.from_dict(_ipv_6_static)

        wan_port_ipv_6_setting_open_api_vo = cls(
            enable=enable,
            proto_type=proto_type,
            ipv_6_dynamic=ipv_6_dynamic,
            ipv_6_pppoe=ipv_6_pppoe,
            ipv_6_tunnel=ipv_6_tunnel,
            ipv_6_static=ipv_6_static,
        )

        wan_port_ipv_6_setting_open_api_vo.additional_properties = d
        return wan_port_ipv_6_setting_open_api_vo

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
