from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="DeviceCopyConfigurationOpenApiVO")


@_attrs_define
class DeviceCopyConfigurationOpenApiVO:
    """
    Attributes:
        source_mac (str): Source device MAC, like AA-BB-CC-DD-EE-FF
        target_mac (str): Target device MAC, like AA-BB-CC-DD-EE-FF
    """

    source_mac: str
    target_mac: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_mac = self.source_mac

        target_mac = self.target_mac

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sourceMac": source_mac,
                "targetMac": target_mac,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        source_mac = d.pop("sourceMac")

        target_mac = d.pop("targetMac")

        device_copy_configuration_open_api_vo = cls(
            source_mac=source_mac,
            target_mac=target_mac,
        )

        device_copy_configuration_open_api_vo.additional_properties = d
        return device_copy_configuration_open_api_vo

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
