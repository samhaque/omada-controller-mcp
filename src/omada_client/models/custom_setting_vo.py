from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.planning_advanced_setting_vo import PlanningAdvancedSettingVO


T = TypeVar("T", bound="CustomSettingVO")


@_attrs_define
class CustomSettingVO:
    """Custom setting. Cannot be null when parameter [mode] is 1.

    Attributes:
        channel_deploy_enable (bool): Whether to enable channel deployment.
        channel_width_deploy_enable (bool): Whether to enable channel width deployment.
        band_deploy_enable (bool): Whether to enable band deployment.
        power_adjust_enable (bool): Whether to enable power adjustment.
        advanced_setting (PlanningAdvancedSettingVO | Unset):
    """

    channel_deploy_enable: bool
    channel_width_deploy_enable: bool
    band_deploy_enable: bool
    power_adjust_enable: bool
    advanced_setting: PlanningAdvancedSettingVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel_deploy_enable = self.channel_deploy_enable

        channel_width_deploy_enable = self.channel_width_deploy_enable

        band_deploy_enable = self.band_deploy_enable

        power_adjust_enable = self.power_adjust_enable

        advanced_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.advanced_setting, Unset):
            advanced_setting = self.advanced_setting.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channelDeployEnable": channel_deploy_enable,
                "channelWidthDeployEnable": channel_width_deploy_enable,
                "bandDeployEnable": band_deploy_enable,
                "powerAdjustEnable": power_adjust_enable,
            }
        )
        if advanced_setting is not UNSET:
            field_dict["advancedSetting"] = advanced_setting

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.planning_advanced_setting_vo import (
            PlanningAdvancedSettingVO,
        )

        d = dict(src_dict)
        channel_deploy_enable = d.pop("channelDeployEnable")

        channel_width_deploy_enable = d.pop("channelWidthDeployEnable")

        band_deploy_enable = d.pop("bandDeployEnable")

        power_adjust_enable = d.pop("powerAdjustEnable")

        _advanced_setting = d.pop("advancedSetting", UNSET)
        advanced_setting: PlanningAdvancedSettingVO | Unset
        if isinstance(_advanced_setting, Unset):
            advanced_setting = UNSET
        else:
            advanced_setting = PlanningAdvancedSettingVO.from_dict(_advanced_setting)

        custom_setting_vo = cls(
            channel_deploy_enable=channel_deploy_enable,
            channel_width_deploy_enable=channel_width_deploy_enable,
            band_deploy_enable=band_deploy_enable,
            power_adjust_enable=power_adjust_enable,
            advanced_setting=advanced_setting,
        )

        custom_setting_vo.additional_properties = d
        return custom_setting_vo

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
