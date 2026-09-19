from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_planning_history_detail_vo import ApPlanningHistoryDetailVO


T = TypeVar("T", bound="PlanningHistoryDetail")


@_attrs_define
class PlanningHistoryDetail:
    """
    Attributes:
        channel_deploy_enable (bool | Unset): Whether to enable channel deployment.
        channel_width_deploy_enable (bool | Unset): Whether to enable channel width deployment.
        band_deploy_enable (bool | Unset): Whether to enable band deployment.
        power_adjust_enable (bool | Unset): Whether to enable power adjustment.
        time (int | Unset): Timestamp corresponding to the start of optimization.
        current_config (int | Unset): 0: This entry does not correspond to the current configuration. 1: The recommended
            values are the current configuration. 2: The previous/origin values are the current configuration.
        success_devices (int | Unset): The number of devices which have been successfully optimized.
        fail_devices (int | Unset): The number of devices which have been optimized unsuccessfully.
        data (list[ApPlanningHistoryDetailVO] | Unset): Optimization history details.
    """

    channel_deploy_enable: bool | Unset = UNSET
    channel_width_deploy_enable: bool | Unset = UNSET
    band_deploy_enable: bool | Unset = UNSET
    power_adjust_enable: bool | Unset = UNSET
    time: int | Unset = UNSET
    current_config: int | Unset = UNSET
    success_devices: int | Unset = UNSET
    fail_devices: int | Unset = UNSET
    data: list[ApPlanningHistoryDetailVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel_deploy_enable = self.channel_deploy_enable

        channel_width_deploy_enable = self.channel_width_deploy_enable

        band_deploy_enable = self.band_deploy_enable

        power_adjust_enable = self.power_adjust_enable

        time = self.time

        current_config = self.current_config

        success_devices = self.success_devices

        fail_devices = self.fail_devices

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel_deploy_enable is not UNSET:
            field_dict["channelDeployEnable"] = channel_deploy_enable
        if channel_width_deploy_enable is not UNSET:
            field_dict["channelWidthDeployEnable"] = channel_width_deploy_enable
        if band_deploy_enable is not UNSET:
            field_dict["bandDeployEnable"] = band_deploy_enable
        if power_adjust_enable is not UNSET:
            field_dict["powerAdjustEnable"] = power_adjust_enable
        if time is not UNSET:
            field_dict["time"] = time
        if current_config is not UNSET:
            field_dict["currentConfig"] = current_config
        if success_devices is not UNSET:
            field_dict["successDevices"] = success_devices
        if fail_devices is not UNSET:
            field_dict["failDevices"] = fail_devices
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_planning_history_detail_vo import (
            ApPlanningHistoryDetailVO,
        )

        d = dict(src_dict)
        channel_deploy_enable = d.pop("channelDeployEnable", UNSET)

        channel_width_deploy_enable = d.pop("channelWidthDeployEnable", UNSET)

        band_deploy_enable = d.pop("bandDeployEnable", UNSET)

        power_adjust_enable = d.pop("powerAdjustEnable", UNSET)

        time = d.pop("time", UNSET)

        current_config = d.pop("currentConfig", UNSET)

        success_devices = d.pop("successDevices", UNSET)

        fail_devices = d.pop("failDevices", UNSET)

        _data = d.pop("data", UNSET)
        data: list[ApPlanningHistoryDetailVO] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = ApPlanningHistoryDetailVO.from_dict(data_item_data)

                data.append(data_item)

        planning_history_detail = cls(
            channel_deploy_enable=channel_deploy_enable,
            channel_width_deploy_enable=channel_width_deploy_enable,
            band_deploy_enable=band_deploy_enable,
            power_adjust_enable=power_adjust_enable,
            time=time,
            current_config=current_config,
            success_devices=success_devices,
            fail_devices=fail_devices,
            data=data,
        )

        planning_history_detail.additional_properties = d
        return planning_history_detail

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
