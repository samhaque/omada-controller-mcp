from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DialupSettingOpenApiVO")


@_attrs_define
class DialupSettingOpenApiVO:
    """Second SIM card's dial-up setting

    Attributes:
        network_search (int): Network search mode should be a value as follows: 0: auto; 1: manual.
        apn_mode (int): Apn mode should be a value as follows: 0: auto; 1: manual.
        isp (str | Unset): Only for networkSearch mode manual and the ISP from the scan result must be available.
        isp_num (int | Unset): Only for networkSearch mode manual and the ISP from the scan result must be available.
        apn (str | Unset): APN profile ID, only for apnMode manual
    """

    network_search: int
    apn_mode: int
    isp: str | Unset = UNSET
    isp_num: int | Unset = UNSET
    apn: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network_search = self.network_search

        apn_mode = self.apn_mode

        isp = self.isp

        isp_num = self.isp_num

        apn = self.apn

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "networkSearch": network_search,
                "apnMode": apn_mode,
            }
        )
        if isp is not UNSET:
            field_dict["isp"] = isp
        if isp_num is not UNSET:
            field_dict["ispNum"] = isp_num
        if apn is not UNSET:
            field_dict["apn"] = apn

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        network_search = d.pop("networkSearch")

        apn_mode = d.pop("apnMode")

        isp = d.pop("isp", UNSET)

        isp_num = d.pop("ispNum", UNSET)

        apn = d.pop("apn", UNSET)

        dialup_setting_open_api_vo = cls(
            network_search=network_search,
            apn_mode=apn_mode,
            isp=isp,
            isp_num=isp_num,
            apn=apn,
        )

        dialup_setting_open_api_vo.additional_properties = d
        return dialup_setting_open_api_vo

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
