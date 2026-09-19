from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dialup_setting_open_api_vo import DialupSettingOpenApiVO


T = TypeVar("T", bound="LteWanPortSettingConfigOpenApiVO")


@_attrs_define
class LteWanPortSettingConfigOpenApiVO:
    """
    Attributes:
        port_id (str): Port ID
        mobile_data (bool): mobile data
        data_roaming (bool): First SIM card's data roaming
        network_mode (int): First SIM card's networkMode: 1:3G Only, 2:4G Only, 3:4G Preferred4: 5G-NSA/4G, 5: 5G-SA, 6:
            5G/4G/3G
        dialup_setting (DialupSettingOpenApiVO): Second SIM card's dial-up setting
        port_description (str | Unset): Port description should contain 1 to 32 characters.
        sim_priority (int | Unset): Set which SIM card is used first. SIM Priority takes effect only when the device is
            powered on and the priority is changed. If only one SIM card is inserted, this card is used by default.
        band_mode (int | Unset): First SIM card's bandMode: 0:auto, 1:manual, only for networkMode 4g Only and 4G
            Preferred
        bands (list[str] | Unset): First SIM card's bands. Only for band mode manual
        bands5g (list[str] | Unset): First SIM card's. Only for band mode manual
        failover_timeout (int | Unset): First SIM card's failoverTimeout. Set the dial-up timeout (100 to 3552 seconds).
            If the connection is not successfully established within the specified time, the gateway will use the other SIM
            card to connect to the internet.
        data_roaming_2 (bool | Unset): Second SIM card's data roaming
        network_mode_2 (int | Unset): Second SIM card's networkMode: 1:3G Only, 2:4G Only, 3:4G Preferred4: 5G-NSA/4G,
            5: 5G-SA, 6: 5G/4G/3G
        band_mode_2 (int | Unset): Second SIM card's bandMode: 0:auto, 1:manual, only for networkMode 4g Only and 4G
            Preferred
        bands2 (list[str] | Unset): Second SIM card's bands. Only for band mode manual
        bands5g2 (list[str] | Unset): Second SIM card's. Only for band mode manual
        dialup_setting_2 (DialupSettingOpenApiVO | Unset): Second SIM card's dial-up setting
        failover_timeout_2 (int | Unset): Second SIM card's failoverTimeout. Set the dial-up timeout (100 to 3552
            seconds). If the connection is not successfully established within the specified time, the gateway will use the
            other SIM card to connect to the internet.
    """

    port_id: str
    mobile_data: bool
    data_roaming: bool
    network_mode: int
    dialup_setting: DialupSettingOpenApiVO
    port_description: str | Unset = UNSET
    sim_priority: int | Unset = UNSET
    band_mode: int | Unset = UNSET
    bands: list[str] | Unset = UNSET
    bands5g: list[str] | Unset = UNSET
    failover_timeout: int | Unset = UNSET
    data_roaming_2: bool | Unset = UNSET
    network_mode_2: int | Unset = UNSET
    band_mode_2: int | Unset = UNSET
    bands2: list[str] | Unset = UNSET
    bands5g2: list[str] | Unset = UNSET
    dialup_setting_2: DialupSettingOpenApiVO | Unset = UNSET
    failover_timeout_2: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_id = self.port_id

        mobile_data = self.mobile_data

        data_roaming = self.data_roaming

        network_mode = self.network_mode

        dialup_setting = self.dialup_setting.to_dict()

        port_description = self.port_description

        sim_priority = self.sim_priority

        band_mode = self.band_mode

        bands: list[str] | Unset = UNSET
        if not isinstance(self.bands, Unset):
            bands = self.bands

        bands5g: list[str] | Unset = UNSET
        if not isinstance(self.bands5g, Unset):
            bands5g = self.bands5g

        failover_timeout = self.failover_timeout

        data_roaming_2 = self.data_roaming_2

        network_mode_2 = self.network_mode_2

        band_mode_2 = self.band_mode_2

        bands2: list[str] | Unset = UNSET
        if not isinstance(self.bands2, Unset):
            bands2 = self.bands2

        bands5g2: list[str] | Unset = UNSET
        if not isinstance(self.bands5g2, Unset):
            bands5g2 = self.bands5g2

        dialup_setting_2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dialup_setting_2, Unset):
            dialup_setting_2 = self.dialup_setting_2.to_dict()

        failover_timeout_2 = self.failover_timeout_2

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "portId": port_id,
                "mobileData": mobile_data,
                "dataRoaming": data_roaming,
                "networkMode": network_mode,
                "dialupSetting": dialup_setting,
            }
        )
        if port_description is not UNSET:
            field_dict["portDescription"] = port_description
        if sim_priority is not UNSET:
            field_dict["simPriority"] = sim_priority
        if band_mode is not UNSET:
            field_dict["bandMode"] = band_mode
        if bands is not UNSET:
            field_dict["bands"] = bands
        if bands5g is not UNSET:
            field_dict["bands5g"] = bands5g
        if failover_timeout is not UNSET:
            field_dict["failoverTimeout"] = failover_timeout
        if data_roaming_2 is not UNSET:
            field_dict["dataRoaming2"] = data_roaming_2
        if network_mode_2 is not UNSET:
            field_dict["networkMode2"] = network_mode_2
        if band_mode_2 is not UNSET:
            field_dict["bandMode2"] = band_mode_2
        if bands2 is not UNSET:
            field_dict["bands2"] = bands2
        if bands5g2 is not UNSET:
            field_dict["bands5g2"] = bands5g2
        if dialup_setting_2 is not UNSET:
            field_dict["dialupSetting2"] = dialup_setting_2
        if failover_timeout_2 is not UNSET:
            field_dict["failoverTimeout2"] = failover_timeout_2

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.dialup_setting_open_api_vo import (
            DialupSettingOpenApiVO,
        )

        d = dict(src_dict)
        port_id = d.pop("portId")

        mobile_data = d.pop("mobileData")

        data_roaming = d.pop("dataRoaming")

        network_mode = d.pop("networkMode")

        dialup_setting = DialupSettingOpenApiVO.from_dict(d.pop("dialupSetting"))

        port_description = d.pop("portDescription", UNSET)

        sim_priority = d.pop("simPriority", UNSET)

        band_mode = d.pop("bandMode", UNSET)

        bands = cast(list[str], d.pop("bands", UNSET))

        bands5g = cast(list[str], d.pop("bands5g", UNSET))

        failover_timeout = d.pop("failoverTimeout", UNSET)

        data_roaming_2 = d.pop("dataRoaming2", UNSET)

        network_mode_2 = d.pop("networkMode2", UNSET)

        band_mode_2 = d.pop("bandMode2", UNSET)

        bands2 = cast(list[str], d.pop("bands2", UNSET))

        bands5g2 = cast(list[str], d.pop("bands5g2", UNSET))

        _dialup_setting_2 = d.pop("dialupSetting2", UNSET)
        dialup_setting_2: DialupSettingOpenApiVO | Unset
        if isinstance(_dialup_setting_2, Unset):
            dialup_setting_2 = UNSET
        else:
            dialup_setting_2 = DialupSettingOpenApiVO.from_dict(_dialup_setting_2)

        failover_timeout_2 = d.pop("failoverTimeout2", UNSET)

        lte_wan_port_setting_config_open_api_vo = cls(
            port_id=port_id,
            mobile_data=mobile_data,
            data_roaming=data_roaming,
            network_mode=network_mode,
            dialup_setting=dialup_setting,
            port_description=port_description,
            sim_priority=sim_priority,
            band_mode=band_mode,
            bands=bands,
            bands5g=bands5g,
            failover_timeout=failover_timeout,
            data_roaming_2=data_roaming_2,
            network_mode_2=network_mode_2,
            band_mode_2=band_mode_2,
            bands2=bands2,
            bands5g2=bands5g2,
            dialup_setting_2=dialup_setting_2,
            failover_timeout_2=failover_timeout_2,
        )

        lte_wan_port_setting_config_open_api_vo.additional_properties = d
        return lte_wan_port_setting_config_open_api_vo

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
