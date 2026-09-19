from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="HotspotSetting")


@_attrs_define
class HotspotSetting:
    """Hotspot types setting.

    Attributes:
        enabled_types (list[int]): Hotspot enabled auth types, should be a value as follows: 3: Voucher, 5: Local User,
            8: Hotspot RADIUS, 6: Sms, 12: Form Auth.
    """

    enabled_types: list[int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled_types = self.enabled_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabledTypes": enabled_types,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enabled_types = cast(list[int], d.pop("enabledTypes"))

        hotspot_setting = cls(
            enabled_types=enabled_types,
        )

        hotspot_setting.additional_properties = d
        return hotspot_setting

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
