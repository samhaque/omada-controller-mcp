from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OsgSsidOverrideOpenApiVO")


@_attrs_define
class OsgSsidOverrideOpenApiVO:
    """Overrided SSID List

    Attributes:
        index (int): SSID Entry ID
        global_ssid (str): SSID Name
        security (int): SSID Security Mode, must be the same as the current SSID Security
        enable (bool): Enable/disable SSID override
        vlan_enable (bool): Enable/disable VLAN override
        ssid (str): Override SSID
        ssid_enable (bool): Enable/disable SSID
        hide_pwd (bool): hide password
        band_info (int | Unset): Band. Deprecated, use supportBands instead
        support_bands (list[int] | Unset): support band 2.4GHz(0) 5GHz(1) 6GHz(2)
        vlan_id (int | Unset): VLAN ID
        psk (str | Unset): Override SSID Password
    """

    index: int
    global_ssid: str
    security: int
    enable: bool
    vlan_enable: bool
    ssid: str
    ssid_enable: bool
    hide_pwd: bool
    band_info: int | Unset = UNSET
    support_bands: list[int] | Unset = UNSET
    vlan_id: int | Unset = UNSET
    psk: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        index = self.index

        global_ssid = self.global_ssid

        security = self.security

        enable = self.enable

        vlan_enable = self.vlan_enable

        ssid = self.ssid

        ssid_enable = self.ssid_enable

        hide_pwd = self.hide_pwd

        band_info = self.band_info

        support_bands: list[int] | Unset = UNSET
        if not isinstance(self.support_bands, Unset):
            support_bands = self.support_bands

        vlan_id = self.vlan_id

        psk = self.psk

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "index": index,
                "globalSsid": global_ssid,
                "security": security,
                "enable": enable,
                "vlanEnable": vlan_enable,
                "ssid": ssid,
                "ssidEnable": ssid_enable,
                "hidePwd": hide_pwd,
            }
        )
        if band_info is not UNSET:
            field_dict["bandInfo"] = band_info
        if support_bands is not UNSET:
            field_dict["supportBands"] = support_bands
        if vlan_id is not UNSET:
            field_dict["vlanId"] = vlan_id
        if psk is not UNSET:
            field_dict["psk"] = psk

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        index = d.pop("index")

        global_ssid = d.pop("globalSsid")

        security = d.pop("security")

        enable = d.pop("enable")

        vlan_enable = d.pop("vlanEnable")

        ssid = d.pop("ssid")

        ssid_enable = d.pop("ssidEnable")

        hide_pwd = d.pop("hidePwd")

        band_info = d.pop("bandInfo", UNSET)

        support_bands = cast(list[int], d.pop("supportBands", UNSET))

        vlan_id = d.pop("vlanId", UNSET)

        psk = d.pop("psk", UNSET)

        osg_ssid_override_open_api_vo = cls(
            index=index,
            global_ssid=global_ssid,
            security=security,
            enable=enable,
            vlan_enable=vlan_enable,
            ssid=ssid,
            ssid_enable=ssid_enable,
            hide_pwd=hide_pwd,
            band_info=band_info,
            support_bands=support_bands,
            vlan_id=vlan_id,
            psk=psk,
        )

        osg_ssid_override_open_api_vo.additional_properties = d
        return osg_ssid_override_open_api_vo

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
