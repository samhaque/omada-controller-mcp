from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_bind_result_open_api_vo import DeviceBindResultOpenApiVO


T = TypeVar("T", bound="BatchBindDeviceResultOpenApiVO")


@_attrs_define
class BatchBindDeviceResultOpenApiVO:
    """
    Attributes:
        successed_devices (list[DeviceBindResultOpenApiVO] | Unset): Devices with successful operation.
        failed_devices (list[DeviceBindResultOpenApiVO] | Unset): Devices with failed operation.
    """

    successed_devices: list[DeviceBindResultOpenApiVO] | Unset = UNSET
    failed_devices: list[DeviceBindResultOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        successed_devices: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.successed_devices, Unset):
            successed_devices = []
            for successed_devices_item_data in self.successed_devices:
                successed_devices_item = successed_devices_item_data.to_dict()
                successed_devices.append(successed_devices_item)

        failed_devices: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.failed_devices, Unset):
            failed_devices = []
            for failed_devices_item_data in self.failed_devices:
                failed_devices_item = failed_devices_item_data.to_dict()
                failed_devices.append(failed_devices_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if successed_devices is not UNSET:
            field_dict["successedDevices"] = successed_devices
        if failed_devices is not UNSET:
            field_dict["failedDevices"] = failed_devices

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.device_bind_result_open_api_vo import (
            DeviceBindResultOpenApiVO,
        )

        d = dict(src_dict)
        _successed_devices = d.pop("successedDevices", UNSET)
        successed_devices: list[DeviceBindResultOpenApiVO] | Unset = UNSET
        if _successed_devices is not UNSET:
            successed_devices = []
            for successed_devices_item_data in _successed_devices:
                successed_devices_item = DeviceBindResultOpenApiVO.from_dict(
                    successed_devices_item_data
                )

                successed_devices.append(successed_devices_item)

        _failed_devices = d.pop("failedDevices", UNSET)
        failed_devices: list[DeviceBindResultOpenApiVO] | Unset = UNSET
        if _failed_devices is not UNSET:
            failed_devices = []
            for failed_devices_item_data in _failed_devices:
                failed_devices_item = DeviceBindResultOpenApiVO.from_dict(
                    failed_devices_item_data
                )

                failed_devices.append(failed_devices_item)

        batch_bind_device_result_open_api_vo = cls(
            successed_devices=successed_devices,
            failed_devices=failed_devices,
        )

        batch_bind_device_result_open_api_vo.additional_properties = d
        return batch_bind_device_result_open_api_vo

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
