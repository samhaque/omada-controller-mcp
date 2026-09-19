from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_config_result_base_setting_vo import ApConfigResultBaseSettingVO


T = TypeVar("T", bound="ApRadioConfigResultSettingsVO")


@_attrs_define
class ApRadioConfigResultSettingsVO:
    """ap radio config result detail setting.

    Attributes:
        status_setting (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        wireless_mode_setting (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        channel_width_setting (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        channel_setting (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        freq_setting (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        channel_range_setting (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
        tx_power_setting (ApConfigResultBaseSettingVO | Unset): vlan tagged setting config result
    """

    status_setting: ApConfigResultBaseSettingVO | Unset = UNSET
    wireless_mode_setting: ApConfigResultBaseSettingVO | Unset = UNSET
    channel_width_setting: ApConfigResultBaseSettingVO | Unset = UNSET
    channel_setting: ApConfigResultBaseSettingVO | Unset = UNSET
    freq_setting: ApConfigResultBaseSettingVO | Unset = UNSET
    channel_range_setting: ApConfigResultBaseSettingVO | Unset = UNSET
    tx_power_setting: ApConfigResultBaseSettingVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status_setting, Unset):
            status_setting = self.status_setting.to_dict()

        wireless_mode_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wireless_mode_setting, Unset):
            wireless_mode_setting = self.wireless_mode_setting.to_dict()

        channel_width_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.channel_width_setting, Unset):
            channel_width_setting = self.channel_width_setting.to_dict()

        channel_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.channel_setting, Unset):
            channel_setting = self.channel_setting.to_dict()

        freq_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.freq_setting, Unset):
            freq_setting = self.freq_setting.to_dict()

        channel_range_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.channel_range_setting, Unset):
            channel_range_setting = self.channel_range_setting.to_dict()

        tx_power_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tx_power_setting, Unset):
            tx_power_setting = self.tx_power_setting.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status_setting is not UNSET:
            field_dict["statusSetting"] = status_setting
        if wireless_mode_setting is not UNSET:
            field_dict["wirelessModeSetting"] = wireless_mode_setting
        if channel_width_setting is not UNSET:
            field_dict["channelWidthSetting"] = channel_width_setting
        if channel_setting is not UNSET:
            field_dict["channel setting"] = channel_setting
        if freq_setting is not UNSET:
            field_dict["freq setting"] = freq_setting
        if channel_range_setting is not UNSET:
            field_dict["channelRangeSetting"] = channel_range_setting
        if tx_power_setting is not UNSET:
            field_dict["txPowerSetting"] = tx_power_setting

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

        _wireless_mode_setting = d.pop("wirelessModeSetting", UNSET)
        wireless_mode_setting: ApConfigResultBaseSettingVO | Unset
        if isinstance(_wireless_mode_setting, Unset):
            wireless_mode_setting = UNSET
        else:
            wireless_mode_setting = ApConfigResultBaseSettingVO.from_dict(
                _wireless_mode_setting
            )

        _channel_width_setting = d.pop("channelWidthSetting", UNSET)
        channel_width_setting: ApConfigResultBaseSettingVO | Unset
        if isinstance(_channel_width_setting, Unset):
            channel_width_setting = UNSET
        else:
            channel_width_setting = ApConfigResultBaseSettingVO.from_dict(
                _channel_width_setting
            )

        _channel_setting = d.pop("channel setting", UNSET)
        channel_setting: ApConfigResultBaseSettingVO | Unset
        if isinstance(_channel_setting, Unset):
            channel_setting = UNSET
        else:
            channel_setting = ApConfigResultBaseSettingVO.from_dict(_channel_setting)

        _freq_setting = d.pop("freq setting", UNSET)
        freq_setting: ApConfigResultBaseSettingVO | Unset
        if isinstance(_freq_setting, Unset):
            freq_setting = UNSET
        else:
            freq_setting = ApConfigResultBaseSettingVO.from_dict(_freq_setting)

        _channel_range_setting = d.pop("channelRangeSetting", UNSET)
        channel_range_setting: ApConfigResultBaseSettingVO | Unset
        if isinstance(_channel_range_setting, Unset):
            channel_range_setting = UNSET
        else:
            channel_range_setting = ApConfigResultBaseSettingVO.from_dict(
                _channel_range_setting
            )

        _tx_power_setting = d.pop("txPowerSetting", UNSET)
        tx_power_setting: ApConfigResultBaseSettingVO | Unset
        if isinstance(_tx_power_setting, Unset):
            tx_power_setting = UNSET
        else:
            tx_power_setting = ApConfigResultBaseSettingVO.from_dict(_tx_power_setting)

        ap_radio_config_result_settings_vo = cls(
            status_setting=status_setting,
            wireless_mode_setting=wireless_mode_setting,
            channel_width_setting=channel_width_setting,
            channel_setting=channel_setting,
            freq_setting=freq_setting,
            channel_range_setting=channel_range_setting,
            tx_power_setting=tx_power_setting,
        )

        ap_radio_config_result_settings_vo.additional_properties = d
        return ap_radio_config_result_settings_vo

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
