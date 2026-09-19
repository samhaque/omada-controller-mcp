from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SsidOverrideConfigOpenApiV2VO")


@_attrs_define
class SsidOverrideConfigOpenApiV2VO:
    """SsidOverride Config List

    Attributes:
        ssid_id (str): SSID ID
        ssid_name (str): SSID name. It should contain 1 to 32 UTF-8 characters.
        ssid_entry_id (int | Unset): SSID Entry ID
        ssid_password (str | Unset): SSID password. It should contain 8-63 printable ASCII characters or 8-63
            hexadecimal digits.
        band (list[int] | Unset): SSID band should be a value as follows: 0: 2.4GHz; 1: 5GHz; 2: 6GHz
        security (int | Unset): SSID security mode should be a value as follows: 0: None; 2: WPA-Enterprise; 3: WPA-
            Personal;4: PPSK without RADIUS; 5: PPSK with RADIUS.
        vlan_enable (bool | Unset): Enable/disable VLAN
        vlan_id (int | Unset): VLAN ID
        vlan_pool_ids (str | Unset): VLAN POOL IDS
        ssid_enable (bool | Unset): Enable/disable SSID
    """

    ssid_id: str
    ssid_name: str
    ssid_entry_id: int | Unset = UNSET
    ssid_password: str | Unset = UNSET
    band: list[int] | Unset = UNSET
    security: int | Unset = UNSET
    vlan_enable: bool | Unset = UNSET
    vlan_id: int | Unset = UNSET
    vlan_pool_ids: str | Unset = UNSET
    ssid_enable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ssid_id = self.ssid_id

        ssid_name = self.ssid_name

        ssid_entry_id = self.ssid_entry_id

        ssid_password = self.ssid_password

        band: list[int] | Unset = UNSET
        if not isinstance(self.band, Unset):
            band = self.band

        security = self.security

        vlan_enable = self.vlan_enable

        vlan_id = self.vlan_id

        vlan_pool_ids = self.vlan_pool_ids

        ssid_enable = self.ssid_enable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ssidId": ssid_id,
                "ssidName": ssid_name,
            }
        )
        if ssid_entry_id is not UNSET:
            field_dict["ssidEntryId"] = ssid_entry_id
        if ssid_password is not UNSET:
            field_dict["ssidPassword"] = ssid_password
        if band is not UNSET:
            field_dict["band"] = band
        if security is not UNSET:
            field_dict["security"] = security
        if vlan_enable is not UNSET:
            field_dict["vlanEnable"] = vlan_enable
        if vlan_id is not UNSET:
            field_dict["vlanId"] = vlan_id
        if vlan_pool_ids is not UNSET:
            field_dict["vlanPoolIds"] = vlan_pool_ids
        if ssid_enable is not UNSET:
            field_dict["ssidEnable"] = ssid_enable

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ssid_id = d.pop("ssidId")

        ssid_name = d.pop("ssidName")

        ssid_entry_id = d.pop("ssidEntryId", UNSET)

        ssid_password = d.pop("ssidPassword", UNSET)

        band = cast(list[int], d.pop("band", UNSET))

        security = d.pop("security", UNSET)

        vlan_enable = d.pop("vlanEnable", UNSET)

        vlan_id = d.pop("vlanId", UNSET)

        vlan_pool_ids = d.pop("vlanPoolIds", UNSET)

        ssid_enable = d.pop("ssidEnable", UNSET)

        ssid_override_config_open_api_v2vo = cls(
            ssid_id=ssid_id,
            ssid_name=ssid_name,
            ssid_entry_id=ssid_entry_id,
            ssid_password=ssid_password,
            band=band,
            security=security,
            vlan_enable=vlan_enable,
            vlan_id=vlan_id,
            vlan_pool_ids=vlan_pool_ids,
            ssid_enable=ssid_enable,
        )

        ssid_override_config_open_api_v2vo.additional_properties = d
        return ssid_override_config_open_api_v2vo

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
