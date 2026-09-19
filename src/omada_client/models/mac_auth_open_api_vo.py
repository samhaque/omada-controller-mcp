from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ssid_simple_open_api_vo import SsidSimpleOpenApiVO


T = TypeVar("T", bound="MacAuthOpenApiVO")


@_attrs_define
class MacAuthOpenApiVO:
    """
    Attributes:
        enable (bool | Unset): MAC-Based Authentication enable status
        ssids (list[SsidSimpleOpenApiVO] | Unset): SSID list with MAC-Based authentication configured
        radius_profile_id (str | Unset): This field represents radius profile ID. Radius profile can be created using
            'Create a new RADIUS profile' ('Create a new RADIUS profile template') interface, and radius profile ID can be
            obtained from 'Get RADIUS profile list' ('Get RADIUS profile template list') interface
        mab_enable (bool | Unset): MAB enable status
        mac_format (int | Unset): Format of the MAC address. MacFormat should be a value as follows: 0: aabbccddeeff, 1:
            aa-bb-cc-dd-ee-ff, 2: aa:bb:cc:dd:ee:ff, 3: AABBCCDDEEFF, 4: AA-BB-CC-DD-EE-FF, 5: AA:BB:CC:DD:EE:FF
        empty_pwd_enable (bool | Unset): Whether to enable empty password
        nas_id (str | Unset): NAS ID issued to AP. NasId should contain 1 to 64 characters
    """

    enable: bool | Unset = UNSET
    ssids: list[SsidSimpleOpenApiVO] | Unset = UNSET
    radius_profile_id: str | Unset = UNSET
    mab_enable: bool | Unset = UNSET
    mac_format: int | Unset = UNSET
    empty_pwd_enable: bool | Unset = UNSET
    nas_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        ssids: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ssids, Unset):
            ssids = []
            for ssids_item_data in self.ssids:
                ssids_item = ssids_item_data.to_dict()
                ssids.append(ssids_item)

        radius_profile_id = self.radius_profile_id

        mab_enable = self.mab_enable

        mac_format = self.mac_format

        empty_pwd_enable = self.empty_pwd_enable

        nas_id = self.nas_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if ssids is not UNSET:
            field_dict["ssids"] = ssids
        if radius_profile_id is not UNSET:
            field_dict["radiusProfileId"] = radius_profile_id
        if mab_enable is not UNSET:
            field_dict["mabEnable"] = mab_enable
        if mac_format is not UNSET:
            field_dict["macFormat"] = mac_format
        if empty_pwd_enable is not UNSET:
            field_dict["emptyPwdEnable"] = empty_pwd_enable
        if nas_id is not UNSET:
            field_dict["nasId"] = nas_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ssid_simple_open_api_vo import (
            SsidSimpleOpenApiVO,
        )

        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        _ssids = d.pop("ssids", UNSET)
        ssids: list[SsidSimpleOpenApiVO] | Unset = UNSET
        if _ssids is not UNSET:
            ssids = []
            for ssids_item_data in _ssids:
                ssids_item = SsidSimpleOpenApiVO.from_dict(ssids_item_data)

                ssids.append(ssids_item)

        radius_profile_id = d.pop("radiusProfileId", UNSET)

        mab_enable = d.pop("mabEnable", UNSET)

        mac_format = d.pop("macFormat", UNSET)

        empty_pwd_enable = d.pop("emptyPwdEnable", UNSET)

        nas_id = d.pop("nasId", UNSET)

        mac_auth_open_api_vo = cls(
            enable=enable,
            ssids=ssids,
            radius_profile_id=radius_profile_id,
            mab_enable=mab_enable,
            mac_format=mac_format,
            empty_pwd_enable=empty_pwd_enable,
            nas_id=nas_id,
        )

        mac_auth_open_api_vo.additional_properties = d
        return mac_auth_open_api_vo

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
