from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DialupSettingOpenApiV2VO")


@_attrs_define
class DialupSettingOpenApiV2VO:
    """Second SIM card's dial-up setting

    Attributes:
        network_search (int): Network search mode should be a value as follows: 0: auto; 1: manual.
        apn_mode (int): Apn mode should be a value as follows: 0: auto; 1: manual.
        data_roaming (bool): SIM card's data roaming
        network_mode (int): SIM card's networkMode: 1:3G Only, 2:4G Only, 3:4G Preferred4: 5G-NSA/4G, 5: 5G-SA, 6:
            5G/4G/3G
        isp (str | Unset): Only for networkSearch mode manual.
        isp_num (int | Unset): Only for networkSearch mode manual.
        apn (str | Unset): APN profile ID, only for apnMode manual
        failover_timeout (int | Unset): SIM card's failoverTimeout. Set the dial-up timeout (100 to 3552 seconds). If
            the connection is not successfully established within the specified time, the gateway will use the other SIM
            card to connect to the internet.
        band_mode (int | Unset): SIM card's bandMode: 0:auto, 1:manual, only for networkMode 4g Only and 4G Preferred
        bands (list[str] | Unset): SIM card's 5g bands. Only for band mode manual
    """

    network_search: int
    apn_mode: int
    data_roaming: bool
    network_mode: int
    isp: str | Unset = UNSET
    isp_num: int | Unset = UNSET
    apn: str | Unset = UNSET
    failover_timeout: int | Unset = UNSET
    band_mode: int | Unset = UNSET
    bands: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network_search = self.network_search

        apn_mode = self.apn_mode

        data_roaming = self.data_roaming

        network_mode = self.network_mode

        isp = self.isp

        isp_num = self.isp_num

        apn = self.apn

        failover_timeout = self.failover_timeout

        band_mode = self.band_mode

        bands: list[str] | Unset = UNSET
        if not isinstance(self.bands, Unset):
            bands = self.bands

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "networkSearch": network_search,
                "apnMode": apn_mode,
                "dataRoaming": data_roaming,
                "networkMode": network_mode,
            }
        )
        if isp is not UNSET:
            field_dict["isp"] = isp
        if isp_num is not UNSET:
            field_dict["ispNum"] = isp_num
        if apn is not UNSET:
            field_dict["apn"] = apn
        if failover_timeout is not UNSET:
            field_dict["failoverTimeout"] = failover_timeout
        if band_mode is not UNSET:
            field_dict["bandMode"] = band_mode
        if bands is not UNSET:
            field_dict["bands"] = bands

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        network_search = d.pop("networkSearch")

        apn_mode = d.pop("apnMode")

        data_roaming = d.pop("dataRoaming")

        network_mode = d.pop("networkMode")

        isp = d.pop("isp", UNSET)

        isp_num = d.pop("ispNum", UNSET)

        apn = d.pop("apn", UNSET)

        failover_timeout = d.pop("failoverTimeout", UNSET)

        band_mode = d.pop("bandMode", UNSET)

        bands = cast(list[str], d.pop("bands", UNSET))

        dialup_setting_open_api_v2vo = cls(
            network_search=network_search,
            apn_mode=apn_mode,
            data_roaming=data_roaming,
            network_mode=network_mode,
            isp=isp,
            isp_num=isp_num,
            apn=apn,
            failover_timeout=failover_timeout,
            band_mode=band_mode,
            bands=bands,
        )

        dialup_setting_open_api_v2vo.additional_properties = d
        return dialup_setting_open_api_v2vo

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
