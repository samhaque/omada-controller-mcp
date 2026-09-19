from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ant_switch_radio_config import AntSwitchRadioConfig


T = TypeVar("T", bound="UpdateApAntSwitchConfig")


@_attrs_define
class UpdateApAntSwitchConfig:
    """
    Attributes:
        ant_mode (int | Unset): Antenna Mode. 0: Auto, 1: built-In, 2: Omni, 3: Custom
        ant_setting_2_g (AntSwitchRadioConfig | Unset):
        ant_setting_5_g (AntSwitchRadioConfig | Unset):
        ant_setting_5_g_2 (AntSwitchRadioConfig | Unset):
        ant_setting_6_g (AntSwitchRadioConfig | Unset):
    """

    ant_mode: int | Unset = UNSET
    ant_setting_2_g: AntSwitchRadioConfig | Unset = UNSET
    ant_setting_5_g: AntSwitchRadioConfig | Unset = UNSET
    ant_setting_5_g_2: AntSwitchRadioConfig | Unset = UNSET
    ant_setting_6_g: AntSwitchRadioConfig | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ant_mode = self.ant_mode

        ant_setting_2_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ant_setting_2_g, Unset):
            ant_setting_2_g = self.ant_setting_2_g.to_dict()

        ant_setting_5_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ant_setting_5_g, Unset):
            ant_setting_5_g = self.ant_setting_5_g.to_dict()

        ant_setting_5_g_2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ant_setting_5_g_2, Unset):
            ant_setting_5_g_2 = self.ant_setting_5_g_2.to_dict()

        ant_setting_6_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ant_setting_6_g, Unset):
            ant_setting_6_g = self.ant_setting_6_g.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ant_mode is not UNSET:
            field_dict["antMode"] = ant_mode
        if ant_setting_2_g is not UNSET:
            field_dict["antSetting2g"] = ant_setting_2_g
        if ant_setting_5_g is not UNSET:
            field_dict["antSetting5g"] = ant_setting_5_g
        if ant_setting_5_g_2 is not UNSET:
            field_dict["antSetting5g2"] = ant_setting_5_g_2
        if ant_setting_6_g is not UNSET:
            field_dict["antSetting6g"] = ant_setting_6_g

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ant_switch_radio_config import (
            AntSwitchRadioConfig,
        )

        d = dict(src_dict)
        ant_mode = d.pop("antMode", UNSET)

        _ant_setting_2_g = d.pop("antSetting2g", UNSET)
        ant_setting_2_g: AntSwitchRadioConfig | Unset
        if isinstance(_ant_setting_2_g, Unset):
            ant_setting_2_g = UNSET
        else:
            ant_setting_2_g = AntSwitchRadioConfig.from_dict(_ant_setting_2_g)

        _ant_setting_5_g = d.pop("antSetting5g", UNSET)
        ant_setting_5_g: AntSwitchRadioConfig | Unset
        if isinstance(_ant_setting_5_g, Unset):
            ant_setting_5_g = UNSET
        else:
            ant_setting_5_g = AntSwitchRadioConfig.from_dict(_ant_setting_5_g)

        _ant_setting_5_g_2 = d.pop("antSetting5g2", UNSET)
        ant_setting_5_g_2: AntSwitchRadioConfig | Unset
        if isinstance(_ant_setting_5_g_2, Unset):
            ant_setting_5_g_2 = UNSET
        else:
            ant_setting_5_g_2 = AntSwitchRadioConfig.from_dict(_ant_setting_5_g_2)

        _ant_setting_6_g = d.pop("antSetting6g", UNSET)
        ant_setting_6_g: AntSwitchRadioConfig | Unset
        if isinstance(_ant_setting_6_g, Unset):
            ant_setting_6_g = UNSET
        else:
            ant_setting_6_g = AntSwitchRadioConfig.from_dict(_ant_setting_6_g)

        update_ap_ant_switch_config = cls(
            ant_mode=ant_mode,
            ant_setting_2_g=ant_setting_2_g,
            ant_setting_5_g=ant_setting_5_g,
            ant_setting_5_g_2=ant_setting_5_g_2,
            ant_setting_6_g=ant_setting_6_g,
        )

        update_ap_ant_switch_config.additional_properties = d
        return update_ap_ant_switch_config

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
