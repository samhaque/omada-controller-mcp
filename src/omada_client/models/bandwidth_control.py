from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bandwidth_port_setting import BandwidthPortSetting


T = TypeVar("T", bound="BandwidthControl")


@_attrs_define
class BandwidthControl:
    """
    Attributes:
        enable (bool): Enable the bandwidth control.
        threshold_control_enable (bool | Unset): Enable the threshold control of the bandwidth control.
        threshold_value (int | Unset): Threshold value should be within the range of 1–100. Threshold value must be
            entered when threshold control is enable.
        bandwidth_port_settings (list[BandwidthPortSetting] | Unset): Bandwidth port settings of the bandwidth control.
    """

    enable: bool
    threshold_control_enable: bool | Unset = UNSET
    threshold_value: int | Unset = UNSET
    bandwidth_port_settings: list[BandwidthPortSetting] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        threshold_control_enable = self.threshold_control_enable

        threshold_value = self.threshold_value

        bandwidth_port_settings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.bandwidth_port_settings, Unset):
            bandwidth_port_settings = []
            for bandwidth_port_settings_item_data in self.bandwidth_port_settings:
                bandwidth_port_settings_item = (
                    bandwidth_port_settings_item_data.to_dict()
                )
                bandwidth_port_settings.append(bandwidth_port_settings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
            }
        )
        if threshold_control_enable is not UNSET:
            field_dict["thresholdControlEnable"] = threshold_control_enable
        if threshold_value is not UNSET:
            field_dict["thresholdValue"] = threshold_value
        if bandwidth_port_settings is not UNSET:
            field_dict["bandwidthPortSettings"] = bandwidth_port_settings

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.bandwidth_port_setting import (
            BandwidthPortSetting,
        )

        d = dict(src_dict)
        enable = d.pop("enable")

        threshold_control_enable = d.pop("thresholdControlEnable", UNSET)

        threshold_value = d.pop("thresholdValue", UNSET)

        _bandwidth_port_settings = d.pop("bandwidthPortSettings", UNSET)
        bandwidth_port_settings: list[BandwidthPortSetting] | Unset = UNSET
        if _bandwidth_port_settings is not UNSET:
            bandwidth_port_settings = []
            for bandwidth_port_settings_item_data in _bandwidth_port_settings:
                bandwidth_port_settings_item = BandwidthPortSetting.from_dict(
                    bandwidth_port_settings_item_data
                )

                bandwidth_port_settings.append(bandwidth_port_settings_item)

        bandwidth_control = cls(
            enable=enable,
            threshold_control_enable=threshold_control_enable,
            threshold_value=threshold_value,
            bandwidth_port_settings=bandwidth_port_settings,
        )

        bandwidth_control.additional_properties = d
        return bandwidth_control

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
