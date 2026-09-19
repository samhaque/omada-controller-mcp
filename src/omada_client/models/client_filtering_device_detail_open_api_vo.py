from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientFilteringDeviceDetailOpenApiVO")


@_attrs_define
class ClientFilteringDeviceDetailOpenApiVO:
    """Device detail info list.

    Attributes:
        mac (str | Unset): Device MAC
        name (str | Unset): Device name
        stack (bool | Unset): Does this device belong to a stack group
        stack_name (str | Unset): Stack group name
    """

    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    stack: bool | Unset = UNSET
    stack_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        name = self.name

        stack = self.stack

        stack_name = self.stack_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if stack is not UNSET:
            field_dict["stack"] = stack
        if stack_name is not UNSET:
            field_dict["stackName"] = stack_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        stack = d.pop("stack", UNSET)

        stack_name = d.pop("stackName", UNSET)

        client_filtering_device_detail_open_api_vo = cls(
            mac=mac,
            name=name,
            stack=stack,
            stack_name=stack_name,
        )

        client_filtering_device_detail_open_api_vo.additional_properties = d
        return client_filtering_device_detail_open_api_vo

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
