from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_location_detail_vo import DeviceLocationDetailVO


T = TypeVar("T", bound="EasyManagedSwitchGeneralConfig")


@_attrs_define
class EasyManagedSwitchGeneralConfig:
    """
    Attributes:
        name (str | Unset): Device name should contain 1 to 32 characters.
        led_setting (int | Unset): LED setting should be a value as follows: 0:off; 1:on; 2:Use Site Settings
        tag_ids (list[str] | Unset): Tag IDs
        jumbo_enable (bool | Unset): Parameter [jumboEnable] should be true or false.
        location (DeviceLocationDetailVO | Unset): Device location
        remember (bool | Unset): Parameter [remember] should be true or false.
        power_alert_enable (bool | Unset): Power alert status.
    """

    name: str | Unset = UNSET
    led_setting: int | Unset = UNSET
    tag_ids: list[str] | Unset = UNSET
    jumbo_enable: bool | Unset = UNSET
    location: DeviceLocationDetailVO | Unset = UNSET
    remember: bool | Unset = UNSET
    power_alert_enable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        led_setting = self.led_setting

        tag_ids: list[str] | Unset = UNSET
        if not isinstance(self.tag_ids, Unset):
            tag_ids = self.tag_ids

        jumbo_enable = self.jumbo_enable

        location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        remember = self.remember

        power_alert_enable = self.power_alert_enable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if led_setting is not UNSET:
            field_dict["ledSetting"] = led_setting
        if tag_ids is not UNSET:
            field_dict["tagIds"] = tag_ids
        if jumbo_enable is not UNSET:
            field_dict["jumboEnable"] = jumbo_enable
        if location is not UNSET:
            field_dict["location"] = location
        if remember is not UNSET:
            field_dict["remember"] = remember
        if power_alert_enable is not UNSET:
            field_dict["powerAlertEnable"] = power_alert_enable

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.device_location_detail_vo import (
            DeviceLocationDetailVO,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        led_setting = d.pop("ledSetting", UNSET)

        tag_ids = cast(list[str], d.pop("tagIds", UNSET))

        jumbo_enable = d.pop("jumboEnable", UNSET)

        _location = d.pop("location", UNSET)
        location: DeviceLocationDetailVO | Unset
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = DeviceLocationDetailVO.from_dict(_location)

        remember = d.pop("remember", UNSET)

        power_alert_enable = d.pop("powerAlertEnable", UNSET)

        easy_managed_switch_general_config = cls(
            name=name,
            led_setting=led_setting,
            tag_ids=tag_ids,
            jumbo_enable=jumbo_enable,
            location=location,
            remember=remember,
            power_alert_enable=power_alert_enable,
        )

        easy_managed_switch_general_config.additional_properties = d
        return easy_managed_switch_general_config

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
