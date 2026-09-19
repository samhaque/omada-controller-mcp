from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dhcp_ip_setting_entity import DhcpIpSettingEntity
    from ..models.static_ip_setting_entity import StaticIpSettingEntity


T = TypeVar("T", bound="ApIPSetting")


@_attrs_define
class ApIPSetting:
    """
    Attributes:
        mode (str): Mode should be a value as follows: Static; DHCP
        dhcp_ip_setting (DhcpIpSettingEntity | Unset): DHCP IP setting
        static_ip_setting (StaticIpSettingEntity | Unset): Static IP setting
    """

    mode: str
    dhcp_ip_setting: DhcpIpSettingEntity | Unset = UNSET
    static_ip_setting: StaticIpSettingEntity | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        dhcp_ip_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dhcp_ip_setting, Unset):
            dhcp_ip_setting = self.dhcp_ip_setting.to_dict()

        static_ip_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.static_ip_setting, Unset):
            static_ip_setting = self.static_ip_setting.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
            }
        )
        if dhcp_ip_setting is not UNSET:
            field_dict["dhcpIpSetting"] = dhcp_ip_setting
        if static_ip_setting is not UNSET:
            field_dict["staticIpSetting"] = static_ip_setting

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.dhcp_ip_setting_entity import DhcpIpSettingEntity
        from ..models.static_ip_setting_entity import (
            StaticIpSettingEntity,
        )

        d = dict(src_dict)
        mode = d.pop("mode")

        _dhcp_ip_setting = d.pop("dhcpIpSetting", UNSET)
        dhcp_ip_setting: DhcpIpSettingEntity | Unset
        if isinstance(_dhcp_ip_setting, Unset):
            dhcp_ip_setting = UNSET
        else:
            dhcp_ip_setting = DhcpIpSettingEntity.from_dict(_dhcp_ip_setting)

        _static_ip_setting = d.pop("staticIpSetting", UNSET)
        static_ip_setting: StaticIpSettingEntity | Unset
        if isinstance(_static_ip_setting, Unset):
            static_ip_setting = UNSET
        else:
            static_ip_setting = StaticIpSettingEntity.from_dict(_static_ip_setting)

        ap_ip_setting = cls(
            mode=mode,
            dhcp_ip_setting=dhcp_ip_setting,
            static_ip_setting=static_ip_setting,
        )

        ap_ip_setting.additional_properties = d
        return ap_ip_setting

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
