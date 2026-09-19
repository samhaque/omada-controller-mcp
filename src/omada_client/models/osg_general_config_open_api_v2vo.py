from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_location_detail_open_api_vo import (
        DeviceLocationDetailOpenApiVO,
    )
    from ..models.osg_snmp_open_api_vo import OsgSnmpOpenApiVO


T = TypeVar("T", bound="OsgGeneralConfigOpenApiV2VO")


@_attrs_define
class OsgGeneralConfigOpenApiV2VO:
    """
    Attributes:
        led_setting (int): Led setting should be a value as follows: 0:off; 1:on; 2:Use Site Settings
        name (str | Unset): Device name should contain 1 to 128 characters. This subsection is deprecated.
        tag_ids (list[str] | Unset): Tag IDs. This subsection is deprecated.
        location (DeviceLocationDetailOpenApiVO | Unset): Device location. This subsection is deprecated.
        snmp (OsgSnmpOpenApiVO | Unset): Snmp setting
        remember_device (int | Unset):
    """

    led_setting: int
    name: str | Unset = UNSET
    tag_ids: list[str] | Unset = UNSET
    location: DeviceLocationDetailOpenApiVO | Unset = UNSET
    snmp: OsgSnmpOpenApiVO | Unset = UNSET
    remember_device: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        led_setting = self.led_setting

        name = self.name

        tag_ids: list[str] | Unset = UNSET
        if not isinstance(self.tag_ids, Unset):
            tag_ids = self.tag_ids

        location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        snmp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.snmp, Unset):
            snmp = self.snmp.to_dict()

        remember_device = self.remember_device

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ledSetting": led_setting,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if tag_ids is not UNSET:
            field_dict["tagIds"] = tag_ids
        if location is not UNSET:
            field_dict["location"] = location
        if snmp is not UNSET:
            field_dict["snmp"] = snmp
        if remember_device is not UNSET:
            field_dict["rememberDevice"] = remember_device

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.device_location_detail_open_api_vo import (
            DeviceLocationDetailOpenApiVO,
        )
        from ..models.osg_snmp_open_api_vo import OsgSnmpOpenApiVO

        d = dict(src_dict)
        led_setting = d.pop("ledSetting")

        name = d.pop("name", UNSET)

        tag_ids = cast(list[str], d.pop("tagIds", UNSET))

        _location = d.pop("location", UNSET)
        location: DeviceLocationDetailOpenApiVO | Unset
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = DeviceLocationDetailOpenApiVO.from_dict(_location)

        _snmp = d.pop("snmp", UNSET)
        snmp: OsgSnmpOpenApiVO | Unset
        if isinstance(_snmp, Unset):
            snmp = UNSET
        else:
            snmp = OsgSnmpOpenApiVO.from_dict(_snmp)

        remember_device = d.pop("rememberDevice", UNSET)

        osg_general_config_open_api_v2vo = cls(
            led_setting=led_setting,
            name=name,
            tag_ids=tag_ids,
            location=location,
            snmp=snmp,
            remember_device=remember_device,
        )

        osg_general_config_open_api_v2vo.additional_properties = d
        return osg_general_config_open_api_v2vo

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
