from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ipv_4_dhcp_open_api_vo import Ipv4DhcpOpenApiVO
    from ..models.ipv_4_ds_lite_open_api_vo import Ipv4DsLiteOpenApiVO
    from ..models.ipv_4_ipoa_open_api_vo import Ipv4IpoaOpenApiVO
    from ..models.ipv_4_map_e_open_api_vo import Ipv4MapEOpenApiVO
    from ..models.ipv_4_pppoa_open_api_vo import Ipv4PppoaOpenApiVO
    from ..models.ipv_4_pppoe_open_api_vo import Ipv4PppoeOpenApiVO
    from ..models.ipv_4_pptp_open_api_vo import Ipv4PptpOpenApiVO
    from ..models.ipv_4_static_open_api_vo import Ipv4StaticOpenApiVO
    from ..models.ipv_4l2_tp_open_api_vo import Ipv4L2TpOpenApiVO


T = TypeVar("T", bound="WanPortIpv4SettingOpenApiVO")


@_attrs_define
class WanPortIpv4SettingOpenApiVO:
    """Port IPv4 setting

    Attributes:
        proto_type (int): IPv4 connection type should be one of the following values: 0:static; 1:DHCP; 2:PPPoE; 3:L2TP;
            4:PPTP; 5:DS-Lite; 6:MAP-E.
        vlan_id (int): VLAN ID should be within the range of 0–4094, 0 means disable.
        qos_tag_enable (bool): 802.1Q Tag. It takes effect when [vlanId] is not 0.
        vlan_priority (int | Unset): Vlan Priority. It takes effect when [vlanId] is not 0, and it should be within the
            range of 0–7.
        ipv_4_static (Ipv4StaticOpenApiVO | Unset): It is required when [protoType] is 0.
        ipv_4_dhcp (Ipv4DhcpOpenApiVO | Unset): It is required when [protoType] is 1.
        ipv_4_pppoe (Ipv4PppoeOpenApiVO | Unset): It is required when [protoType] is 2.
        ipv_4l2_tp (Ipv4L2TpOpenApiVO | Unset): It is required when [protoType] is 3.
        ipv_4_pptp (Ipv4PptpOpenApiVO | Unset): It is required when [protoType] is 4.
        ipv_4_dslite (Ipv4DsLiteOpenApiVO | Unset): It is required when [protoType] is 5.
        ipv_4_mape (Ipv4MapEOpenApiVO | Unset): It is required when [protoType] is 6.
        ipv_4_pppoa (Ipv4PppoaOpenApiVO | Unset): It is required when [protoType] is 7.
        ipv_4_ipoa (Ipv4IpoaOpenApiVO | Unset): It is required when [protoType] is 8.
    """

    proto_type: int
    vlan_id: int
    qos_tag_enable: bool
    vlan_priority: int | Unset = UNSET
    ipv_4_static: Ipv4StaticOpenApiVO | Unset = UNSET
    ipv_4_dhcp: Ipv4DhcpOpenApiVO | Unset = UNSET
    ipv_4_pppoe: Ipv4PppoeOpenApiVO | Unset = UNSET
    ipv_4l2_tp: Ipv4L2TpOpenApiVO | Unset = UNSET
    ipv_4_pptp: Ipv4PptpOpenApiVO | Unset = UNSET
    ipv_4_dslite: Ipv4DsLiteOpenApiVO | Unset = UNSET
    ipv_4_mape: Ipv4MapEOpenApiVO | Unset = UNSET
    ipv_4_pppoa: Ipv4PppoaOpenApiVO | Unset = UNSET
    ipv_4_ipoa: Ipv4IpoaOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        proto_type = self.proto_type

        vlan_id = self.vlan_id

        qos_tag_enable = self.qos_tag_enable

        vlan_priority = self.vlan_priority

        ipv_4_static: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ipv_4_static, Unset):
            ipv_4_static = self.ipv_4_static.to_dict()

        ipv_4_dhcp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ipv_4_dhcp, Unset):
            ipv_4_dhcp = self.ipv_4_dhcp.to_dict()

        ipv_4_pppoe: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ipv_4_pppoe, Unset):
            ipv_4_pppoe = self.ipv_4_pppoe.to_dict()

        ipv_4l2_tp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ipv_4l2_tp, Unset):
            ipv_4l2_tp = self.ipv_4l2_tp.to_dict()

        ipv_4_pptp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ipv_4_pptp, Unset):
            ipv_4_pptp = self.ipv_4_pptp.to_dict()

        ipv_4_dslite: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ipv_4_dslite, Unset):
            ipv_4_dslite = self.ipv_4_dslite.to_dict()

        ipv_4_mape: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ipv_4_mape, Unset):
            ipv_4_mape = self.ipv_4_mape.to_dict()

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
                "protoType": proto_type,
                "vlanId": vlan_id,
                "qosTagEnable": qos_tag_enable,
            }
        )
        if vlan_priority is not UNSET:
            field_dict["vlanPriority"] = vlan_priority
        if ipv_4_static is not UNSET:
            field_dict["ipv4Static"] = ipv_4_static
        if ipv_4_dhcp is not UNSET:
            field_dict["ipv4Dhcp"] = ipv_4_dhcp
        if ipv_4_pppoe is not UNSET:
            field_dict["ipv4Pppoe"] = ipv_4_pppoe
        if ipv_4l2_tp is not UNSET:
            field_dict["ipv4L2tp"] = ipv_4l2_tp
        if ipv_4_pptp is not UNSET:
            field_dict["ipv4Pptp"] = ipv_4_pptp
        if ipv_4_dslite is not UNSET:
            field_dict["ipv4Dslite"] = ipv_4_dslite
        if ipv_4_mape is not UNSET:
            field_dict["ipv4Mape"] = ipv_4_mape
        if ipv_4_pppoa is not UNSET:
            field_dict["ipv4Pppoa"] = ipv_4_pppoa
        if ipv_4_ipoa is not UNSET:
            field_dict["ipv4Ipoa"] = ipv_4_ipoa

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ipv_4_dhcp_open_api_vo import Ipv4DhcpOpenApiVO
        from ..models.ipv_4_ds_lite_open_api_vo import (
            Ipv4DsLiteOpenApiVO,
        )
        from ..models.ipv_4_ipoa_open_api_vo import Ipv4IpoaOpenApiVO
        from ..models.ipv_4_map_e_open_api_vo import Ipv4MapEOpenApiVO
        from ..models.ipv_4_pppoa_open_api_vo import Ipv4PppoaOpenApiVO
        from ..models.ipv_4_pppoe_open_api_vo import Ipv4PppoeOpenApiVO
        from ..models.ipv_4_pptp_open_api_vo import Ipv4PptpOpenApiVO
        from ..models.ipv_4_static_open_api_vo import (
            Ipv4StaticOpenApiVO,
        )
        from ..models.ipv_4l2_tp_open_api_vo import Ipv4L2TpOpenApiVO

        d = dict(src_dict)
        proto_type = d.pop("protoType")

        vlan_id = d.pop("vlanId")

        qos_tag_enable = d.pop("qosTagEnable")

        vlan_priority = d.pop("vlanPriority", UNSET)

        _ipv_4_static = d.pop("ipv4Static", UNSET)
        ipv_4_static: Ipv4StaticOpenApiVO | Unset
        if isinstance(_ipv_4_static, Unset):
            ipv_4_static = UNSET
        else:
            ipv_4_static = Ipv4StaticOpenApiVO.from_dict(_ipv_4_static)

        _ipv_4_dhcp = d.pop("ipv4Dhcp", UNSET)
        ipv_4_dhcp: Ipv4DhcpOpenApiVO | Unset
        if isinstance(_ipv_4_dhcp, Unset):
            ipv_4_dhcp = UNSET
        else:
            ipv_4_dhcp = Ipv4DhcpOpenApiVO.from_dict(_ipv_4_dhcp)

        _ipv_4_pppoe = d.pop("ipv4Pppoe", UNSET)
        ipv_4_pppoe: Ipv4PppoeOpenApiVO | Unset
        if isinstance(_ipv_4_pppoe, Unset):
            ipv_4_pppoe = UNSET
        else:
            ipv_4_pppoe = Ipv4PppoeOpenApiVO.from_dict(_ipv_4_pppoe)

        _ipv_4l2_tp = d.pop("ipv4L2tp", UNSET)
        ipv_4l2_tp: Ipv4L2TpOpenApiVO | Unset
        if isinstance(_ipv_4l2_tp, Unset):
            ipv_4l2_tp = UNSET
        else:
            ipv_4l2_tp = Ipv4L2TpOpenApiVO.from_dict(_ipv_4l2_tp)

        _ipv_4_pptp = d.pop("ipv4Pptp", UNSET)
        ipv_4_pptp: Ipv4PptpOpenApiVO | Unset
        if isinstance(_ipv_4_pptp, Unset):
            ipv_4_pptp = UNSET
        else:
            ipv_4_pptp = Ipv4PptpOpenApiVO.from_dict(_ipv_4_pptp)

        _ipv_4_dslite = d.pop("ipv4Dslite", UNSET)
        ipv_4_dslite: Ipv4DsLiteOpenApiVO | Unset
        if isinstance(_ipv_4_dslite, Unset):
            ipv_4_dslite = UNSET
        else:
            ipv_4_dslite = Ipv4DsLiteOpenApiVO.from_dict(_ipv_4_dslite)

        _ipv_4_mape = d.pop("ipv4Mape", UNSET)
        ipv_4_mape: Ipv4MapEOpenApiVO | Unset
        if isinstance(_ipv_4_mape, Unset):
            ipv_4_mape = UNSET
        else:
            ipv_4_mape = Ipv4MapEOpenApiVO.from_dict(_ipv_4_mape)

        _ipv_4_pppoa = d.pop("ipv4Pppoa", UNSET)
        ipv_4_pppoa: Ipv4PppoaOpenApiVO | Unset
        if isinstance(_ipv_4_pppoa, Unset):
            ipv_4_pppoa = UNSET
        else:
            ipv_4_pppoa = Ipv4PppoaOpenApiVO.from_dict(_ipv_4_pppoa)

        _ipv_4_ipoa = d.pop("ipv4Ipoa", UNSET)
        ipv_4_ipoa: Ipv4IpoaOpenApiVO | Unset
        if isinstance(_ipv_4_ipoa, Unset):
            ipv_4_ipoa = UNSET
        else:
            ipv_4_ipoa = Ipv4IpoaOpenApiVO.from_dict(_ipv_4_ipoa)

        wan_port_ipv_4_setting_open_api_vo = cls(
            proto_type=proto_type,
            vlan_id=vlan_id,
            qos_tag_enable=qos_tag_enable,
            vlan_priority=vlan_priority,
            ipv_4_static=ipv_4_static,
            ipv_4_dhcp=ipv_4_dhcp,
            ipv_4_pppoe=ipv_4_pppoe,
            ipv_4l2_tp=ipv_4l2_tp,
            ipv_4_pptp=ipv_4_pptp,
            ipv_4_dslite=ipv_4_dslite,
            ipv_4_mape=ipv_4_mape,
            ipv_4_pppoa=ipv_4_pppoa,
            ipv_4_ipoa=ipv_4_ipoa,
        )

        wan_port_ipv_4_setting_open_api_vo.additional_properties = d
        return wan_port_ipv_4_setting_open_api_vo

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
