from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.virtual_wan_dsl_open_api_vo import VirtualWanDslOpenApiVO
    from ..models.virtual_wan_ipv_4_setting_config_open_api_vo import (
        VirtualWanIpv4SettingConfigOpenApiVO,
    )
    from ..models.virtual_wan_mac_setting_open_api_vo import (
        VirtualWanMacSettingOpenApiVO,
    )


T = TypeVar("T", bound="VirtualWanConfigOpenApiVO")


@_attrs_define
class VirtualWanConfigOpenApiVO:
    """VirtualWanConfig

    Attributes:
        name (str): Virtual WAN name should contain 1 to 128 characters. Only letters, digits and underscores are
            allowed.
        physical_wan_id (str): Physical WAN ID. Physical WAN ID can be obtained from 'Get internet basic info'
            interface. Physical WAN ID. Physical WAN ID can be obtained from 'Get internet basic info' interface. Only DSL
            WAN, Ethernet WAN, and SFP WAN support virtual WAN configuration.
        virtual_wan_ipv_4_setting (VirtualWanIpv4SettingConfigOpenApiVO): VirtualWanIpv4SettingConfigOpenApiVO
        virtual_wan_dsl (VirtualWanDslOpenApiVO | Unset): VirtualWanDslOpenApiVO
        wan_port_mac_setting (VirtualWanMacSettingOpenApiVO | Unset): VirtualWanMacSettingOpenApiVO
    """

    name: str
    physical_wan_id: str
    virtual_wan_ipv_4_setting: VirtualWanIpv4SettingConfigOpenApiVO
    virtual_wan_dsl: VirtualWanDslOpenApiVO | Unset = UNSET
    wan_port_mac_setting: VirtualWanMacSettingOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        physical_wan_id = self.physical_wan_id

        virtual_wan_ipv_4_setting = self.virtual_wan_ipv_4_setting.to_dict()

        virtual_wan_dsl: dict[str, Any] | Unset = UNSET
        if not isinstance(self.virtual_wan_dsl, Unset):
            virtual_wan_dsl = self.virtual_wan_dsl.to_dict()

        wan_port_mac_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wan_port_mac_setting, Unset):
            wan_port_mac_setting = self.wan_port_mac_setting.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "physicalWanId": physical_wan_id,
                "virtualWanIpv4Setting": virtual_wan_ipv_4_setting,
            }
        )
        if virtual_wan_dsl is not UNSET:
            field_dict["virtualWanDsl"] = virtual_wan_dsl
        if wan_port_mac_setting is not UNSET:
            field_dict["wanPortMacSetting"] = wan_port_mac_setting

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.virtual_wan_dsl_open_api_vo import (
            VirtualWanDslOpenApiVO,
        )
        from ..models.virtual_wan_ipv_4_setting_config_open_api_vo import (
            VirtualWanIpv4SettingConfigOpenApiVO,
        )
        from ..models.virtual_wan_mac_setting_open_api_vo import (
            VirtualWanMacSettingOpenApiVO,
        )

        d = dict(src_dict)
        name = d.pop("name")

        physical_wan_id = d.pop("physicalWanId")

        virtual_wan_ipv_4_setting = VirtualWanIpv4SettingConfigOpenApiVO.from_dict(
            d.pop("virtualWanIpv4Setting")
        )

        _virtual_wan_dsl = d.pop("virtualWanDsl", UNSET)
        virtual_wan_dsl: VirtualWanDslOpenApiVO | Unset
        if isinstance(_virtual_wan_dsl, Unset):
            virtual_wan_dsl = UNSET
        else:
            virtual_wan_dsl = VirtualWanDslOpenApiVO.from_dict(_virtual_wan_dsl)

        _wan_port_mac_setting = d.pop("wanPortMacSetting", UNSET)
        wan_port_mac_setting: VirtualWanMacSettingOpenApiVO | Unset
        if isinstance(_wan_port_mac_setting, Unset):
            wan_port_mac_setting = UNSET
        else:
            wan_port_mac_setting = VirtualWanMacSettingOpenApiVO.from_dict(
                _wan_port_mac_setting
            )

        virtual_wan_config_open_api_vo = cls(
            name=name,
            physical_wan_id=physical_wan_id,
            virtual_wan_ipv_4_setting=virtual_wan_ipv_4_setting,
            virtual_wan_dsl=virtual_wan_dsl,
            wan_port_mac_setting=wan_port_mac_setting,
        )

        virtual_wan_config_open_api_vo.additional_properties = d
        return virtual_wan_config_open_api_vo

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
