from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_object_dto_lag_ports_map import DeviceObjectDTOLagPortsMap


T = TypeVar("T", bound="DeviceObjectDTO")


@_attrs_define
class DeviceObjectDTO:
    """Device objects map used by this advice. Key is MAC address, value is device info.

    Attributes:
        name (str | Unset): Default uses the MAC address as the name.
        type_ (str | Unset): Device type:ap、gateway、switch、olt.
        model (str | Unset): Device model, such as EAP225.
        model_version (str | Unset): Model version of device, for example:3.0.
        ip (str | Unset): Ip address,such as 192.168.0.105.
        port_num (int | Unset): Number of ports.
        lag_ports_map (DeviceObjectDTOLagPortsMap | Unset): Switch LAG ports map. Key is LAG ID, value is member port
            set.
        support_anomaly (bool | Unset): Whether the device firmware support intelligent anomaly detection.
        support5g (bool | Unset): Whether the device supports 5 GHz radio.
        support5g2 (bool | Unset): Whether the device supports 5 GHZ-2 radio.
        support6g (bool | Unset): Whether the device supports 6 GHz radio.
        ap_temp_thresholds (list[int] | Unset): AP temperature thresholds.
        osw_cpu_temp_threshold (int | Unset): Switch CPU temperature threshold.
        osw_mac_temp_threshold (int | Unset): Switch MAC chip temperature threshold.
        osw_pse_temp_threshold (int | Unset): Switch PSE temperature threshold.
        osw_phy_temp_threshold (int | Unset): Switch PHY temperature threshold.
        osg_temp_threshold (int | Unset): Gateway temperature threshold.
        radio_2_g_enable (bool | Unset): Whether 2.4 GHz radio is enabled.
        radio_5_g_enable (bool | Unset): Whether 5 GHz radio is enabled.
        radio_5_g_2_enable (bool | Unset): Whether 5 GHz-2 radio is enabled.
        radio_6_g_enable (bool | Unset): Whether 6 GHz radio is enabled.
        filled_temp_threshold (bool | Unset): Whether temperature threshold fields have been filled.
        device_series_type (int | Unset): Device series type. 0: Advanced, 1: Pro.
    """

    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    ip: str | Unset = UNSET
    port_num: int | Unset = UNSET
    lag_ports_map: DeviceObjectDTOLagPortsMap | Unset = UNSET
    support_anomaly: bool | Unset = UNSET
    support5g: bool | Unset = UNSET
    support5g2: bool | Unset = UNSET
    support6g: bool | Unset = UNSET
    ap_temp_thresholds: list[int] | Unset = UNSET
    osw_cpu_temp_threshold: int | Unset = UNSET
    osw_mac_temp_threshold: int | Unset = UNSET
    osw_pse_temp_threshold: int | Unset = UNSET
    osw_phy_temp_threshold: int | Unset = UNSET
    osg_temp_threshold: int | Unset = UNSET
    radio_2_g_enable: bool | Unset = UNSET
    radio_5_g_enable: bool | Unset = UNSET
    radio_5_g_2_enable: bool | Unset = UNSET
    radio_6_g_enable: bool | Unset = UNSET
    filled_temp_threshold: bool | Unset = UNSET
    device_series_type: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        model = self.model

        model_version = self.model_version

        ip = self.ip

        port_num = self.port_num

        lag_ports_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lag_ports_map, Unset):
            lag_ports_map = self.lag_ports_map.to_dict()

        support_anomaly = self.support_anomaly

        support5g = self.support5g

        support5g2 = self.support5g2

        support6g = self.support6g

        ap_temp_thresholds: list[int] | Unset = UNSET
        if not isinstance(self.ap_temp_thresholds, Unset):
            ap_temp_thresholds = self.ap_temp_thresholds

        osw_cpu_temp_threshold = self.osw_cpu_temp_threshold

        osw_mac_temp_threshold = self.osw_mac_temp_threshold

        osw_pse_temp_threshold = self.osw_pse_temp_threshold

        osw_phy_temp_threshold = self.osw_phy_temp_threshold

        osg_temp_threshold = self.osg_temp_threshold

        radio_2_g_enable = self.radio_2_g_enable

        radio_5_g_enable = self.radio_5_g_enable

        radio_5_g_2_enable = self.radio_5_g_2_enable

        radio_6_g_enable = self.radio_6_g_enable

        filled_temp_threshold = self.filled_temp_threshold

        device_series_type = self.device_series_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if ip is not UNSET:
            field_dict["ip"] = ip
        if port_num is not UNSET:
            field_dict["portNum"] = port_num
        if lag_ports_map is not UNSET:
            field_dict["lagPortsMap"] = lag_ports_map
        if support_anomaly is not UNSET:
            field_dict["supportAnomaly"] = support_anomaly
        if support5g is not UNSET:
            field_dict["support5g"] = support5g
        if support5g2 is not UNSET:
            field_dict["support5g2"] = support5g2
        if support6g is not UNSET:
            field_dict["support6g"] = support6g
        if ap_temp_thresholds is not UNSET:
            field_dict["apTempThresholds"] = ap_temp_thresholds
        if osw_cpu_temp_threshold is not UNSET:
            field_dict["oswCpuTempThreshold"] = osw_cpu_temp_threshold
        if osw_mac_temp_threshold is not UNSET:
            field_dict["oswMacTempThreshold"] = osw_mac_temp_threshold
        if osw_pse_temp_threshold is not UNSET:
            field_dict["oswPseTempThreshold"] = osw_pse_temp_threshold
        if osw_phy_temp_threshold is not UNSET:
            field_dict["oswPhyTempThreshold"] = osw_phy_temp_threshold
        if osg_temp_threshold is not UNSET:
            field_dict["osgTempThreshold"] = osg_temp_threshold
        if radio_2_g_enable is not UNSET:
            field_dict["radio2gEnable"] = radio_2_g_enable
        if radio_5_g_enable is not UNSET:
            field_dict["radio5gEnable"] = radio_5_g_enable
        if radio_5_g_2_enable is not UNSET:
            field_dict["radio5g2Enable"] = radio_5_g_2_enable
        if radio_6_g_enable is not UNSET:
            field_dict["radio6gEnable"] = radio_6_g_enable
        if filled_temp_threshold is not UNSET:
            field_dict["filledTempThreshold"] = filled_temp_threshold
        if device_series_type is not UNSET:
            field_dict["deviceSeriesType"] = device_series_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.device_object_dto_lag_ports_map import (
            DeviceObjectDTOLagPortsMap,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        ip = d.pop("ip", UNSET)

        port_num = d.pop("portNum", UNSET)

        _lag_ports_map = d.pop("lagPortsMap", UNSET)
        lag_ports_map: DeviceObjectDTOLagPortsMap | Unset
        if isinstance(_lag_ports_map, Unset):
            lag_ports_map = UNSET
        else:
            lag_ports_map = DeviceObjectDTOLagPortsMap.from_dict(_lag_ports_map)

        support_anomaly = d.pop("supportAnomaly", UNSET)

        support5g = d.pop("support5g", UNSET)

        support5g2 = d.pop("support5g2", UNSET)

        support6g = d.pop("support6g", UNSET)

        ap_temp_thresholds = cast(list[int], d.pop("apTempThresholds", UNSET))

        osw_cpu_temp_threshold = d.pop("oswCpuTempThreshold", UNSET)

        osw_mac_temp_threshold = d.pop("oswMacTempThreshold", UNSET)

        osw_pse_temp_threshold = d.pop("oswPseTempThreshold", UNSET)

        osw_phy_temp_threshold = d.pop("oswPhyTempThreshold", UNSET)

        osg_temp_threshold = d.pop("osgTempThreshold", UNSET)

        radio_2_g_enable = d.pop("radio2gEnable", UNSET)

        radio_5_g_enable = d.pop("radio5gEnable", UNSET)

        radio_5_g_2_enable = d.pop("radio5g2Enable", UNSET)

        radio_6_g_enable = d.pop("radio6gEnable", UNSET)

        filled_temp_threshold = d.pop("filledTempThreshold", UNSET)

        device_series_type = d.pop("deviceSeriesType", UNSET)

        device_object_dto = cls(
            name=name,
            type_=type_,
            model=model,
            model_version=model_version,
            ip=ip,
            port_num=port_num,
            lag_ports_map=lag_ports_map,
            support_anomaly=support_anomaly,
            support5g=support5g,
            support5g2=support5g2,
            support6g=support6g,
            ap_temp_thresholds=ap_temp_thresholds,
            osw_cpu_temp_threshold=osw_cpu_temp_threshold,
            osw_mac_temp_threshold=osw_mac_temp_threshold,
            osw_pse_temp_threshold=osw_pse_temp_threshold,
            osw_phy_temp_threshold=osw_phy_temp_threshold,
            osg_temp_threshold=osg_temp_threshold,
            radio_2_g_enable=radio_2_g_enable,
            radio_5_g_enable=radio_5_g_enable,
            radio_5_g_2_enable=radio_5_g_2_enable,
            radio_6_g_enable=radio_6_g_enable,
            filled_temp_threshold=filled_temp_threshold,
            device_series_type=device_series_type,
        )

        device_object_dto.additional_properties = d
        return device_object_dto

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
