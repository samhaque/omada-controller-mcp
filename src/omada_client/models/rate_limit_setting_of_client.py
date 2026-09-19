from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RateLimitSettingOfClient")


@_attrs_define
class RateLimitSettingOfClient:
    """RateLimit setting.

    Attributes:
        rate_limit_id (str | Unset): Rate limit profile ID. Nullable when ratelimit type is custom.
        enable (bool | Unset): Rate limit enable.
        up_enable (bool | Unset): Up limit enable.
        up_unit (int | Unset): Up limit unit should be a value as follows: 1: Kbps; 2: Mbps.
        up_limit (int | Unset): Up limit should be within the range of 1–1024.
        down_enable (bool | Unset): Down limit enable.
        down_unit (int | Unset): Down limit unit should be a value as follows: 1: Kbps; 2: Mbps.
        down_limit (int | Unset): Down limit should be within the range of 1–1024.
    """

    rate_limit_id: str | Unset = UNSET
    enable: bool | Unset = UNSET
    up_enable: bool | Unset = UNSET
    up_unit: int | Unset = UNSET
    up_limit: int | Unset = UNSET
    down_enable: bool | Unset = UNSET
    down_unit: int | Unset = UNSET
    down_limit: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rate_limit_id = self.rate_limit_id

        enable = self.enable

        up_enable = self.up_enable

        up_unit = self.up_unit

        up_limit = self.up_limit

        down_enable = self.down_enable

        down_unit = self.down_unit

        down_limit = self.down_limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rate_limit_id is not UNSET:
            field_dict["rateLimitId"] = rate_limit_id
        if enable is not UNSET:
            field_dict["enable"] = enable
        if up_enable is not UNSET:
            field_dict["upEnable"] = up_enable
        if up_unit is not UNSET:
            field_dict["upUnit"] = up_unit
        if up_limit is not UNSET:
            field_dict["upLimit"] = up_limit
        if down_enable is not UNSET:
            field_dict["downEnable"] = down_enable
        if down_unit is not UNSET:
            field_dict["downUnit"] = down_unit
        if down_limit is not UNSET:
            field_dict["downLimit"] = down_limit

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        rate_limit_id = d.pop("rateLimitId", UNSET)

        enable = d.pop("enable", UNSET)

        up_enable = d.pop("upEnable", UNSET)

        up_unit = d.pop("upUnit", UNSET)

        up_limit = d.pop("upLimit", UNSET)

        down_enable = d.pop("downEnable", UNSET)

        down_unit = d.pop("downUnit", UNSET)

        down_limit = d.pop("downLimit", UNSET)

        rate_limit_setting_of_client = cls(
            rate_limit_id=rate_limit_id,
            enable=enable,
            up_enable=up_enable,
            up_unit=up_unit,
            up_limit=up_limit,
            down_enable=down_enable,
            down_unit=down_unit,
            down_limit=down_limit,
        )

        rate_limit_setting_of_client.additional_properties = d
        return rate_limit_setting_of_client

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
