from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_setting_vo import CustomSettingVO


T = TypeVar("T", bound="RFPlanningDeployConfig")


@_attrs_define
class RFPlanningDeployConfig:
    """
    Attributes:
        mode (int): 0: Auto configuration. 1: Custom configuration.
        custom_setting (CustomSettingVO | Unset): Custom setting. Cannot be null when parameter [mode] is 1.
    """

    mode: int
    custom_setting: CustomSettingVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        custom_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom_setting, Unset):
            custom_setting = self.custom_setting.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
            }
        )
        if custom_setting is not UNSET:
            field_dict["customSetting"] = custom_setting

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.custom_setting_vo import CustomSettingVO

        d = dict(src_dict)
        mode = d.pop("mode")

        _custom_setting = d.pop("customSetting", UNSET)
        custom_setting: CustomSettingVO | Unset
        if isinstance(_custom_setting, Unset):
            custom_setting = UNSET
        else:
            custom_setting = CustomSettingVO.from_dict(_custom_setting)

        rf_planning_deploy_config = cls(
            mode=mode,
            custom_setting=custom_setting,
        )

        rf_planning_deploy_config.additional_properties = d
        return rf_planning_deploy_config

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
