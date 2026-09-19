from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="UpdateSsidEnableStatusOpenApiVO")


@_attrs_define
class UpdateSsidEnableStatusOpenApiVO:
    """
    Attributes:
        ssid_enable (bool): Enable or disable the SSID
    """

    ssid_enable: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ssid_enable = self.ssid_enable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ssidEnable": ssid_enable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ssid_enable = d.pop("ssidEnable")

        update_ssid_enable_status_open_api_vo = cls(
            ssid_enable=ssid_enable,
        )

        update_ssid_enable_status_open_api_vo.additional_properties = d
        return update_ssid_enable_status_open_api_vo

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
