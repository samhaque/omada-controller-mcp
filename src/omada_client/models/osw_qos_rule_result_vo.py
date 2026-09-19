from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qos_rule_device_info import QosRuleDeviceInfo


T = TypeVar("T", bound="OswQosRuleResultVO")


@_attrs_define
class OswQosRuleResultVO:
    """
    Attributes:
        fail_devices (list[QosRuleDeviceInfo] | Unset): List of device information for which QoS rules failed to be
            issued.
        success_devices (list[QosRuleDeviceInfo] | Unset): List of device information for which QoS rules have been
            successfully issued.
    """

    fail_devices: list[QosRuleDeviceInfo] | Unset = UNSET
    success_devices: list[QosRuleDeviceInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fail_devices: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fail_devices, Unset):
            fail_devices = []
            for fail_devices_item_data in self.fail_devices:
                fail_devices_item = fail_devices_item_data.to_dict()
                fail_devices.append(fail_devices_item)

        success_devices: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.success_devices, Unset):
            success_devices = []
            for success_devices_item_data in self.success_devices:
                success_devices_item = success_devices_item_data.to_dict()
                success_devices.append(success_devices_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fail_devices is not UNSET:
            field_dict["failDevices"] = fail_devices
        if success_devices is not UNSET:
            field_dict["successDevices"] = success_devices

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.qos_rule_device_info import QosRuleDeviceInfo

        d = dict(src_dict)
        _fail_devices = d.pop("failDevices", UNSET)
        fail_devices: list[QosRuleDeviceInfo] | Unset = UNSET
        if _fail_devices is not UNSET:
            fail_devices = []
            for fail_devices_item_data in _fail_devices:
                fail_devices_item = QosRuleDeviceInfo.from_dict(fail_devices_item_data)

                fail_devices.append(fail_devices_item)

        _success_devices = d.pop("successDevices", UNSET)
        success_devices: list[QosRuleDeviceInfo] | Unset = UNSET
        if _success_devices is not UNSET:
            success_devices = []
            for success_devices_item_data in _success_devices:
                success_devices_item = QosRuleDeviceInfo.from_dict(
                    success_devices_item_data
                )

                success_devices.append(success_devices_item)

        osw_qos_rule_result_vo = cls(
            fail_devices=fail_devices,
            success_devices=success_devices,
        )

        osw_qos_rule_result_vo.additional_properties = d
        return osw_qos_rule_result_vo

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
