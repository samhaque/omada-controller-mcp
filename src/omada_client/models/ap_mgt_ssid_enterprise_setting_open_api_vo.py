from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="ApMgtSsidEnterpriseSettingOpenApiVO")


@_attrs_define
class ApMgtSsidEnterpriseSettingOpenApiVO:
    """WPA-Enterprise SSID config. This is necessary when the value of security is 2(WPA-Enterprise).

    Attributes:
        radius_profile_id (str): This field represents RADIUS Profile ID. RADIUS Profile(RADIUS Profile Template) can be
            created using Create a new RADIUS profile(Create a new RADIUS profile template) interface, and RADIUS Profile
            ID(RADIUS Profile Template ID) can be obtained from Get RADIUS profile list(Get RADIUS profile template list)
            interface.
        version_ent (int): WPA-Enterprise version. This is necessary when the value of security is 2(WPA-Enterprise); It
            should be a value as follows: 1: WPA-Enterprise; 2: WPA2-Enterprise; 3: WPA/WPA2-Enterprise.
        encryption_ent (int): WPA-Enterprise encryption. This is necessary when the value of security is 2(WPA-
            Enterprise); It should be a value as follows: 1: Auto; 3: AES.
    """

    radius_profile_id: str
    version_ent: int
    encryption_ent: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        radius_profile_id = self.radius_profile_id

        version_ent = self.version_ent

        encryption_ent = self.encryption_ent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "radiusProfileId": radius_profile_id,
                "versionEnt": version_ent,
                "encryptionEnt": encryption_ent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        radius_profile_id = d.pop("radiusProfileId")

        version_ent = d.pop("versionEnt")

        encryption_ent = d.pop("encryptionEnt")

        ap_mgt_ssid_enterprise_setting_open_api_vo = cls(
            radius_profile_id=radius_profile_id,
            version_ent=version_ent,
            encryption_ent=encryption_ent,
        )

        ap_mgt_ssid_enterprise_setting_open_api_vo.additional_properties = d
        return ap_mgt_ssid_enterprise_setting_open_api_vo

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
