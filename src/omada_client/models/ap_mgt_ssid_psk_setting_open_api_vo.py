from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="ApMgtSsidPskSettingOpenApiVO")


@_attrs_define
class ApMgtSsidPskSettingOpenApiVO:
    """WPA-Personal SSID config. This is necessary when the value of security is 3(WPA-Personal).

    Attributes:
        security_key (str): WPA-Personal SSID password. This is necessary when the value of security is 3(WPA-
            Personal);It should contain 8-63 printable ASCII characters or 8-63 hexadecimal digits.
        version_psk (int): WPA-Personal version. This is necessary when the value of security is 3(WPA-Personal); It
            should be a value as follows: 1: WPA-PSK; 2: WPA2-PSK; 3: WPA/WPA2-PSK.
        encryption_psk (int): WPA-Personal encryption. This is necessary when the value of security is 3(WPA-Personal);
            It should be a value as follows: 1: Auto; 3: AES.
    """

    security_key: str
    version_psk: int
    encryption_psk: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        security_key = self.security_key

        version_psk = self.version_psk

        encryption_psk = self.encryption_psk

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "securityKey": security_key,
                "versionPsk": version_psk,
                "encryptionPsk": encryption_psk,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        security_key = d.pop("securityKey")

        version_psk = d.pop("versionPsk")

        encryption_psk = d.pop("encryptionPsk")

        ap_mgt_ssid_psk_setting_open_api_vo = cls(
            security_key=security_key,
            version_psk=version_psk,
            encryption_psk=encryption_psk,
        )

        ap_mgt_ssid_psk_setting_open_api_vo.additional_properties = d
        return ap_mgt_ssid_psk_setting_open_api_vo

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
