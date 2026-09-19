from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SsidOverrideVO")


@_attrs_define
class SsidOverrideVO:
    """
    Attributes:
        index (int):
        enable (bool):
        global_ssid (str | Unset):
        band_info (int | Unset):
        support_bands (list[int] | Unset):
        security (int | Unset):
        vlan_enable (bool | Unset):
        vlan_id (int | Unset):
        vlan_pool_ids (str | Unset):
        ssid (str | Unset):
        psk (str | Unset):
        ssid_enable (bool | Unset):
        hide_pwd (bool | Unset):
        ssid_configurable (bool | Unset):
    """

    index: int
    enable: bool
    global_ssid: str | Unset = UNSET
    band_info: int | Unset = UNSET
    support_bands: list[int] | Unset = UNSET
    security: int | Unset = UNSET
    vlan_enable: bool | Unset = UNSET
    vlan_id: int | Unset = UNSET
    vlan_pool_ids: str | Unset = UNSET
    ssid: str | Unset = UNSET
    psk: str | Unset = UNSET
    ssid_enable: bool | Unset = UNSET
    hide_pwd: bool | Unset = UNSET
    ssid_configurable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        index = self.index

        enable = self.enable

        global_ssid = self.global_ssid

        band_info = self.band_info

        support_bands: list[int] | Unset = UNSET
        if not isinstance(self.support_bands, Unset):
            support_bands = self.support_bands

        security = self.security

        vlan_enable = self.vlan_enable

        vlan_id = self.vlan_id

        vlan_pool_ids = self.vlan_pool_ids

        ssid = self.ssid

        psk = self.psk

        ssid_enable = self.ssid_enable

        hide_pwd = self.hide_pwd

        ssid_configurable = self.ssid_configurable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "index": index,
                "enable": enable,
            }
        )
        if global_ssid is not UNSET:
            field_dict["globalSsid"] = global_ssid
        if band_info is not UNSET:
            field_dict["bandInfo"] = band_info
        if support_bands is not UNSET:
            field_dict["supportBands"] = support_bands
        if security is not UNSET:
            field_dict["security"] = security
        if vlan_enable is not UNSET:
            field_dict["vlanEnable"] = vlan_enable
        if vlan_id is not UNSET:
            field_dict["vlanId"] = vlan_id
        if vlan_pool_ids is not UNSET:
            field_dict["vlanPoolIds"] = vlan_pool_ids
        if ssid is not UNSET:
            field_dict["ssid"] = ssid
        if psk is not UNSET:
            field_dict["psk"] = psk
        if ssid_enable is not UNSET:
            field_dict["ssidEnable"] = ssid_enable
        if hide_pwd is not UNSET:
            field_dict["hidePwd"] = hide_pwd
        if ssid_configurable is not UNSET:
            field_dict["ssidConfigurable"] = ssid_configurable

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        index = d.pop("index")

        enable = d.pop("enable")

        global_ssid = d.pop("globalSsid", UNSET)

        band_info = d.pop("bandInfo", UNSET)

        support_bands = cast(list[int], d.pop("supportBands", UNSET))

        security = d.pop("security", UNSET)

        vlan_enable = d.pop("vlanEnable", UNSET)

        vlan_id = d.pop("vlanId", UNSET)

        vlan_pool_ids = d.pop("vlanPoolIds", UNSET)

        ssid = d.pop("ssid", UNSET)

        psk = d.pop("psk", UNSET)

        ssid_enable = d.pop("ssidEnable", UNSET)

        hide_pwd = d.pop("hidePwd", UNSET)

        ssid_configurable = d.pop("ssidConfigurable", UNSET)

        ssid_override_vo = cls(
            index=index,
            enable=enable,
            global_ssid=global_ssid,
            band_info=band_info,
            support_bands=support_bands,
            security=security,
            vlan_enable=vlan_enable,
            vlan_id=vlan_id,
            vlan_pool_ids=vlan_pool_ids,
            ssid=ssid,
            psk=psk,
            ssid_enable=ssid_enable,
            hide_pwd=hide_pwd,
            ssid_configurable=ssid_configurable,
        )

        ssid_override_vo.additional_properties = d
        return ssid_override_vo

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
