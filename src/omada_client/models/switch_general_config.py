from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_location_detail_vo import DeviceLocationDetailVO
    from ..models.osw_sdm_template_vo import OswSdmTemplateVO
    from ..models.osw_snmp_open_api_vo import OswSnmpOpenApiVO


T = TypeVar("T", bound="SwitchGeneralConfig")


@_attrs_define
class SwitchGeneralConfig:
    """After the device is added to the stack group, the interface can only modify the device name.

    Attributes:
        name (str | Unset): Device name should contain 1 to 128 characters.
        led_setting (int | Unset): Led setting should be a value as follows: 0:off; 1:on; 2:Use Site Settings
        tag_ids (list[str] | Unset): Tag IDs
        location (DeviceLocationDetailVO | Unset): Device location
        jumbo_follow_site (bool | Unset): Whether jumbo setting follows site setting.
        jumbo (int | Unset): Required only when jumboFollowSite = false. Range: 1518–9216.
        lag_hash_alg_follow_site (bool | Unset): Whether lag hash algorithm setting follows site setting.
        lag_hash_alg (int | Unset): Required only when lagHashAlgFollowSite = false. It should be a value as follows: 0:
            SRC MAC; 1: DST MAC; 2: SRC MAC + DST MAC; 3: SRC IP; 4: DST IP; 5: SRC IP + DST IP
        snmp (OswSnmpOpenApiVO | Unset): SNMP setting
        sdm (OswSdmTemplateVO | Unset): Sdm template
    """

    name: str | Unset = UNSET
    led_setting: int | Unset = UNSET
    tag_ids: list[str] | Unset = UNSET
    location: DeviceLocationDetailVO | Unset = UNSET
    jumbo_follow_site: bool | Unset = UNSET
    jumbo: int | Unset = UNSET
    lag_hash_alg_follow_site: bool | Unset = UNSET
    lag_hash_alg: int | Unset = UNSET
    snmp: OswSnmpOpenApiVO | Unset = UNSET
    sdm: OswSdmTemplateVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        led_setting = self.led_setting

        tag_ids: list[str] | Unset = UNSET
        if not isinstance(self.tag_ids, Unset):
            tag_ids = self.tag_ids

        location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        jumbo_follow_site = self.jumbo_follow_site

        jumbo = self.jumbo

        lag_hash_alg_follow_site = self.lag_hash_alg_follow_site

        lag_hash_alg = self.lag_hash_alg

        snmp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.snmp, Unset):
            snmp = self.snmp.to_dict()

        sdm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sdm, Unset):
            sdm = self.sdm.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if led_setting is not UNSET:
            field_dict["ledSetting"] = led_setting
        if tag_ids is not UNSET:
            field_dict["tagIds"] = tag_ids
        if location is not UNSET:
            field_dict["location"] = location
        if jumbo_follow_site is not UNSET:
            field_dict["jumboFollowSite"] = jumbo_follow_site
        if jumbo is not UNSET:
            field_dict["jumbo"] = jumbo
        if lag_hash_alg_follow_site is not UNSET:
            field_dict["lagHashAlgFollowSite"] = lag_hash_alg_follow_site
        if lag_hash_alg is not UNSET:
            field_dict["lagHashAlg"] = lag_hash_alg
        if snmp is not UNSET:
            field_dict["snmp"] = snmp
        if sdm is not UNSET:
            field_dict["sdm"] = sdm

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.device_location_detail_vo import (
            DeviceLocationDetailVO,
        )
        from ..models.osw_sdm_template_vo import OswSdmTemplateVO
        from ..models.osw_snmp_open_api_vo import OswSnmpOpenApiVO

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        led_setting = d.pop("ledSetting", UNSET)

        tag_ids = cast(list[str], d.pop("tagIds", UNSET))

        _location = d.pop("location", UNSET)
        location: DeviceLocationDetailVO | Unset
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = DeviceLocationDetailVO.from_dict(_location)

        jumbo_follow_site = d.pop("jumboFollowSite", UNSET)

        jumbo = d.pop("jumbo", UNSET)

        lag_hash_alg_follow_site = d.pop("lagHashAlgFollowSite", UNSET)

        lag_hash_alg = d.pop("lagHashAlg", UNSET)

        _snmp = d.pop("snmp", UNSET)
        snmp: OswSnmpOpenApiVO | Unset
        if isinstance(_snmp, Unset):
            snmp = UNSET
        else:
            snmp = OswSnmpOpenApiVO.from_dict(_snmp)

        _sdm = d.pop("sdm", UNSET)
        sdm: OswSdmTemplateVO | Unset
        if isinstance(_sdm, Unset):
            sdm = UNSET
        else:
            sdm = OswSdmTemplateVO.from_dict(_sdm)

        switch_general_config = cls(
            name=name,
            led_setting=led_setting,
            tag_ids=tag_ids,
            location=location,
            jumbo_follow_site=jumbo_follow_site,
            jumbo=jumbo,
            lag_hash_alg_follow_site=lag_hash_alg_follow_site,
            lag_hash_alg=lag_hash_alg,
            snmp=snmp,
            sdm=sdm,
        )

        switch_general_config.additional_properties = d
        return switch_general_config

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
