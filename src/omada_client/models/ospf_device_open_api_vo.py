from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OspfDeviceOpenApiVO")


@_attrs_define
class OspfDeviceOpenApiVO:
    """
    Attributes:
        device_name (str | Unset): Device Name
        mac (str | Unset): Device Mac
        is_stack (bool | Unset): Indicates whether the device is a stack member device.
        support_dead_interval (bool | Unset): Indicates whether the device supports interface dead interval.
    """

    device_name: str | Unset = UNSET
    mac: str | Unset = UNSET
    is_stack: bool | Unset = UNSET
    support_dead_interval: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_name = self.device_name

        mac = self.mac

        is_stack = self.is_stack

        support_dead_interval = self.support_dead_interval

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name
        if mac is not UNSET:
            field_dict["mac"] = mac
        if is_stack is not UNSET:
            field_dict["isStack"] = is_stack
        if support_dead_interval is not UNSET:
            field_dict["supportDeadInterval"] = support_dead_interval

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        device_name = d.pop("deviceName", UNSET)

        mac = d.pop("mac", UNSET)

        is_stack = d.pop("isStack", UNSET)

        support_dead_interval = d.pop("supportDeadInterval", UNSET)

        ospf_device_open_api_vo = cls(
            device_name=device_name,
            mac=mac,
            is_stack=is_stack,
            support_dead_interval=support_dead_interval,
        )

        ospf_device_open_api_vo.additional_properties = d
        return ospf_device_open_api_vo

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
