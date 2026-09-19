from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SsidOverrideOpenApiV2VO")


@_attrs_define
class SsidOverrideOpenApiV2VO:
    """SsidOverride Config List

    Attributes:
        ssid_entry_id (int): This field represents SSID Entry ID.SSID Entry ID can be obtained from 'Get ap WLANs
            override config' interface.
        override_ssid_enable (bool): Enable/disable SSID override
        override_vlan_enable (bool): Enable/disable VLAN override
        override_ssid_name (str | Unset): Override SSID name. It should contain 1 to 32 UTF-8 characters.
        override_ssid_password (str | Unset): Override SSID password(when security is WPA-Personal need fill).It should
            contain 8-63 printable ASCII characters or 8-63 hexadecimal digits.
        vlan_id (int | Unset): VLAN ID
        vlan_pool_ids (str | Unset): VLAN POOL IDS
        ssid_enable (bool | Unset): Enable/disable SSID
    """

    ssid_entry_id: int
    override_ssid_enable: bool
    override_vlan_enable: bool
    override_ssid_name: str | Unset = UNSET
    override_ssid_password: str | Unset = UNSET
    vlan_id: int | Unset = UNSET
    vlan_pool_ids: str | Unset = UNSET
    ssid_enable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ssid_entry_id = self.ssid_entry_id

        override_ssid_enable = self.override_ssid_enable

        override_vlan_enable = self.override_vlan_enable

        override_ssid_name = self.override_ssid_name

        override_ssid_password = self.override_ssid_password

        vlan_id = self.vlan_id

        vlan_pool_ids = self.vlan_pool_ids

        ssid_enable = self.ssid_enable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ssidEntryId": ssid_entry_id,
                "overrideSsidEnable": override_ssid_enable,
                "overrideVlanEnable": override_vlan_enable,
            }
        )
        if override_ssid_name is not UNSET:
            field_dict["overrideSsidName"] = override_ssid_name
        if override_ssid_password is not UNSET:
            field_dict["overrideSsidPassword"] = override_ssid_password
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
        ssid_entry_id = d.pop("ssidEntryId")

        override_ssid_enable = d.pop("overrideSsidEnable")

        override_vlan_enable = d.pop("overrideVlanEnable")

        override_ssid_name = d.pop("overrideSsidName", UNSET)

        override_ssid_password = d.pop("overrideSsidPassword", UNSET)

        vlan_id = d.pop("vlanId", UNSET)

        vlan_pool_ids = d.pop("vlanPoolIds", UNSET)

        ssid_enable = d.pop("ssidEnable", UNSET)

        ssid_override_open_api_v2vo = cls(
            ssid_entry_id=ssid_entry_id,
            override_ssid_enable=override_ssid_enable,
            override_vlan_enable=override_vlan_enable,
            override_ssid_name=override_ssid_name,
            override_ssid_password=override_ssid_password,
            vlan_id=vlan_id,
            vlan_pool_ids=vlan_pool_ids,
            ssid_enable=ssid_enable,
        )

        ssid_override_open_api_v2vo.additional_properties = d
        return ssid_override_open_api_v2vo

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
