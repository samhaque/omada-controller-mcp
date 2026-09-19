from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SsidEnterpriseSettingOpenApiVO")


@_attrs_define
class SsidEnterpriseSettingOpenApiVO:
    """WPA-Enterprise SSID config. This is necessary when the value of security is 2(WPA-Enterprise).

    Attributes:
        radius_profile_id (str): This field represents RADIUS Profile ID. RADIUS Profile(RADIUS Profile Template) can be
            created using Create a new RADIUS profile(Create a new RADIUS profile template) interface, and RADIUS Profile
            ID(RADIUS Profile Template ID) can be obtained from Get RADIUS profile list(Get RADIUS profile template list)
            interface.
        version_ent (int): WPA-Enterprise version. This is necessary when the value of security is 2(WPA-Enterprise); It
            should be a value as follows: 1: WPA-Enterprise; 2: WPA2-Enterprise; 3: WPA/WPA2-Enterprise; 4.WPA3-Enterprise.
        encryption_ent (int): WPA-Enterprise encryption. This is necessary when the value of security is 2(WPA-
            Enterprise); It should be a value as follows: 1: Auto; 3: AES; 4: AES-GCM 256; 5:AES-CNSA; 6:CCMP_128; When
            versionEnt is WPA3-Enterprise, Parameter [encryptionEnt] must be AES/AES-GCM 256/AES-CNSA/CCMP-128, and if ssid
            only enable 6G or contains 6G and enable mlo, Parameter [encryptionEnt] can not be AES.
        gik_rekey_ent_enable (bool): WPA-Enterprise SSID group key update period config status. True: enable, false:
            disable.
        rekey_ent_interval (int | Unset): WPA-Enterprise SSID group key update period interval config. When the value of
            Parameter [intervalEntType] is 0(Seconds), it should be within the range of 30-86400; when the value of
            Parameter [intervalEntType] is 1(Minutes), it should be within the range of 1-1440; when the value of Parameter
            [intervalEntType] is 2(Hours), it should be within the range of 1-24.
        interval_ent_type (int | Unset): WPA-Enterprise SSID group key update period interval unit config. It should be
            a value as follows: 0: Seconds; 1: Minutes; 2: Hours.
        nas_id_mode (int | Unset): Indicates the status of nasid under enterprise-level encryption. It should be a value
            as follows: 0: default (TP LINK: MAC Address), 1: follow device name, 2: custom.
        nas_id (str | Unset): This field is necessary when the nasIdMode type is custom.
    """

    radius_profile_id: str
    version_ent: int
    encryption_ent: int
    gik_rekey_ent_enable: bool
    rekey_ent_interval: int | Unset = UNSET
    interval_ent_type: int | Unset = UNSET
    nas_id_mode: int | Unset = UNSET
    nas_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        radius_profile_id = self.radius_profile_id

        version_ent = self.version_ent

        encryption_ent = self.encryption_ent

        gik_rekey_ent_enable = self.gik_rekey_ent_enable

        rekey_ent_interval = self.rekey_ent_interval

        interval_ent_type = self.interval_ent_type

        nas_id_mode = self.nas_id_mode

        nas_id = self.nas_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "radiusProfileId": radius_profile_id,
                "versionEnt": version_ent,
                "encryptionEnt": encryption_ent,
                "gikRekeyEntEnable": gik_rekey_ent_enable,
            }
        )
        if rekey_ent_interval is not UNSET:
            field_dict["rekeyEntInterval"] = rekey_ent_interval
        if interval_ent_type is not UNSET:
            field_dict["intervalEntType"] = interval_ent_type
        if nas_id_mode is not UNSET:
            field_dict["nasIdMode"] = nas_id_mode
        if nas_id is not UNSET:
            field_dict["nasId"] = nas_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        radius_profile_id = d.pop("radiusProfileId")

        version_ent = d.pop("versionEnt")

        encryption_ent = d.pop("encryptionEnt")

        gik_rekey_ent_enable = d.pop("gikRekeyEntEnable")

        rekey_ent_interval = d.pop("rekeyEntInterval", UNSET)

        interval_ent_type = d.pop("intervalEntType", UNSET)

        nas_id_mode = d.pop("nasIdMode", UNSET)

        nas_id = d.pop("nasId", UNSET)

        ssid_enterprise_setting_open_api_vo = cls(
            radius_profile_id=radius_profile_id,
            version_ent=version_ent,
            encryption_ent=encryption_ent,
            gik_rekey_ent_enable=gik_rekey_ent_enable,
            rekey_ent_interval=rekey_ent_interval,
            interval_ent_type=interval_ent_type,
            nas_id_mode=nas_id_mode,
            nas_id=nas_id,
        )

        ssid_enterprise_setting_open_api_vo.additional_properties = d
        return ssid_enterprise_setting_open_api_vo

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
