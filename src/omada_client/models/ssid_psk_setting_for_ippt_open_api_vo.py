from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SsidPskSettingForIpptOpenApiVO")


@_attrs_define
class SsidPskSettingForIpptOpenApiVO:
    """WPA-Personal SSID config. This is necessary when the value of security is 3(WPA-Personal).

    Attributes:
        version_psk (int): WPA-Personal version. This is necessary when the value of security is 3(WPA-Personal); It
            should be a value as follows: 1: WPA-PSK; 2: WPA2-PSK; 3: WPA/WPA2-PSK; 4: WPA3-SAE.
        encryption_psk (int): WPA-Personal encryption. This is necessary when the value of security is 3(WPA-Personal);
            It should be a value as follows: 1: Auto; 3: AES; When versionPsk is WPA3-SAE, Parameter [encryptionPsk] must be
            AES.
        security_key (str | Unset): WPA-Personal SSID password. This is necessary when the value of security is 3(WPA-
            Personal);It should contain 8-63 printable ASCII characters or 8-63 hexadecimal digits.
    """

    version_psk: int
    encryption_psk: int
    security_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version_psk = self.version_psk

        encryption_psk = self.encryption_psk

        security_key = self.security_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "versionPsk": version_psk,
                "encryptionPsk": encryption_psk,
            }
        )
        if security_key is not UNSET:
            field_dict["securityKey"] = security_key

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        version_psk = d.pop("versionPsk")

        encryption_psk = d.pop("encryptionPsk")

        security_key = d.pop("securityKey", UNSET)

        ssid_psk_setting_for_ippt_open_api_vo = cls(
            version_psk=version_psk,
            encryption_psk=encryption_psk,
            security_key=security_key,
        )

        ssid_psk_setting_for_ippt_open_api_vo.additional_properties = d
        return ssid_psk_setting_for_ippt_open_api_vo

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
