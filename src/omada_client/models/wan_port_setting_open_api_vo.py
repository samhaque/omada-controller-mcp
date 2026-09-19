from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wan_port_dsl_setting_open_api_vo import WanPortDslSettingOpenApiVO
    from ..models.wan_port_ipv_4_setting_open_api_vo import WanPortIpv4SettingOpenApiVO
    from ..models.wan_port_ipv_6_setting_open_api_vo import WanPortIpv6SettingOpenApiVO
    from ..models.wan_port_mac_setting_open_api_vo import WanPortMacSettingOpenApiVO


T = TypeVar("T", bound="WanPortSettingOpenApiVO")


@_attrs_define
class WanPortSettingOpenApiVO:
    """WAN ports config

    Attributes:
        port_id (str): Port ID
        wan_port_ipv_4_setting (WanPortIpv4SettingOpenApiVO): Port IPv4 setting
        wan_port_ipv_6_setting (WanPortIpv6SettingOpenApiVO): Port IPv6 setting
        wan_port_mac_setting (WanPortMacSettingOpenApiVO): Port MAC setting
        port_name (str | Unset): Port name
        port_description (str | Unset): Port description should contain 1 to 32 characters.
        dsl_setting (WanPortDslSettingOpenApiVO | Unset): DSL settings. Only for DSL WAN.
    """

    port_id: str
    wan_port_ipv_4_setting: WanPortIpv4SettingOpenApiVO
    wan_port_ipv_6_setting: WanPortIpv6SettingOpenApiVO
    wan_port_mac_setting: WanPortMacSettingOpenApiVO
    port_name: str | Unset = UNSET
    port_description: str | Unset = UNSET
    dsl_setting: WanPortDslSettingOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_id = self.port_id

        wan_port_ipv_4_setting = self.wan_port_ipv_4_setting.to_dict()

        wan_port_ipv_6_setting = self.wan_port_ipv_6_setting.to_dict()

        wan_port_mac_setting = self.wan_port_mac_setting.to_dict()

        port_name = self.port_name

        port_description = self.port_description

        dsl_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dsl_setting, Unset):
            dsl_setting = self.dsl_setting.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "portId": port_id,
                "wanPortIpv4Setting": wan_port_ipv_4_setting,
                "wanPortIpv6Setting": wan_port_ipv_6_setting,
                "wanPortMacSetting": wan_port_mac_setting,
            }
        )
        if port_name is not UNSET:
            field_dict["portName"] = port_name
        if port_description is not UNSET:
            field_dict["portDescription"] = port_description
        if dsl_setting is not UNSET:
            field_dict["dslSetting"] = dsl_setting

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.wan_port_dsl_setting_open_api_vo import (
            WanPortDslSettingOpenApiVO,
        )
        from ..models.wan_port_ipv_4_setting_open_api_vo import (
            WanPortIpv4SettingOpenApiVO,
        )
        from ..models.wan_port_ipv_6_setting_open_api_vo import (
            WanPortIpv6SettingOpenApiVO,
        )
        from ..models.wan_port_mac_setting_open_api_vo import (
            WanPortMacSettingOpenApiVO,
        )

        d = dict(src_dict)
        port_id = d.pop("portId")

        wan_port_ipv_4_setting = WanPortIpv4SettingOpenApiVO.from_dict(
            d.pop("wanPortIpv4Setting")
        )

        wan_port_ipv_6_setting = WanPortIpv6SettingOpenApiVO.from_dict(
            d.pop("wanPortIpv6Setting")
        )

        wan_port_mac_setting = WanPortMacSettingOpenApiVO.from_dict(
            d.pop("wanPortMacSetting")
        )

        port_name = d.pop("portName", UNSET)

        port_description = d.pop("portDescription", UNSET)

        _dsl_setting = d.pop("dslSetting", UNSET)
        dsl_setting: WanPortDslSettingOpenApiVO | Unset
        if isinstance(_dsl_setting, Unset):
            dsl_setting = UNSET
        else:
            dsl_setting = WanPortDslSettingOpenApiVO.from_dict(_dsl_setting)

        wan_port_setting_open_api_vo = cls(
            port_id=port_id,
            wan_port_ipv_4_setting=wan_port_ipv_4_setting,
            wan_port_ipv_6_setting=wan_port_ipv_6_setting,
            wan_port_mac_setting=wan_port_mac_setting,
            port_name=port_name,
            port_description=port_description,
            dsl_setting=dsl_setting,
        )

        wan_port_setting_open_api_vo.additional_properties = d
        return wan_port_setting_open_api_vo

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
