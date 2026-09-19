from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dynamic_ipv_6_setting_entity import DynamicIpv6SettingEntity
    from ..models.static_ipv_6_setting_entity import StaticIpv6SettingEntity


T = TypeVar("T", bound="ApIPv6Setting")


@_attrs_define
class ApIPv6Setting:
    """
    Attributes:
        ipv_6_enable (bool): ipv6 enable
        mode (str | Unset): Mode should be a value as follows: static; dynamic
        dynamic_ipv_6_setting (DynamicIpv6SettingEntity | Unset): Dynamic Ipv6 Setting(SLAAC/DHCPv6)
        static_ipv_6_setting (StaticIpv6SettingEntity | Unset): Static Ipv6 Setting
    """

    ipv_6_enable: bool
    mode: str | Unset = UNSET
    dynamic_ipv_6_setting: DynamicIpv6SettingEntity | Unset = UNSET
    static_ipv_6_setting: StaticIpv6SettingEntity | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ipv_6_enable = self.ipv_6_enable

        mode = self.mode

        dynamic_ipv_6_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dynamic_ipv_6_setting, Unset):
            dynamic_ipv_6_setting = self.dynamic_ipv_6_setting.to_dict()

        static_ipv_6_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.static_ipv_6_setting, Unset):
            static_ipv_6_setting = self.static_ipv_6_setting.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ipv6Enable": ipv_6_enable,
            }
        )
        if mode is not UNSET:
            field_dict["mode"] = mode
        if dynamic_ipv_6_setting is not UNSET:
            field_dict["dynamicIpv6Setting"] = dynamic_ipv_6_setting
        if static_ipv_6_setting is not UNSET:
            field_dict["staticIpv6Setting"] = static_ipv_6_setting

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.dynamic_ipv_6_setting_entity import (
            DynamicIpv6SettingEntity,
        )
        from ..models.static_ipv_6_setting_entity import (
            StaticIpv6SettingEntity,
        )

        d = dict(src_dict)
        ipv_6_enable = d.pop("ipv6Enable")

        mode = d.pop("mode", UNSET)

        _dynamic_ipv_6_setting = d.pop("dynamicIpv6Setting", UNSET)
        dynamic_ipv_6_setting: DynamicIpv6SettingEntity | Unset
        if isinstance(_dynamic_ipv_6_setting, Unset):
            dynamic_ipv_6_setting = UNSET
        else:
            dynamic_ipv_6_setting = DynamicIpv6SettingEntity.from_dict(
                _dynamic_ipv_6_setting
            )

        _static_ipv_6_setting = d.pop("staticIpv6Setting", UNSET)
        static_ipv_6_setting: StaticIpv6SettingEntity | Unset
        if isinstance(_static_ipv_6_setting, Unset):
            static_ipv_6_setting = UNSET
        else:
            static_ipv_6_setting = StaticIpv6SettingEntity.from_dict(
                _static_ipv_6_setting
            )

        ap_i_pv_6_setting = cls(
            ipv_6_enable=ipv_6_enable,
            mode=mode,
            dynamic_ipv_6_setting=dynamic_ipv_6_setting,
            static_ipv_6_setting=static_ipv_6_setting,
        )

        ap_i_pv_6_setting.additional_properties = d
        return ap_i_pv_6_setting

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
