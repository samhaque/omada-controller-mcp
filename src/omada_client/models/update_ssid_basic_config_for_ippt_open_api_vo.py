from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ssid_psk_setting_for_ippt_open_api_vo import (
        SsidPskSettingForIpptOpenApiVO,
    )


T = TypeVar("T", bound="UpdateSsidBasicConfigForIpptOpenApiVO")


@_attrs_define
class UpdateSsidBasicConfigForIpptOpenApiVO:
    """
    Attributes:
        name (str): SSID name. It should contain 1 to 32 UTF-8 characters.
        band (int): SSID band. The lowest bit indicates whether 2.4G is included; the second lowest bit indicates
            whether 5G is included; the third lowest bit indicates whether 6G is included; 1 means included while 0 means
            not included. For example, 7(111) means that 2G/5G/6G are enabled; 1(001) means that 2G is enabled. (When 5G is
            included，it means 5G/5G1/5G2 are enabled.)
        security (int): SSID security mode; Security should be a value as follows: 0: None; 2: WPA-Enterprise; 3: WPA-
            Personal; 4: PPSK without RADIUS; 5: PPSK with RADIUS.
        broadcast (bool): SSID broadcast config status. True: enable, false: disable.
        auto_wan_access (bool | Unset): Whether to enable auto wan access. True: enable, false: disable.
        owe_enable (bool | Unset): Opportunistic Wireless Encryption, also known as Enhanced Open, is a certification
            provided by the Wi-Fi Alliance as part of the WPA3 wireless security standard. OWE will enable two wireless VAPs
            per radio, one for access of OWE-supported stations, and one for access of other stations. An SSID with OWE
            enabled will be counted as two SSID entries for 2G and 5G. Only for security is None and band contains 2.4G or
            5G.
        psk_setting (SsidPskSettingForIpptOpenApiVO | Unset): WPA-Personal SSID config. This is necessary when the value
            of security is 3(WPA-Personal).
    """

    name: str
    band: int
    security: int
    broadcast: bool
    auto_wan_access: bool | Unset = UNSET
    owe_enable: bool | Unset = UNSET
    psk_setting: SsidPskSettingForIpptOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        band = self.band

        security = self.security

        broadcast = self.broadcast

        auto_wan_access = self.auto_wan_access

        owe_enable = self.owe_enable

        psk_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.psk_setting, Unset):
            psk_setting = self.psk_setting.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "band": band,
                "security": security,
                "broadcast": broadcast,
            }
        )
        if auto_wan_access is not UNSET:
            field_dict["autoWanAccess"] = auto_wan_access
        if owe_enable is not UNSET:
            field_dict["oweEnable"] = owe_enable
        if psk_setting is not UNSET:
            field_dict["pskSetting"] = psk_setting

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ssid_psk_setting_for_ippt_open_api_vo import (
            SsidPskSettingForIpptOpenApiVO,
        )

        d = dict(src_dict)
        name = d.pop("name")

        band = d.pop("band")

        security = d.pop("security")

        broadcast = d.pop("broadcast")

        auto_wan_access = d.pop("autoWanAccess", UNSET)

        owe_enable = d.pop("oweEnable", UNSET)

        _psk_setting = d.pop("pskSetting", UNSET)
        psk_setting: SsidPskSettingForIpptOpenApiVO | Unset
        if isinstance(_psk_setting, Unset):
            psk_setting = UNSET
        else:
            psk_setting = SsidPskSettingForIpptOpenApiVO.from_dict(_psk_setting)

        update_ssid_basic_config_for_ippt_open_api_vo = cls(
            name=name,
            band=band,
            security=security,
            broadcast=broadcast,
            auto_wan_access=auto_wan_access,
            owe_enable=owe_enable,
            psk_setting=psk_setting,
        )

        update_ssid_basic_config_for_ippt_open_api_vo.additional_properties = d
        return update_ssid_basic_config_for_ippt_open_api_vo

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
