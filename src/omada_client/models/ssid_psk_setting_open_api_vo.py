from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SsidPskSettingOpenApiVO")


@_attrs_define
class SsidPskSettingOpenApiVO:
    """WPA-Personal SSID config. This is necessary when the value of security is 3(WPA-Personal), 4(PPSK without RADIUS),
    5(PPSK with RADIUS).

        Attributes:
            version_psk (int): WPA-Personal version. This is necessary when the value of security is 3(WPA-Personal); It
                should be a value as follows: 1: WPA-PSK; 2: WPA2-PSK; 3: WPA/WPA2-PSK; 4: WPA2-PSK/WPA3-SAE (or WPA3-SAE for 6
                GHz-only SSIDs). The value must be 4 for 6 GHz-enabled SSIDs.
            encryption_psk (int): WPA-Personal encryption. This is necessary when the value of security is 3(WPA-Personal);
                It should be a value as follows: 1: Auto; 3: AES; When versionPsk is WPA3-SAE, Parameter [encryptionPsk] must be
                AES.
            gik_rekey_psk_enable (bool): WPA-Personal SSID group key update period config status. True: enable, false:
                disable.
            security_key (str | Unset): WPA-Personal SSID password. This is necessary when the value of security is 3(WPA-
                Personal);It should contain 8-63 printable ASCII characters or 8-63 hexadecimal digits.
            rekey_psk_interval (int | Unset): WPA-Personal SSID group key update period interval config. When the value of
                Parameter [intervalPskType] is 0 (Seconds), it should be within the range of 30-86400; when the value of
                Parameter [intervalPskType] is 1 (Minutes), it should be within the range of 1-1440; when the value of Parameter
                [intervalPskType] is 2 (Hours), it should be within the range of 1-24.
            interval_psk_type (int | Unset): WPA-Personal SSID group key update period interval unit config. It should be a
                value as follows: 0: Seconds; 1: Minutes; 2: Hours.
    """

    version_psk: int
    encryption_psk: int
    gik_rekey_psk_enable: bool
    security_key: str | Unset = UNSET
    rekey_psk_interval: int | Unset = UNSET
    interval_psk_type: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version_psk = self.version_psk

        encryption_psk = self.encryption_psk

        gik_rekey_psk_enable = self.gik_rekey_psk_enable

        security_key = self.security_key

        rekey_psk_interval = self.rekey_psk_interval

        interval_psk_type = self.interval_psk_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "versionPsk": version_psk,
                "encryptionPsk": encryption_psk,
                "gikRekeyPskEnable": gik_rekey_psk_enable,
            }
        )
        if security_key is not UNSET:
            field_dict["securityKey"] = security_key
        if rekey_psk_interval is not UNSET:
            field_dict["rekeyPskInterval"] = rekey_psk_interval
        if interval_psk_type is not UNSET:
            field_dict["intervalPskType"] = interval_psk_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        version_psk = d.pop("versionPsk")

        encryption_psk = d.pop("encryptionPsk")

        gik_rekey_psk_enable = d.pop("gikRekeyPskEnable")

        security_key = d.pop("securityKey", UNSET)

        rekey_psk_interval = d.pop("rekeyPskInterval", UNSET)

        interval_psk_type = d.pop("intervalPskType", UNSET)

        ssid_psk_setting_open_api_vo = cls(
            version_psk=version_psk,
            encryption_psk=encryption_psk,
            gik_rekey_psk_enable=gik_rekey_psk_enable,
            security_key=security_key,
            rekey_psk_interval=rekey_psk_interval,
            interval_psk_type=interval_psk_type,
        )

        ssid_psk_setting_open_api_vo.additional_properties = d
        return ssid_psk_setting_open_api_vo

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
