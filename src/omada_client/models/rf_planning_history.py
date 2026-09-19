from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RFPlanningHistory")


@_attrs_define
class RFPlanningHistory:
    """
    Attributes:
        planning_histroy_id (str | Unset): Planning histroy ID.
        time (int | Unset): Timestamp corresponding to the start of optimization.
        channel_deploy_enable (bool | Unset): Whether to enable channel deployment.
        channel_width_deploy_enable (bool | Unset): Whether to enable channel width deployment.
        power_adjust_enable (bool | Unset): Whether to enable power adjustment.
        band_deploy_enable (bool | Unset): Whether to enable band deployment.
        before_index (int | Unset): Index before WLAN Optimization, between 0 and 100.
        after_index (int | Unset): Index after WLAN Optimization, between 0 and 100.
        ap_num (int | Unset): The number of EAPs.
        length (int | Unset): Parameter [length] means the duration of the WLAN Optimization in seconds.
        mode (int | Unset): 0: by WLAN Optimization schedule. 1: by one-click WLAN Optimization.
        is_scan_success (bool | Unset): True: Succeeded to obtain device scan results. False: Failed to obtain device
            scan results.
        is_applied_success (bool | Unset): True: Succeeded to apply settings recommended by the algorithm. False or
            null: Failed to apply settings recommended by the algorithm.
        current_config (int | Unset): 0: This entry does not correspond to the current configuration. 1: The recommended
            values are the current configuration. 2: The previous/origin values are the current configuration.
        msg (str | Unset):
        msg_type (int | Unset):
        failed_macs_2_g (str | Unset):
        failed_macs_5_g (str | Unset):
        failed_macs_6_g (str | Unset):
    """

    planning_histroy_id: str | Unset = UNSET
    time: int | Unset = UNSET
    channel_deploy_enable: bool | Unset = UNSET
    channel_width_deploy_enable: bool | Unset = UNSET
    power_adjust_enable: bool | Unset = UNSET
    band_deploy_enable: bool | Unset = UNSET
    before_index: int | Unset = UNSET
    after_index: int | Unset = UNSET
    ap_num: int | Unset = UNSET
    length: int | Unset = UNSET
    mode: int | Unset = UNSET
    is_scan_success: bool | Unset = UNSET
    is_applied_success: bool | Unset = UNSET
    current_config: int | Unset = UNSET
    msg: str | Unset = UNSET
    msg_type: int | Unset = UNSET
    failed_macs_2_g: str | Unset = UNSET
    failed_macs_5_g: str | Unset = UNSET
    failed_macs_6_g: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        planning_histroy_id = self.planning_histroy_id

        time = self.time

        channel_deploy_enable = self.channel_deploy_enable

        channel_width_deploy_enable = self.channel_width_deploy_enable

        power_adjust_enable = self.power_adjust_enable

        band_deploy_enable = self.band_deploy_enable

        before_index = self.before_index

        after_index = self.after_index

        ap_num = self.ap_num

        length = self.length

        mode = self.mode

        is_scan_success = self.is_scan_success

        is_applied_success = self.is_applied_success

        current_config = self.current_config

        msg = self.msg

        msg_type = self.msg_type

        failed_macs_2_g = self.failed_macs_2_g

        failed_macs_5_g = self.failed_macs_5_g

        failed_macs_6_g = self.failed_macs_6_g

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if planning_histroy_id is not UNSET:
            field_dict["planningHistroyId"] = planning_histroy_id
        if time is not UNSET:
            field_dict["time"] = time
        if channel_deploy_enable is not UNSET:
            field_dict["channelDeployEnable"] = channel_deploy_enable
        if channel_width_deploy_enable is not UNSET:
            field_dict["channelWidthDeployEnable"] = channel_width_deploy_enable
        if power_adjust_enable is not UNSET:
            field_dict["powerAdjustEnable"] = power_adjust_enable
        if band_deploy_enable is not UNSET:
            field_dict["bandDeployEnable"] = band_deploy_enable
        if before_index is not UNSET:
            field_dict["beforeIndex"] = before_index
        if after_index is not UNSET:
            field_dict["afterIndex"] = after_index
        if ap_num is not UNSET:
            field_dict["apNum"] = ap_num
        if length is not UNSET:
            field_dict["length"] = length
        if mode is not UNSET:
            field_dict["mode"] = mode
        if is_scan_success is not UNSET:
            field_dict["isScanSuccess"] = is_scan_success
        if is_applied_success is not UNSET:
            field_dict["isAppliedSuccess"] = is_applied_success
        if current_config is not UNSET:
            field_dict["currentConfig"] = current_config
        if msg is not UNSET:
            field_dict["msg"] = msg
        if msg_type is not UNSET:
            field_dict["msgType"] = msg_type
        if failed_macs_2_g is not UNSET:
            field_dict["failedMacs2g"] = failed_macs_2_g
        if failed_macs_5_g is not UNSET:
            field_dict["failedMacs5g"] = failed_macs_5_g
        if failed_macs_6_g is not UNSET:
            field_dict["failedMacs6g"] = failed_macs_6_g

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        planning_histroy_id = d.pop("planningHistroyId", UNSET)

        time = d.pop("time", UNSET)

        channel_deploy_enable = d.pop("channelDeployEnable", UNSET)

        channel_width_deploy_enable = d.pop("channelWidthDeployEnable", UNSET)

        power_adjust_enable = d.pop("powerAdjustEnable", UNSET)

        band_deploy_enable = d.pop("bandDeployEnable", UNSET)

        before_index = d.pop("beforeIndex", UNSET)

        after_index = d.pop("afterIndex", UNSET)

        ap_num = d.pop("apNum", UNSET)

        length = d.pop("length", UNSET)

        mode = d.pop("mode", UNSET)

        is_scan_success = d.pop("isScanSuccess", UNSET)

        is_applied_success = d.pop("isAppliedSuccess", UNSET)

        current_config = d.pop("currentConfig", UNSET)

        msg = d.pop("msg", UNSET)

        msg_type = d.pop("msgType", UNSET)

        failed_macs_2_g = d.pop("failedMacs2g", UNSET)

        failed_macs_5_g = d.pop("failedMacs5g", UNSET)

        failed_macs_6_g = d.pop("failedMacs6g", UNSET)

        rf_planning_history = cls(
            planning_histroy_id=planning_histroy_id,
            time=time,
            channel_deploy_enable=channel_deploy_enable,
            channel_width_deploy_enable=channel_width_deploy_enable,
            power_adjust_enable=power_adjust_enable,
            band_deploy_enable=band_deploy_enable,
            before_index=before_index,
            after_index=after_index,
            ap_num=ap_num,
            length=length,
            mode=mode,
            is_scan_success=is_scan_success,
            is_applied_success=is_applied_success,
            current_config=current_config,
            msg=msg,
            msg_type=msg_type,
            failed_macs_2_g=failed_macs_2_g,
            failed_macs_5_g=failed_macs_5_g,
            failed_macs_6_g=failed_macs_6_g,
        )

        rf_planning_history.additional_properties = d
        return rf_planning_history

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
