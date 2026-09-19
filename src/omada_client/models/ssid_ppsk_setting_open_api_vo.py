from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SsidPpskSettingOpenApiVO")


@_attrs_define
class SsidPpskSettingOpenApiVO:
    """PPSK without RADIUS/PPSK without RADIUS SSID config. This is necessary when the value of security is 4(PPSK without
    RADIUS), 5(PPSK with RADIUS).

        Attributes:
            ppsk_profile_id (str | Unset): This field represents PPSK Profile ID; This is necessary when the value of
                security is 4(PPSK without RADIUS); PPSK Profile(PPSK Profile Template) can be created using Create PPSK profile
                interface(Create PPSK profile template interface), and PPSK Profile ID(PPSK Profile Template ID) can be obtained
                from Get PPSK profiles list(Get PPSK profile templates list) interface.
            radius_profile_id (str | Unset): This field represents RADIUS Profile ID; This is necessary when the value of
                security is 5(PPSK with RADIUS); RADIUS Profile(RADIUS Profile Template) can be created using Create a new
                RADIUS profile(Create a new RADIUS profile template) interface, and RADIUS Profile ID(RADIUS Profile Template
                ID) can be obtained from Get RADIUS profile list(Get RADIUS profile template list) interface.
            mac_format (int | Unset): MAC address format. This is necessary when the value of security is 5(PPSK with
                RADIUS); It should be a value as follows: 0: aabbccddeeff; 1: aa-bb-cc-dd-ee-ff; 2: aa:bb:cc:dd:ee:ff; 3:
                AABBCCDDEEFF; 4: AA-BB-CC-DD-EE-FF; 5: AA:BB:CC:DD:EE:FF.
            nas_id (str | Unset): NAS ID. This is necessary when the value of security is 5(PPSK with RADIUS); It should
                contain 1 to 64 characters.
            type_ (int | Unset): Authentication type. This is necessary when the value of security is 5(PPSK with RADIUS);
                It should be a value as follows: 0: Mac Auth(Generic RADIUS with bound MAC); 1: EKMS(This configuration applies
                to the Pro Site of the Omada Pro Controller only); 2: Generic RADIUS with unbound MAC(This configuration applies
                to the Pro Site of the Omada Pro Controller only).
    """

    ppsk_profile_id: str | Unset = UNSET
    radius_profile_id: str | Unset = UNSET
    mac_format: int | Unset = UNSET
    nas_id: str | Unset = UNSET
    type_: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ppsk_profile_id = self.ppsk_profile_id

        radius_profile_id = self.radius_profile_id

        mac_format = self.mac_format

        nas_id = self.nas_id

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ppsk_profile_id is not UNSET:
            field_dict["ppskProfileId"] = ppsk_profile_id
        if radius_profile_id is not UNSET:
            field_dict["radiusProfileId"] = radius_profile_id
        if mac_format is not UNSET:
            field_dict["macFormat"] = mac_format
        if nas_id is not UNSET:
            field_dict["nasId"] = nas_id
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ppsk_profile_id = d.pop("ppskProfileId", UNSET)

        radius_profile_id = d.pop("radiusProfileId", UNSET)

        mac_format = d.pop("macFormat", UNSET)

        nas_id = d.pop("nasId", UNSET)

        type_ = d.pop("type", UNSET)

        ssid_ppsk_setting_open_api_vo = cls(
            ppsk_profile_id=ppsk_profile_id,
            radius_profile_id=radius_profile_id,
            mac_format=mac_format,
            nas_id=nas_id,
            type_=type_,
        )

        ssid_ppsk_setting_open_api_vo.additional_properties = d
        return ssid_ppsk_setting_open_api_vo

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
