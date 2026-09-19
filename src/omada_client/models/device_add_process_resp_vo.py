from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sn_add_result_vo import SnAddResultVO


T = TypeVar("T", bound="DeviceAddProcessRespVO")


@_attrs_define
class DeviceAddProcessRespVO:
    """
    Attributes:
        process_status (int | Unset): It should be a value as follows: 0: init; 1: doing; 2: done
        devices (list[SnAddResultVO] | Unset): Devices add result
    """

    process_status: int | Unset = UNSET
    devices: list[SnAddResultVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        process_status = self.process_status

        devices: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.devices, Unset):
            devices = []
            for devices_item_data in self.devices:
                devices_item = devices_item_data.to_dict()
                devices.append(devices_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if process_status is not UNSET:
            field_dict["processStatus"] = process_status
        if devices is not UNSET:
            field_dict["devices"] = devices

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.sn_add_result_vo import SnAddResultVO

        d = dict(src_dict)
        process_status = d.pop("processStatus", UNSET)

        _devices = d.pop("devices", UNSET)
        devices: list[SnAddResultVO] | Unset = UNSET
        if _devices is not UNSET:
            devices = []
            for devices_item_data in _devices:
                devices_item = SnAddResultVO.from_dict(devices_item_data)

                devices.append(devices_item)

        device_add_process_resp_vo = cls(
            process_status=process_status,
            devices=devices,
        )

        device_add_process_resp_vo.additional_properties = d
        return device_add_process_resp_vo

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
