from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_config_result_base_setting_vo import ApConfigResultBaseSettingVO


T = TypeVar("T", bound="ApPortConfigResultSettingsVO")


@_attrs_define
class ApPortConfigResultSettingsVO:
    """ap port config result detail setting.

    Attributes:
        status_setting (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        vlan_setting (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        poe_out_setting (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        band_width_control_setting (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        vlan_tagged_setting (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
    """

    status_setting: ApConfigResultBaseSettingVO | Unset = UNSET
    vlan_setting: ApConfigResultBaseSettingVO | Unset = UNSET
    poe_out_setting: ApConfigResultBaseSettingVO | Unset = UNSET
    band_width_control_setting: ApConfigResultBaseSettingVO | Unset = UNSET
    vlan_tagged_setting: ApConfigResultBaseSettingVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status_setting, Unset):
            status_setting = self.status_setting.to_dict()

        vlan_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vlan_setting, Unset):
            vlan_setting = self.vlan_setting.to_dict()

        poe_out_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.poe_out_setting, Unset):
            poe_out_setting = self.poe_out_setting.to_dict()

        band_width_control_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.band_width_control_setting, Unset):
            band_width_control_setting = self.band_width_control_setting.to_dict()

        vlan_tagged_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vlan_tagged_setting, Unset):
            vlan_tagged_setting = self.vlan_tagged_setting.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status_setting is not UNSET:
            field_dict["statusSetting"] = status_setting
        if vlan_setting is not UNSET:
            field_dict["vlanSetting"] = vlan_setting
        if poe_out_setting is not UNSET:
            field_dict["poeOutSetting"] = poe_out_setting
        if band_width_control_setting is not UNSET:
            field_dict["bandWidthControlSetting"] = band_width_control_setting
        if vlan_tagged_setting is not UNSET:
            field_dict["vlanTaggedSetting"] = vlan_tagged_setting

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_config_result_base_setting_vo import (
            ApConfigResultBaseSettingVO,
        )

        d = dict(src_dict)
        _status_setting = d.pop("statusSetting", UNSET)
        status_setting: ApConfigResultBaseSettingVO | Unset
        if isinstance(_status_setting, Unset):
            status_setting = UNSET
        else:
            status_setting = ApConfigResultBaseSettingVO.from_dict(_status_setting)

        _vlan_setting = d.pop("vlanSetting", UNSET)
        vlan_setting: ApConfigResultBaseSettingVO | Unset
        if isinstance(_vlan_setting, Unset):
            vlan_setting = UNSET
        else:
            vlan_setting = ApConfigResultBaseSettingVO.from_dict(_vlan_setting)

        _poe_out_setting = d.pop("poeOutSetting", UNSET)
        poe_out_setting: ApConfigResultBaseSettingVO | Unset
        if isinstance(_poe_out_setting, Unset):
            poe_out_setting = UNSET
        else:
            poe_out_setting = ApConfigResultBaseSettingVO.from_dict(_poe_out_setting)

        _band_width_control_setting = d.pop("bandWidthControlSetting", UNSET)
        band_width_control_setting: ApConfigResultBaseSettingVO | Unset
        if isinstance(_band_width_control_setting, Unset):
            band_width_control_setting = UNSET
        else:
            band_width_control_setting = ApConfigResultBaseSettingVO.from_dict(
                _band_width_control_setting
            )

        _vlan_tagged_setting = d.pop("vlanTaggedSetting", UNSET)
        vlan_tagged_setting: ApConfigResultBaseSettingVO | Unset
        if isinstance(_vlan_tagged_setting, Unset):
            vlan_tagged_setting = UNSET
        else:
            vlan_tagged_setting = ApConfigResultBaseSettingVO.from_dict(
                _vlan_tagged_setting
            )

        ap_port_config_result_settings_vo = cls(
            status_setting=status_setting,
            vlan_setting=vlan_setting,
            poe_out_setting=poe_out_setting,
            band_width_control_setting=band_width_control_setting,
            vlan_tagged_setting=vlan_tagged_setting,
        )

        ap_port_config_result_settings_vo.additional_properties = d
        return ap_port_config_result_settings_vo

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
