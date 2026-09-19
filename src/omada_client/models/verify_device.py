from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitor_device import MonitorDevice


T = TypeVar("T", bound="VerifyDevice")


@_attrs_define
class VerifyDevice:
    """
    Attributes:
        monitor_device (MonitorDevice | Unset): The device to be verified whether it can be monitored
    """

    monitor_device: MonitorDevice | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        monitor_device: dict[str, Any] | Unset = UNSET
        if not isinstance(self.monitor_device, Unset):
            monitor_device = self.monitor_device.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if monitor_device is not UNSET:
            field_dict["monitorDevice"] = monitor_device

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.monitor_device import MonitorDevice

        d = dict(src_dict)
        _monitor_device = d.pop("monitorDevice", UNSET)
        monitor_device: MonitorDevice | Unset
        if isinstance(_monitor_device, Unset):
            monitor_device = UNSET
        else:
            monitor_device = MonitorDevice.from_dict(_monitor_device)

        verify_device = cls(
            monitor_device=monitor_device,
        )

        verify_device.additional_properties = d
        return verify_device

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
