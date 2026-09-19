from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="Dot1XSwitchResOpenApiVO")


@_attrs_define
class Dot1XSwitchResOpenApiVO:
    """
    Attributes:
        enable (bool): Switch 802.1x function enable status
        radius_profile_id (str | Unset): This field represents radius profile ID. Radius profile can be created using
            'Create a new RADIUS profile' ('Create a new RADIUS profile template') interface, and radius profile ID can be
            obtained from 'Get RADIUS profile list' ('Get RADIUS profile template list') interface
        auth_mode (int | Unset): Mode of authentication protocol. AuthMode should be a value as follows: 0: PAP, 1: EAP
        auth_type (int | Unset): Type of the authentication. AuthType should be a value as follows: 0: Port based, 1:
            Mac based
        vlan_assign (bool | Unset): VLAN Assignment enable status
        mab (bool | Unset): MAB enable status
        mac_format (int | Unset): Format of the MAC address. MacFormat should be a value as follows: 0: aabbccddeeff, 1:
            aa-bb-cc-dd-ee-ff, 2: aa:bb:cc:dd:ee:ff, 3: AABBCCDDEEFF, 4: AA-BB-CC-DD-EE-FF, 5: AA:BB:CC:DD:EE:FF
        nas_id (str | Unset): Nas ID,NasId should contain 1~31 characters, except the question mark (?) and double quote
            (").
        guest_vlan (int | Unset): Guest VLAN, clients that have not been authorized will be added to the guest VLAN.The
            value of guest VLAN should be selected from the created LAN Network.
    """

    enable: bool
    radius_profile_id: str | Unset = UNSET
    auth_mode: int | Unset = UNSET
    auth_type: int | Unset = UNSET
    vlan_assign: bool | Unset = UNSET
    mab: bool | Unset = UNSET
    mac_format: int | Unset = UNSET
    nas_id: str | Unset = UNSET
    guest_vlan: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        radius_profile_id = self.radius_profile_id

        auth_mode = self.auth_mode

        auth_type = self.auth_type

        vlan_assign = self.vlan_assign

        mab = self.mab

        mac_format = self.mac_format

        nas_id = self.nas_id

        guest_vlan = self.guest_vlan

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
            }
        )
        if radius_profile_id is not UNSET:
            field_dict["radiusProfileId"] = radius_profile_id
        if auth_mode is not UNSET:
            field_dict["authMode"] = auth_mode
        if auth_type is not UNSET:
            field_dict["authType"] = auth_type
        if vlan_assign is not UNSET:
            field_dict["vlanAssign"] = vlan_assign
        if mab is not UNSET:
            field_dict["mab"] = mab
        if mac_format is not UNSET:
            field_dict["macFormat"] = mac_format
        if nas_id is not UNSET:
            field_dict["nasId"] = nas_id
        if guest_vlan is not UNSET:
            field_dict["guestVlan"] = guest_vlan

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable = d.pop("enable")

        radius_profile_id = d.pop("radiusProfileId", UNSET)

        auth_mode = d.pop("authMode", UNSET)

        auth_type = d.pop("authType", UNSET)

        vlan_assign = d.pop("vlanAssign", UNSET)

        mab = d.pop("mab", UNSET)

        mac_format = d.pop("macFormat", UNSET)

        nas_id = d.pop("nasId", UNSET)

        guest_vlan = d.pop("guestVlan", UNSET)

        dot_1x_switch_res_open_api_vo = cls(
            enable=enable,
            radius_profile_id=radius_profile_id,
            auth_mode=auth_mode,
            auth_type=auth_type,
            vlan_assign=vlan_assign,
            mab=mab,
            mac_format=mac_format,
            nas_id=nas_id,
            guest_vlan=guest_vlan,
        )

        dot_1x_switch_res_open_api_vo.additional_properties = d
        return dot_1x_switch_res_open_api_vo

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
