from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.ssid_override_open_api_v2vo import SsidOverrideOpenApiV2VO


T = TypeVar("T", bound="ApSsidOverrideOpenApiV2VO")


@_attrs_define
class ApSsidOverrideOpenApiV2VO:
    """
    Attributes:
        ssid_overrides (list[SsidOverrideOpenApiV2VO]): SsidOverride Config List
    """

    ssid_overrides: list[SsidOverrideOpenApiV2VO]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ssid_overrides = []
        for ssid_overrides_item_data in self.ssid_overrides:
            ssid_overrides_item = ssid_overrides_item_data.to_dict()
            ssid_overrides.append(ssid_overrides_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ssidOverrides": ssid_overrides,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ssid_override_open_api_v2vo import (
            SsidOverrideOpenApiV2VO,
        )

        d = dict(src_dict)
        ssid_overrides = []
        _ssid_overrides = d.pop("ssidOverrides")
        for ssid_overrides_item_data in _ssid_overrides:
            ssid_overrides_item = SsidOverrideOpenApiV2VO.from_dict(
                ssid_overrides_item_data
            )

            ssid_overrides.append(ssid_overrides_item)

        ap_ssid_override_open_api_v2vo = cls(
            ssid_overrides=ssid_overrides,
        )

        ap_ssid_override_open_api_v2vo.additional_properties = d
        return ap_ssid_override_open_api_v2vo

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
