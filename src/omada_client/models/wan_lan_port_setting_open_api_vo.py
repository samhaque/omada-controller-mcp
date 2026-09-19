from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="WanLanPortSettingOpenApiVO")


@_attrs_define
class WanLanPortSettingOpenApiVO:
    """
    Attributes:
        port_uuid (str | Unset): port uuid
        port_name (str | Unset): port name
        type_ (int | Unset): 0: WAN, 1: WAN/LAN, 2: LAN
        mode (int | Unset): 0: WAN, 1: LAN
        lan_network_names (list[str] | Unset): names of lan networks
        support_vpn (bool | Unset): support vpn or not, true: support
        support_iptv (bool | Unset): support iptv or not, true: support
        closable (bool | Unset): can this port be closed or not, true: support
        support_internet_vlan (bool | Unset): does this port support vlan or not, true: support
        wan_ipv_6_component (int | Unset): component version of gateway wan ipv6
        support_qos_tag_enable (bool | Unset): does this port support qos tage enable
        status (int | Unset): whether to open this port
    """

    port_uuid: str | Unset = UNSET
    port_name: str | Unset = UNSET
    type_: int | Unset = UNSET
    mode: int | Unset = UNSET
    lan_network_names: list[str] | Unset = UNSET
    support_vpn: bool | Unset = UNSET
    support_iptv: bool | Unset = UNSET
    closable: bool | Unset = UNSET
    support_internet_vlan: bool | Unset = UNSET
    wan_ipv_6_component: int | Unset = UNSET
    support_qos_tag_enable: bool | Unset = UNSET
    status: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_uuid = self.port_uuid

        port_name = self.port_name

        type_ = self.type_

        mode = self.mode

        lan_network_names: list[str] | Unset = UNSET
        if not isinstance(self.lan_network_names, Unset):
            lan_network_names = self.lan_network_names

        support_vpn = self.support_vpn

        support_iptv = self.support_iptv

        closable = self.closable

        support_internet_vlan = self.support_internet_vlan

        wan_ipv_6_component = self.wan_ipv_6_component

        support_qos_tag_enable = self.support_qos_tag_enable

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port_uuid is not UNSET:
            field_dict["portUuid"] = port_uuid
        if port_name is not UNSET:
            field_dict["portName"] = port_name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if mode is not UNSET:
            field_dict["mode"] = mode
        if lan_network_names is not UNSET:
            field_dict["lanNetworkNames"] = lan_network_names
        if support_vpn is not UNSET:
            field_dict["supportVpn"] = support_vpn
        if support_iptv is not UNSET:
            field_dict["supportIptv"] = support_iptv
        if closable is not UNSET:
            field_dict["closable"] = closable
        if support_internet_vlan is not UNSET:
            field_dict["supportInternetVlan"] = support_internet_vlan
        if wan_ipv_6_component is not UNSET:
            field_dict["wanIpv6Component"] = wan_ipv_6_component
        if support_qos_tag_enable is not UNSET:
            field_dict["supportQosTagEnable"] = support_qos_tag_enable
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port_uuid = d.pop("portUuid", UNSET)

        port_name = d.pop("portName", UNSET)

        type_ = d.pop("type", UNSET)

        mode = d.pop("mode", UNSET)

        lan_network_names = cast(list[str], d.pop("lanNetworkNames", UNSET))

        support_vpn = d.pop("supportVpn", UNSET)

        support_iptv = d.pop("supportIptv", UNSET)

        closable = d.pop("closable", UNSET)

        support_internet_vlan = d.pop("supportInternetVlan", UNSET)

        wan_ipv_6_component = d.pop("wanIpv6Component", UNSET)

        support_qos_tag_enable = d.pop("supportQosTagEnable", UNSET)

        status = d.pop("status", UNSET)

        wan_lan_port_setting_open_api_vo = cls(
            port_uuid=port_uuid,
            port_name=port_name,
            type_=type_,
            mode=mode,
            lan_network_names=lan_network_names,
            support_vpn=support_vpn,
            support_iptv=support_iptv,
            closable=closable,
            support_internet_vlan=support_internet_vlan,
            wan_ipv_6_component=wan_ipv_6_component,
            support_qos_tag_enable=support_qos_tag_enable,
            status=status,
        )

        wan_lan_port_setting_open_api_vo.additional_properties = d
        return wan_lan_port_setting_open_api_vo

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
