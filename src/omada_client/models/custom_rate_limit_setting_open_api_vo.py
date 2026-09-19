from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomRateLimitSettingOpenApiVO")


@_attrs_define
class CustomRateLimitSettingOpenApiVO:
    """Rate limit custom setting

    Attributes:
        down_limit_enable (bool): Whether to limit downlink speed; This field is required when select custom setting.
            True: enable, false: disable.
        up_limit_enable (bool): Whether to limit uplink speed; This field is required when select custom setting. True:
            enable, false: disable.
        down_limit (int | Unset): Downlink speed limit value. When the value of Parameter [downLimitType] is 0(Kbps),
            downLimit should be within the range of 1–10485760; when the value of Parameter [downLimitType] is 1(Mbps),
            downLimit should be within the range of 1-10240.
        down_limit_type (int | Unset): Downlink speed limit unit config; DownLimitType should be a value as follows: 0:
            Kbps; 1: Mbps.
        up_limit (int | Unset): Uplink speed limit value. When the value of Parameter [upLimitType] is 0(Kbps), upLimit
            should be within the range of 1–10485760; when the value of Parameter [upLimitType] is 1(Mbps), upLimit should
            be within the range of 1-10240.
        up_limit_type (int | Unset): Uplink speed limit unit config; UpLimitType should be a value as follows: 0: Kbps;
            1: Mbps.
    """

    down_limit_enable: bool
    up_limit_enable: bool
    down_limit: int | Unset = UNSET
    down_limit_type: int | Unset = UNSET
    up_limit: int | Unset = UNSET
    up_limit_type: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        down_limit_enable = self.down_limit_enable

        up_limit_enable = self.up_limit_enable

        down_limit = self.down_limit

        down_limit_type = self.down_limit_type

        up_limit = self.up_limit

        up_limit_type = self.up_limit_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "downLimitEnable": down_limit_enable,
                "upLimitEnable": up_limit_enable,
            }
        )
        if down_limit is not UNSET:
            field_dict["downLimit"] = down_limit
        if down_limit_type is not UNSET:
            field_dict["downLimitType"] = down_limit_type
        if up_limit is not UNSET:
            field_dict["upLimit"] = up_limit
        if up_limit_type is not UNSET:
            field_dict["upLimitType"] = up_limit_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        down_limit_enable = d.pop("downLimitEnable")

        up_limit_enable = d.pop("upLimitEnable")

        down_limit = d.pop("downLimit", UNSET)

        down_limit_type = d.pop("downLimitType", UNSET)

        up_limit = d.pop("upLimit", UNSET)

        up_limit_type = d.pop("upLimitType", UNSET)

        custom_rate_limit_setting_open_api_vo = cls(
            down_limit_enable=down_limit_enable,
            up_limit_enable=up_limit_enable,
            down_limit=down_limit,
            down_limit_type=down_limit_type,
            up_limit=up_limit,
            up_limit_type=up_limit_type,
        )

        custom_rate_limit_setting_open_api_vo.additional_properties = d
        return custom_rate_limit_setting_open_api_vo

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
