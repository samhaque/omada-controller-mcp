from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="FailedDeviceUpgradeFirmwareInfo")


@_attrs_define
class FailedDeviceUpgradeFirmwareInfo:
    """
    Attributes:
        firmware_status (int | Unset): Target firmware status. 0: normal. 1: The target firmware has been
            removed/deleted.
    """

    firmware_status: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        firmware_status = self.firmware_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if firmware_status is not UNSET:
            field_dict["firmwareStatus"] = firmware_status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        firmware_status = d.pop("firmwareStatus", UNSET)

        failed_device_upgrade_firmware_info = cls(
            firmware_status=firmware_status,
        )

        failed_device_upgrade_firmware_info.additional_properties = d
        return failed_device_upgrade_firmware_info

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
