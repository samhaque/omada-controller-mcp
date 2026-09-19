from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.virtual_wan_ipv_4_dhcp_open_api_vo import VirtualWanIpv4DhcpOpenApiVO
    from ..models.virtual_wan_ipv_4_pppoe_open_api_vo import (
        VirtualWanIpv4PppoeOpenApiVO,
    )
    from ..models.virtual_wan_ipv_4_static_open_api_vo import (
        VirtualWanIpv4StaticOpenApiVO,
    )


T = TypeVar("T", bound="VirtualWanIpv4SettingInfoOpenApiVO")


@_attrs_define
class VirtualWanIpv4SettingInfoOpenApiVO:
    """VirtualWanIpv4SettingInfo

    Attributes:
        proto (str | Unset): Virtual WAN IPv4 connection type.
        proto_type (int | Unset): Virtual WAN IPv4 proto type, 0:static; 1:DHCP; 2:PPPoE.
        vlan_id (int | Unset): Vlan ID.
        vlan_priority (int | Unset): Vlan Priority.
        support_internet_vlan (bool | Unset): Whether support internet vlan.
        support_qos_tag_enable (bool | Unset): Whether support Qos Tag enable.
        qos_tag_enable (bool | Unset): Whether Qos Tag is enable.
        qos_tag (int | Unset): Qos Tag.
        ipv_4_static (VirtualWanIpv4StaticOpenApiVO | Unset): VirtualWanIpv4StaticOpenApiVO
        ipv_4_dhcp (VirtualWanIpv4DhcpOpenApiVO | Unset): VirtualWanIpv4DhcpOpenApiVO
        ipv_4_pppoe (VirtualWanIpv4PppoeOpenApiVO | Unset): VirtualWanIpv4PppoeOpenApiVO
    """

    proto: str | Unset = UNSET
    proto_type: int | Unset = UNSET
    vlan_id: int | Unset = UNSET
    vlan_priority: int | Unset = UNSET
    support_internet_vlan: bool | Unset = UNSET
    support_qos_tag_enable: bool | Unset = UNSET
    qos_tag_enable: bool | Unset = UNSET
    qos_tag: int | Unset = UNSET
    ipv_4_static: VirtualWanIpv4StaticOpenApiVO | Unset = UNSET
    ipv_4_dhcp: VirtualWanIpv4DhcpOpenApiVO | Unset = UNSET
    ipv_4_pppoe: VirtualWanIpv4PppoeOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        proto = self.proto

        proto_type = self.proto_type

        vlan_id = self.vlan_id

        vlan_priority = self.vlan_priority

        support_internet_vlan = self.support_internet_vlan

        support_qos_tag_enable = self.support_qos_tag_enable

        qos_tag_enable = self.qos_tag_enable

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if proto is not UNSET:
            field_dict["proto"] = proto
        if proto_type is not UNSET:
            field_dict["protoType"] = proto_type
        if vlan_id is not UNSET:
            field_dict["vlanId"] = vlan_id
        if vlan_priority is not UNSET:
            field_dict["vlanPriority"] = vlan_priority
        if support_internet_vlan is not UNSET:
            field_dict["supportInternetVlan"] = support_internet_vlan
        if support_qos_tag_enable is not UNSET:
            field_dict["supportQosTagEnable"] = support_qos_tag_enable
        if qos_tag_enable is not UNSET:
            field_dict["qosTagEnable"] = qos_tag_enable
        if qos_tag is not UNSET:
            field_dict["qosTag"] = qos_tag
        if ipv_4_static is not UNSET:
            field_dict["ipv4Static"] = ipv_4_static
        if ipv_4_dhcp is not UNSET:
            field_dict["ipv4Dhcp"] = ipv_4_dhcp
        if ipv_4_pppoe is not UNSET:
            field_dict["ipv4Pppoe"] = ipv_4_pppoe

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.virtual_wan_ipv_4_dhcp_open_api_vo import (
            VirtualWanIpv4DhcpOpenApiVO,
        )
        from ..models.virtual_wan_ipv_4_pppoe_open_api_vo import (
            VirtualWanIpv4PppoeOpenApiVO,
        )
        from ..models.virtual_wan_ipv_4_static_open_api_vo import (
            VirtualWanIpv4StaticOpenApiVO,
        )

        d = dict(src_dict)
        proto = d.pop("proto", UNSET)

        proto_type = d.pop("protoType", UNSET)

        vlan_id = d.pop("vlanId", UNSET)

        vlan_priority = d.pop("vlanPriority", UNSET)

        support_internet_vlan = d.pop("supportInternetVlan", UNSET)

        support_qos_tag_enable = d.pop("supportQosTagEnable", UNSET)

        qos_tag_enable = d.pop("qosTagEnable", UNSET)

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

        virtual_wan_ipv_4_setting_info_open_api_vo = cls(
            proto=proto,
            proto_type=proto_type,
            vlan_id=vlan_id,
            vlan_priority=vlan_priority,
            support_internet_vlan=support_internet_vlan,
            support_qos_tag_enable=support_qos_tag_enable,
            qos_tag_enable=qos_tag_enable,
            qos_tag=qos_tag,
            ipv_4_static=ipv_4_static,
            ipv_4_dhcp=ipv_4_dhcp,
            ipv_4_pppoe=ipv_4_pppoe,
        )

        virtual_wan_ipv_4_setting_info_open_api_vo.additional_properties = d
        return virtual_wan_ipv_4_setting_info_open_api_vo

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
