from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dot_1x_eap_setting_open_api_vo import Dot1XEapSettingOpenApiVO
    from ..models.dot_1x_guest_vlan_setting_open_api_vo import (
        Dot1XGuestVlanSettingOpenApiVO,
    )


T = TypeVar("T", bound="Dot1XEapOpenApiVO")


@_attrs_define
class Dot1XEapOpenApiVO:
    """
    Attributes:
        enable (bool): EAP 802.1x function enable status
        radius_profile_id (str | Unset): This field represents radius profile ID. Radius profile can be created using
            'Create a new RADIUS profile' ('Create a new RADIUS profile template') interface, and radius profile ID can be
            obtained from 'Get RADIUS profile list' ('Get RADIUS profile template list') interface
        mac_format (int | Unset): Format of the MAC address. MacFormat should be a value as follows: 0: aabbccddeeff, 1:
            aa-bb-cc-dd-ee-ff, 2: aa:bb:cc:dd:ee:ff, 3: AABBCCDDEEFF, 4: AA-BB-CC-DD-EE-FF, 5: AA:BB:CC:DD:EE:FF
        guest_vlan_setting (Dot1XGuestVlanSettingOpenApiVO | Unset): Guest VLAN configuration used for EAP 802.1x
            authentication. Supports three modes: 0 = None, 1 = By Network, 2 = By VLAN ID. Parameter [guestVlanSetting]
            should not be null when [enable] is TRUE.
        eaps (list[Dot1XEapSettingOpenApiVO] | Unset): Enabled eap ports
    """

    enable: bool
    radius_profile_id: str | Unset = UNSET
    mac_format: int | Unset = UNSET
    guest_vlan_setting: Dot1XGuestVlanSettingOpenApiVO | Unset = UNSET
    eaps: list[Dot1XEapSettingOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        radius_profile_id = self.radius_profile_id

        mac_format = self.mac_format

        guest_vlan_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.guest_vlan_setting, Unset):
            guest_vlan_setting = self.guest_vlan_setting.to_dict()

        eaps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.eaps, Unset):
            eaps = []
            for eaps_item_data in self.eaps:
                eaps_item = eaps_item_data.to_dict()
                eaps.append(eaps_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
            }
        )
        if radius_profile_id is not UNSET:
            field_dict["radiusProfileId"] = radius_profile_id
        if mac_format is not UNSET:
            field_dict["macFormat"] = mac_format
        if guest_vlan_setting is not UNSET:
            field_dict["guestVlanSetting"] = guest_vlan_setting
        if eaps is not UNSET:
            field_dict["eaps"] = eaps

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.dot_1x_eap_setting_open_api_vo import (
            Dot1XEapSettingOpenApiVO,
        )
        from ..models.dot_1x_guest_vlan_setting_open_api_vo import (
            Dot1XGuestVlanSettingOpenApiVO,
        )

        d = dict(src_dict)
        enable = d.pop("enable")

        radius_profile_id = d.pop("radiusProfileId", UNSET)

        mac_format = d.pop("macFormat", UNSET)

        _guest_vlan_setting = d.pop("guestVlanSetting", UNSET)
        guest_vlan_setting: Dot1XGuestVlanSettingOpenApiVO | Unset
        if isinstance(_guest_vlan_setting, Unset):
            guest_vlan_setting = UNSET
        else:
            guest_vlan_setting = Dot1XGuestVlanSettingOpenApiVO.from_dict(
                _guest_vlan_setting
            )

        _eaps = d.pop("eaps", UNSET)
        eaps: list[Dot1XEapSettingOpenApiVO] | Unset = UNSET
        if _eaps is not UNSET:
            eaps = []
            for eaps_item_data in _eaps:
                eaps_item = Dot1XEapSettingOpenApiVO.from_dict(eaps_item_data)

                eaps.append(eaps_item)

        dot_1x_eap_open_api_vo = cls(
            enable=enable,
            radius_profile_id=radius_profile_id,
            mac_format=mac_format,
            guest_vlan_setting=guest_vlan_setting,
            eaps=eaps,
        )

        dot_1x_eap_open_api_vo.additional_properties = d
        return dot_1x_eap_open_api_vo

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
