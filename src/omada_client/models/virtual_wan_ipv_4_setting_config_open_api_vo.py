from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.virtual_wan_ipv_4_dhcp_open_api_vo import VirtualWanIpv4DhcpOpenApiVO
    from ..models.virtual_wan_ipv_4_ipoa_open_api_vo import VirtualWanIpv4IpoaOpenApiVO
    from ..models.virtual_wan_ipv_4_pppoa_open_api_vo import (
        VirtualWanIpv4PppoaOpenApiVO,
    )
    from ..models.virtual_wan_ipv_4_pppoe_open_api_vo import (
        VirtualWanIpv4PppoeOpenApiVO,
    )
    from ..models.virtual_wan_ipv_4_static_open_api_vo import (
        VirtualWanIpv4StaticOpenApiVO,
    )


T = TypeVar("T", bound="VirtualWanIpv4SettingConfigOpenApiVO")


@_attrs_define
class VirtualWanIpv4SettingConfigOpenApiVO:
    """VirtualWanIpv4SettingConfigOpenApiVO

    Attributes:
        proto (str): Virtual WAN IPv4 protocol type: static, dhcp, pppoe for all connections; pppoa and ipoa options are
            only available for ADSL modulation connections. The configuration for the selected protocol type is required and
            must not be empty (e.g., ipv4Static for static).
        vlan_id (int): Vlan ID. Parameter [vlanId] should between 1 and 4094.
        qos_tag_enable (bool): Whether to enable 802.1Q Tag.
        vlan_priority (int | Unset): Vlan Priority. It takes effect when [vlanId] is not 0, and it should be within the
            range of 0–7.
        qos_tag (int | Unset): Qos Tag. Parameter [qosTag] should between 0 and 7.
        ipv_4_static (VirtualWanIpv4StaticOpenApiVO | Unset): VirtualWanIpv4StaticOpenApiVO
        ipv_4_dhcp (VirtualWanIpv4DhcpOpenApiVO | Unset): VirtualWanIpv4DhcpOpenApiVO
        ipv_4_pppoe (VirtualWanIpv4PppoeOpenApiVO | Unset): VirtualWanIpv4PppoeOpenApiVO
        ipv_4_pppoa (VirtualWanIpv4PppoaOpenApiVO | Unset): VirtualWanIpv4PppoaOpenApiVO
        ipv_4_ipoa (VirtualWanIpv4IpoaOpenApiVO | Unset): VirtualWanIpv4IpoaOpenApiVO
    """

    proto: str
    vlan_id: int
    qos_tag_enable: bool
    vlan_priority: int | Unset = UNSET
    qos_tag: int | Unset = UNSET
    ipv_4_static: VirtualWanIpv4StaticOpenApiVO | Unset = UNSET
    ipv_4_dhcp: VirtualWanIpv4DhcpOpenApiVO | Unset = UNSET
    ipv_4_pppoe: VirtualWanIpv4PppoeOpenApiVO | Unset = UNSET
    ipv_4_pppoa: VirtualWanIpv4PppoaOpenApiVO | Unset = UNSET
    ipv_4_ipoa: VirtualWanIpv4IpoaOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        proto = self.proto

        vlan_id = self.vlan_id

        qos_tag_enable = self.qos_tag_enable

        vlan_priority = self.vlan_priority

        qos_tag = self.qos_tag

        ipv_4_static: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ipv_4_static, Unset):
            ipv_4_static = self.ipv_4_static.to_dict()

        ipv_4_dhcp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ipv_4_dhcp, Unset):
            ipv_4_dhcp = self.ipv_4_dhcp.to_dict()

        ipv_4_pppoe: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ipv_4_pppoe, Unset):
            ipv_4_pppoe = self.ipv_4_pppoe.to_dict()

        ipv_4_pppoa: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ipv_4_pppoa, Unset):
            ipv_4_pppoa = self.ipv_4_pppoa.to_dict()

        ipv_4_ipoa: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ipv_4_ipoa, Unset):
            ipv_4_ipoa = self.ipv_4_ipoa.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "proto": proto,
                "vlanId": vlan_id,
                "qosTagEnable": qos_tag_enable,
            }
        )
        if vlan_priority is not UNSET:
            field_dict["vlanPriority"] = vlan_priority
        if qos_tag is not UNSET:
            field_dict["qosTag"] = qos_tag
        if ipv_4_static is not UNSET:
            field_dict["ipv4Static"] = ipv_4_static
        if ipv_4_dhcp is not UNSET:
            field_dict["ipv4Dhcp"] = ipv_4_dhcp
        if ipv_4_pppoe is not UNSET:
            field_dict["ipv4Pppoe"] = ipv_4_pppoe
        if ipv_4_pppoa is not UNSET:
            field_dict["ipv4Pppoa"] = ipv_4_pppoa
        if ipv_4_ipoa is not UNSET:
            field_dict["ipv4Ipoa"] = ipv_4_ipoa

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.virtual_wan_ipv_4_dhcp_open_api_vo import (
            VirtualWanIpv4DhcpOpenApiVO,
        )
        from ..models.virtual_wan_ipv_4_ipoa_open_api_vo import (
            VirtualWanIpv4IpoaOpenApiVO,
        )
        from ..models.virtual_wan_ipv_4_pppoa_open_api_vo import (
            VirtualWanIpv4PppoaOpenApiVO,
        )
        from ..models.virtual_wan_ipv_4_pppoe_open_api_vo import (
            VirtualWanIpv4PppoeOpenApiVO,
        )
        from ..models.virtual_wan_ipv_4_static_open_api_vo import (
            VirtualWanIpv4StaticOpenApiVO,
        )

        d = dict(src_dict)
        proto = d.pop("proto")

        vlan_id = d.pop("vlanId")

        qos_tag_enable = d.pop("qosTagEnable")

        vlan_priority = d.pop("vlanPriority", UNSET)

        qos_tag = d.pop("qosTag", UNSET)

        _ipv_4_static = d.pop("ipv4Static", UNSET)
        ipv_4_static: VirtualWanIpv4StaticOpenApiVO | Unset
        if isinstance(_ipv_4_static, Unset):
            ipv_4_static = UNSET
        else:
            ipv_4_static = VirtualWanIpv4StaticOpenApiVO.from_dict(_ipv_4_static)

        _ipv_4_dhcp = d.pop("ipv4Dhcp", UNSET)
        ipv_4_dhcp: VirtualWanIpv4DhcpOpenApiVO | Unset
        if isinstance(_ipv_4_dhcp, Unset):
            ipv_4_dhcp = UNSET
        else:
            ipv_4_dhcp = VirtualWanIpv4DhcpOpenApiVO.from_dict(_ipv_4_dhcp)

        _ipv_4_pppoe = d.pop("ipv4Pppoe", UNSET)
        ipv_4_pppoe: VirtualWanIpv4PppoeOpenApiVO | Unset
        if isinstance(_ipv_4_pppoe, Unset):
            ipv_4_pppoe = UNSET
        else:
            ipv_4_pppoe = VirtualWanIpv4PppoeOpenApiVO.from_dict(_ipv_4_pppoe)

        _ipv_4_pppoa = d.pop("ipv4Pppoa", UNSET)
        ipv_4_pppoa: VirtualWanIpv4PppoaOpenApiVO | Unset
        if isinstance(_ipv_4_pppoa, Unset):
            ipv_4_pppoa = UNSET
        else:
            ipv_4_pppoa = VirtualWanIpv4PppoaOpenApiVO.from_dict(_ipv_4_pppoa)

        _ipv_4_ipoa = d.pop("ipv4Ipoa", UNSET)
        ipv_4_ipoa: VirtualWanIpv4IpoaOpenApiVO | Unset
        if isinstance(_ipv_4_ipoa, Unset):
            ipv_4_ipoa = UNSET
        else:
            ipv_4_ipoa = VirtualWanIpv4IpoaOpenApiVO.from_dict(_ipv_4_ipoa)

        virtual_wan_ipv_4_setting_config_open_api_vo = cls(
            proto=proto,
            vlan_id=vlan_id,
            qos_tag_enable=qos_tag_enable,
            vlan_priority=vlan_priority,
            qos_tag=qos_tag,
            ipv_4_static=ipv_4_static,
            ipv_4_dhcp=ipv_4_dhcp,
            ipv_4_pppoe=ipv_4_pppoe,
            ipv_4_pppoa=ipv_4_pppoa,
            ipv_4_ipoa=ipv_4_ipoa,
        )

        virtual_wan_ipv_4_setting_config_open_api_vo.additional_properties = d
        return virtual_wan_ipv_4_setting_config_open_api_vo

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
